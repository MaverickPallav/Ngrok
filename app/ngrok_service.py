from tunnel import Tunnel
from observer import TunnelObserver
from load_balancer import LoadBalancingStrategy

class NgrokService:
    _instance = None

    def __init__(self):
        if NgrokService._instance is not None:
            raise Exception("This is a singleton class. Use get_instance() to access.")
        self.tunnels = []
        self.observers = []
        self.load_balancer = None

    @staticmethod
    def get_instance():
        if NgrokService._instance is None:
            NgrokService._instance = NgrokService()
        return NgrokService._instance

    def add_tunnel(self, tunnel: Tunnel):
        self.tunnels.append(tunnel)
        self.notify_observers(tunnel, "Tunnel added")
        print(f"Tunnel added: {tunnel.get_type()}")

    def start_all_tunnels(self):
        for tunnel in self.tunnels:
            tunnel.start()
            self.notify_observers(tunnel, "Tunnel started")

    def add_observer(self, observer: TunnelObserver):
        self.observers.append(observer)

    def notify_observers(self, tunnel, event: str):
        for observer in self.observers:
            observer.update(tunnel, event)

    def set_load_balancing_strategy(self, strategy: LoadBalancingStrategy):
        self.load_balancer = strategy

    def handle_request(self):
        if not self.load_balancer or not self.tunnels:
            raise Exception("No load balancing strategy set or no tunnels available")
        selected_tunnel = self.load_balancer.select_tunnel(self.tunnels)
        print(f"Request handled by tunnel: {selected_tunnel.get_type()}")
