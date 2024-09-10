from tunnel import Tunnel, HttpTunnel, TcpTunnel
from decorators import LoggingTunnelDecorator, SecureTunnelDecorator

class TunnelBuilder:
    def __init__(self, tunnel_type: str, local_address: str):
        self.tunnel = self.create_tunnel(tunnel_type, local_address)
        self.logging_enabled = False
        self.encryption_enabled = False

    def create_tunnel(self, tunnel_type: str, local_address: str) -> Tunnel:
        if tunnel_type.upper() == "HTTP":
            return HttpTunnel(local_address)
        elif tunnel_type.upper() == "TCP":
            return TcpTunnel(local_address)
        else:
            raise ValueError(f"Unknown tunnel type: {tunnel_type}")

    def enable_logging(self):
        self.logging_enabled = True
        return self

    def enable_encryption(self):
        self.encryption_enabled = True
        return self

    def build(self) -> Tunnel:
        tunnel = self.tunnel
        if self.logging_enabled:
            tunnel = LoggingTunnelDecorator(tunnel)
        if self.encryption_enabled:
            tunnel = SecureTunnelDecorator(tunnel)
        return tunnel
