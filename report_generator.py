import csv
import os
from datetime import datetime


class ReportGenerator:

    def __init__(self):

        self.report_file = "reports/security_report.csv"

        self.create_report_file()

    def create_report_file(self):

        if not os.path.exists(self.report_file):

            with open(
                self.report_file,
                "w",
                newline="",
                encoding="utf-8"
            ) as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Timestamp",
                    "Process",
                    "PID",
                    "Threat Score",
                    "Executable Path",
                    "Parent Process",
                    "Command Line",
                    "Action Taken"
                ])

    def write_report(
        self,
        process_name,
        pid,
        score,
        path,
        parent,
        cmdline,
        action
    ):

        with open(
            self.report_file,
            "a",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                datetime.now(),
                process_name,
                pid,
                score,
                path,
                parent,
                cmdline,
                action
            ])