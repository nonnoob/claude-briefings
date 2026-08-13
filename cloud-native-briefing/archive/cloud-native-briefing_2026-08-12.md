☁️ 云原生每日简报 · 2026-08-12

**安全通告**

- CVE-2026-17106（"CopyEscape"）：Docker `docker cp`（及 AI Agent 沙箱场景下的 `sbx cp`）命令存在容器逃逸漏洞，恶意容器可覆写宿主机任意文件，特定配置下（如以特权运行 docker cp 时该写入原语可替换 runc 等系统二进制）可实现宿主机 root 代码执行；由 Imperva 红队披露并于近日引发广泛报道，CVSS 分数未公开但影响严重。Docker 已在 Engine/CLI 29.7.2、Desktop 4.86.0、Sandboxes 0.38.0 中修复，使用 docker cp 自动化流程（尤其是以提权方式运行）的团队应尽快升级 | 来源：Imperva Research | https://www.imperva.com/blog/copyescape-taking-over-docker-hosts-with-docker-cp/
- CVE-2026-72971：Windows Container Isolation FS Filter Driver（unionfs.sys）曝出篡改（tampering）漏洞（CVSSv3 5.5，Important），随微软 2026 年 8 月补丁星期二发布；漏洞在补丁发布前已被公开披露，微软评估"不太可能被利用"，但仍可能削弱 Windows 容器的隔离边界。运行 Windows 容器、构建代理或 CI 基础设施的团队应优先安装本月更新 | 来源：CSO Online（Patch Tuesday 分析）| https://www.csoonline.com/article/4208185/patch-tuesday-august-2026-a-zero-day-winsock-driver-hole-under-exploit-and-a-maximum-severity-sap-vulnerability.html

---

版本与变更、云厂商动态、CNCF 与社区、商业动向、工程实践五个板块本期（2026-08-11 12:15 UTC – 2026-08-12 12:15 UTC）经核实均无落在窗口内、且未曾报道过的实质新内容，故整节省略。

进行中事件复核：Kubernetes v1.37 发布周期仍停留在 v1.37.0-rc.0，未见新 RC 或 GA 消息，GA 仍定档 8/26；GitHub Actions 8/6 大规模故障的官方 postmortem/根因分析全文截至本次运行仍未发布。两项均继续跟踪。
