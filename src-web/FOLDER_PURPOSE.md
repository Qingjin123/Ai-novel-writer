# 前端应用: src-web

该目录包含了 AI小说写作工具 的前端用户界面代码。

## 技术栈:

- **框架:** Vue.js 3
- **语言:** TypeScript
- **构建工具:** Vite

## 主要子目录结构 (由Vite生成):

- `public/`: 存放不会被 Vite 处理的静态资源，例如 `favicon.ico`。构建时会直接复制到输出目录。
- `src/`: 前端应用的核心源代码。
    - `assets/`: 存放会被 Vite 处理的静态资源，如图片、字体等。
    - `components/`: 可复用的 Vue 组件。建议按功能或类型组织子目录。
    - `views/` (或 `pages/`): 用于表示应用中不同页面或视图的组件。
    - `router/`: (如果使用 Vue Router) 存放路由配置。
    - `store/`: (如果使用 Pinia 等状态管理库) 存放状态管理逻辑。
    - `App.vue`: 应用的根 Vue 组件。
    - `main.ts`: Vue 应用的入口文件，负责初始化 Vue 实例、插件等。
- `index.html`: 单页应用的 HTML 入口文件，Vite 会将其作为模板。
- `package.json`: 定义前端项目的依赖、脚本 (如 `dev`, `build`, `lint`) 等。
- `vite.config.ts`: Vite 构建工具的配置文件。
- `tsconfig.json`: TypeScript 编译器的配置文件。

## 开发与构建:

- **开发模式:** 通常通过 Tauri 的开发命令 (`pnpm tauri dev` 从项目根目录) 间接启动 Vite 的开发服务器。也可以在 `src-web` 目录下单独运行 `pnpm dev` 来调试前端。
- **构建:** 前端代码的生产构建通常也由 Tauri 的构建命令 (`pnpm tauri build` 从项目根目录) 触发，Vite 会将优化后的静态文件输出到其配置的 `dist` 目录 (默认为 `src-web/dist`)。