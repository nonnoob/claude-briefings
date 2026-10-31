# 🗓️ 一周回顾 · 2026-10-31

> 覆盖窗口：2026-10-26 08:25 UTC 至 2026-10-31 11:32 UTC（常规；下周节点按 America/Los_Angeles 日期）

本周要闻：AI 模型与开发工具进入新一轮可用性更新，但开放权重、限定访问、融资目标和实际交割仍须分开看。

## 本周大事

- 【续报】前沿模型的发布承诺陆续落地：Mistral Large 4 从 API 预览走到可下载权重，GPT-6.1 Terra 已进入 Bedrock，Google 也公布此前传闻中的 Carbon；三者当前分别是可自部署、云端正式可用和限定伙伴访问，不能笼统视为全面开放。来源：Mistral https://mistral.ai/news/mistral-large-4-oss/ ；AWS https://aws.amazon.com/about-aws/whats-new/2026/10/openai-gpt-6-1-terra-on-amazon-bedrock/ ；Google https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/
- 【续报】【传闻】【单源】AI 融资进展出现分化：Anthropic 从草案流出进入公开招股材料阶段，另一边 FT 据知情人士称 OpenAI 把本轮目标从 300 亿美元削减至约 200 亿美元；前者尚待发行定价，后者尚待公司确认和实际交割，不应把报道中的目标当作现金到账。来源：Semafor https://www.semafor.com/article/10/27/2026/anthropic-prospectus-cheers-investors-ahead-of-ipo ；Reuters／CNA（转述 FT）https://www.channelnewsasia.com/business/openai-slashes-funding-target-10-billion-amid-tech-rout-ft-reports-6508816
- 【续报】编码 Agent 的长会话与无人值守工作流继续补齐控制机制：Claude Code 修复压缩后的旧指令缓存、增加目录写入约束并纠正非交互错误退出码，VS Code 1.144 恢复实验性 Keep／Undo；目前终端改动仍不进入工作集，审核完整 Git diff 不能省略。来源：Anthropic https://github.com/anthropics/claude-code/releases/tag/v2.1.314 ；Microsoft https://code.visualstudio.com/updates/v1_144
- Flux 从子控制器先行发版走到 v2.10.0 聚合发布，Notification v1 与默认 token RBAC 变更已有正式升级目标；读者实际版本和所用字段尚未确认，当前应先识别迁移范围，不能直接推断生产必须立即升级。来源：Flux https://github.com/fluxcd/flux2/releases/tag/v2.10.0
- 【续报】苹果触控 MacBook Pro 从供应链传闻变为正式产品，M5 Pro／Max OLED 触控款与 M6 非触控 MacBook Pro、iMac 并行推出；11 月 6 日开售前，选购时要分清芯片、屏幕与价格，不能把 M6 当作触控款的默认配置。来源：CNBC https://www.cnbc.com/2026/10/28/apple-mac-touchscreen-launch.html ；Apple https://www.apple.com/newsroom/2026/10/apple-introduces-the-new-14-inch-macbook-pro-with-m6/
- 【续报】车企三季报待办已有结果：比亚迪单季归母净利 100.2 亿元、同比增长 28.08%，长城为 13.62 亿元、同比下降 40.75%，赛力斯为 14.2 亿元；本轮财报发布节点结束，下一步转向现金流和车型交付，赛力斯已明确新 M8 于 11 月 13 日上市。来源：比亚迪三季报 https://static.cninfo.com.cn/finalpage/2026-10-30/1225641442.PDF ；新浪财经 https://finance.sina.com.cn/roll/2026-10-31/doc-inixaraz7640051.shtml ；中证网 https://www.cs.com.cn/ssgs/07/2026/10/30/detail_2026103010048673.html
- 【续报】美联储 10 月议息从市场预期落为 10 比 2 维持 3.75%—4.00%，两名委员仍主张加息；同期中国制造业 PMI 降至 49.3、非制造业为 49.7，利率维持和景气回落是已公布数据，后续政策方向仍需新的决策证据。来源：Federal Reserve https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm ；中国新闻网 https://www.chinanews.com.cn/cj/2026/10-31/10723787.shtml
- 【续报】【单源】美国选前司法争议延伸至加州选票处理：USA Today 报道第九巡回法院拒绝隔离约 2 万张争议选票的紧急请求；11 月 3 日投票日尚未到来，这项临时救济裁定不等于选举结果或诉讼终局。来源：USA Today https://www.usatoday.com/story/news/state/california/2026/10/30/trump-appeal-rejected-in-california-noncitizen-ballot-fight/92521036007/
- 【续报】麻疹疫情继续累积：CDC 将全国截至 10 月 29 日的确诊数更新为 4852 例，比上期多 264 例，约 96% 与暴发有关；病例增加已有同口径数字支持，州与联邦死亡归因分歧本期没有足够新证据可宣布解决。来源：CDC https://www.cdc.gov/measles/data-research/index.html
- 【续报】Artemis III 在任务调整后推进硬件集成，10 月 28 日 SLS 芯级与双助推器完成装配，接下来是检查和加注测试；本阶段目标仍是为猎户座与商业航天器对接做准备，总装进度不能直接换算成登月日期。来源：NASA https://www.nasa.gov/image-article/artemis-iii-sls-core-stage-joins-boosters-at-kennedy/

