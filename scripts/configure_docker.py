#!/usr/bin/env python3
# /// script
# dependencies = [
#   "rich",
# ]
# ///
# 解释：上面的内容是 PEP 723 脚本元数据，用于 uv 自动管理依赖。

import json
import subprocess
import sys
from pathlib import Path
from rich.console import Console
from rich.panel import Panel

console = Console()

DOCKER_CONFIG_PATH = Path("/etc/docker/daemon.json")

# 2026-01-02 实测验证可用的镜像站
CONFIG = {
    "registry-mirrors": [
        "https://docker.m.daocloud.io",
        "https://docker.1ms.run",
        "https://hub.rat.dev"
    ],
    "log-driver": "json-file",
    "log-opts": {
        "max-size": "100m",
        "max-file": "3"
    }
}

def run_cmd(cmd: list[str], sudo: bool = True, capture: bool = True):
    full_cmd = ["sudo"] + cmd if sudo else cmd
    try:
        return subprocess.run(full_cmd, check=True, capture_output=capture, text=True)
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]执行命令失败 {' '.join(full_cmd)}:[/bold red]\n{e.stderr}")
        sys.exit(1)

def main():
    console.print(Panel("Docker 引擎配置 (中国区加速优化)", style="bold blue"))

    # 1. 写入 daemon.json
    try:
        with console.status("[bold yellow]正在写入配置..."):
            run_cmd(["mkdir", "-p", str(DOCKER_CONFIG_PATH.parent)])
            # 先写临时文件再移动，确保原子性，防止因意外中断损坏配置文件
            tmp_file = Path("/tmp/docker_daemon.json")
            tmp_file.write_text(json.dumps(CONFIG, indent=2))
            run_cmd(["mv", str(tmp_file), str(DOCKER_CONFIG_PATH)])
            run_cmd(["chmod", "644", str(DOCKER_CONFIG_PATH)])
        console.print(f"[green]✓[/green] 已更新 {DOCKER_CONFIG_PATH}")
    except Exception as e:
        console.print(f"[bold red]配置失败:[/bold red] {e}")
        sys.exit(1)

    # 2. 重启 Docker 服务
    with console.status("[bold yellow]正在重启 Docker..."):
        run_cmd(["systemctl", "daemon-reload"])
        run_cmd(["systemctl", "restart", "docker"])
    console.print("[green]✓[/green] Docker 服务已重启。")

    # 3. 拉取测试 (验证是否真的可用)
    console.print("\n[bold cyan]正在执行连通性验证...[/bold cyan]")
    with console.status("[bold yellow]正在尝试拉取 alpine:latest...") as status:
        try:
            # 清理旧的测试镜像
            subprocess.run(["sudo", "docker", "rmi", "alpine:latest"], capture_output=True)
            # 实际拉取动作
            run_cmd(["docker", "pull", "alpine:latest"], capture=False)
            console.print("[green]✓[/green] 镜像拉取测试通过！")
        except Exception:
            console.print("[red]✗[/red] 拉取测试失败。请检查网络或代理设置。")

    console.print("\n[bold green]最终生效的镜像列表:[/bold green]")
    for mirror in CONFIG["registry-mirrors"]:
        console.print(f"  - {mirror}")

if __name__ == "__main__":
    main()
