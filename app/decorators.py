from tunnel import Tunnel

# Base TunnelDecorator class
class TunnelDecorator(Tunnel):
    def __init__(self, decorated_tunnel: Tunnel):
        self.decorated_tunnel = decorated_tunnel

    def start(self):
        self.decorated_tunnel.start()

    def get_type(self):
        return self.decorated_tunnel.get_type()

    def get_local_address(self):
        return self.decorated_tunnel.get_local_address()

class LoggingTunnelDecorator(TunnelDecorator):
    def __init__(self, decorated_tunnel: Tunnel):
        super().__init__(decorated_tunnel)

    def start(self):
        super().start()
        print(f"Logging enabled for tunnel: {self.decorated_tunnel.get_type()}")

class SecureTunnelDecorator(TunnelDecorator):
    def __init__(self, decorated_tunnel: Tunnel):
        super().__init__(decorated_tunnel)

    def start(self):
        super().start()
        print(f"Encryption enabled for tunnel: {self.decorated_tunnel.get_type()}")


