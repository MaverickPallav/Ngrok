from tunnel import Tunnel
from decorators import LoggingTunnelDecorator, SecureTunnelDecorator
from tunnel import HttpTunnel, TcpTunnel

# TunnelBuilder for building tunnels with optional features
class TunnelBuilder:
    def __init__(self, type: str, local_address: str):
        self.tunnel = self.create_tunnel(type, local_address)
        self.logging_enabled = False
        self.encryption_enabled = False

    def create_tunnel(self, type: str, local_address: str) -> Tunnel:
        if type.upper() == "HTTP":
            return HttpTunnel(local_address)
        elif type.upper() == "TCP":
            return TcpTunnel(local_address)
        else:
            raise ValueError("Unknown tunnel type")

    def enable_logging(self):
        self.logging_enabled = True
        return self

    def enable_encryption(self):
        self.encryption_enabled = True
        return self

    def build(self) -> Tunnel:
        if self.logging_enabled:
            self.tunnel = LoggingTunnelDecorator(self.tunnel)
        if self.encryption_enabled:
            self.tunnel = SecureTunnelDecorator(self.tunnel)
        return self.tunnel
