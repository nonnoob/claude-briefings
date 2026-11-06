# 📰 每日科技简报 · 2026-11-06

> 覆盖窗口：2026-10-31 11:32 UTC 至 2026-11-06 16:22 UTC（常规）

今日要闻：美满电子（Marvell）宣布以约 1150 亿美元全股票交易收购光通信企业 Lumentum，苹果公布创纪录的 2026 财年第四季度及全年财报且首款 OLED 触控屏 MacBook Pro 正式开售，美光则因台湾桃园厂劳资分红争议暂停当地新晶圆厂建设。

## 谷歌 / 安卓

- 谷歌于 11 月 3 日发布 2026 年 11 月 Android 安全公告（含 2026-11-01 与 2026-11-05 补丁级别），修复逾 200 个安全漏洞，其中最严重的是无需额外执行权限或用户交互即可触发的 Framework 组件严重远程代码执行漏洞 CVE-2026-58868；同月 Google 系统更新还确认将在 Android 设置菜单中新增集中管理家庭账号与共享权限的“Family Hub”入口，建议 Android 用户在收到固件更新后尽快升级。来源：Android Security Bulletin https://source.android.com/docs/security/bulletin/2026-11-01 、9to5Google https://9to5google.com/2026/11/02/whats-new-in-androids-november-2026-google-system-updates/
- 谷歌向 Windows、macOS、Linux 与 Android 正式推送 Chrome 157 稳定版（桌面端版本号 157.0.8103.38/.39），共修复 213 个安全漏洞，其中包括 WebGPU（Dawn）与 ANGLE 缓冲区溢出以及 WebGL、Prerender 组件释放后重用（Use-After-Free）等 7 个严重级别内存安全漏洞，用户应尽快重启浏览器完成更新。来源：Chrome Releases https://chromereleases.googleblog.com/2026/11/stable-channel-update-for-desktop.html

## 系统更新

- 苹果于 11 月 3 日向开发者及公测用户推送 iOS 27.3、iPadOS 27.3 与 macOS 27.3（Golden Gate）首个测试版，重构“健康”应用（新增基于 Apple Intelligence 的 Insights 趋势页与评估生理年龄的 Longevity 标签页）、为 Apple Music 引入“Selfie Sing”视频 K 歌模式，并在获监管放行后正式启动集成阿里通义千问等本地模型的国行版 Apple Intelligence 开发者测试。来源：9to5Mac https://9to5mac.com/2026/11/03/everything-new-in-ios-27-3-beta-1-so-far/ 、Apple Newsroom https://www.apple.com/newsroom/2026/11/redesigned-health-app-expands-language-support/
- 小米于 11 月初面向全球市场正式启动基于 Android 17 的澎湃 OS 4（HyperOS 4）稳定版推送，首批覆盖小米 17 系列与小米 15 Ultra 等旗舰机型。来源：Gizmochina https://www.gizmochina.com/

## 新品发布

- 【续报】苹果首款搭载 PROLED XDR 双层串联 OLED 触控屏与灵动岛的 M5 Pro/Max 版 14/16 英寸 MacBook Pro（2899/3399 美元起）、M6 版 14 英寸入门 MacBook Pro（1999 美元起）、M6 版 24 英寸 iMac 以及搭载 A20 Pro 的 OLED iPad mini 于 11 月 6 日正式上市开售；首批独立评测肯定了触控屏机型高达 2000 尼特 HDR 峰值亮度的顶级显示素质与减重约 0.7 磅的轻薄机身，但指出 macOS 仍以键鼠和触控板为核心交互、触控目前属于辅助层，而 M6 版 14 英寸机型则属于稳健的常规芯片升级。来源：MacRumors https://www.macrumors.com/2026/11/06/apple-launching-five-new-products-today/ 、Tom's Guide https://www.tomsguide.com/laptops/macbooks/i-tested-the-new-macbook-pro-oled-against-80-laptops-and-even-the-lg-g6-oled-tv
- 华为于 11 月 5 日发布首款实现 100% 国产化元器件供应链的政企商用台式机“华为擎云 HM650”，搭载自研麒麟 X90 处理器与 HarmonyOS V1.0 桌面操作系统。来源：South China Morning Post https://www.scmp.com/tech/tech-trends/article/3289052/no-intel-no-qualcomm-huawei-unveils-desktop-built-entirely-china-made-components

## 科技公司动态

- 苹果于 11 月 2 日公布 2026 财年第四季度（截至 9 月 26 日）及全年业绩：第四财季营收同比增长 12% 至 1144.8 亿美元，净利润 307.1 亿美元，摊薄每股收益同比增长 14% 至 2.10 美元，毛利率在关税退税提振下达 47.9%；其中 iPhone 营收 575.8 亿美元创 9 月季度新高，服务业务营收 315.7 亿美元创历史新高，推动 2026 财年全年总营收达到创纪录的 4790 亿美元。来源：Apple Newsroom https://www.apple.com/newsroom/2026/11/apple-reports-fourth-quarter-results/

## 芯片与硬件

