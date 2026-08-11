# 🤖 AI 行业简报 · 2026-08-11

## 模型与产品

- OpenAI 扩大"Daybreak"网络安全防御计划，推出面向审核合作伙伴（IBM、Palo Alto Networks、Akamai、Accenture、CrowdStrike 等）的新模型 GPT-5.6-Cyber——高阶网络安全任务完成率达 95%（此前 GPT-5.5-Cyber 为 57.3%），并披露该模型发现两个此前未知的 Chrome V8 0day 漏洞（已由谷歌以 CVE-2026-15903 修复）；此举为 OpenAI 对下一代模型 Astra 触发"Critical"级网络安全评级后暂停发布的后续安全响应。来源：OpenAI 官方 https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows/ ，TechCrunch/Axios/CyberScoop 交叉验证
- Meta 发布开放权重智能体模型 Muse Glimmer（296 亿参数，Apache 2.0 协议），4-bit 量化后可在单张消费级 GPU 本地运行（约 20GB 显存，单卡 2 万 token/秒），在 SWE-bench Verified、AIME 2026 等基准上领先同尺寸开源模型；扎克伯格同时预告将开放更大模型 Muse Spark 1.2 权重。来源：Meta 官方 https://developer.meta.com/ai/models/muse-glimmer/ ，VentureBeat https://venturebeat.com/technology/meta-returns-to-open-source-with-muse-glimmer-an-apache-2-0-licensed-30b-parameter-ai-model-optimized-for-agents-available-now

## 研究与技术

- Anthropic 披露一个未发布的 Claude 研究版本，通过约 60 个子代理协同运行 36 小时（合计约 3100 万 tokens），将黎曼 ζ 函数零点满足黎曼猜想比例的已证明下界从 41.6% 提升至 67.2%——单次提升幅度超过此前数十年人类研究的累计进展，已获数学家 Brian Conrey、Dan Goldston 复核并提供 Lean 形式化证明（未证明黎曼猜想本身）。来源：Anthropic 官方研究博客 https://www.anthropic.com/research/riemann-zeta

## 商业与资本

- OpenAI 完成 70 亿美元员工股份要约回购，未引入外部新投资者，估值维持最近一轮的 8520 亿美元不变，被视为 IPO 前的铺垫动作。来源：Bloomberg https://www.bloomberg.com/news/articles/2026-08-10/openai-buys-back-7-billion-of-employee-shares-in-tender-offer ，TechCrunch 跟进

## 算力与基建

- 英伟达联合黑石、贝莱德、阿波罗、博枫、高盛、KKR 六大华尔街机构签署谅解备忘录，拟合作设立 AI 算力基础设施融资平台，长期动员超 5000 亿美元第三方资本用于数据中心建设与芯片采购（尚处 MOU 意向阶段，未转化为具体最终协议）。来源：NVIDIA 官方 https://nvidianews.nvidia.com/news/nvidia-partners-with-apollo-blackrock-blackstone-brookfield-goldman-sachs-and-kkr-to-establish-ai-compute-infrastructure-financing-platforms-to-mobilize-over-500-billion-of-third-party-capital ，CNBC 交叉验证

## 传闻与前瞻

- 【传闻】据 The Information 援引知情人士报道，微软计划最快 9 月发布下一代 AI 芯片 Maia 300，正与台积电洽谈 2027 年交付超 30 万片产能（较 Maia 200 数万片规模大幅提升），并已向 Anthropic 等大客户推销；微软、台积电、Anthropic 均未公开证实细节。来源：The Information（经 Yahoo Finance 转引）https://finance.yahoo.com/technology/ai/articles/microsoft-plans-maia-300-chip-140432692.html
