from tunnel import Tunnel
from observer import TunnelObserver
from load_balancer import LoadBalancingStrategy
from redirect_handler import start_redirect_server
import requests
import threading

class NgrokService:
    _instance = None

    def __init__(self):
        if NgrokService._instance is not None:
            raise Exception("This is a singleton class. Use get_instance() to access.")
        self.tunnels = []
        self.observers = []
        self.load_balancer = None
        self.redirects = {}
        self.redirect_server_thread = None

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

    def handle_request(self, request_url: str):
        if request_url in self.redirects:
            target_url = self.redirects[request_url]
            print(f"Redirecting {request_url} to {target_url}")
            response = requests.get(target_url)
            print(f"Response from redirected URL: {response.status_code} - {response.text}")
            return

        if not self.load_balancer or not self.tunnels:
            raise Exception("No load balancing strategy set or no tunnels available")
        
        selected_tunnel = self.load_balancer.select_tunnel(self.tunnels)
        print(f"Request handled by tunnel: {selected_tunnel.get_type()}")

    def add_redirect(self, source_url: str, target_tunnel: Tunnel):
        # Use '/' for the path in the redirect dictionary
        self.redirects['/'] = f"http://{target_tunnel.get_local_address()}"
        print(f"Redirect added: / -> {target_tunnel.get_local_address()}")
        # Ensure the redirect server is started
        if not self.redirect_server_thread:
            redirect_port = int(source_url.split(':')[1])
            self.redirect_server_thread = threading.Thread(target=start_redirect_server, args=(redirect_port, self.redirects))
            self.redirect_server_thread.start()


