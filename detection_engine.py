import config


class DetectionEngine:

    def __init__(self):

        self.blacklist = self.load_blacklist()

    def load_blacklist(self):

        blacklist = []

        with open(
            "blacklist/process_blacklist.txt",
            "r",
            encoding="utf-8"
        ) as file:

            for line in file:
                blacklist.append(line.strip().lower())

        return blacklist

    def analyze_process(self, process_info):

        indicators = {
            "blacklisted": False,
            "suspicious_path": False,
            "high_cpu": False,
            "high_memory": False,
            "encoded_powershell": False,
            "office_child_process": False
        }

        process_name = process_info["name"].lower()
        if process_name in config.WHITELIST_PROCESSES:
            return indicators
        process_path = process_info["path"].lower()
        cmdline = process_info["cmdline"].lower()
        cpu = process_info["cpu"]
        memory = process_info["memory"]
        parent_name = process_info["parent_name"].lower()

        for bad_process in self.blacklist:
            if (
                   bad_process in process_name
                   or bad_process in process_path
            ):

                     indicators["blacklisted"] = True

        suspicious_directories = [
            "temp",
            "downloads",
            "public"
        ]

        for directory in suspicious_directories:

           if directory in process_path:
              indicators["suspicious_path"] = True

        if ( cpu > config.CPU_THRESHOLD and memory < config.MEMORY_THRESHOLD and process_name not in config.WHITELIST_PROCESSES ):
                indicators["high_cpu"] = True

        if ( memory > config.MEMORY_THRESHOLD and process_name not in config.WHITELIST_PROCESSES ):
               indicators["high_memory"] = True

        if ( "powershell" in process_name or "pwsh" in process_name ) and "-enc" in cmdline:
            indicators["encoded_powershell"] = True

        office_apps = [
            "winword.exe",
            "excel.exe",
            "powerpnt.exe"
        ]

        suspicious_children = [
            "cmd.exe",
            "powershell.exe"
        ]

        if parent_name in office_apps:
            if process_name in suspicious_children:
                indicators["office_child_process"] = True

        return indicators