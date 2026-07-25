# 📰 每日科技简报 · 2026年7月13日

*（上次运行为7月11日约10:29太平洋时间，7月12日未运行，本期覆盖范围延长至7月11日10:29–7月13日13:49太平洋时间，约51小时。）*

**今日要闻**：苹果诉OpenAI商业机密案持续发酵，马斯克与奥特曼周末在X上公开互怼骂战，苹果据悉正筹划法庭外反制措施。

## 科技人物动态

- 【续报】苹果诉OpenAI案细节升级：起诉书指出现有超400名前苹果员工任职于OpenAI（此前诉状仅点名两名被告），苹果将其招募定性为针对芯片与硬件人才的"协同性"技术套取行动而非正常跳槽，涉案技术部分源自苹果已终止的自动驾驶项目；据悉苹果正筹划法庭外反制措施。来源：The Hill — https://thehill.com/policy/technology/5965640-apple-openai-trade-secret-lawsuit/
- 【续报】马斯克与奥特曼周末在X上公开互怼：马斯克讽刺奥特曼"骗术又发作了"，奥特曼反讽马斯克靠"兜售短期太空数据中心故事"忽悠公开市场投资者，并暗示GPT-5.6 Sol才是"全球最强模型"；OpenAI发言人回应称"我们对其他公司的商业机密没有兴趣"。来源：CNBC — https://www.cnbc.com/2026/07/12/elon-musk-and-sam-altman-spar-.html

## 安全与隐私

- 研究人员曝光"Ghostcommit"攻击：密苏里大学堪萨斯城分校团队发现，攻击者可将提示词注入指令隐藏在PNG图片中，通过项目AGENTS.md文件诱导Cursor、Antigravity等AI编程工具读取图片并窃取.env密钥，人工与LLM代码审查均难以察觉；测试中仅Claude Code全线拒绝执行。建议团队对AI提交代码中引用的图片文件加强人工复核，或部署多模态审查工具防范同类攻击。来源：BleepingComputer — https://www.bleepingcomputer.com/news/security/ghostcommit-hides-prompt-injection-in-images-to-fool-ai-agents-steal-secrets/
- 安全厂商jscrambler遭供应链攻击：其npm包8.14.0至8.20.0版本被植入Rust编写的信息窃取程序，瞄准云凭据、CI令牌、加密钱包及Claude Desktop/Cursor等AI工具配置文件，发布6分钟后即被安全公司Socket发现。安装过上述版本的用户应立即升级至8.22.0并轮换所有相关密钥。来源：TheHackerNews — https://thehackernews.com/2026/07/compromised-jscrambler-8140-npm-release.html

## 开源软件

- Debian 13.6"Trixie"发布，包含124项错误修复与120项安全更新。来源：9to5Linux — https://9to5linux.com/9to5linux-weekly-roundup-july-12th-2026
- PyTorch 2.13发布：新增FlexAttention支持苹果芯片（最高12倍加速）、CuTeDSL为Inductor带来CUTLASS级GEMM内核，大词表模型显存峰值最多降低4倍。来源：PyTorch官方博客 — https://pytorch.org/blog/pytorch-2-13-release-blog/
