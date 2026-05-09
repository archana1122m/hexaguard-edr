# 🛡 HexaGuard EDR

HexaGuard EDR is a lightweight behavioral Endpoint Detection and Response (EDR) platform developed in Python for real-time threat detection, suspicious process monitoring, automated response, and incident reporting.

> ⚠️ Recommended to run as Administrator for proper process monitoring and process termination.

---

# 🚀 Features

- Real-Time Process Monitoring
- Behavioral Threat Detection
- Encoded PowerShell Detection
- Suspicious Path Execution Detection
- Blacklisted Process Detection
- High CPU Usage Detection
- High Memory Usage Detection
- Office → Shell Spawn Detection
- Automated Process Termination
- Quarantine System
- Live Monitoring Dashboard
- Alert Logging
- Incident Reporting
- CSV Report Generation

---

# 🧠 Detection Capabilities

- Encoded PowerShell Detection  
  Detects Base64 encoded PowerShell commands and suspicious scripting activity.

- Suspicious Path Execution Detection  
  Detects executables launched from suspicious directories such as Temp, Public, and Downloads.

- Blacklisted Process Detection  
  Detects known malicious or blacklisted process names.

- High CPU Usage Detection  
  Detects abnormal CPU-consuming processes and potential resource abuse behavior.

- High Memory Usage Detection  
  Detects excessive memory consumption and memory abuse activity.

- Office Child Process Detection  
  Detects Office applications spawning shell processes such as CMD or PowerShell.

---

# 🛠 Technologies Used

- Python
- psutil
- customtkinter
- plyer

---

# 📂 Project Structure

```text
HexaGuard-EDR/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
│
├── engine/
│   ├── process_monitor.py
│   ├── detection_engine.py
│   ├── response_engine.py
│   ├── threat_scoring.py
│   ├── report_generator.py
│   └── service_monitor.py
│
├── gui/
│   └── dashboard.py
│
├── blacklist/
│   ├── process_blacklist.txt
│   └── path_blacklist.txt
│
├── screenshots/
```

---

# ⚙️ Installation

## Download Project

Download the repository as ZIP and extract it.

---

## Navigate Into Project Folder

```bash
cd HexaGuard-EDR
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running The Project

```bash
python main.py
```

---

# 🧪 Test Commands

## Encoded PowerShell Detection

```powershell
powershell -enc VwBoAGkAbABlACAAKAAkAHQAcgB1AGUAKQAgAHsAIABTAHQAYQByAHQALQBTAGwAZQBlAHAAIAAxACAAfQA=
```

---

## Blacklisted Malware Detection

```cmd
copy C:\Windows\System32\cmd.exe mimikatz.exe
mimikatz.exe
```

---

## Suspicious Path Execution Detection

```cmd
copy C:\Windows\System32\cmd.exe %TEMP%\evil.exe
%TEMP%\evil.exe
```

---

## High CPU Usage Detection

```powershell
powershell -command "while($true){}"
```

---

## High Memory Usage Detection

```powershell
powershell -command "$a=@(); while($true){$a += 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'}"
```

---

# 📊 Dashboard

HexaGuard EDR includes a modern graphical dashboard with:

- Live Threat Feed
- Threat Scores
- Detection Reasons
- Blocked Process Counter
- Real-Time Monitoring Status

---

# 📑 Reporting

The platform automatically generates:

- Alert Logs
- Incident Logs
- CSV Security Reports

---

# 🔒 Automated Response

When malicious or suspicious behavior is detected, HexaGuard EDR can:

- Terminate Processes
- Generate Alerts
- Log Incidents
- Quarantine Executables
- Generate Security Reports

---

# 📸 Screenshots

Recommended screenshots:

- Dashboard
- Testing
- Alert Generation 
- Terminal Output
- Dashboard Output
  
<img width="960" height="503" alt="dashboard_output" src="https://github.com/user-attachments/assets/6e178ac0-718d-400c-8a1b-cf147d58765e" />
<img width="941" height="480" alt="terminal_output" src="https://github.com/user-attachments/assets/5584c9bf-0a94-4127-924f-e4cdeaecbfb5" />
<img width="945" height="459" alt="alert_generation" src="https://github.com/user-attachments/assets/348b051b-37e0-47f3-a743-9c5490361fa5" />
<img width="942" height="375" alt="testing" src="https://github.com/user-attachments/assets/26d1d898-b3df-4ad8-b505-5452c0feb62f" />
<img width="960" height="503" alt="dashboard" src="https://github.com/user-attachments/assets/2ee8077b-c5e3-49b1-a12b-f014a5ac9811" />

---

# 🎯 Project Type

Cybersecurity / Blue Team / Endpoint Security / Behavioral Detection

---

# 👨‍💻 Author

Developed as a cybersecurity project focused on behavioral endpoint detection, threat monitoring, and automated incident response.
