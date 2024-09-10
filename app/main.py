from ngrok_service import NgrokService
from builder import TunnelBuilder
from observer import LoggingObserver, MonitoringObserver
from load_balancer import RoundRobinStrategy, LeastConnectionsStrategy

if __name__ == "__main__":
    # Get the singleton instance of the NgrokService
    ngrok_service = NgrokService.get_instance()

    # Add observers
    logging_observer = LoggingObserver()
    monitoring_observer = MonitoringObserver()

    ngrok_service.add_observer(logging_observer)
    ngrok_service.add_observer(monitoring_observer)

    # Build tunnels with logging and encryption
    http_tunnel = TunnelBuilder("HTTP", "localhost:8080")\
                    .enable_logging()\
                    .enable_encryption()\
                    .build()

    tcp_tunnel = TunnelBuilder("TCP", "localhost:9090")\
                    .enable_logging()\
                    .build()

    # Add tunnels to the ngrok service
    ngrok_service.add_tunnel(http_tunnel)
    ngrok_service.add_tunnel(tcp_tunnel)

    # Set a load-balancing strategy
    round_robin_strategy = RoundRobinStrategy()
    ngrok_service.set_load_balancing_strategy(round_robin_strategy)

    # Start all tunnels
    ngrok_service.start_all_tunnels()

    # Handle a request
    ngrok_service.handle_request()
    ngrok_service.handle_request()  # This will use the next tunnel (round-robin)
