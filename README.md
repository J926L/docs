# Role: WSL2 (Ubuntu 24 LTS) / RTX 3060 (6GB) / Spec-Ready Env

# Language: 简体中文 (Mixed with Keywords)

# Style: Telegraphic | No Fluff | High-Density | Zero-Filler | Unambiguous | Rule-Friendly

# 0. Protocol

- **Ops**: `/home/j/docs/` | Check `scripts/` `workflows/`
- **GitOps**: **Truth in Git**. Infra / Config / Memory: Declarative & Versioned
- **Safety**: **Safety > Speed**
- **Glue**: **胶水编程**. 抄 > 写 | 连 > 造 | **Must** 标源
- **Refactor**: 失败 > 3 次 -> 重构数据结构
- **Cognitive**: **Docs**(Context7) + **Search**(Tavily)
- **Memory**: `core_memory/` (State Machine). **Ban** Logs/Diaries. One component, one file.
- **SOP**: 原生扫盲 -> Tavily 排坑 -> **GitOps** 文档 (AI 提议 -> User 确认)
- **Test**: **分模块测试** | 完成即校验 | **Ban** 全量生成后调试
- **Meta**: 本文档仅限硬约束 | **Ban** 理由描述

# 1. Stack

- **Logic**: **Right Tool > P-Priority** | 已有栈优先 | 工具/环境 大段代码 **Ask**
- **UI / Platform**:
  - 📱 **Mobile**: **Ref** Flutter (Dart)
    - **Android**: **Restricted** Kotlin (Gradle Only). **Ban** System `kotlinc`
  - 🖥️ **Desktop**: **Ref** Flutter (Dart) | **Restricted** Tauri 2 (Low-level/Hacker only)
- **JVM Stack**: `sdkman` | **Ban** system install
- **Languages**:
  - 🥇 **P1: Go**: Primary | `mage` | `Context` | Channel Only | Nil check
  - 🥈 **P2: TS**: Web/Scripts | <100 行 | `Zod` + `Prisma 7` | `strict` | **Ban** `any`
  - 🥉 **P3: Python**: Packages > Code | `uv` | `src/` | GPU: 限额
  - 📉 **P4: Rust 2024**: Specialized | `clippy::pedantic` | **Zero** Unsafe/Panic | **Ban** `.clone()`
- 🚫 **Restricted**: Big Data (Java) | C/C++ (Modern/RAII | FFI Only) | Bash (>5 行 -> Py/Go)

# 2. Constraints & Ops

- **Path**: `/home/j/projects/{project_name}/` | **Absolute** | `snake_case`
- **Layout**: **Idiomatic** | **Clean Root**
- **Env**: **Docker** 隔离 | **Secrets**: `.env` | **Ban** 明文 | `check-env`
- **VRAM/Port**: 6GB/CUDA 13.x | Check `/home/j/dockge/PORTS.md`
- **Net**: `localhost` | `BASE_URL` ENV | `192.168.x.x` restricted
- **Data**: SQLite (Temp) | Supabase (PG 17.6.1) | **Auth**: `auth.users` (**Ban** Custom PW)
- **ORM**: Prisma 7.x (Singleton) | Project-local `npx` | **Gen**: `src/generated/`
- **Schema**: **Source of Truth**: `schema.prisma` | **Ban** GUI Sync
- **Infra**: caddy/redpanda/uptime-kuma/redis (alpine) | `task infra:sync` | CLI 2.70.5
- **Task**: `taskfile` | 原子化 `db:sync` | REST Client (**Ban** Postman)

# 3. Automation

- **CI/CD**: **GitHub Actions** | Workflows & Secrets 检查 | `concurrency` + `timeout-minutes` (<15m)
- **Tasks**: `db:sync` | `db:logs`

# 4. Android (WSL -> Windows)
- **Task**: `task android:run` (`build` -> `cp to Win` -> `adb install`)
- **Logic**: `adb.exe` | **Ban** Linux native `adb`
