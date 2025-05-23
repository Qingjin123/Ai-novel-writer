# AI小说写作工具 - 设计与编码规范

**1. 总则 (General Principles)**

1.1. **清晰性优先 (Clarity First):** 代码首先是写给人看的，其次才是给机器执行的。优先保证代码的逻辑清晰、易于理解，避免过度追求技巧性的“炫技”代码。
1.2. **一致性是关键 (Consistency is Key):** 在整个项目中，对相同的概念和操作应采用一致的命名、结构和风格。
1.3. **保持简单 (Keep It Simple, Stupid - KISS):** 除非有充分的理由，否则选择最简单直接的解决方案。避免不必要的复杂性。
1.4. **不要重复自己 (Don't Repeat Yourself - DRY):** 尽量将重复的逻辑抽象成可复用的函数、类或组件。
1.5. **关注点分离 (Separation of Concerns - SoC):** 不同功能模块的代码应该保持独立，UI、业务逻辑、数据访问等应分离开。
1.6. **逐步完善 (Iterative Refinement):** 初期不必追求完美，先让功能跑起来，后续在理解加深和需求明确后进行重构和优化。
1.7. **本文档是活文档 (Living Document):** 随着项目的进展和经验的积累，本规范可以被修订和完善。

**2. 项目结构 (Project Structure)**

*   **目标：** 清晰地组织文件，方便查找和管理。
*   **Tauri 项目典型结构：**
    ```
    project-root/
    ├── src/                     # Rust Tauri核心代码 (主进程)
    │   ├── main.rs              # Tauri应用入口
    │   └── ...                  # 其他Rust模块 (如自定义命令、插件)
    ├── src-web/                 # 前端Web应用代码 (React/Vue + Tiptap)
    │   ├── public/              # 静态资源 (index.html, favicons等)
    │   ├── src/                 # 前端源代码
    │   │   ├── assets/          # 图片、字体等静态资源
    │   │   ├── components/      # 可复用的UI组件 (如Button.tsx, EditorToolbar.vue)
    │   │   │   └── common/      # 通用基础组件
    │   │   │   └── layout/      # 布局组件
    │   │   │   └── specific/    # 特定功能组件
    │   │   ├── contexts/        # (React) Context API
    │   │   ├── hooks/           # (React) 自定义Hooks
    │   │   ├── pages/           # (或 views/) 页面级组件
    │   │   ├── services/        # 与后端API交互的逻辑 (或直接在组件/hooks中处理)
    │   │   ├── store/           # (Vuex/Pinia/Redux/Zustand) 全局状态管理
    │   │   ├── styles/          # 全局样式、主题等
    │   │   ├── types/           # TypeScript类型定义 (interfaces, types)
    │   │   ├── utils/           # 通用工具函数
    │   │   └── App.tsx/vue      # 应用根组件
    │   │   └── main.tsx/ts      # 前端入口文件
    │   ├── package.json
    │   └── tsconfig.json (或 jsconfig.json)
    ├── backend/                 # Python FastAPI后端代码
    │   ├── app/                 # 应用核心代码
    │   │   ├── api/             # API路由 (endpoints)
    │   │   │   └── v1/          # API版本控制
    │   │   │       └── endpoints/ # 具体功能的路由文件 (e.g., ai_writing.py, knowledge_base.py)
    │   │   ├── core/            # 核心配置、数据库连接、中间件等
    │   │   │   └── config.py
    │   │   ├── crud/            # (或 repositories/) 数据库增删改查操作 (Data Access Layer)
    │   │   ├── models/          # Pydantic模型 (请求/响应体)、数据库ORM模型 (如SQLAlchemy)
    │   │   ├── schemas/         # (若不用Pydantic作ORM映射) Pydantic schema (与models分离时)
    │   │   ├── services/        # 业务逻辑层 (Business Logic Layer)
    │   │   ├── utils/           # 后端通用工具函数
    │   │   └── main.py          # FastAPI应用入口
    │   ├── tests/               # 后端测试代码
    │   ├── .env                 # 环境变量 (不提交到Git)
    │   ├── requirements.txt     # (或 pyproject.toml for Poetry/PDM) Python依赖
    │   └── venv/                # Python虚拟环境 (不提交到Git)
    ├── .git/
    ├── .gitignore
    └── README.md
    ```

**3. 命名规范 (Naming Conventions)**

*   **目标：** 通过名称快速理解变量、函数、类等的用途和类型。
*   **通用规则：**
    *   使用**英文**命名。
    *   名称应具有描述性，清晰表达其含义。避免使用无意义的缩写 (如 `usr` 代替 `user`)，除非是广泛接受的缩写 (如 `id`, `db`, `url`)。
    *   保持一致性。

*   **具体规范：**

    | 类别                     | JavaScript/TypeScript (前端)        | Python (后端)                   | 示例 (JS/TS)         | 示例 (Python)           |
    | :----------------------- | :---------------------------------- | :------------------------------ | :--------------------- | :---------------------- |
    | **文件 (JS/TS)**         | `kebab-case.ts` / `kebab-case.tsx`  | N/A                             | `user-profile.tsx`     | N/A                     |
    | **文件 (Python)**        | N/A                                 | `snake_case.py`                 | N/A                    | `user_profile.py`       |
    | **目录**                 | `kebab-case` 或 `camelCase`         | `snake_case`                    | `user-components`      | `user_services`         |
    | **变量 (Variables)**     | `camelCase`                         | `snake_case`                    | `userName`             | `user_name`             |
    | **常量 (Constants)**     | `UPPER_SNAKE_CASE`                  | `UPPER_SNAKE_CASE`              | `MAX_USERS`            | `MAX_USERS`             |
    | **函数 (Functions)**     | `camelCase`                         | `snake_case`                    | `getUserById()`        | `get_user_by_id()`      |
    | **类 (Classes)**         | `PascalCase`                        | `PascalCase`                    | `UserService`          | `UserService`           |
    | **接口 (Interfaces - TS)** | `PascalCase` (可加`I`前缀, 但非必需) | N/A                             | `IUserProfile` / `UserProfile` | N/A                     |
    | **类型别名 (Type Aliases - TS)** | `PascalCase`                  | N/A (Python用`TypeAlias`或注释) | `UserId`               | `UserId = NewType('UserId', int)` |
    | **React组件**            | `PascalCase`                        | N/A                             | `UserProfileCard.tsx`  | N/A                     |
    | **Vue组件**              | `PascalCase.vue` 或 `kebab-case.vue`| N/A                             | `UserProfileCard.vue`  | N/A                     |
    | **CSS类名**              | `kebab-case` 或 BEM (`block__element--modifier`) | N/A                | `user-profile-card`    | N/A                     |
    | **API端点 (URL路径)**    | N/A                                 | `kebab-case` (或 `snake_case`), 复数名词 | N/A                | `/api/v1/ai-suggestions` |
    | **数据库表名**           | N/A                                 | `snake_case`, 复数名词          | N/A                    | `users`, `novel_chapters` |
    | **数据库列名**           | N/A                                 | `snake_case`                    | N/A                    | `user_id`, `created_at` |
    | **布尔变量/函数**        | `is` / `has` / `should` 前缀        | `is_` / `has_` / `should_` 前缀  | `isLoading`, `hasPermission` | `is_loading`, `has_permission` |
    | **事件处理函数**         | `on` / `handle` 前缀                | N/A (GUI中常见, 后端API较少)    | `onClick`, `handleSubmit` | N/A                     |

**4. 编码风格 (Coding Style)**

*   **目标：** 统一代码外观，提高可读性。强烈建议使用自动化工具。
*   **通用工具：**
    *   **Prettier:** 用于代码格式化 (JS/TS, HTML, CSS, JSON, Markdown)。
    *   **ESLint:** 用于JavaScript/TypeScript代码质量和风格检查。
    *   **Black:** 用于Python代码格式化 (PEP 8的严格子集)。
    *   **Flake8 / Pylint:** 用于Python代码质量和风格检查 (PEP 8)。
*   **具体规范：**

    *   **缩进：**
        *   JS/TS: 使用2个空格。
        *   Python: 使用4个空格 (PEP 8)。
    *   **行长度：**
        *   建议不超过80-120个字符。Prettier和Black会自动处理。
    *   **引号：**
        *   JS/TS: 优先使用单引号 (`'`) 或模板字符串 (`` ` ``)，保持一致。ESLint可配置。
        *   Python: 优先使用双引号 (`"`) 或单引号 (`'`)，保持一致。Black默认双引号。
    *   **分号 (JS/TS):** 建议使用。Prettier可配置。
    *   **花括号 `{}`：**
        *   `if`, `for`, `while` 等语句块即使只有一行也使用花括号，以增加清晰度和避免错误。
    *   **空格：**
        *   操作符两侧 (如 `a + b`)，逗号后，关键字后 (如 `if (condition)`) 使用空格。格式化工具会自动处理。
    *   **导入 (Imports)：**
        *   分组导入：标准库、第三方库、项目内部模块，组间空一行。
        *   排序：按字母顺序。ESLint和Python的`isort`工具可以自动完成。
        *   JS/TS: 优先使用绝对路径导入 (配置`baseUrl`或路径别名)。
    *   **TypeScript特定：**
        *   尽可能使用强类型，避免使用 `any` (除非必要且有充分理由)。
        *   使用 `interface` 定义对象结构，使用 `type` 定义联合类型、交叉类型或简单类型别名。
        *   显式声明函数返回类型。
    *   **Python特定：**
        *   严格遵循PEP 8。
        *   使用类型提示 (Type Hints)。
        *   使用f-strings进行字符串格式化 (如 `f"Hello, {name}"`)。
        *   FastAPI: 大量使用Pydantic模型进行数据验证和序列化。

**5. 注释与文档 (Comments and Documentation)**

*   **目标：** 解释代码的设计思路、复杂逻辑和“为什么”，而不是“是什么”。
*   **规范：**
    *   **何时注释：**
        *   复杂的算法或业务逻辑。
        *   代码中不明显的原因或意图。
        *   临时的解决方案或已知问题 (使用 `// TODO:` 或 `# FIXME:`)。
        *   对外部API或库的特定用法或注意事项。
    *   **注释风格：**
        *   JS/TS: `//` 用于单行注释，`/* ... */` 用于多行注释。
        *   Python: `#` 用于单行注释，多行注释使用多个 `#` 或三引号文档字符串。
    *   **文档字符串 (Docstrings/JSDoc)：**
        *   **Python:** 为所有公共模块、类、函数和方法编写符合PEP 257的文档字符串。FastAPI会用它们生成API文档。
            ```python
            def get_user(user_id: int) -> User:
                """
                Retrieves a user by their ID.

                Args:
                    user_id: The ID of the user to retrieve.

                Returns:
                    The User object if found, otherwise raises NotFoundException.
                """
                # ... logic ...
            ```
        *   **JS/TS (JSDoc):** 为公共函数、类、方法、React组件的Props编写JSDoc风格的注释。
            ```typescript
            /**
             * Retrieves a user by their ID.
             * @param userId - The ID of the user to retrieve.
             * @returns The User object or null if not found.
             */
            function getUserById(userId: string): User | null {
              // ... logic ...
            }
            ```
    *   **避免过度注释：** 不要注释显而易见的代码。好的命名和清晰的结构本身就是最好的文档。
    *   **`TODO` / `FIXME` / `XXX` / `NOTE`：**
        *   `// TODO: Implement password reset functionality`
        *   `# FIXME: This logic is not efficient for large datasets`
        *   `// XXX: This is a hack, needs proper solution`
        *   `# NOTE: Remember to update the cache инвалидацию logic if this changes`

**6. 错误处理 (Error Handling)**

*   **目标：** 优雅地处理预期和意外的错误，提供有用的反馈，保证应用的稳定性。
*   **规范：**
    *   **显式处理：** 使用 `try...catch` (JS/TS) 或 `try...except...finally` (Python)。
    *   **避免空 `catch`/`except` 块：** 至少记录错误信息。
    *   **具体的异常类型：** 捕获尽可能具体的异常类型，而不是通用的 `Exception` 或 `Error` (除非你知道你在做什么)。
    *   **FastAPI错误处理：** 使用FastAPI的 `HTTPException` 来返回标准的HTTP错误响应。可以创建自定义异常处理器。
    *   **前端错误展示：** 向用户展示友好的错误信息，而不是原始错误栈。可以在全局或组件级别捕获错误。
    *   **日志记录：** 在后端记录详细的错误信息 (包括堆栈跟踪) 以便调试。前端也可以将关键错误发送到日志服务。

**7. 版本控制 (Version Control - Git)**

*   **目标：** 跟踪代码变更历史，方便协作和回滚。
*   **规范：**
    *   **提交频率：** 频繁提交小的、逻辑完整的变更。
    *   **提交信息 (Commit Messages)：**
        *   遵循 **Conventional Commits** 规范 (强烈推荐)。格式：`type(scope): subject`
            *   `feat(api): add endpoint for user creation`
            *   `fix(editor): resolve issue with list indentation`
            *   `docs(readme): update installation instructions`
            *   `style(auth): reformat login component`
            *   `refactor(service): improve performance of suggestion generation`
            *   `test(crud): add unit tests for user repository`
            *   `chore(deps): update fastapi to version 0.100.0`
        *   主题行简洁明了，祈使句 (如 `Add feature` 而不是 `Added feature` 或 `Adds feature`)。
        *   正文 (可选) 详细描述变更内容和原因。
    *   **分支策略 (Branching Strategy)：**
        *   `main` (或 `master`): 稳定的、可发布的代码。禁止直接提交到`main`。
        *   `develop`: 集成和测试新功能的分支。
        *   特性分支 (`feature/feature-name`): 开发新功能。从`develop`创建，完成后合并回`develop`。
        *   修复分支 (`fix/issue-description`): 修复bug。从`develop`或`main`创建，修复后合并回去。
        *   发布分支 (`release/version-number`): 准备发布版本时使用。
    *   **合并请求/拉取请求 (Merge/Pull Requests)：** 所有代码合并到`develop`或`main`都应通过MR/PR，并进行代码审查 (即使是单人项目，也可以进行自我审查)。

**8. 测试 (Testing)**

*   **目标：** 确保代码的正确性和稳定性，减少回归错误。
*   **规范 (新手可逐步引入)：**
    *   **单元测试：** 测试最小的代码单元 (函数、方法、组件的独立行为)。
        *   Python: `unittest` (内置), `pytest` (更流行、功能更强)。
        *   JS/TS: `Jest`, `Vitest`, `React Testing Library`, `Vue Test Utils`.
    *   **集成测试：** 测试多个模块协同工作的正确性 (如API端点与服务层、数据库的交互)。
    *   **命名：** 测试文件 `test_*.py` 或 `*.test.ts` / `*.spec.ts`。测试函数/描述 `test_function_name_with_condition` 或 `it('should do something when condition')`。
    *   **覆盖率：** (进阶) 关注核心逻辑的测试覆盖率。

**9. 安全性 (Security)**

*   **目标：** 保护用户数据和应用免受常见威胁。
*   **规范 (基础)：**
    *   **输入验证：** 永远不要相信来自客户端的输入。使用Pydantic (FastAPI) 或类似库在后端严格验证所有输入数据。
    *   **SQL注入防护：** 使用ORM (如SQLAlchemy) 或参数化查询，绝不手动拼接SQL语句。
    *   **XSS防护：** React/Vue等现代前端框架默认有一定防护，但仍需注意动态插入HTML或URL时的风险。对用户生成的内容进行适当转义。
    *   **API密钥/敏感配置：** 不要硬编码在代码中。使用环境变量 (`.env`文件，由Tauri或FastAPI加载) 或安全的配置管理服务。`.env`文件不应提交到Git。
    *   **依赖管理：** 定期更新依赖库，修复已知的安全漏洞 (如使用`npm audit`或Python的`safety`/`pip-audit`)。

**10. 工具配置**

*   在项目根目录中包含所有相关工具的配置文件，如：
    *   `.prettierrc.js` / `.prettierignore`
    *   `.eslintrc.js` / `.eslintignore`
    *   `pyproject.toml` (用于Black, isort, Flake8/Pylint等Python工具的配置)
    *   `tsconfig.json`
*   确保IDE (如VS Code) 集成了这些工具，以便在保存时自动格式化和提示。

**给新手的执行建议：**

1.  **从基础开始：** 首先关注命名规范、基本的文件结构和版本控制的提交信息。
2.  **依赖工具：** 尽早配置并使用Prettier, ESLint, Black, Flake8。它们能帮您自动养成好习惯。
3.  **逐步采纳：** 不要试图一次性完美执行所有规范。选择几个对您当前阶段最重要的，熟练后再引入其他。
4.  **多看好代码：** 阅读优秀的开源项目代码，学习它们是如何组织和编写的。
5.  **自我审查：** 在提交代码前，花几分钟回顾一下，对照这份规范检查自己的代码。
