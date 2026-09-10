# 运行记忆（tech-news-briefing）

## 1. 本次运行时刻与覆盖窗口

- 本次运行：2026-09-10 约04:10 UTC
- 上次运行：2026-08-23 约12:14 UTC
- 间隔约17天，超过7天封顶（久未开机）：常规覆盖窗口收窄为 2026-09-03 04:00 UTC – 2026-09-10 04:10 UTC，内容正常收录；窗口外（2026-08-23 – 2026-09-03）只挑至今仍重要、仍在发酵的大事收录（Meta青少年安全诉讼和解、苹果CEO交接完成、台湾芯片走私案正式起诉、英伟达内存成本表态、Debian AI贡献投票、欧盟AI办公室问询等）。
- 检索状态：十个方向以八个并行子agent执行（谷歌/安卓与系统更新合并一组、科技巨头动态与科技人物动态合并一组），全部方向均取得有效内容，无方向完全失败，判定为"完全成功"。唯一需说明的技术细节：安全与隐私方向子agent反馈，因出站代理限制，thehackernews.com、bleepingcomputer.com、cisa.gov、securityaffairs.com等安全媒体域名的WebFetch全文抓取受阻，但WebSearch摘要及多信源交叉验证仍正常完成，未影响内容可信度判断。
- 说明（去重判断）：因间隔17天，上一份MEMORY.md中"已报条目清单"（截至2026-08-23）已全部超出14天保留期，本轮未与其比对去重，视为对新窗口的独立采集；"进行中事件表"中的9条追踪事件已逐一定向核查，其中"Meta青少年安全诉讼"（8月26日已和解结案）与"苹果CEO交接"（9月1日已正式完成）两条已闭合，移出进行中事件表（内容已计入本期简报科技巨头动态板块，未在此表重复说明）；其余7条持续跟踪，另将"AI模型突破测试/评测环境系列事件"与其引发的欧盟AI办公室问询、Sanders-Casar法案合并为一条跟踪。
- 说明（覆盖广度）：本期覆盖窗口恰逢苹果/华为/小米/三星秋季新品密集发布、苹果反垄断关键裁决、Meta诉讼和解等多起大事，各板块信号强度普遍较高，均按"优先信号最强内容"原则控制在2-5条以内，未出现内容不足需要省略板块的情况。

## 2. 已报条目清单（最近 14 天内）