- 【续报】受台湾桃园厂工会要求将营业利润 15% 用于员工分红的劳资谈判僵局及工会抗议台中厂协议缺乏透明度影响，美光（Micron）于 11 月 5 日至 6 日被曝暂停总投资约 30 亿至 45 亿美元的台湾桃园新内存晶圆厂（Fab 11E）建设；台湾经济部表示将继续协助劳资双方沟通协商。来源：TheStreet https://www.thestreet.com/investing/stocks/micron-freezes-taiwan-plant-as-workers-demand-bigger-cut
- AMD、高通与 Arm 本周密集发布最新财报：AMD 第三季度营收同比大增 45% 至创纪录的 134 亿美元（数据中心业务收入同比激增 97% 至 85 亿美元），并给出约 170 亿美元的强劲第四季度营收指引；高通第四财季非 GAAP 营收达 104.4 亿美元（汽车与物联网业务合计增长 36%），重申 2027 财年数据中心收入达 50 亿美元目标；Arm 第二财季营收同比增长 27% 至创纪录的 14.43 亿美元，单季基于 Arm 架构的芯片出货量历史首次突破 100 亿颗。来源：AMD https://ir.amd.com/news-events/press-releases/detail/7308/amd-reports-third-quarter-2026-financial-results 、Qualcomm https://investor.qualcomm.com/financial-information 、Arm Newsroom https://newsroom.arm.com/news/arm-q2-fye27-results
- 【传闻】据 The Information 11 月 6 日报道，应最大客户英伟达缓解 AI 高带宽内存（HBM）与 DRAM 严重供应瓶颈的要求，台积电正在评估突破纯逻辑晶圆代工边界、直接涉足垂直堆叠 3D DRAM 等先进存储芯片制造。来源：Investing.com https://www.investing.com/news/stock-market-news/tsmc-considers-making-advanced-memory-chips-the-information-reports-93CH-3832185 、StreetInsider https://www.streetinsider.com/Insider+Reports/TSMC+rises+on+report+of+potential+push+into+advanced+memory+for+Nvidia/25841258.html

## 科技人物动态

- 【续报】在特斯拉与 SpaceX 双方董事会特别委员会持续评估合并方案（巴克莱测算合并后马斯克将掌握约 56% 投票权）之际，马斯克宣布特斯拉计划逐步关停 Cybertruck 电动皮卡产线，将制造产能重心全面转向 Cybercab 无人驾驶出租车；受美国中期选举民主党重掌国会引发的监管与反垄断审查担忧冲击，特斯拉与 SpaceX 在选后两个交易日内市值累计蒸发逾 4110 亿美元。来源：Decrypt https://decrypt.co/290074/tesla-wind-down-cybertruck-production-elon-musk-robotaxis-ai 、Quartz https://qz.com/elon-musks-tesla-spacex-lose-411-billion-in-post-electio-1851944883

## 投融资与并购

- 美满电子（Marvell Technology）于 11 月 2 日宣布达成最终协议，以隐含企业价值约 1150 亿美元的全股票交易收购光通信与光子技术厂商 Lumentum，打造 AI 算力光互连基础设施龙头；云联络中心厂商 Five9 则于 11 月 5 日宣布达成最终协议，以约 3.25 亿美元收购 AI 原生客户体验平台 Level AI。来源：Marvell https://investor.marvell.com/news-releases/news-release-details/marvell-and-lumentum-combine-creating-category-leader-ai 、Five9 https://www.five9.com/blog/five9-to-acquire-level-ai-advancing-ai-powered-cx-platform

## 安全与隐私

- 美国 CISA 将已遭在野扫描与利用的 WordPress 核心 TOCTOU 竞争条件漏洞 CVE-2026-119977（CVSS 8.1，攻击者可在核心完整包升级的临时目录窗口期实现未授权远程代码执行）列入 KEV 强制限期修补目录；同时 Debian 与 Ubuntu 发布更新修复 APT 包管理器高危中间人漏洞，相关站点与 Linux 服务器管理员应尽快安装补丁。来源：The Hacker News https://thehackernews.com/2026/11/some-wordpress-sites-can-still-be.html 、The Hacker News https://thehackernews.com/2026/11/debian-and-ubuntu-apt-flaw-lets-mitm.html

## 开源软件

- Fedora 45 正式版于 11 月 3 日发布，以 KMSCON 取代内核控制台、在 Anaconda 安装器中集成 Stratis 存储、增强高通骁龙 X 笔记本支持并默认限制 ptrace 权限，同时搭载 GNOME 51、GCC 16.2 与 Python 3.15；此外 systemd 正式合并由核心开发者提交的初步 Rust 语言支持，允许在独立二进制组件中使用 Rust。来源：Phoronix https://www.phoronix.com/news/Fedora-45-Released 、Phoronix https://www.phoronix.com/news/systemd-With-Its-Initial-Support-For-Rust
- GitHub 宣布在仓库概览页原生支持展示 `ACCESSIBILITY.md` 无障碍声明文件，便于开源维护者集中记录无障碍目标、已知障碍与反馈流程，并同步启动主题为“SHIFT”的 Game Off 2026 年度游戏开发挑战赛。来源：GitHub Blog https://github.blog/news-insights/company-news/accessibility-statements-now-have-a-home-on-github/

## 政策与监管

- 【续报】针对马斯克旗下 X 与 xAI 提起的生成式 AI 反垄断诉讼（原告此前已于 9 月撤回对苹果的起诉），OpenAI 于 11 月初向美国联邦法官申请简易判决以驳回全部剩余指控，辩称其与苹果的 ChatGPT 集成合作并非排他性协议，竞争对手仍可自由洽谈商业条款或通过 App Store 分发应用。来源：PYMNTS https://www.pymnts.com/artificial-intelligence/2026/openai-says-apple-chatgpt-deal-doesnt-shut-out-ai-rivals/
