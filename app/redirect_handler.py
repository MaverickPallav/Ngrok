from http.server import SimpleHTTPRequestHandler, HTTPServer
import threading

class RedirectHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.redirects = kwargs.pop('redirects')
        super().__init__(*args, **kwargs)

    def do_GET(self):
        # Debugging output
        print(f"Handling request for path: {self.path}")
        print(f"REDIRECTS {self.redirects}")

        # Adjusted to handle requests properly
        redirect_target = self.redirects.get(self.path)
        if redirect_target:
            print(f"Redirecting to: {redirect_target}")
            self.send_response(302)  # HTTP status code for redirection
            self.send_header('Location', redirect_target)
            self.end_headers()
        else:
            print("No redirect found, sending 404")
            self.send_response(404)
            self.end_headers()

def start_redirect_server(port, redirects):
    server_address = ('', port)
    handler = lambda *args, **kwargs: RedirectHandler(*args, redirects=redirects, **kwargs)
    httpd = HTTPServer(server_address, handler)
    print(f"Starting redirect server on port {port}")
    httpd.serve_forever()