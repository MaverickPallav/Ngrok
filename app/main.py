from ngrok_service import NgrokService
from builder import TunnelBuilder
from observer import LoggingObserver, MonitoringObserver
from load_balancer import RoundRobinStrategy

def get_port_from_user(prompt):
    while True:
        try:
            port = int(input(prompt))
            if 1 <= port <= 65535:
                return port
            else:
                print("Port number must be between 1 and 65535.")
        except ValueError:
            print("Invalid input. Please enter a valid port number.")

if __name__ == "__main__":
    ngrok_service = NgrokService.get_instance()

    logging_observer = LoggingObserver()
    monitoring_observer = MonitoringObserver()

    ngrok_service.add_observer(logging_observer)
    ngrok_service.add_observer(monitoring_observer)

    http_port = get_port_from_user("Enter the port for HTTP tunnel (e.g., 8080): ")
    # tcp_port = get_port_from_user("Enter the port for TCP tunnel (e.g., 9090): ")

    # Build tunnels with logging and encryption
    http_tunnel = TunnelBuilder("HTTP", f"localhost:{http_port}")\
                    .enable_logging()\
                    .enable_encryption()\
                    .build()

    # tcp_tunnel = TunnelBuilder("TCP", f"localhost:{tcp_port}")\
    #                 .enable_logging()\
    #                 .build()

    ngrok_service.add_tunnel(http_tunnel)
    # ngrok_service.add_tunnel(tcp_tunnel)

    round_robin_strategy = RoundRobinStrategy()
    ngrok_service.set_load_balancing_strategy(round_robin_strategy)

    ngrok_service.start_all_tunnels()

    # Get dynamic redirect port input from the user
    redirect_port = get_port_from_user("Enter the port for redirect (e.g., 3000): ")
    ngrok_service.add_redirect(f"localhost:{redirect_port}", http_tunnel)

    # Handle requests (assuming requests come with URLs)
    ngrok_service.handle_request(f"localhost:{redirect_port}")
    ngrok_service.handle_request(f"localhost:{http_port}")
