# AI小说写作工具 - 开发日志

## 项目启动日期: 2025-05-23 (假设为今天)

---

## 阶段 0: 项目启动与基础架构搭建

**状态:** ✅ **完成**

**完成日期:** 2025-05-23

### 一、环境管理与核心工具版本：

- **Python 版本:** `3.12.x` (具体版本待用户确认后填写)
- **uv (Python环境与包管理器):** `0.1.x` (具体版本待用户确认后填写, 例如 `0.1.30`)
- **Node.js 版本:** `v20.x.x` 或更高 (例如 `v20.11.0`)
- **pnpm (Node包管理器):** `8.x.x` 或更高 (例如 `8.15.0`)
- **Rustc (Rust编译器):** `1.7x.x` (例如 `1.78.0`)
- **Cargo (Rust包管理器):** `1.7x.x` (例如 `1.78.0`)
- **Tauri CLI (v1):** `1.x.x` (例如 `1.6.0`) 或 **Tauri CLI (v2):** `2.x.x-beta.x` (根据实际安装)
- **IDE:** Visual Studio Code

### 二、主要任务与决策：

1.  **[✅] 任务 0.1: 开发环境搭建**
    *   确认并安装了必要的开发工具：Node.js, pnpm, Rust (rustc, cargo), Python, uv。
    *   安装了 Visual Studio Code 及推荐插件 (Rust Analyzer, Prettier, ESLint, Python (Pylance), Ruff/Black, Tauri)。
    *   配置了全局 Git 信息。

2.  **[✅] 任务 0.2: 技术选型最终确认与Demo**
    *   **前端框架选型：** 确定使用 **Vue.js 3 + TypeScript**。
    *   **前端项目创建 (`src-web`):**
        *   使用 `pnpm create vite src-web --template vue-ts` 创建了 Vue + TS 前端项目骨架。
        *   在 `src-web` 目录下成功运行 `pnpm install` 和 `pnpm dev` (基础测试)。
    *   **Tauri 项目初始化:**
        *   在项目根目录 (`new-AI-novel`) 使用 `pnpm create tauri-app@1` (或相应Tauri版本命令) 初始化Tauri项目。
        *   配置了 `tauri.conf.json` 中的 `build.devPath` 指向 Vite 开发服务器 (如 `http://localhost:5173`)，`build.distDir` 指向 `../src-web/dist`。
        *   配置了 `build.beforeDevCommand` 和 `build.beforeBuildCommand` 以便Tauri能正确启动和构建 `src-web` 前端。
        *   成功在根目录运行 `pnpm dev` (或 `pnpm tauri dev`) 启动了Tauri应用并加载了Vue前端。
    *   **后端项目创建 (`backend`):**
        *   在 `backend` 目录下使用 `uv venv` 创建了 Python 虚拟环境 (`.venv`)。
        *   使用 `uv pip install fastapi "uvicorn[standard]"` 安装了FastAPI和Uvicorn。
        *   创建了基础的 `backend/main.py` 并成功运行 `uvicorn main:app --reload --port 8000` 启动了FastAPI服务。
        *   测试了后端API端点 (如 `/` 和 `/api/v1/ping`)。

3.  **[✅] 任务 0.3: 项目结构与代码规范 (进行中/待完善)**
    *   **项目结构规划:**
        *   确定了主要的目录结构：`src-web` (前端), `src-tauri` (Tauri核心), `backend` (后端), `plan` (文档)。
        *   为每个主要模块创建了 `FOLDER_PURPOSE.md` 描述文件。
    *   **`.gitignore` 配置:** 创建了 `.gitignore` 文件，并添加了针对Node, Python, Rust, macOS, VSCode的忽略规则。
    *   **代码格式化与检查工具配置:**
        *   **前端 (`src-web`):**
            *   计划配置 Prettier (`.prettierrc.json`) 和 ESLint (`.eslintrc.cjs`)。
            *   VS Code 工作区设置 (`.vscode/settings.json`) 中已初步添加相关格式化和linting配置。
        *   **后端 (`backend`):**
            *   计划使用 Ruff (或 Black + Flake8)。
            *   计划在 `backend/pyproject.toml` 中配置相关规则。
            *   VS Code 工作区设置中已初步添加相关Python格式化和linting配置。
    *   **代码规范文档:** 初步起草了《设计与编码规范》的大纲。

4.  **[❌] 任务 0.4: CI/CD初步设置 (暂未开始/可选)**(短期内不实现)
    *   计划后续根据代码托管平台 (如GitHub Actions) 配置CI/CD流程。

5.  **[🚧] 任务 0.5: 核心数据模型初稿 (进行中/待完善)**
    *   **初步设想:**
        *   小说项目文件结构 (本地存储方案)。
        *   应用用户配置项。
        *   AI交互数据的基本结构。
    *   **Pydantic模型 (后端):** 开始思考并计划定义核心API的请求和响应模型。
    *   **TypeScript类型 (前端):** 开始思考并计划定义前端需要处理的核心数据类型。

### 三、遇到的问题与解决方案：

*   **(示例问题) 问题1:** 在配置 `tauri.conf.json` 的 `beforeDevCommand` 时，直接使用 `cd src-web && pnpm dev` 不稳定。
    *   **解决方案1:** 通过在项目根目录的 `package.json` 中定义脚本 (如 `"frontend:dev": "pnpm --filter src-web dev"`)，然后在 `tauri.conf.json` 中引用该脚本 (`"pnpm frontend:dev"`)，使得命令执行更可靠和清晰。

*   **(示例问题) 问题2:** Vite开发服务器端口与预想不一致。
    *   **解决方案2:** 启动Vite开发服务器后，根据实际输出的端口号更新 `tauri.conf.json` 中的 `build.devPath`。

### 四、后续计划 (下一阶段的重点):

*   完成并固化 **任务 0.3 (项目结构与代码规范)** 的所有配置。
*   详细设计并文档化 **任务 0.5 (核心数据模型)**。
*   开始 **阶段 1: MVP - 核心编辑与基础AI集成** 的开发：
    *   Tauri应用外壳与文件操作。
    *   Tiptap 富文本编辑器的集成与基础功能实现。
    *   后端AI接口模块的搭建。
    *   实现第一个AI辅助功能 (如内容扩写)。

---