## 下周看点

- 11月3日 周二：美国中期选举正式投票，加州投票站开放时间为 07:00—20:00，邮寄选票须不晚于当天加盖邮戳；选举夜初步计票不等于最终认证结果。来源：California Secretary of State https://www.sos.ca.gov/elections/upcoming-elections/general-election-november-3-2026
- 【单源】11月4日 周三：核对 Kimi K3.1 Pro 此前承诺的权重开放节点，当前报道仍将这天列为期限；下载文件、许可证与部署文档实际出现后才能认定履约，不能预先写成已开源。来源：Digital Applied https://www.digitalapplied.com/blog/kimi-k3-1-pro-release-pricing-weights
- 11月6日 周五：苹果新 Mac 计划开售，重点核对实际交付和独立评测；M6 MacBook Pro／iMac 与 M5 Pro／Max 触控 MacBook Pro 的上市安排需按型号分别确认。来源：Apple https://www.apple.com/newsroom/2026/10/apple-introduces-the-new-14-inch-macbook-pro-with-m6/ ；CNBC https://www.cnbc.com/2026/10/28/apple-mac-touchscreen-launch.html
- 11月6日 周五：Idina Menzel 与 Pacific Symphony 于 20:00 在 Costa Mesa 演出，需要提前购买单场票；Symphony Pass 兑换席售罄不代表所有席位售罄，余票以官方售票页为准。来源：Pacific Symphony https://www.pacificsymphony.org/show-details/idina-menzel

## 本周闭合

- Mistral Large 4 的开放权重承诺已兑现，后续追踪转向尚未确认兑现的 Kimi 权重节点。来源：Mistral https://mistral.ai/news/mistral-large-4-oss/
- Flux v2.10.0 聚合 Release 已正式发布，不再作为“等待主仓库发版”事项保留；读者的升级实施并未因此完成。来源：Flux https://github.com/fluxcd/flux2/releases/tag/v2.10.0
- 10 月 FOMC 决议已公布，原“等待议息结果”节点闭合，未来利率路径仍开放。来源：Federal Reserve https://www.federalreserve.gov/newsevents/pressreleases/monetary20261028a.htm
- 苹果 10 月 Mac 发布会的触控屏传闻已确认，原“等待官宣”节点结束，后续观察转为 11 月 6 日开售。来源：CNBC https://www.cnbc.com/2026/10/28/apple-mac-touchscreen-launch.html
- 比亚迪、长城和赛力斯第三季度报告均已公布，原财报日期提醒结束，枧下窝复产与 NHTSA 合规答复不能一并视为完成。来源：比亚迪三季报 https://static.cninfo.com.cn/finalpage/2026-10-30/1225641442.PDF ；新浪财经 https://finance.sina.com.cn/roll/2026-10-31/doc-inixaraz7640051.shtml ；中证网 https://www.cs.com.cn/ssgs/07/2026/10/30/detail_2026103010048673.html
