import socket
import threading
from utils import logger

class UDPServer:
    def __init__(self):
        self.server_socket = None
        self.running = False

    def start_server(self, ip, port, callback):
        """Starts the UDP server on the given IP and port."""
        if self.running:
            return "Server is already running!"

        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.server_socket.bind((ip, port))
            self.running = True
            threading.Thread(target=self.listen, args=(callback,), daemon=True).start()
            return f"Server started at {ip}:{port}"
        except OSError as e:
            return f"Error: {e}"

    def listen(self, callback):
        """Listens for incoming UDP messages."""
        while self.running:
            try:
                data, addr = self.server_socket.recvfrom(1024)
                callback(f"Received from {addr}: {data.decode()}")
            except Exception as e:
                callback(f"Error: {e}")
                break

    def stop_server(self):
        """Stops the UDP server."""
        if self.server_socket:
            self.running = False
            self.server_socket.close()
            return "Server stopped"
        return "No server is running"

    def refresh_ips():
        ip_list = []
        hostname = socket.gethostname()
        ips = socket.getaddrinfo(hostname, None)

        for ip in ips:
            ip_address = ip[4][0]
            if "." in ip_address:  # Filter IPv4 only
                ip_list.append(ip_address)
    
        return ip_list