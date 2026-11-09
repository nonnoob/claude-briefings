# 📰 每日科技简报 · 2026-11-09

> 覆盖窗口：2026-11-06 16:22 UTC 至 2026-11-09 21:50 UTC（常规）

今日要闻：英伟达董事会宣布就首席执行官黄仁勋涉华情报安全隐忧启动独立调查导致单日市值蒸发逾 3000 亿美元，台积电正式否认应英伟达要求进军 3D DRAM 制造，国防科技独角兽 Shield AI 则宣布融资 25 亿美元并以最高 53 亿美元收购雷达厂商 Echodyne。

## 谷歌 / 安卓

- 谷歌在 Gemini 应用中向美区英语订阅用户推送“Memory summary（记忆摘要）”功能，将 AI 记录的个人背景与偏好按职业、旅行、生活方式等分类汇总并支持手动编辑或查看历史记录；同时谷歌确认自 11 月 13 日起从每月 4.99 美元的 Google AI Plus 低价订阅档位中移除 Gemini Pro 模型访问权限，仅保留 Flash 与 Flash-Lite 模型。来源：9to5Google https://9to5google.com/2026/11/09/google-gemini-memory-summary/ 、9to5Google https://9to5google.com/2026/10/14/gemini-ai-plus-subscribers-will-lose-access-to-pro-models-next-month/
- Google Messages 测试版启动主页界面改版，引入置顶会话头像、底部常驻搜索栏并将 Gemini 快捷入口移至右上角个人头像旁。来源：9to5Google https://9to5google.com/2026/11/07/google-messages-homepage-redesign/

## 系统更新

- 苹果于 11 月 9 日推送 macOS 27.2.1（以及面向旧系统的 macOS 26.7.3 与 macOS 15.8.3）及 iOS 27.2.1 正式版安全更新，从 `/etc/ssl/cert.pem` 中移除存在弱私钥缺陷的印度证书颁发机构 eMudhra 中间证书，修补此前 `curl` 与 `git` 等命令行工具仍可能信任伪造证书的漏洞，并修复蓝牙与内存管理故障，建议 Mac 用户尽快升级。来源：MacRumors https://www.macrumors.com/2026/11/09/macos-27-2-1-emudhra-fix/
- 微软向 Beta 预览通道推送 Windows 11 Build 26320.9876（通过启用包全面切换至 26H2 版本），带来支持在搜索结果内直接切换深色模式或蓝牙等快捷操作的全新 WinUI 3 搜索界面、实时字幕音频源细粒度选择及 Xbox 模式快捷设置；同时向 Experimental 通道推送 Build 26340.9882，优化 Windows Hello 多生物特征识别登录与弱光屏幕补光体验。来源：Windows Insider Blog https://blogs.windows.com/windows-insider/2026/11/06/announcing-new-builds-for-6-november-2026/

## 新品发布

- 德国光量子计算企业 Q.ANT 与欧洲云服务商 IONOS 于 11 月 9 日联合推出商业光子计算试点项目，首次通过云端裸金属服务器向开发者开放实体光子处理器算力，用于运行高性能计算与 AI 推理负载。来源：GlobeNewswire https://www.globenewswire.com/news-release/2026/11/09/3398482/0/en/Q-ANT-and-IONOS-Launch-Photonic-Computing-Pilot.html

## 科技公司动态

- 英伟达董事会于 11 月 8 日至 9 日宣布由独立董事委员会聘请外部法律顾问对首席执行官黄仁勋启动独立调查；此前美媒曝出黄仁勋曾与新加坡数据中心客户 Megaspeed 高管存在私人关系，而美方情报机构怀疑该人士为中国国安部门收集情报，黄仁勋在内部信中就个人行为致歉但坚称未泄露公司机密或危害国家安全，董事会亦表示目前无证据显示机密外泄并继续支持其留任，受“关键人物风险”冲击英伟达股价 11 月 9 日盘中下跌约 5% 至 7.5%、市值蒸发逾 3000 亿美元。来源：The Guardian https://www.theguardian.com/us-news/2026/nov/08/nvidia-investigation-ceo-jensen-huang-foreign-intelligence 、Business Insider https://www.businessinsider.com/nvidia-board-investigation-jensen-huang-foreign-intelligence-effort-2026-11
- 字节跳动被曝正评估扩建其位于巴西塞阿拉州佩塞姆港的大规模数据中心二期项目，同时自 11 月起收紧内部员工使用外部 AI 编程与效率工具（如在核心代码库与飞书文档中调用个人 Claude、Codex 账号）的权限以防范代码与数据外泄；其核心海外算力基建供应商 DayOne（原万国数据国际业务）亦于近日向美国 SEC 提交 F-1 招股书拟赴纳斯达克上市。来源：钛媒体 https://www.tmtpost.com/7581566.html

