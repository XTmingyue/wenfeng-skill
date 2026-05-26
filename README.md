# 文风.skill

> *从一本书里，提炼可复用的叙事与文风。*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Compatible-green)](https://agentskills.io)
[![Skills](https://img.shields.io/badge/Skills-Portable-blue)](#安装)

**文风.skill 是一个单本作品写作 Skill 蒸馏器。**

给它一部小说文本或文件路径，它会提炼这部作品的叙事模型、语言指纹、母题意象、人物塑造、情节技法和创作边界，生成一个可直接调用的写作 `SKILL.md`。

它不复述剧情，不摘抄原文，不帮你盗版一部书。它只做一件事：把作品背后的“怎么写”变成可执行的创作规则。

[效果示例](#效果示例) · [安装](#安装) · [使用](#使用) · [它蒸馏了什么](#它蒸馏了什么) · [工作原理](#工作原理) · [版权与边界](#版权与边界)

---

## 效果示例

输入：

```text
$wenfeng-skill 请从 /path/to/novel.txt 蒸馏一个 qingdi-novelist skill，输出到 <skills-dir>/qingdi-novelist
```

输出：

```text
qingdi-novelist/
└── SKILL.md
```

生成的 `SKILL.md` 会包含类似这样的结构：

```text
叙事模型：气数账本、重生先知、制度化修仙、阶梯扩容
语言指纹：句式节奏、词汇光谱、对话风格、感官偏好
母题意象：天命、体制、世界本源、五德循环
创作规则：如何开篇、如何升级冲突、如何收束
不可写：无成本突破、扁平反派、空泛设定、万能先知
诚实边界：分析范围、取样限制、不能代表作者全部阶段
```

然后你可以直接调用新生成的 skill：

```text
$qingdi-novelist 帮我写一个县试前夜的开篇场景，要有制度压力和命运转折。
```

这不是“仿写几句像原文的话”。文风.skill 追求的是把作品内部反复出现的叙事机制提炼成一个可迁移的写作引擎。

---

## 安装

文风.skill 基于开放的 Agent Skills 目录规范：根目录有 `SKILL.md`，即可被兼容运行环境发现。

### 方式一：一行命令

如果你使用支持 Agent Skills 的安装器：

```bash
npx skills add xiongtao/wenfeng-skill
```

如果你的 GitHub owner 不是 `xiongtao`，请把命令中的 owner 替换成实际仓库地址。

### 方式二：手动安装

把仓库 clone 到你使用的运行环境的 skills 目录：

```bash
git clone https://github.com/xiongtao/wenfeng-skill <skills-dir>/wenfeng-skill
```

```bash
mkdir -p <skills-dir>
git clone <repo-url> <skills-dir>/wenfeng-skill
```

重启或重载运行环境后，调用：

```text
$wenfeng-skill
```

### 方式三：直接粘贴

如果你的工具暂不支持自动加载 Skill，也可以把 `SKILL.md` 内容直接粘贴进对话。它本质是一份带 YAML frontmatter 的 Markdown 指令。

---

## 使用

从本地小说文本蒸馏：

```text
$wenfeng-skill 请从 /Users/me/novels/example.txt 蒸馏一个 example-novelist skill，输出到 <skills-dir>/example-novelist
```

从粘贴文本蒸馏：

```text
$wenfeng-skill 下面是一部中篇小说，请只基于这部作品生成一个可用的 SKILL.md：

[粘贴文本]
```

指定输出名：

```text
$wenfeng-skill 把这本书蒸馏成 river-city-novelist，输出到 <skills-dir>/river-city-novelist
```

---

## 它蒸馏了什么

文风.skill 不只提取“像不像”的表层文风，它会把一部作品拆成六层可执行规则：

| 层次 | 提取内容 | 目的 |
|---|---|---|
| 叙事模型 | 反复出现的结构手法 | 让新故事按同一套引擎运转 |
| 语言指纹 | 句式、节奏、词汇、对话、感官偏好 | 让文本气质稳定 |
| 母题意象 | 主题、隐喻、意象系统 | 让作品有内在精神轴线 |
| 人物塑造 | 原型、弧线、关系推进 | 让人物不是只换名字 |
| 情节技法 | 开篇、转场、悬念、冲突、收束 | 让创作规则能落到章节 |
| 风格边界 | 不可写、诚实边界、分析范围 | 防止过拟合、胡编和侵权 |

一个规则要进入最终 `SKILL.md`，至少要满足：

1. **复现性**：在同一作品中不止一次出现。
2. **生成力**：能指导面对新场景时怎么写。
3. **排他性**：不是所有小说都会使用的普通建议。

---

## 工作原理

输入一部作品后，文风.skill 会做五件事：

**1. 确认语料**  
只处理单本作品。多部作品时先让用户选一部主作品。

**2. 阅读与抽样**  
短篇和中篇尽量完整阅读；长篇优先阅读开篇、关键中段、高潮段和结尾，用户指定章节优先。

**3. 提炼技法**  
从叙事模型、语言指纹、母题意象、人物塑造、情节技法、不可写和诚实边界七个维度提取规则。

**4. 过滤通用建议**  
只保留可复现、可生成、相对有排他性的技法。没有把握的内容降级或删除。

**5. 生成 Skill**  
输出一个目标 skill 目录，最终只交付：

```text
[skill-name]/
└── SKILL.md
```

---

## 不做什么

- 不做多作家融合。
- 不做模糊需求推荐。
- 不做长期阅读灵感库。
- 不生成 `AGENTS.md` 或 `system_prompt.md`。
- 不收集、分发或内置任何小说原文。
- 不把原作句子、段落、对话或可替代阅读的情节复述写进目标 skill。

---

## 仓库结构

```text
wenfeng-skill/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── README.md
└── LICENSE
```

`SKILL.md` 是必需文件。`agents/openai.yaml` 是可选的元数据文件，可用于提供展示名、短描述和默认调用提示。

---

## 版权与边界

本仓库只提供蒸馏流程，不包含任何受版权保护的小说文本。

使用者应只分析自己有权处理的文本。生成的目标 `SKILL.md` 应只包含抽象后的写作技法、叙事规则和风格边界，不应包含原作句子、段落、对话或可替代原文阅读的情节复述。

文风.skill 不是作者本人，也不保证复现作者全部创作阶段。它生成的是基于单本作品的风格快照。

---

## 灵感来源

README 的呈现方式参考了这些优秀的 Skill 项目：

- [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill)
- [Schlaflied/hr-skill](https://github.com/Schlaflied/hr-skill)
- [ybq22/supervisor](https://github.com/ybq22/supervisor)

---

## License

MIT
