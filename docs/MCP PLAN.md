# felix-to-Skills 实施计划

> 目标：构建一个可共享、可扩展的 Agent 技能仓库，让多个 Kimi Code CLI Agent 实例共用同一套 Skill 知识层与 MCP 工具层。
>
> 基于现有 `sales-mcp` 项目扩展，建立标准化的 Skill Registry 体系。

---

## 一、现状分析

### 1.1 已有资产
| 资产 | 位置 | 说明 |
|------|------|------|
| MCP 服务器 | `/Users/mac/sales-mcp` | 基于 FastMCP，含 20+ 工具，覆盖销售数据查询/导入/清洗/报表 |
| MCP 配置 | `~/.kimi/mcp.json` | 本地 stdio 方式启动 sales-mcp |
| Skill 目录 | `~/.kimi/skills/` | 当前仅有 design-refs、html-report、karpathy-guidelines 等 |
| Skill 配置 | `~/.kimi/config.toml` | `merge_all_available_skills = true` |

### 1.2 核心痛点
- **Skill 与工具分离**：sales-mcp 的 instructions 硬编码在 Python 中，Agent 不通过 Skill 系统了解何时该调用这些工具
- **无法共享**：skills 散落各处，同事机器无法快速复用同一套业务知识 + 工具链
- **扩展成本高**：新增业务领域时，需要同时改 MCP Server 代码 + 手动维护 Prompt，没有统一规范

---

## 二、架构设计

### 2.1 双层模型

```
┌─────────────────────────────────────────────────────────────┐
│                      Skill Registry (Git)                    │
├─────────────────────────────┬───────────────────────────────┤
│       知识层 (Skills)        │        工具层 (MCP Servers)    │
├─────────────────────────────┼───────────────────────────────┤
│ • SKILL.md — 触发逻辑        │ • server.py — 工具实现         │
│ • references/ — 领域知识     │ • db.py — 数据访问             │
│ • scripts/ — 辅助脚本        │ • cleaner.py — 清洗逻辑        │
│ • assets/ — 模板资源         │ • exporter.py — 导出逻辑       │
└─────────────────────────────┴───────────────────────────────┘
              │                              │
              │  Git clone / pull            │  uv run python -m xxx.server
              ▼                              ▼
┌─────────────────────────────────────────────────────────────┐
│                         Agent 实例                           │
│   ┌──────────────┐          ┌──────────────────────────┐   │
│   │ ~/.kimi/skills│          │      MCP Client           │   │
│   │ (文件系统加载) │          │  (JSON-RPC over stdio)   │   │
│   └──────────────┘          └──────────────────────────┘   │
│          │                              │                   │
│          │  Skill 触发时                │  Tool Call         │
│          ▼                              ▼                   │
│   "用户问销售额 → 加载       query_sales(sql="...")          │
│    sales-analysis SKILL"                                    │
└─────────────────────────────────────────────────────────────┘
```

**设计原则**：
- **知识层与工具层解耦**：Skill 决定"什么时候用、用什么参数"，MCP Server 决定"怎么执行"
- **一份仓库，多处部署**：Git 保证 Skill 知识同步；MCP Server 可在各机器独立安装或通过 SSE 集中服务
- **渐进式加载**：沿用 Kimi Skill 的三级披露机制（metadata → SKILL.md body → bundled resources）

### 2.2 与现有 sales-mcp 的集成关系

```
felix-to-Skills/
├── skills/
│   └── sales-data/                  ← 新增：对应 sales-mcp 的 Skill 知识层
│       ├── SKILL.md                 ← 包含 sales-mcp 所有工具的调用指南
│       └── references/
│           ├── schema.md            ← 数据库表结构文档
│           └── cleaning-guide.md    ← 清洗规则说明
├── mcp-servers/
│   └── sales-mcp/                   ← 迁移：现有 sales-mcp 代码
│       ├── src/sales_mcp/
│       └── pyproject.toml
└── config/
    └── mcp.json.template            ← 统一的 MCP 配置模板
```

`sales-mcp` 作为第一个被纳入 Skill Registry 的 MCP 服务器，承担"标杆"角色，验证整个流程。

---

## 三、目录结构规范

