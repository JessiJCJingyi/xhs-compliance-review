---
name: xhs-compliance-review
description: Xiaohongshu/Rednote copy compliance quick-review for Chinese social posts, finance-adjacent posts, product marketing copy, and creator captions, with local updatable term JSON, feedback capture, and a final natural-Chinese rewrite pass to reduce AI-sounding rewrite artifacts. Use when the user asks to check 小红书文案, 红书帖, 图文卡文案, 标题, caption, hashtags, or marketing copy for 违禁词, 敏感词, 平台合规, 金融合规, 荐股风险, 收益承诺, 导流风险, or asks to “筛掉违禁词/过一遍合规/快审/发布前检查/改得自然一点/减少AI味”. Also use when the user says “这条被限流了”, “这条通过了”, “这个词误杀”, “把这个词加入小红书风险词库”, or wants to update/learn from compliance feedback.
---

# Xiaohongshu Compliance Review

Run a fast pre-publish review for Xiaohongshu/Rednote copy. The goal is to reduce obvious platform, commercial, and finance-adjacent compliance risk, then make the safe rewrite sound like natural Chinese social copy, not a mechanical word replacement. This is a zero-API local system with an updatable term file and team feedback log. It is not legal advice and does not guarantee platform approval.

## Quick Workflow

1. Put the user's text into the scanner:

```bash
python3 codex-skills/xhs-compliance-review/scripts/review_xhs_copy.py --text '<文案>'
```

For longer drafts, write the text to a temporary file and use `--file`.

2. Read `references/rules.md` when the result is yellow/red, when the topic is finance/investing, or when manual judgment is needed. Read `references/source-notes.md` when explaining where the free/local rule categories came from.

3. Treat the scanner's `建议改写` as a rough compliance-safe draft, not the final copy. Apply `humanizer-zh` principles before presenting the final version:
- Remove stiff replacement artifacts such as awkward noun piles, repeated “风险/不确定性”, and literal word-for-word swaps.
- Keep the risk reduction intact. Do not reintroduce hit words, trading instructions, return promises, hard CTAs, or exaggerated claims.
- Make the copy feel like a person writing on Xiaohongshu: specific, conversational, lightly opinionated, and not slogan-heavy.
- Avoid AI-ish patterns such as “不仅…而且…”, “本质上”, “赋能”, “打造闭环”, “极致体验”, “开启新篇章”, and over-neat three-part structures.

4. Return:
- Verdict: `可以发`, `修改后发`, or `禁止发`
- Hit list grouped by severity
- Term-list version and update date
- Why each hit is risky
- A cleaned version that removes or softens the risky wording
- A `自然化可发布版本` after the humanizer-zh pass
- Remaining manual-review notes, especially for investing, securities, sign-up links, commercial disclosure, or employee/partner relationship disclosure

## Feedback Workflow

When the user reports a post outcome, record it locally before giving advice.

Limited or risky case:

```bash
python3 xhs-compliance-review/scripts/record_feedback.py --type limited_case --text '<原文案>' --phrase '<可疑词或短语>' --severity yellow --category '账号反馈'
```

False positive:

```bash
python3 xhs-compliance-review/scripts/record_feedback.py --type false_positive --phrase '<误杀词>' --reason '用户反馈该词在此账号/语境下可发布'
```

Passed case:

```bash
python3 xhs-compliance-review/scripts/record_feedback.py --type passed_case --text '<已通过文案>'
```

Use feedback carefully:
- A `limited_case` phrase is included in future scans as a feedback-derived risk term.
- A `false_positive` does not automatically remove a term; it tells Codex to mention possible overblocking and use judgment.
- Do not store private account credentials, links, phone numbers, or customer data in feedback logs.

## Updating The Local Rule Base

Core terms live in `data/xhs_terms.json`; do not add new risk terms by editing Python code. Use `scripts/update_public_rules.py` after manually reviewing public-source candidates:

```bash
python3 codex-skills/xhs-compliance-review/scripts/update_public_rules.py --candidate-json /path/to/reviewed-candidates.json
```

Run without candidates to stamp a public-source check date:

```bash
python3 codex-skills/xhs-compliance-review/scripts/update_public_rules.py
```

## Verdict Rules

- `禁止发`: Any hard financial solicitation, explicit trading instruction, guaranteed return, paid stock-picking, real-time call, unapproved performance metric, or Mainland-facing purchase/sign-up CTA.
- `修改后发`: Sensitive platform words, exaggerated claims, soft investment direction, private-message/group guidance, or unclear product capability claims.
- `可以发`: No detected hard/yellow risks and the copy stays informational, personal-experience based, or methodology-focused.

## Finance And Disclosure Defaults

For finance-adjacent, securities, investing, product-affiliated, or commercial copy:
- Keep `不构成投资建议` or equivalent disclaimer for finance-adjacent posts.
- Prefer “记录判断 / 复盘依据 / 辅助研究” over “推荐买卖 / 预测收益 / 选出牛股”.
- Do not invent metrics, endorsements, prices, investment outcomes, accuracy rates, or product capabilities.
- If the author is an employee, founder, investor, partner, affiliate, or otherwise related to the promoted product/company, flag whether a relationship disclosure is needed.

## Natural Rewrite Example

If the scanner produces a rough sentence like:

> 这款 AI 投研工具历史观察可能有帮助，一个待验证的研究线索已经选出，评论区交流拿。

Do not return it as-is. Humanize it into something like:

> 我最近在用一个投研工具记录自己的判断。它更适合把“我为什么这么看”“后面怎么验证”这些依据留住，而不是直接告诉你买什么。仅分享研究流程，不构成投资建议。

The humanized version should be clean enough for compliance review and natural enough for a Xiaohongshu reader.

## Tool Notes

The bundled script is deterministic and conservative. It catches known risky phrases and common variants; Codex should still use judgment for context, screenshots, hashtags, images, and comments.

This skill is the zero-API path. Do not call third-party web checkers unless the user explicitly asks for external verification and accepts sending the copy to that service.
