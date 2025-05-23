# Python FastAPI 后端: backend

该目录包含了 AI小说写作工具 的 Python 后端服务。

## 技术栈:

- **框架:** FastAPI
- **语言:** Python
- **环境管理:** uv

## 作用:

- **AI 核心逻辑:** 处理与大语言模型 (LLM) 的交互，如调用API、处理Prompt等。
- **复杂业务逻辑:** 实现如 RAG (Retrieval Augmented Generation)、知识图谱查询、内容一致性检查等复杂功能。
- **API 服务:** 为前端应用提供 HTTP API 接口。
- **数据处理与持久化:** (如果需要超出Tauri本地存储能力的数据库交互) 连接和操作数据库。
- **耗时任务:** 执行不适合在前端或 Tauri Rust 核心中长时间运行的任务。

## 建议目录结构 (后续可扩展):

- `app/`: 存放核心应用代码。
    - `main.py`: FastAPI 应用实例和主要路由定义。
    - `api/`: 存放不同模块的 API 路由。
    - `services/`: 业务逻辑层。
    - `models/` (或 `schemas/`): Pydantic 数据模型。
    - `core/`: 配置文件、数据库连接等。
    - `utils/`: 通用工具函数。
- `tests/`: 存放后端测试代码。
- `.venv/`: Python 虚拟环境 (由 `uv venv` 创建，通常被 `.gitignore` 忽略)。
- `requirements.txt` (或 `pyproject.toml`): Python 依赖列表。
- `.env`: (可选) 存放环境变量，如 API 密钥 (不应提交到版本控制)。

## 开发:

1.  **激活虚拟环境:** 在 `backend` 目录下运行 `source .venv/bin/activate`。
2.  **安装/更新依赖:** `uv pip install -r requirements.txt` 或 `uv pip install <package_name>`。
3.  **启动开发服务器:** `uvicorn app.main:app --reload --port 8000` (假设 FastAPI 实例在 `app/main.py` 中)。
