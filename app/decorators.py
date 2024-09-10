from tunnel import Tunnel

# Base Decorator class
class TunnelDecorator(Tunnel):
    def __init__(self, tunnel: Tunnel):
        self._tunnel = tunnel

    def start(self):
        self._tunnel.start()

    def get_type(self):
        return self._tunnel.get_type()

# Concrete Logging decorator
class LoggingTunnelDecorator(TunnelDecorator):
    def start(self):
        super().start()
        print(f"Logging enabled for tunnel: {self._tunnel.get_type()}")

# Concrete Encryption decorator
class SecureTunnelDecorator(TunnelDecorator):
    def start(self):
        super().start()
        print(f"Encryption enabled for tunnel: {self._tunnel.get_type()}")