## 芯片与硬件

- 【续报】针对此前《The Information》关于台积电应英伟达要求评估制造垂直堆叠 3D DRAM 的传闻，台积电官方正式回应予以否认，重申公司将继续严格专注于纯逻辑晶圆代工与先进封装核心主业，无意进入大宗存储芯片制造市场，业内亦指出商业化 3D DRAM 距大规模量产仍需数年时间。来源：Tom's Hardware https://www.tomshardware.com/semiconductors/tsmc-denies-exploring-3d-dram-at-nvidias-request-advanced-memory-tech-is-still-years-from-market-viability
- 英飞凌（Infineon）于 11 月 9 日宣布在奥地利菲拉赫晶圆厂利用现有硅基制造设备成功加工出全球首批全功能 300 毫米（12 英寸）碳化硅（SiC）功率半导体晶圆，单晶圆芯片产出量较传统 200 毫米晶圆提升约 2.3 倍，并在德国德累斯顿基地验证了减少材料损耗的 Cold Split 晶体切割技术，将大幅降低电动汽车与 AI 数据中心电源模块成本。来源：TechPowerUp https://www.techpowerup.com/354619/infineon-starts-worlds-first-300-millimeter-power-silicon-carbide-sic-wafer-production
- 【续报】据日经新闻等报道，马斯克旗下特斯拉与 SpaceX 合资半导体企业 Terafab 已向日本半导体设备商通报远期规划，目标到 2032 年在得克萨斯州基地实现每月 100 万片晶圆产能（含约 70 万片存储晶圆与逾 30 万片先进逻辑晶圆，相当于台积电全球总产能约七成），并力争 2028 年下半年启动初步量产；同时马斯克已软化此前坚持完全自主运营的立场，重新探讨赋予台积电运营角色的可能性。来源：TechPowerUp https://www.techpowerup.com/354610/terafab-wants-to-become-one-of-the-largest-memory-makers-by-2032

## 科技人物动态

- 【续报】马斯克进一步确认特斯拉得州超级工厂 Cybertruck 电动皮卡产线将于约 8 个月后（2027 年年中）正式关停以腾出产能全力生产 Cybercab 无人驾驶出租车，并表示因剩余订单超出停产前可交付上限，特斯拉将向大批预订车主退还定金；此外马斯克预计受 AI 算力租赁与轨道计算业务拉动，SpaceX 年化营收将于今年 12 月突破 1000 亿美元并在 2027 年底达 5000 亿美元，而政府合同占 SpaceX 营收比重本季度将降至 10% 以下、明年进一步缩至约 5%。来源：CBS News https://www.cbsnews.com/news/tesla-cybertruck-deposits-production-winds-down-elon-musk/ 、Gizmodo https://gizmodo.com/musk-says-spacex-government-revenue-will-shrivel-next-year-2000523423

## 投融资与并购

- 国防科技公司 Shield AI 宣布完成 25 亿美元融资组合（含 10 亿美元 H 轮股权融资、黑石 10 亿美元结构化股权投资及摩根大通牵头的 5 亿美元债务融资），投后估值翻倍至 288 亿美元，并同步签署最终协议以最高 53 亿美元收购比尔·盖茨参投的超材料固态雷达厂商 Echodyne。来源：Shield AI https://shield.ai/shield-to-acquire-echodyne-in-a-transaction-valued-at-5-3-billion-and-raise-2-5-billion-at-a-28-8-billion-valuation/ 、GeekWire https://www.geekwire.com/2026/shield-ai-to-buy-bill-gates-backed-radar-maker-echodyne-in-5-3b-deal-doubling-down-on-seattle-area/
- 自动驾驶无人机配送企业 Zipline 宣布完成由 Paradigm、WCM Investment Management 与 Layer Global 联合领投的 15 亿美元后期融资，投后估值较年初翻近三倍至 215 亿美元，资金将用于扩建美国本土制造工厂并推进与沃尔玛、Uber 合作的全国性无人机配送网络。来源：FinSMEs https://www.finsmes.com/2026/11/zipline-raises-1-5b-in-funding.html

