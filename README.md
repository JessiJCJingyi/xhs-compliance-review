# xhs-compliance-review

Zero-API Xiaohongshu/Rednote copy compliance quick-review skill.

This skill screens Chinese social copy for common Xiaohongshu risk patterns such as:

- prohibited or sensitive terms
- off-platform traffic guidance
- exaggerated marketing claims
- medical/beauty efficacy claims
- money-making and gray-market phrasing
- investment advice, return promises, stock-picking, and unsupported performance metrics

It uses a local JSON term list and a local feedback log. It does not submit copy to third-party checking services.

## Install

Install the skill folder with your agent/skill manager, for example:

```bash
openclaw skills install ./xhs-compliance-review --agent main --as xhs-compliance-review
```

## Use

Ask your agent:

```text
小红书合规快审：
<paste copy here>
```

The skill returns:

- verdict: 可以发 / 修改后发 / 禁止发
- hit list by severity
- term-list version and update date
- replacement suggestions
- a compliance-safe draft
- a more natural Chinese rewrite
- manual-review notes

## Local Scanner

```bash
python3 xhs-compliance-review/scripts/review_xhs_copy.py --text "这款 AI 投研神器准确率第一，下一只牛股已经选出来了，私信拿注册链接。"
```

## Feedback

Record a limited or risky case:

```bash
python3 xhs-compliance-review/scripts/record_feedback.py --type limited_case --text "<copy>" --phrase "<suspected phrase>"
```

Record a false positive:

```bash
python3 xhs-compliance-review/scripts/record_feedback.py --type false_positive --phrase "<phrase>"
```

Feedback-derived limited-case phrases participate in future scans.

## Update Public Rule Metadata

```bash
python3 xhs-compliance-review/scripts/update_public_rules.py
```

To import manually reviewed candidate terms:

```bash
python3 xhs-compliance-review/scripts/update_public_rules.py --candidate-json ./candidate_terms.json
```

## Important Limits

This is a practical guardrail, not legal advice and not an official Xiaohongshu policy endpoint. Xiaohongshu does not publish a complete real-time banned-word API. Review risky finance, medical, commercial, and relationship-disclosure content manually before publishing.

Do not scrape private databases, bypass login/paywalls, or submit confidential copy to third-party checkers without explicit consent.
