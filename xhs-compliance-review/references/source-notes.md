# Free Web Checker Source Notes

Use these pages as public reference inspiration for the local zero-API rule categories. Do not copy private word databases, bypass login/paywalls, or automate form submission unless the user explicitly accepts that service's terms and data handling.

## 账号帮

URL: https://www.zhanghaobang.cn/tools/word-checker

Useful public notes:
- Supports 小红书, 抖音, 通用广告法.
- Shows high/medium risk and replacement suggestions.
- States that checking is completed in the user's browser and copy is not uploaded.
- Public categories include 敏感词, 违规词, 极限词, 引流词, 医疗功效词, 广告法风险词.

## 违禁查

URL: https://weijincha.com/xhs/

Useful public notes:
- Lists common Xiaohongshu risk categories: 诱导与引流, 虚假与夸大, 医美与功效风险, 其他敏感词.
- Example public terms include 求关注, 私信, VX, 公众号, 淘宝, 购买, 链接, 全网第一, 100%有效, 治疗, 消炎, 赚钱, 兼职, 刷单, 高仿, 复刻.

## 薯小二

URL: https://xhs.jvxiao.cn/

Useful public notes:
- Provides 敏感词检测, 标题生成, 收录检测, 文案排版.
- Free tier has daily limits; paid tiers advertise daily wordlist updates.
- Treat as optional manual verification, not as the default skill backend.

## 小红书聚光审核规则

URL: https://ad.xiaohongshu.com/next_help/docs/8dc5bd9c45c9a90cb9912f3400d43f92

Use as official advertising-review context when copy is ad-like, product-led, commercial, or conversion-oriented.

Public check on 2026-08-10 found the page marked updated 2026-03-23. It explicitly covers
obfuscated off-platform contact prompts (for example “V我”, “主页联系我”, “头像有微”),
unsupported platform endorsement, authorization, factual/data evidence, and industry qualification.

## 蒲公英内容审核规范

URL: https://pgy.xiaohongshu.com/help/detail?id=6495c527d1eedeeb48fb18b1f875650e&userType=4

Public check on 2026-08-10 found the page dated 2026-07-15. It explicitly restricts absolute
product/service guarantees such as “完全有效”, “适用于所有人”, “永远不出错”, and “毫无缺陷”.

## 专业号认证规则规范

URL: https://ad.xiaohongshu.com/next_help/docs/195c5fe505c71b4b0335a2fe0d61d8e0

Public check on 2026-08-10 found the page updated 2026-07-22. Strong-qualification industries,
including finance, require matching certification for service or marketing content. Treat this as
manual-review context rather than a blanket banned-word list.

## 蒲公英不正当商业竞争治理公告

URL: https://pgy.xiaohongshu.com/help/detail?id=8c0b127f03a949d71f1f218a55e7d7f6&userType=4

Public check on 2026-08-10 found the announcement dated 2026-07-19. It identifies unsupported
competitor disparagement, unfair “踩一捧一” comparisons, and poaching prospects through competitor
comments or private messages as governed commercial conduct.

## 蒲公英帮助中心

URL: https://pgy.xiaohongshu.com/faq

Public check on 2026-08-10 confirmed the public index links the content-review rules, legal
requirements, community covenant, and commercial-governance announcements used above.

## Weekly check: 2026-08-17

- Rechecked all eight configured public sources. The four core official/semiofficial pages retained
  the same public dates seen on 2026-08-10: 聚光 2026-03-23, 蒲公英内容审核 2026-07-15,
  专业号认证 2026-07-22, and 不正当商业竞争治理 2026-07-19.
- The 蒲公英内容审核规范 publicly lists financial-investment expressions including 包回报、投资回报、
  保底收益、返本销售、承诺保底、保本稳赚、无风险回报、快速回报、高收益回报、固定回报、年化收益、
  升值、众筹. Added the unambiguous return-promise phrases to the formal local terms. Kept 升值 and
  众筹 as candidates because exact-match scanning cannot reliably distinguish neutral discussion from solicitation.
- The public third-party pages were used only to confirm their visible category/function descriptions. No ARTi
  copy was submitted, and no private, login-gated, paid, or rate-limited word list was accessed.

## Weekly check: 2026-08-24

- Rechecked all eight configured public sources. The four core official/semiofficial pages still show
  the same public dates: 聚光 2026-03-23, 蒲公英内容审核 2026-07-15, 专业号认证
  2026-07-22, and 不正当商业竞争治理 2026-07-19. No newly dated rule or substantive
  rule change was found.
- The 蒲公英帮助中心 index still exposes the existing review and governance documents. Its visible
  categories did not provide a new, sufficiently specific term or rule beyond the current formal and
  candidate sets.
