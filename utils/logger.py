import logging

class Logger:
    def __init__(self, log_ui=None):
        self.log_ui = log_ui
        logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    def log_info(self, message):
        logging.info(message)
        if self.log_ui:
            self.log_ui.log_message(f"INFO: {message}")

    def log_error(self, message):
        logging.error(message)
        if self.log_ui:
            self.log_ui.log_message(f"ERROR: {message}")
