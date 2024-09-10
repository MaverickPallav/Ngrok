from tunnel import Tunnel

class TunnelObserver:
    def update(self, tunnel: Tunnel, event: str):
        pass

# Concrete LoggingObserver
class LoggingObserver(TunnelObserver):
    def update(self, tunnel: Tunnel, event: str):
        print(f"Logging event: '{event}' on tunnel {tunnel.get_type()}")

# Concrete MonitoringObserver
class MonitoringObserver(TunnelObserver):
    def update(self, tunnel: Tunnel, event: str):
        print(f"Monitoring event: '{event}' on tunnel {tunnel.get_type()}")
