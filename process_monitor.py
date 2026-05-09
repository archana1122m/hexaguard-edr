import psutil
import time
from datetime import datetime

import config

from engine.detection_engine import DetectionEngine
from engine.response_engine import ResponseEngine
from engine.threat_scoring import ThreatScorer
from engine.report_generator import ReportGenerator


class ProcessMonitor:

    def __init__(self, alert_queue):

        self.alert_queue = alert_queue
        self.detector = DetectionEngine()
        self.responder = ResponseEngine()
        self.scorer = ThreatScorer()
        self.reporter = ReportGenerator()

    def write_process_log(self, message):

        with open(
            "logs/process.log",
            "a",
            encoding="utf-8"
        ) as log:

            log.write(f"[{datetime.now()}] {message}\n")

    def write_alert_log(self, message):

        with open(
            "logs/alerts.log",
            "a",
            encoding="utf-8"
        ) as log:

            log.write(f"[{datetime.now()}] {message}\n")

    def monitor_processes(self):

        print("[+] Advanced EDR Monitoring Started...")

        while True:

            for process in psutil.process_iter():

                try:
                    pid = process.pid
                    name = process.name()
                    exe = process.exe()

                    cpu = process.cpu_percent(interval=0.1)

                    memory = process.memory_info().rss / (1024 * 1024)

                    cmdline = " ".join(process.cmdline())

                    parent_name = "Unknown"

                    try:
                        parent = process.parent()

                        if parent:
                            parent_name = parent.name()

                    except:
                        pass

                    process_info = {
                        "pid": pid,
                        "name": name,
                        "path": exe,
                        "cpu": cpu,
                        "memory": memory,
                        "cmdline": cmdline,
                        "parent_name": parent_name
                    }

                    self.write_process_log(
                        f"PID={pid} NAME={name} CPU={cpu}% MEM={memory:.2f}MB"
                    )

                    indicators = self.detector.analyze_process(
                        process_info
                    )

                    threat_score = self.scorer.calculate_score(
                        indicators
                    )

                    if threat_score >= 30:

                        print(
                            f"[SUSPICIOUS] "
                            f"{name} | "
                            f"PID={pid} | "
                            f"Score={threat_score}"
                        )

                        reasons = []

                        if indicators["blacklisted"]:
                            reasons.append("Blacklisted Process")

                        if indicators["suspicious_path"]:
                            reasons.append("Executed From Suspicious Directory")

                        if indicators["high_cpu"]:
                            reasons.append("High CPU Usage")

                        if indicators["high_memory"]:
                            reasons.append("High Memory Usage")

                        if indicators["encoded_powershell"]:
                            reasons.append("Encoded PowerShell Detected")

                        if indicators["office_child_process"]:
                            reasons.append("Office Spawned Shell")

                        reason_text = ", ".join(reasons)

                        alert_message = (
                            f"THREAT DETECTED\n"
                            f"Process : {name}\n"
                            f"PID     : {pid}\n"
                            f"Score   : {threat_score}\n"
                            f"Reason  : {reason_text}"
                        )

                        print(f"[ALERT]\n{alert_message}")

                        self.alert_queue.put(alert_message)

                        self.write_alert_log(alert_message)

                        self.responder.alert_user(
                            "Threat Detected",
                            alert_message
                        )

                        time.sleep(3)

                        terminated = self.responder.terminate_process(
                            process
                        )

                        if terminated:

                            self.responder.log_incident(
                                f"Process terminated: {name}"
                            )

                            self.responder.quarantine_file(exe)

                            self.reporter.write_report(
                                process_name=name,
                                pid=pid,
                                score=threat_score,
                                path=exe,
                                parent=parent_name,
                                cmdline=cmdline,
                                action="Process Terminated"
                            )

                            continue

                except (
                    psutil.NoSuchProcess,
                    psutil.AccessDenied,
                    psutil.ZombieProcess
                ):
                    pass

            time.sleep(config.PROCESS_SCAN_INTERVAL)