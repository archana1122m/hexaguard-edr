import psutil
from datetime import datetime


class ServiceMonitor:

    def monitor_services(self):

        while True:

            for service in psutil.win_service_iter():

                try:
                    service_info = service.as_dict()

                    message = (
                        f"[{datetime.now()}] "
                        f"Service: {service_info['name']} | "
                        f"Status: {service_info['status']}\n"
                    )

                    with open(
                        "logs/services.log",
                        "a",
                        encoding="utf-8"
                    ) as log:
                        log.write(message)

                except:
                    pass