- The three public third-party pages were checked only for visible category/function changes. No ARTi
  copy was submitted, and no private, login-gated, paid, or rate-limited word list was accessed.
- No formal terms or candidate terms were added. Existing candidates remain pending contextual review:
  `+V`, `主页有微`, `竞品质量差`, `升值`, and `众筹`.

## Weekly check: 2026-09-07

- Rechecked all eight configured public sources. The accessible official/semiofficial pages and public
  search/page snapshots did not expose a newly dated or substantively changed rule beyond the prior
  baseline: 聚光 2026-03-23, 蒲公英内容审核 2026-07-15, 专业号认证 2026-07-22,
  and 不正当商业竞争治理 2026-07-19.
- Some official pages remained dynamic or intermittently timed out through the public reader, so this
  run does not claim a complete real-time platform rule snapshot. No ambiguous observation was promoted
  into the formal term list.
- The three third-party pages were checked only for publicly visible categories and feature descriptions.
  No ARTi copy was submitted, and no private, login-gated, paid, or rate-limited word list was accessed.
- No formal or candidate terms were added. Existing candidates remain pending contextual review:
  `+V`, `主页有微`, `竞品质量差`, `升值`, and `众筹`.

## Weekly check: 2026-09-28

- Attempted all eight configured URLs. Direct reads of four official documents timed out or returned an empty dynamic shell; the 蒲公英 FAQ also returned no readable body. Agent Reach's Jina route failed DNS resolution. Official-domain search snapshots supplied the evidence below; this is a partial public check, not a live exhaustive platform snapshot.
- 聚光总则 snapshot retains 2026-03-23. 蒲公英内容审核规范 now displays 2026-08-19 02:22:35; 专业号认证规则 displays 2026-08-02; competition governance displays 2026-07-31 09:34:32. These differ from previous observations, but no archived full-text baseline exists to establish when individual clauses changed. Do not describe them as newly issued this week.
- Added three explicitly listed product-promotion guarantees to the local conservative formal list: 无任何负面问题、超越所有竞争产品、所有情况适用. These are contextual screening triggers, not universal banned strings. Quotations and negations still need human review.
- Added dd我、看我主页、看我置顶 as contextual off-platform-guidance candidates and 红黑榜 as an unfair-comparison candidate. No automatic promotion; previous five candidates remain pending.
- Added certification context to manual review: own-entity industry qualifications and the public notice's licence-upload restrictions (effective 2026-06-30). This is not a copy keyword rule.
- 账号帮、违禁查、薯小二 public pages were readable. No sufficiently supported new official rule was inferred from their tool marketing. No copy submitted, private database copied, or login/member/quota restriction bypassed. Homophone substitutions are not evidence of compliance.
- The last persisted audit before this run was 2026-09-07, despite scheduler metadata listing a 2026-09-21 run; this check does not reconstruct missing runs.
- Validation: 112 formal terms and 9 candidates parse successfully. High-risk sample returned 禁止发 with 5 expected hits; neutral sample returned 可以发 with zero hits; safe ARTi sample returned 修改后发 only for relationship-disclosure review. quick_validate.py passed.
- OpenClaw reinstall attempted but failed (exit 1): EPERM creating the installation staging directory under ~/.openclaw/workspace/skills; readonly state database warnings also occurred. Local source is updated; installed copy is not confirmed updated. This automation cannot request elevated permissions.

## Weekly check: 2026-10-05

- Attempted all eight configured public URLs. Official direct reads timed out or returned an empty dynamic shell; Jina Reader failed DNS resolution. Official-domain search snapshots supplied the following observations. This is a partial public-source check, not an official real-time or exhaustive rule snapshot.
- Observed document dates: 聚光总则 2026-03-23; 蒲公英内容审核规范 2026-09-22 09:54:22; 专业号认证 2026-08-02; 不正当商业竞争治理 2026-07-31 09:34:32. The content-review date differs from the 2026-08-19 date observed last run. No archived full-text baseline establishes which clauses changed or when; do not call this a newly issued rule this week.
- The 蒲公英 FAQ search snapshot continues to list review, qualification, community and commercial-governance documents. Reviewed guarantee, off-platform guidance, comparison and qualification passages provide no sufficiently established new term or category for promotion in this run.
- 账号帮、违禁查、薯小二 public descriptions were readable and used only as category/function references. Their marketing claims and substitution suggestions are not official evidence of safety. No ARTi copy was submitted, no private database copied, and no login/member/quota restriction bypassed.
- No formal or candidate terms added. Formal version remains 2026-09-28.manual-3 (112 terms); updated_at and last_public_source_check_at are 2026-10-05 and all eight public_sources are retained. Nine contextual candidates remain pending: +V、主页有微、竞品质量差、升值、众筹、dd我、看我主页、看我置顶、红黑榜.
- Validation: both JSON files parsed; high-risk sample returned 禁止发 with five expected hits; neutral sample returned 可以发 with zero hits; safe ARTi sample had zero hits and only the existing relationship-disclosure note. quick_validate.py passed. Agent Reach update check failed DNS after three retries.
- OpenClaw reinstall failed (exit 1): EPERM creating ~/.openclaw/workspace/skills/.openclaw-install-stage-* and readonly state database warnings. Installed copy is not confirmed updated. The automation permission policy forbids elevation; rerun the authorized install from a writable environment.

