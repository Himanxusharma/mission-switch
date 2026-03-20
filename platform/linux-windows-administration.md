# Linux & Windows Server Administration

> **Source:** Extracted from `notes/All_chats.md` (Akamai SDE-II prep). Content preserved; reorganized into Concepts vs Interview sections.

**How to read:** Start with **At a glance** / talk track if present, then the full chapter. **Fenced code blocks** are copy-paste examples; **tables** compare options; **ASCII diagrams** use monospace — widen the pane or scroll horizontally.

## Concepts

> *Skim **At a glance** first — a short on-ramp. Below the line is the full chapter.*

---

### At a glance · Linux / servers

- **Interview lens:** **troubleshooting** (disk, CPU, memory, network), **permissions**, **services**, **logs**, **security** (firewall, SSH).
- **Show:** you’ve **SSH’d**, read **`journalctl`**, checked **`df`/`du`**, **opened ports** safely.

#### Talk track (~60 s)

Linux servers run **systemd** units; **`systemctl status/restart`**, **`journalctl -u`**. **Disk:** `df -h`, find big dirs with `du`. **Process:** `top`/`htop`, **`ps`**. **Network:** `ss -lntp`, **`curl`**. **Permissions:** `chmod/chown`, avoid **777**. **Hardening:** SSH keys, **sudo**, **firewall** (ufw/iptables), **auto-updates** where appropriate.

#### Easy mistakes

- **chmod 777** “to fix it.”  
- **Editing prod** without **backup/rollback**.  
- No **correlation** between app error and **syslog**.

#### Quick checks

- [ ] Free **disk full** — first three commands you’d run.  
- [ ] **Port already in use** — how you find the PID.  
- [ ] **Service won’t start** — where you look first.

🧠 PART 1: WHAT IS SERVER ADMINISTRATION?
💡 Definition
👉 Managing servers to ensure:

Availability

Performance

Security

🧠 Real Responsibilities
Setup → Configure → Monitor → Troubleshoot → Secure
🐧 PART 2: LINUX SERVER ADMIN
💡 Why Linux?
Most servers run Linux

Lightweight + powerful

Better for automation

⚙️ CORE COMMANDS (YOU Core)
🔹 File System
ls       # list files
cd       # change directory
pwd      # current path
rm -rf   # delete
🔹 Process Management
ps aux        # running processes
top           # real-time monitoring
kill -9 PID   # kill process
🔹 Disk Usage
df -h     # disk space
du -sh    # folder size
🔹 Networking
netstat -tuln
curl http://localhost:3000
ping google.com
🔹 Permissions
chmod 755 file
chown user:group file
🧠 SERVICES MANAGEMENT
systemd
systemctl start nginx
systemctl stop nginx
systemctl restart nginx
systemctl status nginx
🧠 LOGS
tail -f /var/log/syslog
👉 Debugging always starts here 🔥

🪟 PART 3: WINDOWS SERVER ADMIN
💡 Used in:
Enterprise environments

.NET applications

⚙️ CORE TOOLS
🔹 PowerShell
Get-Process
Stop-Process -Id 1234
🔹 Services
Start/Stop services via UI or CLI

🔹 Event Viewer
👉 Logs for debugging

🧠 IIS
👉 Web server for .NET apps

⚖️ LINUX vs WINDOWS
Feature	Linux	Windows
Cost	Free	Paid
Performance	High	Moderate
Use case	Backend servers	Enterprise apps
Control	CLI heavy	GUI + CLI
🧠 PART 4: REAL PRODUCTION TASKS
💣 SCENARIO 1: Server Down
✅ Answer
“I would:

Check server health (CPU, memory)

Check logs

Restart services

Investigate root cause”

💣 SCENARIO 2: High CPU Usage
✅ Commands
top
ps aux --sort=-%cpu
👉 Kill or optimize process

💣 SCENARIO 3: Disk Full
df -h
du -sh *
👉 Clean logs / temp files

