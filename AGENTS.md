# AGENTS.md — 仓库操作规范

本文档面向在此仓库中工作的 AI Agent，定义了添加新技能、维护文档和版本管理的标准流程。

---

## 仓库结构约定

```
felix-to-skills/
├── README.md              # 总索引：所有技能的摘要、文件结构、使用方式
├── AGENTS.md              # 本文件：AI Agent 操作规范
│
├── <skill-name>/          # 每个技能一个独立目录
│   ├── SKILL.md           # 技能入口（必须）
│   ├── README.md          # 技能说明（推荐）
│   └── ...                # 技能相关资源
```

---

## 添加新技能的标准流程

当向仓库中添加一个新的 skill 时，必须按以下步骤操作：

### Step 1: 创建技能目录

```
<skill-name>/
├── SKILL.md      # 技能入口文件，包含 frontmatter（name, description, category）
├── README.md     # 技能说明文档
└── ...           # 其他技能文件
```

### Step 2: 更新 README.md

在根目录 `README.md` 的**目录**表格中添加新技能的条目：

```markdown
| [新技能名](#n-技能锚点) | 类型 | 一句话描述 |
```

然后在文档正文中追加新的技能章节，保持与现有章节风格一致：

- 一段简介（1-3 句话）
- 核心特征表格
- 文件结构树
- 使用方式说明

### Step 3: 提交并推送

```bash
git add -A
git commit -m "Add skill: <skill-name>"
git push origin main
```

**所有 commit message 使用英文**，格式为 `Add skill:` / `Update skill:` / `Fix:` / `Docs:`。

---

## Git 操作规范

| 操作 | 命令 |
|------|------|
| 查看状态 | `git status` |
| 暂存所有变更 | `git add -A` |
| 提交 | `git commit -m "<message>"` |
| 推送 | `git push origin main` |

### 注意事项

- **提交前确保** `README.md` 已同步更新
- `.DS_Store` 已在 `.gitignore` 中，不会被提交
- 大文件（>10MB）不要提交，如果必须，使用 Git LFS
- 提交前运行 `git status` 确认变更范围合理

---

## 维护原则

1. **README 是唯一的真相源** — 仓库包含哪些技能、每个技能的摘要，以 README.md 为准
2. **每次增删改技能必须同步更新 README**
3. **技能目录内保持自描述** — 每个技能目录内有自己的 README.md，详细说明该技能
4. **不要跨技能引用文件** — 各技能目录保持独立，互不依赖