## Weekly check: 2026-10-12

- Attempted all eight requested URLs. 聚光总则 and 蒲公英内容审核 returned empty dynamic shells; 专业号认证、竞争治理、FAQ and 薯小二 timed out. Jina route failed DNS. Official-domain search recovered content-review (2026-09-22 09:54:22), certification (2026-08-02), and FAQ snapshots. These two observed dates match last run. 聚光总则 excerpts were available but its date was not independently reconfirmed; competition-governance content/date could not be independently reverified this week. Previous recorded dates are historical observations only. No exhaustive current-rule claim or full-text change comparison is made.
- FAQ's industry-qualification route exposed an additional official page: https://pgy.xiaohongshu.com/help/detail?id=e0cbd1954fe7364ea0201ba2099affdf&userType=4 . Its displayed date is 2026-10-09 03:25:59. The medical-health cooperation announcement concerns qualification checks and commercial recommendation/efficacy standards; execution timing and detailed standards remain subject to a separate platform notice. The search tool's crawl/publication labels are inconsistent, so the displayed document date is an observation, not proof of issuance this week.
- Added only candidate 医生推荐 under 医疗健康合作笔记推荐背书. It needs commercial-context and execution-notice review and is not scanned as a formal banned phrase. Do not generalize this scoped announcement to all ordinary notes or ARTi financial copy. Existing nine candidates remain pending.
- 账号帮 and 违禁查 public descriptions were readable; 薯小二 search snapshot showed public features and quota/member information only. No sufficiently supported new formal phrase or safe replacement was established. No ARTi copy submitted, private term database copied, or login/member/quota restriction bypassed.
- Formal terms remain 112 and version 2026-09-28.manual-3; updated_at and last_public_source_check_at set to 2026-10-12 with all eight configured public_sources retained. Additional discovery is documented here and in candidate data; it is not a formal source promotion.
- Validation: both JSON files parsed (112 formal terms, 10 candidates); high-risk sample returned 禁止发 with five red hits; neutral safe sample returned 可以发 with zero hits; skill validator passed. OpenClaw main-agent reinstall succeeded after authorized elevated retry; directory comparison matched excluding OpenClaw metadata. Agent Reach update check failed DNS after three retries.


## Monthly manual check: 2026-11-01

- Manually ran the monthly task at the user's request. Attempted all eight configured public URLs. The five official pages returned dynamic shells with no readable body. Agent Reach's Jina Reader route failed DNS resolution; web search/page-reader fallback was used. This is a partial public-source check, not a complete current-rule snapshot.
- Official-domain search snapshots recovered 聚光总则 (displayed update 2026-03-23), 专业号认证 (2026-08-02), and the 蒲公英 FAQ index. The first two dates match historical observations. Content-review and competition-governance document bodies/dates could not be independently reverified this run; previous dates remain historical only. No full-text change comparison or conclusion that rules are unchanged is justified.
- Additional official discovery: https://ad.xiaohongshu.com/next_help/docs/cfa457375a0dffd3bd04453f42b9731e (专业号合规经营指南：自查与规范手册, displayed 2026-06-08). Its qualification, factual marketing and account-operation guidance is manual-review context. It is not established as a newly issued rule, and was not converted into blanket banned phrases.
- 账号帮、违禁查、薯小二 public descriptions were readable. No sufficiently supported new formal phrase, category, or safe replacement was established. Tool marketing claims and homophone substitutions are not official evidence of compliance. No ARTi copy submitted, private database copied, or login/member/quota restriction bypassed.
- No formal or candidate terms added. Version remains 2026-09-28.manual-3 (112 formal terms); all 10 existing candidates remain pending contextual/execution-notice review. Updated only formal check metadata to 2026-11-01; candidate metadata remains unchanged because candidates were not modified.
- Validation: high-risk sample returned 禁止发 with the five expected red hits; neutral safe sample returned 可以发 with zero hits; quick_validate.py passed. Scanner rewrite is still a rough draft and is not publishable without the humanizer/manual review required by SKILL.md.