💣 SCENARIO 4: App Not Running
systemctl status app
journalctl -u app
💣 SCENARIO 5: Port Not Accessible
netstat -tuln
👉 Check firewall / service

🧠 PART 5: SECURITY
🔐 Linux
SSH keys (no password login)

Firewall (ufw)

Disable root login

🔐 Windows
Active Directory

Role-based access

Firewall

🧠 PART 6: AUTOMATION
🔥 Scripts
#!/bin/bash
systemctl restart app
🔥 Cron Jobs
crontab -e
👉 Schedule tasks

🧠 PART 7: MONITORING
Use tools like:

Nagios

New Relic

🧠 PART 8: INTERVIEW QUESTIONS
💥 Q1:
👉 “How do you debug a production issue?”

✅ Answer
“Check logs, monitor system metrics, identify bottleneck, and fix root cause.”

💥 Q2:
👉 “Linux vs Windows server?”

✅ Answer
“Linux is preferred for backend systems due to performance and flexibility, while Windows is used in enterprise environments and .NET ecosystems.”

💥 Q3:
👉 “How to secure server?”

✅ Answer
“Use SSH keys, firewalls, least privilege access, and regular patching.”

🎯 FINAL MENTAL MODEL
Think like:

Server = OS + Services + Logs + Monitoring + Security
### Practice
Answer:

1️⃣ How will you debug high memory usage?
2️⃣ Steps when server is not responding?
3️⃣ How to secure a Linux server?

👉 “Final full mock interview (Akamai-level)” 😈🔥
👉 “1-page revision cheat sheet before interview”


## Interview questions, mocks & scenarios

answe the questions


🧠 1️⃣ How will you debug high memory usage?
✅ Answer
“I would follow a step-by-step approach to identify and resolve high memory usage.”

🔍 Steps
1. Check overall memory
free -h
👉 Understand:

Total vs used vs available

2. Identify top processes
top
# or
ps aux --sort=-%mem
👉 Find which process is consuming memory

3. Deep dive into process
pmap -x <PID>
👉 Check memory allocation

4. Check logs
tail -f /var/log/syslog
👉 Look for:

Memory leaks

Errors

5. Take action
Restart process

Fix memory leak

Increase memory (if needed)

🎯 Interview Line
“I first identify the process consuming memory, analyze its behavior, and then either optimize, restart, or scale resources depending on the root cause.”

🧠 2️⃣ Steps when server is not responding?
✅ Answer
“I would debug systematically, starting from infrastructure to application level.”

🔍 Steps
1. Check server reachability
ping <server-ip>
👉 If not reachable → network issue

2. SSH into server
ssh user@server
👉 If fails → server might be down

3. Check system health
top
df -h
👉 CPU / Memory / Disk

4. Check services
systemctl status <service>
5. Check logs
journalctl -u <service>
6. Restart service
systemctl restart <service>
🎯 Interview Line
“I start by checking network connectivity, then system health, followed by service status and logs to identify and resolve the issue.”

🧠 3️⃣ How to secure a Linux server?
✅ Answer
“I would secure the server using multiple layers of protection.”

🔐 Key Steps
1. Use SSH Keys (No Password Login)
ssh-keygen
👉 Disable password login

2. Disable Root Login
PermitRootLogin no
3. Firewall Setup
ufw allow 22
ufw enable
4. Update System
apt update && apt upgrade
5. Least Privilege Access
Use non-root users

Role-based access

6. Monitor Logs
tail -f /var/log/auth.log
7. Install Security Tools
Fail2Ban

Intrusion detection

🎯 Interview Line
“I secure a Linux server by enforcing SSH key authentication, disabling root login, configuring firewalls, applying updates, and monitoring logs continuously.”

🎯 FINAL TAKEAWAY
You now answer like:

Problem → Diagnose → Fix → Prevent

👉 “1-page revision cheat sheet before interview”
