class Tunnel:
    def start(self):
        raise NotImplementedError("Subclasses should implement this!")

    def get_type(self):
        raise NotImplementedError("Subclasses should implement this!")

# Concrete HTTP Tunnel implementation
class HttpTunnel(Tunnel):
    def __init__(self, local_address):
        self.local_address = local_address

    def start(self):
        print(f"Starting HTTP Tunnel on {self.local_address}")

    def get_type(self):
        return "HTTP"

# Concrete TCP Tunnel implementation
class TcpTunnel(Tunnel):
    def __init__(self, local_address):
        self.local_address = local_address

    def start(self):
        print(f"Starting TCP Tunnel on {self.local_address}")

    def get_type(self):
        return "TCP"