```
felix-to-Skills/
├── README.md                        # 仓库说明、快速开始
├── PLAN.md                          # 本文件
├── .gitignore
│
├── skills/                          # ===== 知识层 =====
│   ├── _template/                   # Skill 创建模板（给新业务用）
│   │   ├── SKILL.md
│   │   └── references/
│   │
│   ├── sales-data/                  # 销售数据分析（对接 sales-mcp）
│   │   ├── SKILL.md
│   │   └── references/
│   │       ├── schema.md            # orders, products, customers, regions 表结构
│   │       ├── cleaning-rules.md    # daily/recycle/members 清洗规则详解
│   │       └── report-templates.md  # HTML/CSV 报表模板说明
│   │
│   └── data-cleaning/               # 通用数据清洗（可复用）
│       ├── SKILL.md
│       └── scripts/
│           └── validate_schema.py
│
├── mcp-servers/                     # ===== 工具层 =====
│   ├── README.md                    # MCP Server 开发规范
│   └── sales-mcp/                   # 现有项目（可保留 Git 历史）
│       ├── src/sales_mcp/
│       │   ├── server.py
│       │   ├── db.py
│       │   ├── importer.py
│       │   ├── exporter.py
│       │   ├── cleaner.py
│       │   └── reports.py
│       ├── pyproject.toml
│       └── INSTRUCTIONS.md          # 从 server.py 解耦的 Agent 指令
│
├── config/                          # ===== 配置层 =====
│   ├── mcp.json.template            # 标准 mcp.json 模板
│   └── sync-skills.sh               # 一键同步脚本（软链接到 ~/.kimi/skills）
│
└── docs/                            # ===== 文档层 =====
    ├── skill-authoring-guide.md     # 如何编写 SKILL.md
    ├── mcp-server-dev-guide.md      # 如何开发/调试 MCP Server
    └── multi-agent-setup.md         # 多机器部署指南
```

---

## 四、实施阶段

### Phase 1: 基础骨架（1-2 天）

**目标**：建立仓库结构，完成 sales-mcp 与 Skill 知识层的首次对接。

| 任务 | 产出 | 负责人 |
|------|------|--------|
| 初始化 Git 仓库 | `felix-to-Skills/` 目录结构 | felix |
| 创建 sales-data Skill | `skills/sales-data/SKILL.md` | felix |
| 迁移 sales-mcp 代码 | `mcp-servers/sales-mcp/` | felix |
| 编写 mcp.json 模板 | `config/mcp.json.template` | felix |
| 编写同步脚本 | `config/sync-skills.sh` | felix |
| 本地验证 | Agent 能正确触发 sales-data Skill 并调用 sales-mcp 工具 | felix |

**sales-data/SKILL.md 核心内容预览**：
- Frontmatter：`name: sales-data`, `description: 销售数据查询、清洗、分析与报表生成。当用户涉及销售订单、产品销量、区域业绩、数据导入导出、经营日报等场景时触发。`
- Body：工具选择决策树（查询 → query_sales/sales_summary/top_products；清洗 → clean_*_tool；报表 → export_to_*_tool/run_external_report_tool）
- References：schema.md（按需加载）

### Phase 2: sales-mcp 重构优化（2-3 天）

**目标**：让 MCP Server 更符合 Skill Registry 的标准化要求。

| 任务 | 说明 |
|------|------|
| 指令外置 | 将 `FastMCP(instructions=...)` 改为读取 `INSTRUCTIONS.md`，支持热更新 |
| 工具分类 | 在 `server.py` 中用注释/分组明确区分：Query / Import / Export / Clean / Report 五类工具 |
| 统一错误格式 | 所有 tool 返回统一 JSON：`{success: bool, data?: any, error?: string, meta?: {...}}` |
| 增加辅助工具 | `health_check()` — 返回数据库状态、表行数、最近数据日期 |
| 配置化 DB 路径 | 支持通过 `MCP_CONFIG_PATH` 读取外部配置，不仅依赖环境变量 |

### Phase 3: 多 Agent 验证（1-2 天）

**目标**：验证"一份仓库，多处运行"的可行性。

| 场景 | 验证内容 |
|------|---------|
| 本机多 Session | 同时开 2 个 Kimi CLI 窗口，都能触发 sales-data Skill，调用同一 sales-mcp 进程 |
| 同事机器部署 | 同事 clone 仓库 → 运行 sync-skills.sh → 复制 mcp.json → 验证工具可用 |
| Skill 更新同步 | 修改 SKILL.md → git push → 同事 pull → 新 Skill 内容生效 |

### Phase 4: 扩展新 Skill（持续）

**目标**：基于模板快速添加新业务领域的 Skill。

候选方向：
- `inventory-mgmt` — 库存管理（可对接新的 inventory-mcp）
- `customer-insight` — 客户分析（基于现有 customers 表扩展）
- `auto-report` — 定时/自动化报表（结合 cron + report 工具）

---

## 五、关键技术细节

### 5.1 Skill 触发与 MCP 工具调用的协作流程

