import os
import shutil
from datetime import datetime
from plyer import notification


class ResponseEngine:

    def log_incident(self, message):

        with open("logs/incidents.log", "a", encoding="utf-8") as file:
            file.write(f"[{datetime.now()}] {message}\n")

    def alert_user(self, title, message):

        notification.notify(
            title=title,
            message=message,
            timeout=5
        )

    def terminate_process(self, process):

        try:
            process.kill()
            return True

        except:
            return False

    def quarantine_file(self, executable_path):

        try:
            if os.path.exists(executable_path):

                filename = os.path.basename(executable_path)

                destination = os.path.join(
                    "quarantine",
                    filename
                )

                shutil.copy2(executable_path, destination)

                return True

        except:
            return False