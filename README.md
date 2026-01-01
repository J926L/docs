# Role: WSL2 (Ubuntu 24 LTS) / RTX 3060 (6GB) / Spec-Ready Env

# Language: 简体中文 (Mixed with Keywords)

# Style: 电报体 (Telegraphic) | No Fluff

# 0. Protocol
- **Safety**: **Safety > Speed**. 宁缺毋滥。
- **Glue**: **胶水编程**。能抄不写，能连不造。**Must** 标源。
- **Refactor**: 失败 > 3 次 -> **Must** 重构数据结构。

# 1. Stack
- **Logic**: **Right Tool > P-Priority** | 工具安装: **No Limits**.
- 🥇 **P1: Rust 2024**: `sccache`+`mold` | **Zero** Unsafe/Panic | **Ban** `.clone()` | `src/` + `tests/`。
- 🖥️ **P2: Tauri v2**: IPC **Must** `serde` | **Ban** WebView 直接调 FS | 后端继承 P1 | 前端继承 P3。
- 🥈 **P3: TS**: <100行/API | `Zod` 校验 | `strict` | **Ban** `any`。
- 🥉 **P4: Go**: `mage` 构建 | **Must** nil check + `Context` | Channel Only。
- 📉 **P5: Py 3.12**: `uv` | 模块化入 `src/` | GPU 调用 **Must** 显存限额。
- 🚫 **Restricted**: Big Data (Java/SDKMAN) | C/C++ (Modern/RAII | FFI/Lib Only) | Bash (>5行 -> Py/Go)。

# 2. Constraints & Ops
- **Path**: **Only** `/home/j/projects/` | **Must** 绝对路径 | `snake_case`。
- **Env**: **Docker** 隔离 | **Ban** `/pip/ etc.` 全局 | `apt/snap` **Must** Consent | `check-env` | `spec-sync`。
- **VRAM/Port**: 6GB/CUDA 13.x | **Must** 查 `/home/j/dockge/PORTS.md`。
- **Data**: 临时/轻量 **Must** SQLite | 持久化 **Must** Supabase CLI。
- **Infra**: caddy:2 (**Ban** nginx) | redpanda:v25 (**Ban** Kafka) | uptime-kuma:2 (**Ban** prometheus) | redis:7 | Supabase CLI。
- **Task**: **Must** `taskfile` | **Ban** Shell | REST Client (**Ban** Postman)。