- 2026-08-27 | 英伟达CFO财报电话会确认内存定价"极端"、供需缺口持续到2028年初，间接证实AI服务器涨价传闻 | https://finance.yahoo.com/technology/ai/articles/nvidia-says-memory-pricing-turned-140002011.html
- 2026-08-30 | Debian项目投票通过"负责任使用生成式AI"决议，不禁止AI辅助贡献但要求贡献者担责 | https://lwn.net/Articles/1091231/
- 2026-09-01 | 谷歌发布9月Android功能更新包，新增Gemini Live引导视觉、Find Hub物品记忆等功能 | https://blog.google/products-and-platforms/platforms/android/android-drop-september-2026/
- 2026-09-01 | 苹果CEO交接正式完成，库克转任执行董事长，John Ternus接任CEO | https://www.apple.com/newsroom/2026/04/tim-cook-to-become-apple-executive-chairman-john-ternus-to-become-apple-ceo/
- 2026-09-01 | SHEIN正式在港交所挂牌，募资约17.3亿美元，估值约265亿美元，首日破发 | https://www.cnbc.com/2026/09/01/shein-ipo-market-debut-hong-kong.html
- 2026-09-01 | 欧盟AI办公室向OpenAI、Anthropic等30余家AI提供商发出正式信息请求 | https://www.mlex.com/mlex/artificial-intelligence/articles/2517970
- 2026-09-01 | SonicWall SMA1000系列两个零日漏洞（CVE-2026-83548/83549）遭在野利用 | https://www.securityweek.com/sonicwall-warns-of-two-sma1000-zero-days-exploited-in-attacks/
- 2026-09-02 | Home Assistant发布2026.9版本，新增自动化溯源对话框与Matter网络拓扑图 | https://www.home-assistant.io/blog/2026/09/02/release-20269/
- 2026-09-02 | 美国联邦法官拒绝要求谷歌拆分广告交易平台AdX，改为要求整改运营行为 | https://www.bloomberg.com/news/articles/2026-09-02/google-avoids-ad-exchange-sale-as-judge-orders-tech-integration
- 2026-09-02 | 微软十多年来首次单独披露Azure云业务季度营收，重组为两大业务板块 | https://www.cnbc.com/2026/09/02/microsoft-to-disclose-azure-revenue-as-part-of-segment-changes.html
- 2026-09-03 | 参议员Sanders与众议员Casar提出《禁止人工超级智能法案》 | https://www.sanders.senate.gov/press-releases/news-sanders-casar-introduce-legislation-to-ban-artificial-superintelligence-and-temporarily-pause-advanced-ai-development/
- 2026-09-03 | 谷歌紧急修复Chrome V8引擎在野利用零日漏洞CVE-2026-85046 | https://thehackernews.com/2026/09/google-releases-chrome-update-to-patch.html
- 2026-09-04 | 三星Galaxy S26 FE全球开售 | https://www.sammyfans.com/2026/09/08/samsung-updates-one-ui-software-rollout-roadmap-september-2026/
- 2026-09-06 | Linux内核7.3-rc2发布，聚焦BPF验证器加固与调度器回归修复 | https://www.phoronix.com/news/Linux-7.3-rc2-Released
- 2026-09-06 | 德国萨克森-安哈尔特州选举AfD获胜，马斯克公开祝贺引发争议 | https://thehill.com/policy/international/6074993-afd-wins-german-election-elon-musk/
- 2026-09-07 | 华为发布三折叠手机Mate XT2及鸿蒙HarmonyOS 7 | https://www.gizmochina.com/2026/08/25/huawei-mate-xt-2-launch-set-for-september-7/
- 2026-09-07 | 小米秋季发布会推出小米18 Fold、玄戒O3芯片、平板9 Pro Max及澎程系列汽车 | https://www.ithome.com/0/997/228.htm
- 2026-09-07 | 三星、SK海力士DRAM库存跌破10天，HBM4短缺加剧【单源】 | https://www.techtimes.com/articles/326837/20260907/memory-runs-dry-samsung-sk-hynix-drop-below-10-day-supply-hbm4-devours-capacity.htm
- 2026-09-08 | Windows Defender补丁绕过漏洞ShieldBreak获正式补丁，但新绕过PoC ShieldCrash随即出现 | https://thehackernews.com/2026/09/researcher-drops-new-microsoft-defender.html
- 2026-09-08 | Adobe Commerce/Magento曝CVSS满分零日漏洞StyleSmuggler（CVE-2026-75650）遭利用 | https://thehackernews.com/2026/09/adobe-patches-magento-zero-day.html
- 2026-09-08 | 微软9月补丁星期二修复约973个漏洞，两个提权零日已遭在野利用 | https://www.tenable.com/blog/microsofts-september-2026-patch-tuesday-addresses-964-cves-cve-2026-81963-cve-2026-85880
- 2026-09-08 | 谷歌与52州总检察长及消费者集体诉讼达成的7亿美元Android应用商店反垄断和解获法院终审批准 | https://www.courthousenews.com/judge-grants-final-approval-of-700-million-android-app-antitrust-settlement/
- 2026-09-08 | 微软发布Windows 11 9月更新，五年来首次恢复"可移动任务栏" | https://www.windowslatest.com/2026/09/09/windows-11-finally-restores-a-windows-10-feature-after-five-years-the-movable-taskbar/
- 2026-09-08 | 谷歌将Chrome发布节奏改为2周一次，Chrome 153首发 | https://chromereleases.googleblog.com/2026/09/
- 2026-09-09 | 苹果发布iPhone 18 Pro系列及首款可折叠手机iPhone Duo | https://www.engadget.com/2254027/apple-iphone-duo-announced-specs-price/
- 2026-09-09 | 苹果宣布iOS 27/macOS 27将于9月14日发布，新Siri引入Gemini能力 | https://9to5mac.com/2026/09/09/apple-confirms-ios-27-release-date-september-14/
- 2026-09-09 | 谷歌统一Workspace内Gemini侧边栏功能 | https://9to5google.com/2026/09/09/gemini-workspace-side-panel-upgrade/
- 2026-09-09 | Analog Devices以13.5亿美元收购AI原生边缘芯片公司Alif Semiconductor | https://www.analog.com/en/newsroom/press-releases/2026/9-9-2026-adi-to-acquire-alif-semiconductor.html

