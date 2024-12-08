import http.server
import socketserver
import argparse
import os

parser = argparse.ArgumentParser(description='Simple HTTP Server')
parser.add_argument('--port', type=int, default=8000, help='Port to run the server on')
args = parser.parse_args()

index_file_path = os.path.join(os.path.dirname(__file__), 'index.html')

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def translate_path(self, path):
        if path == '/index.html':
            return index_file_path
        return http.server.SimpleHTTPRequestHandler.translate_path(self, path)

with socketserver.TCPServer(("", args.port), CustomHandler) as httpd:
    print(f"Serving on port {args.port}")
    httpd.serve_forever()