## 安全与隐私

- 开源 SSH 工具 OpenSSH 曝出高危密码认证绕过漏洞“SSHole”（CVE-2026-123158，CVSS 8.1），攻击者向采用 musl libc 且未启用 PAM 的 Linux 系统（如 Alpine Linux 容器与云镜像）发送 256 至 1024 字符超长密码可触发 `crypt()` 返回 `*` 错误符，从而直接免密登录被禁用密码的系统或管理账户并已遭在野利用；美国 CISA 已将该漏洞、SonicWall SonicOS SSL-VPN 多因素认证（MFA）绕过漏洞 CVE-2026-19868 以及 GPUStack（CVE-2026-102895）、FreeSwitch（CVE-2026-116779）、IBM Aspera Faspex（CVE-2026-123218）漏洞一并列入 KEV 限期修补目录，相关管理员应立即升级至 OpenSSH 10.6p2 及最新 SonicOS 固件。来源：BleepingComputer https://www.bleepingcomputer.com/news/security/open-ssh-flaw-lets-attackers-log-into-password-disabled-linux-accounts/ 、The Hacker News https://thehackernews.com/2026/11/cisa-flags-sonicwall-sonicos-mfa-bypass.html
- Linux 内核 UDP 套接字 `sock_gettstamp()` 组件曝出已在野受测的高危释放后重用（UAF）本地提权竞争漏洞 CVE-2026-98276，AlmaLinux 与 CloudLinux 等企业级发行版已紧急推送内核补丁；此外区块链分析公司 Chainalysis 披露遭遇利用自主 AI 智能体攻击技术的网络入侵，导致部分非敏感用户资料外泄。来源：AlmaLinux https://almalinux.org/blog/2026-11-06-cve-2026-98276/ 、SecurityWeek https://www.securityweek.com/chainalysis-discloses-data-breach-following-ai-driven-cyberattack/

## 开源软件

- Linus Torvalds 于 11 月 8 日发布 Linux 7.4-rc2 内核候选版本，除合入延后的 Coccinelle 自动化脚本更新外，重点带来大幅提升小簇与同步挂载性能的 FAT32 文件系统预分配优化、AMDGPU 驱动 HDMI 2.2 FRL 与“PerfOpt”核显性能调优修复，以及 x86 架构分支历史注入（BHI）缓解措施修正；同时 AMD 工程师已向邮件列表提交逾 1.26 万行代码的 GFX13（下一代 RDNA 5 架构）初步内核驱动补丁，拟于 Linux 7.5 合入。来源：Phoronix https://www.phoronix.com/news/Linux-7.4-rc2 、Phoronix https://www.phoronix.com/news/AMDGPU-Patches-GFX13

## 政策与监管

- 美国联邦贸易委员会（FTC）与亚利桑那、科罗拉多等多州总检察长于 11 月 6 日宣布，单户租房巨头 Progress Residential 及其私募股权母公司 Pretium Partners 同意支付创纪录的 4975 万美元达成执法和解，以了结其隐瞒强制性智能家居与公用事业管理附加费等欺诈性定价及扣留押金指控；此外随着美国中期选举后民主党重掌参众两院，新当选议员已释放信号将对高耗能 AI 数据中心扩建的电网冲击及头部 AI 实验室展开更严厉的国会听证与监管审查。来源：FTC https://www.ftc.gov/news-events/news/press-releases/2026/11/progress-residential-owner-pretium-partners-pay-49.75-million-settle-ftc-states-charges-over-deceptive 、TechTarget https://www.techtarget.com/searchenterpriseai/news/366616335/Enterprises-face-tougher-ai-regulatory-landscape-after-midterms
