from tunnel import Tunnel

# Base Load Balancing Strategy
class LoadBalancingStrategy:
    def select_tunnel(self, tunnels: list[Tunnel]) -> Tunnel:
        pass

# Round-robin strategy
class RoundRobinStrategy(LoadBalancingStrategy):
    def __init__(self):
        self.current_index = 0

    def select_tunnel(self, tunnels: list[Tunnel]) -> Tunnel:
        tunnel = tunnels[self.current_index]
        self.current_index = (self.current_index + 1) % len(tunnels)
        return tunnel

# Least-connections strategy (simplified)
class LeastConnectionsStrategy(LoadBalancingStrategy):
    def select_tunnel(self, tunnels: list[Tunnel]) -> Tunnel:
        return tunnels[0]  # Simplified: always choose the first one for now
