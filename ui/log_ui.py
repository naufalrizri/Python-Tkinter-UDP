import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class LogUI:
    def __init__(self, parent):
        self.frame = tk.LabelFrame(parent, text="Logs", padx=5, pady=5)
        
        # Scrolled text area for logs
        self.text_area = ScrolledText(self.frame, height=6, state="disabled")
        self.text_area.grid(row=0, column=0, sticky="nsew")

        # Allow expansion
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

    def log_message(self, message):
        self.text_area.config(state="normal")
        self.text_area.insert("end", message + "\n")
        self.text_area.config(state="disabled")
        self.text_area.yview("end")  # Auto-scroll to latest log
