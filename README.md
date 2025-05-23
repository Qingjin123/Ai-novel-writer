# AI 小说写作工具 (new-AI-novel)

本项目旨在开发一款功能强大的 AI 辅助小说写作桌面应用。

## 项目结构概览:

- `plan/`: 存放项目规划、设计文档和开发日志。
- `src-web/`: 前端用户界面，使用 Vue.js 3 + TypeScript + Vite 构建。
- `src-tauri/`: Tauri 应用的 Rust 核心，负责原生功能和窗口管理。
- `backend/`: Python 后端服务，使用 FastAPI 构建，处理 AI 逻辑和复杂业务。
- `tauri.conf.json`: Tauri 应用的主要配置文件。
- `package.json`: (根目录) 用于管理整个项目（尤其是前端和Tauri命令）的脚本和可能的 pnpm workspace 配置。

## 技术栈核心:

- **前端:** Vue.js 3, TypeScript, Vite, Tiptap (富文本编辑器)
- **桌面应用框架:** Tauri (Rust)
- **后端AI服务:** Python, FastAPI
- **Python环境与包管理:** uv
- **Node.js包管理:** pnpm

## 开发启动:

1.  确保已安装 Node.js, pnpm, Rust, uv, Python 3.10+。
2.  在项目根目录运行 `pnpm install` (如果配置了 workspace 或根 `package.json` 脚本)。
3.  (可选，单独启动后端) 进入 `backend` 目录，激活虚拟环境 (`source .venv/bin/activate`)，运行 `uvicorn main:app --reload --port 8000`。
4.  在项目根目录运行 `pnpm dev` (或 `pnpm tauri dev`) 来启动整个 Tauri 应用 (会自动处理前端开发服务器)。