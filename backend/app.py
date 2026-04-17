from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello from Effective Mobile!") 
if __name__ == "__main__":
    # Сервер слушает порт 8080 [cite: 16]
    server = HTTPServer(('0.0.0.0', 8080), Handler)
    server.serve_forever()