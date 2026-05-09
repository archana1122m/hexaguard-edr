PROCESS_SCAN_INTERVAL = 1
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 500
THREAT_THRESHOLD = 40

CRITICAL_SERVICES = [
    "WinDefend",
    "EventLog",
    "SecurityHealthService"
]

WHITELIST_PATHS = [
    r"C:\Windows\System32",
    r"C:\Program Files",
    r"C:\Program Files (x86)"
]

WHITELIST_PROCESSES = [
    "chrome.exe",
    "msmpeng.exe",
    "msedge.exe",
    "notion.exe",
    "searchindexer.exe",
    "supportassistagent.exe",
    "explorer.exe",
    "svchost.exe",
    "dwm.exe",
    "services.exe",
    "python.exe",
    "python3.exe",
    "python3.12.exe",
    "code.exe",
    "taskmgr.exe",
    "conhost.exe"
]