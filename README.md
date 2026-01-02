# Role: WSL2 (Ubuntu 24 LTS) / RTX 3060 (6GB) / Spec-Ready Env

# Language: 简体中文 (Mixed with Keywords)

# Style: 电报体 (Telegraphic) | No Fluff

# 0. Protocol

- **Ops**: `/home/j/docs/` | **Must** check `scripts/` & `workflows/`。
- **Safety**: **Safety > Speed**. 宁缺毋滥。
- **Glue**: **胶水编程**。能抄不写，能连不造。**Must** 标源。
- **Refactor**: 失败 > 3 次 -> **Must** 重构数据结构。

# 1. Stack

- **Logic**: **Right Tool > P-Priority** | 工具安装: **No Limits**.
- 🥇 **P1: Rust 2024**: `clippy::pedantic` | `sccache`+`mold` | **Zero** Unsafe/Panic | **Ban** `.clone()` | `src/` + `tests/`。
- 🖥️ **P2: Tauri v2**: IPC **Must** `serde` | **Ban** WebView 直接调 FS | 后端继承 P1 | 前端继承 P3。
- 🥈 **P3: TS**: <100行/API | `Zod` + `Prisma 7` (WASM) | `strict` | **Ban** `any`。
- 🥉 **P4: Go 1.23**: `mage` 构建 | **Must** nil check + `Context` | Channel Only。
- 📉 **P5: Py 3.12**: `uv` | 模块化入 `src/` | GPU 调用 **Must** 显存限额。
- 🚫 **Restricted**: Big Data (Java/SDKMAN) | C/C++ (Modern/RAII | FFI/Lib Only) | Bash (>5行 -> Py/Go)。

# 2. Constraints & Ops

- **Path**: `/home/j/projects/{project_name}/` | **Must** 绝对路径 | `snake_case`。
- **Layout**: **Idiomatic** (遵循语言主流规范) | **Clean Root** (限制根目录杂讯)。
- **Env**: **Docker** 隔离 | **Secrets** **Must** `.env` (Git Ignore) | **Ban** 明文密钥 | `check-env` | `spec-sync`。
- **VRAM/Port**: 6GB/CUDA 13.x | **Must** 查 `/home/j/dockge/PORTS.md`。
- **Data**: 临时 **Must** SQLite | 持久化 **Must** Supabase (PostgreSQL 17.6.1 / Auth) | **禁止自动更新** | ORM/Migrate **Must** Prisma 7.x。
- **Infra**: caddy:2-alpine | redpanda:v25 | uptime-kuma:2 | redis:7-alpine | `task infra:sync` | Docker / Supabase CLI: 2.70.5。
- **Task**: **Must** `taskfile` | **Must** 原子化 `db:sync` | REST Client (**Ban** Postman)。

# 3. Automation

- **CI**: **GitHub Actions** | **Must** `clippy` (Pedantic) | **Must** Prisma Schema 校验。
- **Init**: **AI Must** 预置 `.github/workflows/` | **Must** 检查 `secrets` 配置。
