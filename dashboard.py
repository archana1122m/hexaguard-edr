import customtkinter as ctk
from datetime import datetime


class Dashboard:

    def __init__(self, alert_queue):

        self.alert_queue = alert_queue

        self.total_alerts = 0
        self.blocked_processes = 0

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.app = ctk.CTk()

        self.app.geometry("1400x850")

        self.app.title("HexaGuard EDR")

        # =========================
        # HEADER
        # =========================

        self.header = ctk.CTkFrame(
            self.app,
            corner_radius=15,
            height=80
        )

        self.header.pack(
            fill="x",
            padx=20,
            pady=15
        )

        self.title = ctk.CTkLabel(
            self.header,
            text="🛡 HexaGuard EDR Dashboard",
            font=("Arial", 30, "bold")
        )

        self.title.pack(
            side="left",
            padx=25,
            pady=20
        )

        self.status_label = ctk.CTkLabel(
            self.header,
            text="● ACTIVE",
            text_color="lightgreen",
            font=("Arial", 18, "bold")
        )

        self.status_label.pack(
            side="right",
            padx=25
        )

        # =========================
        # TOP CARDS
        # =========================

        self.cards_frame = ctk.CTkFrame(
            self.app,
            fg_color="transparent"
        )

        self.cards_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        # ALERT CARD

        self.alert_card = ctk.CTkFrame(
            self.cards_frame,
            corner_radius=20,
            width=300,
            height=130
        )

        self.alert_card.pack(
            side="left",
            padx=15,
            pady=10
        )

        self.alert_title = ctk.CTkLabel(
            self.alert_card,
            text="⚠ Threat Alerts",
            font=("Arial", 22, "bold")
        )

        self.alert_title.pack(pady=(20, 5))

        self.alert_count = ctk.CTkLabel(
            self.alert_card,
            text="0",
            font=("Arial", 42, "bold"),
            text_color="orange"
        )

        self.alert_count.pack()

        # BLOCKED CARD

        self.block_card = ctk.CTkFrame(
            self.cards_frame,
            corner_radius=20,
            width=300,
            height=130
        )

        self.block_card.pack(
            side="left",
            padx=15,
            pady=10
        )

        self.block_title = ctk.CTkLabel(
            self.block_card,
            text="⛔ Blocked Processes",
            font=("Arial", 22, "bold")
        )

        self.block_title.pack(pady=(20, 5))

        self.block_count = ctk.CTkLabel(
            self.block_card,
            text="0",
            font=("Arial", 42, "bold"),
            text_color="red"
        )

        self.block_count.pack()

        # SYSTEM STATUS CARD

        self.system_card = ctk.CTkFrame(
            self.cards_frame,
            corner_radius=20,
            width=300,
            height=130
        )

        self.system_card.pack(
            side="left",
            padx=15,
            pady=10
        )

        self.system_title = ctk.CTkLabel(
            self.system_card,
            text="💻 System Status",
            font=("Arial", 22, "bold")
        )

        self.system_title.pack(pady=(20, 5))

        self.system_status = ctk.CTkLabel(
            self.system_card,
            text="SECURE",
            font=("Arial", 32, "bold"),
            text_color="lightgreen"
        )

        self.system_status.pack()

        # =========================
        # INCIDENT PANEL
        # =========================

        self.incident_frame = ctk.CTkFrame(
            self.app,
            corner_radius=20
        )

        self.incident_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        self.incident_title = ctk.CTkLabel(
            self.incident_frame,
            text="🚨 Live Threat Feed",
            font=("Arial", 26, "bold")
        )

        self.incident_title.pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        self.alert_box = ctk.CTkTextbox(
            self.incident_frame,
            font=("Consolas", 15),
            corner_radius=15
        )

        self.alert_box.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=15
        )

        self.alert_box.insert(
            "end",
            "[SYSTEM] HexaGuard EDR Initialized Successfully\n\n"
        )

        self.update_alerts()

    # =========================================
    # LIVE ALERT UPDATE
    # =========================================

    def update_alerts(self):

        while not self.alert_queue.empty():

            alert = self.alert_queue.get()

            current_time = datetime.now().strftime("%H:%M:%S")

            formatted_alert = (
                f"[{current_time}] "
                f"{alert}\n"
                f"{'=' * 80}\n\n"
            )

            self.alert_box.insert(
                "end",
                formatted_alert
            )

            self.alert_box.see("end")

            self.total_alerts += 1
            self.blocked_processes += 1

            self.alert_count.configure(
                text=str(self.total_alerts)
            )

            self.block_count.configure(
                text=str(self.blocked_processes)
            )

            self.system_status.configure(
                text="THREAT DETECTED",
                text_color="red"
            )

        self.app.after(1000, self.update_alerts)

    def run(self):

        self.app.mainloop()