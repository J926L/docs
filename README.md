# Role: WSL2 (Ubuntu 24 LTS) / RTX 3060 (6GB) / Spec-Ready Env

# Language: 简体中文 (Mixed with Keywords)

# Style: Telegraphic | No Fluff

# 0. Protocol

- **Ops**: `/home/j/docs/` | **Must** check `scripts/` & `workflows/`。
- **Safety**: **Safety > Speed**. 宁缺毋滥。
- **Glue**: **胶水编程**。能抄不写，能连不造。**Must** 标源。
- **Refactor**: 失败 > 3 次 -> **Must** 重构数据结构。
- **Cognitive**: **Docs**(Context7) + **Search**(Tavily) | **Memory**: 本地 Markdown (`core_memory/`)。
- **SOP**: 原生扫盲，Tavily 深度排坑；核心记忆走 **GitOps** 文档 (AI 提议 -> User 确认)。
- **Test**: **分模块测试** | 完成单一功能后 **Must** 立即运行校验，严禁全量代码生成后再调试。
- **Meta**: 本文档 **Must** 仅限硬约束 | **Ban** 理由描述。

# 1. Stack

- **Logic**: **Right Tool > P-Priority** | 已有栈绝对优先 | 技术选型 **Must** 先提案确认 (未经同意 **Ban** 大规模生成代码) | 工具安装: **No Limits**。
- 🥇 **P1: Rust 2024**: `clippy::pedantic` | `sccache`+`mold` | **Zero** Unsafe/Panic | **Ban** `.clone()` | `src/` + `tests/`。
- 🖥️ **P2: Tauri v2**: IPC **Must** `serde` | **Ban** WebView 直接调 FS | 后端继承 P1 | 前端继承 P3。
- 🥈 **P3: TS**: <100 行/API | `Zod` + `Prisma 7` (WASM) | `strict` | **Ban** `any`。
- 🥉 **P4: Go**: `mage` 构建 | **Must** nil check + `Context` | Channel Only。
- 📉 **P5: Py 3.12**: `uv` | 模块化入 `src/` | GPU 调用 **Must** 显存限额。
- 🚫 **Restricted**: Big Data (Java/SDKMAN) | C/C++ (Modern/RAII | FFI/Lib Only) | Bash (>5 行 -> Py/Go)。

# 2. Constraints & Ops

- **Path**: `/home/j/projects/{project_name}/` | **Must** 绝对路径 | `snake_case`。
- **Layout**: **Idiomatic** (遵循语言主流规范) | **Clean Root** (限制根目录杂讯)。
- **Env**: **Docker** 隔离 | **Secrets** **Must** `.env` (Git Ignore) | **Ban** 明文密钥 | `check-env` | `spec-sync`。
- **VRAM/Port**: 6GB/CUDA 13.x | **Must** 查 `/home/j/dockge/PORTS.md`。
- **Net**: **Priority** `localhost` | **Limit** `192.168.x.x` (Only if required) | **Pro**: `BASE_URL` ENV.
- **Data**: 临时 **Must** SQLite | Supabase (PG 17.6.1) | **Conn**: `process.env.DATABASE_URL` (6543 + `?pgbouncer=true`) | **Auth**: Native `auth.users` (**Ban** Custom PW) | ORM **Must** Prisma 7.x (Singleton)。
- **Schema**: **Source of Truth** Must be `schema.prisma` | **Ban** Manual GUI Sync。
- **Auth**: Profile 类业务表 **Must** 通过 UUID 关联 `auth.users`。
- **Diagnostics**: 报错 **Must** 查 `docker logs` (无云端 UI)。
- **Edge**: 本地 Deno 仅为模拟环境，上线前 **Must** 校验差异。
- **Infra**: caddy:2-alpine | redpanda:v25 | uptime-kuma:2 | redis:7-alpine | `task infra:sync` | Docker / Supabase CLI: 2.70.5。
- **Task**: **Must** `taskfile` | **Must** 原子化 `db:sync` | REST Client (**Ban** Postman)。

# 3. Automation

- **CI/CD**: **GitHub Actions** | **AI Must** 预置 Workflows & Secrets 检查 (含 `clippy`/`Prisma`) | **Must** `concurrency` (Cancel) + `timeout-minutes` (<15m)。
- **Tasks (Contract)**: `db:sync` (Generate & Migrate) | `db:logs` (Docker Logs)。
