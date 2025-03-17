from services.network_service import NetworkService
from utils.logger import Logger

class ServerController:
    def __init__(self, log_ui):
        self.logger = Logger(log_ui)  # Pass log UI to Logger
        self.server = None

    def get_ip_addresses(self):
        return NetworkService.get_local_ips()

    def start_server(self, ip, port):
        try:
            self.server = NetworkService(ip, port)
            self.server.start()
            self.logger.log_info(f"UDP Server started at {ip}:{port}")
        except OSError as e:
            if "10048" in str(e):
                self.logger.log_error("Port already in use.")
            else:
                self.logger.log_error(str(e))

    def stop_server(self):
        if self.server:
            self.server.stop()
            self.logger.log_info("UDP Server stopped.")
