# Tauri Rust 核心: src-tauri

该目录包含了 AI小说写作工具 的 Tauri 应用的 Rust 核心代码。

## 作用:

- **原生功能:** 实现需要操作系统底层能力的功能 (如文件系统访问、系统托盘、原生通知等)。
- **后端桥梁:** 作为 Web 前端 (Vue.js) 与操作系统之间的桥梁。
- **安全性:** 执行一些不适合在前端执行的敏感操作。
- **性能:** 对于计算密集型任务，Rust 可以提供比 JavaScript 更好的性能。
- **自定义命令:** 定义可以从 JavaScript 前端调用的 Rust 函数 (Tauri commands)。

## 主要文件和目录:

- `src/`: 存放 Rust 源代码。
    - `main.rs`: Rust 应用的入口文件，在这里构建和运行 Tauri 应用。
    - `lib.rs`: (如果项目结构是库)
    - (其他 `.rs` 文件): 可以创建自定义模块来组织代码，例如 `commands.rs`, `menu.rs` 等。
- `Cargo.toml`: Rust 的包配置文件 (类似 `package.json`)，定义项目元数据、依赖项 (crates) 等。
- `build.rs`: (可选) 构建脚本，在编译 Rust 代码之前运行。
- `icons/`: 存放应用在不同平台和尺寸下的图标。
- `target/`: (通常位于项目根目录的 `target/` 或 `src-tauri/target/`) 存放编译后的 Rust 二进制文件和中间产物，此目录通常被 `.gitignore` 忽略。

## 开发:

此目录中的 Rust 代码会在运行 `pnpm tauri dev` 或 `pnpm tauri build` (从项目根目录) 时自动编译。