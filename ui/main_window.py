import tkinter as tk
from ui.server_ui import ServerUI
from ui.log_ui import LogUI

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("UDP Communication")
        self.root.geometry("600x400")

        # Make sure rows and columns can expand properly
        self.root.grid_rowconfigure(0, weight=1)  # Server UI expands
        self.root.grid_rowconfigure(1, weight=0)  # Log UI stays fixed
        self.root.grid_columnconfigure(0, weight=1)

        # Create Log UI first
        self.log_ui = LogUI(self.root)
        self.log_ui.frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

        # Create Server UI and pass log_ui reference
        self.server_ui = ServerUI(self.root, self.log_ui)
        self.server_ui.frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
