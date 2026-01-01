# “开发环境一键对齐工具”

```bash
source ~/.bashrc
sync
```

# 🧰 军火库清单 (Tool Inventory)

### 📦 环境与版本 (Host CLI)

- **Node**: `fnm` (多版本管理)。
- **Python**: `uv` (极速包管/隔离) | SQLite (内置)。
- **Rust**: `rustup` (全套工具链)。
- **Java**: `sdk` (SDKMAN! / Maven / Java 21)。

### 🛠️ 现代替代 (Modern Alternatives)

- **文件**: `eza` (列出文件 / ls) / `bat` (查看文件 / cat)。
- **搜索/跳转**: `rg` (内容查找 / grep) / `z` (智能跳转目录 / cd)。
- **任务**: `task` (任务运行 / make) / `mage` (复杂构建)。

### 🌐 网络诊断 (Network)

- **DNS**: `doggo` (替代 `nslookup`) | 原生 DoH 支持。
- **Trace**: `trippy` (替代 `traceroute`) | 实时 TUI 监控 | 命令: `trip`。

### 🔍 调试与接口 (Dev & Debug)

- **调试**: `ic()` (Icecream 打印) / `rich` (终端美化)。
- **接口**: `.http` (VS Code REST Client)；**严禁** Postman。

### 🐳 容器设施 (Docker Stack)

- **管理**: **Dockge** (`http://localhost:5001`)。

  - **启动**: `./start_dockge.sh` (在 `/home/j/projects/` 下执行)

- **网关**: **Caddy v2** (自动 HTTPS / 反代)。
- **监控**: **Uptime Kuma** (`http://status.localhost`)。
- **数据**:
  - **Supabase**: PG 17 (`http://127.0.0.1:54323`)。
  - **Redis**: 7-alpine (密码保护)。
- **消息**: **Redpanda** (Dockge)；兼容、禁原生 Kafka。

### 📍 资源索引 (Index)

- **端口**: `/home/j/dockge/PORTS.md` (查重必看)。
- **代码**: `/home/j/projects/<name>/src/` (文件名强制 `snake_case`)。