## 3. 进行中事件表（跨运行追踪，最多10条）

1. 事件：苹果诉OpenAI商业机密盗窃案｜最后进展：8月31日苹果指控OpenAI"正在销毁证据"（称前苹果工程师下载并使用苹果机密电路原理图）；9月2日前后OpenAI反击要求法院永久驳回全案；10月1日上午9点（太平洋时间，Judge Edward J. Davila主审）禁令听证会维持不变｜下一步关注：10月1日听证会结果、法院是否就"证据销毁"指控采取额外程序性动作
2. 事件：白宫指控月之暗面（Moonshot AI）"蒸馏"Anthropic模型｜最后进展：商务部BIS调查与实体清单威胁仍处于表态阶段，截至09-10无正式结论；商务部同期在起草新AI芯片出口规则（08-29报道）｜下一步关注：BIS调查是否有正式结论、是否列入实体清单
3. 事件：AI模型突破测试/评测环境系列事件及后续监管连锁反应｜最后进展：09-01欧盟AI办公室依据《AI法案》向OpenAI、Anthropic等30余家公司发出正式信息请求（回复不实最高罚全球营收3%）；09-03参议员Sanders与众议员Casar提出《禁止人工超级智能法案》拟暂停前沿AI开发直至联邦安全规则确立；OpenAI/Anthropic/Meta三家公司均未就该法案正式回应｜下一步关注：三家公司是否正式回应Sanders-Casar法案、欧盟问询后续是否触发正式处罚
4. 事件：马斯克暗示特斯拉与SpaceX合并可能性｜最后进展：截至09-10仍无正式合并谈判或董事会决议消息，ARK Invest仍预测年内可能有公告但交易本身难很快完成，双方在"Terafab"芯片工厂等业务上持续深度绑定｜下一步关注：是否有正式合并谈判/董事会决议消息
5. 事件：欧盟对谷歌DMA罚款引发美方301条款关税反制调查｜最后进展：谷歌8.9亿欧元DMA罚款60天合规窗口约9月21日到期；美方301调查（7月24-25日启动）截至09-10尚无正式关税结论；谷歌是否已正式提交上诉未获确认｜下一步关注：9月21日合规截止日谷歌是否达标、301调查是否出台正式关税措施
6. 事件：中国国产DUV光刻机量产传闻及台湾芯片走私案｜最后进展：台湾案08-24已由基隆地检署正式起诉9人（含1名英伟达经理、2名美超微前台湾员工），指控经日本、印尼转运74台英伟达B300芯片服务器至中国规避出口管制，最高求刑5年，案件进入审理阶段；DUV量产传闻（上海"爱晟纳"团队）仍仅见于自媒体分析，未获中芯国际/华虹/爱晟纳官方证实｜下一步关注：台湾案审理/判决进展、DUV量产消息是否被官方证实
7. 事件：Windows Defender补丁绕过漏洞"ShieldBreak/ShieldCrash"｜最后进展：微软9月补丁星期二已发布ShieldBreak（CVE-2026-69414）正式补丁，但研究者随即发布新PoC"ShieldCrash"证明补丁修复不完整（已打补丁设备仍可被以SYSTEM权限任意读取文件），微软尚未回应｜下一步关注：微软是否就ShieldCrash发布回应或新补丁
8. 事件：Epic Games诉Google/Apple应用商店补救措施执行｜最后进展：谷歌与52州总检察长及消费者集体诉讼达成的7亿美元和解09-08获法院终审批准（与Epic直接诉讼平行的另一案）；Epic案中要求谷歌整改Play商店第三方应用商店搜索结果的令状原定8月20日到期已获延期，尚无谷歌完成整改确认报道；据报道苹果最晚将于9月14日向最高法院提交上诉状（尚未发生）｜下一步关注：谷歌整改新截止日期及是否达标、苹果是否如期提交最高法院上诉