```
用户输入："帮我查一下 2026 年 4 月的销售汇总"

Step 1: Agent 加载所有 Skill metadata
        └─ sales-data 的 description 匹配 "销售汇总" → 触发

Step 2: Agent 读取 skills/sales-data/SKILL.md
        └─ 指南：时间范围汇总 → 优先使用 sales_summary(start_date, end_date)

Step 3: Agent 构造参数，调用 MCP Tool
        └─ JSON-RPC: tools/call → sales_summary("2026-04-01", "2026-04-30", "")

Step 4: sales-mcp 执行 SQL，返回 JSON 结果

Step 5: Agent 解读结果，用自然语言回复用户
```

**关键点**：Skill 里不写具体 SQL，只写"该调哪个工具、参数怎么填"；具体 SQL 由 MCP Server 维护。

### 5.2 同步脚本 `sync-skills.sh` 设计

```bash
#!/bin/bash
# 将仓库 skills/ 目录下的所有 skill 软链接到 ~/.kimi/skills/

SKILLS_ROOT="$(cd "$(dirname "$0")/.." && pwd)/skills"
TARGET_DIR="${HOME}/.kimi/skills"

mkdir -p "$TARGET_DIR"

for skill_dir in "$SKILLS_ROOT"/*; do
    [ -d "$skill_dir" ] || continue
    skill_name=$(basename "$skill_dir")
    target_link="$TARGET_DIR/$skill_name"
    
    # 删除旧链接（如果存在）
    [ -L "$target_link" ] && rm "$target_link"
    
    ln -s "$skill_dir" "$target_link"
    echo "Linked: $skill_name"
done

echo "Skills synced to $TARGET_DIR"
```

### 5.3 MCP 配置模板 `mcp.json.template`

```json
{
  "mcpServers": {
    "sales-mcp": {
      "command": "uv",
      "args": [
        "run",
        "--directory",
        "{{REPO_ROOT}}/mcp-servers/sales-mcp",
        "python",
        "-m",
        "sales_mcp.server"
      ],
      "env": {
        "SALES_DB_PATH": "{{REPO_ROOT}}/mcp-servers/sales-mcp/data/sales.db"
      }
    }
  }
}
```

用户使用时复制为 `mcp.json`，替换 `{{REPO_ROOT}}` 为实际绝对路径。

### 5.4 SSE 模式（未来扩展）

如需从局域网/远程访问，sales-mcp 可支持双模式启动：

```python
# server.py
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--transport", choices=["stdio", "sse"], default="stdio")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    
    mcp.run(transport=args.transport, port=args.port)
```

启动命令：
```bash
# 本机模式（默认）
uv run python -m sales_mcp.server

# 服务模式
uv run python -m sales_mcp.server --transport sse --port 8000
```

---

## 六、里程碑与验收标准

| 里程碑 | 验收标准 |
|--------|---------|
| **M1: 仓库可用** | `felix-to-Skills` 可 clone，包含完整目录结构，README 可执行 |
| **M2: Skill 对接** | 在 Kimi CLI 中输入销售相关问题，自动触发 sales-data Skill，并成功调用 sales-mcp 工具返回正确结果 |
| **M3: 多机验证** | 至少 2 台机器部署成功，Skill 内容通过 Git 同步更新 |
| **M4: 扩展就绪** | 基于 `_template/` 可在 30 分钟内创建一个新的 Skill 并对接任意 MCP Server |

---

## 七、风险与应对

| 风险 | 影响 | 应对 |
|------|------|------|
| MCP 协议版本升级 | 工具接口可能变更 | 锁定 `mcp` Python SDK 版本于 `pyproject.toml`，定期 review 更新日志 |
| Skill 过多导致 context 膨胀 | Agent 加载慢、token 消耗高 | 严格遵循 Progressive Disclosure，metadata 保持精简；大单 skill 拆分为多小 skill |
| 多人同时修改 Skill | 内容冲突 | Skill 内容以业务逻辑为主，减少频繁修改；大改走 PR review |
| MCP Server 进程崩溃 | Agent 工具调用失败 | health_check 工具 + 客户端自动重连机制 |

---

## 八、下一步行动

1. **确认本计划** → 如需调整架构或优先级，在此文件上直接修改
2. **初始化仓库** → `cd /Users/mac/Desktop/felix-to-Skills && git init`
3. **创建 Phase 1 骨架** → 按目录结构创建所有文件夹和初始文件
4. **迁移 sales-mcp** → 将现有代码纳入 `mcp-servers/sales-mcp/`
5. **编写首个 SKILL.md** → 完成 `skills/sales-data/SKILL.md`

---

*计划创建时间：2026-05-12*
*基于：sales-mcp 现状 + Kimi Code CLI Skill 系统规范*
