# MCP Configuration Master

## 配置管理 (Configuration Management)

### 配置分层

- **`mcp_config.template.yaml`**: 结构模板 (Git 追踪)，包含工具集定义。
- **`mcp_config.yaml`**: 私有配置 (Git 忽略)，包含真实 API Key。

## 初始化新项目

### 方案 A: 软链接 (推荐)

直接挂载主配置，实现 **"一次配置，处处生效"** (Single Source of Truth)：

```bash
# 在目标项目根目录下执行
ln -s /home/j/docs/mcp/mcp_config.yaml ./mcp.json
```

_(注：视 IDE 要求，文件名可能需调整为 `mcp.json` 或 `mcp_config.json`/`yaml`)_

### 方案 B: 独立配置

若项目需要隔离环境或独立 Key：

```bash
cp /home/j/docs/mcp/mcp_config.template.yaml ./mcp_config.yaml
# 编辑填入项目专用 Key
```

此操作可直接加载以下预置工具，无需重复配置：

- **Sequential Thinking**: 深度推理引擎 (fnm)
- **GitHub**: 代码仓库读写 (fnm)
- **Top 5 Search Tools**: 联网搜索 (uvx/fnm)
- **Postgres**: 本地数据库连接 (fnm)

## 补充说明

- **Tavily 独立脚本**: 若需要在项目中直接调用 SDK（不通过 MCP），可使用以下代码：
  ```bash
  uv add tavily-python
  ```
  ```python
  from tavily import TavilyClient
  tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
  response = tavily_client.search("Who is Leo Messi?")
  print(response)
  ```
