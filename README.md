<div align="center">

# 文风.skill

**从一本书里，提炼可复用的叙事与文风。**

<p>
  <a href="LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
  <a href="https://agentskills.io"><img alt="Agent Skills" src="https://img.shields.io/badge/Agent%20Skills-Compatible-green"></a>
  <a href="#安装"><img alt="Skills" src="https://img.shields.io/badge/Skills-Portable-blue"></a>
</p>

<p>
  <strong>文风.skill 是作品写作 Skill 蒸馏器。</strong>
</p>

<p>
  给它一部小说文本或文件路径，它会提炼叙事模型、语言指纹、母题意象、人物塑造、情节技法和创作边界，生成一个可直接调用的写作 <code>SKILL</code>。
</p>

<p>
  <a href="#快速开始">快速开始</a> ·
  <a href="#它解决什么问题">它解决什么问题</a> ·
  <a href="#它蒸馏什么">它蒸馏什么</a> ·
  <a href="#安装">安装</a> ·
  <a href="#边界">边界</a>
</p>

</div>

---

## 它解决什么问题

你读完一本小说，常常能说出“它很好看”，却很难说清楚：

- 它到底靠什么推进故事？
- 它的文风是句子像，还是结构像？
- 它的人物关系为什么成立？
- 它的高潮为什么有力？
- 能不能把这种写法变成一个可复用的创作 Skill？

**文风.skill 要做的，就是把这些模糊感觉变成可执行规则。**

它不复述剧情，不摘抄原文，也不把一部书压缩成情节梗概。

它只提炼作品背后的 HOW：这本书是怎么写出来的。

---

## 它蒸馏什么

文风.skill 不只提取表层“文风”。它会把单本作品拆成六层可执行规则：

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

## 安装

### 方式一：让 agent 安装

告诉你正在使用的 agent：

```text
帮我安装这个 skill：https://github.com/XTmingyue/wenfeng-skill
```

### 方式二：CLI 安装

```bash
npx skills add XTmingyue/wenfeng-skill
```

### 方式三：手动安装

把仓库 clone 到你使用的运行环境的 skills 目录：

```bash
mkdir -p <skills-dir>
git clone https://github.com/XTmingyue/wenfeng-skill <skills-dir>/wenfeng-skill
```

### 方式四：直接粘贴

如果你的工具暂不支持自动加载 Skill，也可以把 `SKILL.md` 内容直接粘贴进对话。它本质是一份带 YAML frontmatter 的 Markdown 指令。

---

## 使用

### 从本地小说文本蒸馏文风

```text
/wenfeng-skill 请从 path.txt 蒸馏一个 novel-writer skill，输出到 <skills-dir>/novel-writer
```

### 用蒸馏后的文风创作

```text
/novel-writer 帮我写一个县试前夜的开篇场景，要有制度压力和命运转折。
```

---

## 工作原理

### 1. 确认语料

只处理单本作品。多部作品时，先选择一部主作品。

### 2. 阅读与抽样

短篇和中篇尽量完整阅读。长篇优先阅读开篇、关键中段、高潮段和结尾，用户指定章节优先。

### 3. 提炼技法

从叙事模型、语言指纹、母题意象、人物塑造、情节技法、不可写和诚实边界七个维度提取规则。

### 4. 过滤通用建议

只保留可复现、可生成、相对有排他性的技法。没有把握的内容降级或删除。

### 5. 生成 Skill

输出一个可安装、可调用、可继续写作的目标 `SKILL.md`。

---

## 边界

本仓库只提供蒸馏流程，不包含任何受版权保护的小说文本。

使用者应只分析自己有权处理的文本，生成的目标 `SKILL.md` 应只包含抽象后的写作技法、叙事规则和风格边界，不应包含原作句子、段落、对话或可替代原文阅读的情节复述。

文风.skill 不是作者本人，也不保证复现作者全部创作阶段。

它生成的是基于单本作品的风格快照。

---

## 灵感来源

本项目参考了这些优秀的 Skill 项目：

- [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill)
- [alchaincyf/nuwa-skill](https://github.com/alchaincyf/nuwa-skill)

---

## License

MIT
