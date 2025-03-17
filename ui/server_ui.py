import tkinter as tk
from tkinter import ttk
import socket
from services.network_service import UDPServer

class ServerUI:
    def __init__(self, parent, log_ui):
        self.log_ui = log_ui
        self.frame = tk.LabelFrame(parent, text="Server UDP", padx=10, pady=10, font=("Segoe UI", 10, "bold"))
        
        # Server IP Dropdown
        self.server_ip_label = tk.Label(self.frame, text="Server IP Address:", font=("Segoe UI", 10))
        self.server_ip_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.server_ip_menu = ttk.Combobox(self.frame, width=20, state="readonly")
        self.server_ip_menu.grid(row=0, column=1, padx=5, pady=5)

        self.refresh_button = ttk.Button(self.frame, text="Refresh", command=self.refresh_ip_dropdown, width=10)
        self.refresh_button.grid(row=0, column=2, padx=5, pady=5)

        # Port Input
        self.port_label = tk.Label(self.frame, text="Port:", font=("Segoe UI", 10))
        self.port_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)

        self.port_entry = ttk.Entry(self.frame, width=15)
        self.port_entry.grid(row=1, column=1, padx=5, pady=5)

        # Buttons (Set & Stop)
        button_frame = tk.Frame(self.frame)
        button_frame.grid(row=1, column=2, padx=5, pady=5, sticky="ew")

        self.set_button = ttk.Button(button_frame, text="Set", command=self.start_server, width=10)
        self.set_button.pack(pady=2)

        self.stop_button = ttk.Button(button_frame, text="Stop", command=self.stop_server, width=10)
        self.stop_button.pack(pady=2)
    
    # Getter IP list dropdown
    def refresh_ip_dropdown(self):
        """Updates the dropdown with available IP addresses."""
        self.server_ip_menu['values'] = UDPServer.refresh_ips()
        if self.server_ip_menu['values']:
            self.server_ip_menu.current(0)  # Select first IP by default

    def start_server(self):
        """Start the thread for udp server"""
        # take the needed variable
        UDPServer.start_server(UDPServer, self.server_ip_menu.get(), self.port_entry.get(),)

    def stop_server(self):
        pass