# Novelist Lite

一个用于 Codex 的轻量 Skill：从**单本小说 / 单本作品**中蒸馏叙事技艺，生成一个可复用的作家风格 `SKILL.md`。

它适合这样的任务：

- 从一部长篇小说中提炼叙事模型、语言指纹和创作规则
- 把一部作品的“写法”整理成可调用的 Codex Skill
- 为写作、续写、改写、文风分析生成一个专用叙事人格

它不做这些事：

- 多作家融合
- 模糊需求推荐
- 长期阅读灵感库
- 拆书笔记系统
- `AGENTS.md` 或 `system_prompt.md` 生成
- 收集、分发或内置任何小说原文

## 安装

把 skill 复制到 Codex skills 目录：

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/novelist-lite "${CODEX_HOME:-$HOME/.codex}/skills/"
```

重启或重载 Codex 后，使用：

```text
$novelist-lite
```

## 使用示例

```text
$novelist-lite 请从 /path/to/novel.txt 蒸馏一个 writer-novelist skill，输出到 ~/.codex/skills/writer-novelist
```

```text
$novelist-lite 这是一部中篇小说文本，请只基于这部作品生成一个可用的 SKILL.md
```

生成结果通常是：

```text
[skill-name]/
└── SKILL.md
```

## 设计原则

Novelist Lite 只关心一件事：从单本作品中提炼 HOW，而不是复述 WHAT。

它会要求目标 skill：

- 不引用原文
- 不摘抄对话
- 不复述长段情节
- 不把通用建议伪装成独门技法
- 明确说明取样范围和分析限制

## 校验

运行基础校验：

```bash
python3 scripts/validate_skill.py skills/novelist-lite
```

校验内容包括：

- `SKILL.md` 是否存在
- YAML frontmatter 是否只包含 `name` 和 `description`
- skill name 是否符合小写连字符规范
- description 是否在合理长度内

## 目录结构

```text
.
├── README.md
├── LICENSE
├── scripts/
│   └── validate_skill.py
└── skills/
    └── novelist-lite/
        ├── SKILL.md
        └── agents/
            └── openai.yaml
```

## 版权与合规

本仓库只提供蒸馏流程，不包含任何受版权保护的小说文本。

使用者应只分析自己有权处理的文本。生成的目标 `SKILL.md` 应只包含抽象后的写作技法、叙事规则和风格边界，不应包含原作句子、段落、对话或可替代原文阅读的情节复述。

## License

MIT
