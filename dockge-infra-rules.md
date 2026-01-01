#Role: DevOps Expert
# 容器配置规范
## 目录结构* **位置**: `~/dockge/stacks/[服务名]/compose.yaml`
* **管理**: 必须通过 Dockge 面板操作
* **端口**: 必须在 `~/dockge/PORTS.md` 登记

## 配置原则
### 1. 稳定性* **重启策略**: 必须设为 `restart: unless-stopped`
* **数据安全**: 必须使用 Bind Mounts (本地目录挂载)

### 2. 网络互通 (新增)* **公共网络**: 基础设施必须加入 `infra-net` 外部网络
* **内部通信**: 禁止使用 IP，必须使用容器名（如 `redis-infra`）进行服务间调用

### 3. 资源限制* **强制限制内存**:
* 重型服务: 3G (如 GitLab, Jenkins)
* 开发工具: 2G (如 MySQL, Postgres)
* 轻量服务: 512M (如 Redis, Nginx)



### 4. 注释规范* **风格**: 简体中文
* **原则**: 极简短的解释“为什么” (配置意图)，极精简词汇写出“是什么”

## 文件结构示例
```yaml
services:
  redis-infra:
    image: redis:7-alpine # 版本锁定
    restart: unless-stopped
    ports:
      - "6379:6379"
    volumes:
      - ./data:/data
    networks:
      - infra-net # 公共网络
    
    mem_limit: 512m # 硬限制 (防卡死)
    command: redis-server --maxmemory 400mb --maxmemory-policy allkeys-lru --appendonly yes # 内存策略 (主动清理)

networks:
  infra-net:
    external: true # 外部网络
```
