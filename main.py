import threading
import queue

from engine.process_monitor import ProcessMonitor
from engine.service_monitor import ServiceMonitor
from gui.dashboard import Dashboard


alert_queue = queue.Queue()


def start_process_monitor():

    monitor = ProcessMonitor(alert_queue)
    monitor.monitor_processes()


def start_service_monitor():

    service_monitor = ServiceMonitor()
    service_monitor.monitor_services()


if __name__ == "__main__":

    process_thread = threading.Thread(
        target=start_process_monitor,
        daemon=True
    )

    service_thread = threading.Thread(
        target=start_service_monitor,
        daemon=True
    )

    process_thread.start()
    service_thread.start()

    dashboard = Dashboard(alert_queue)
    dashboard.run()