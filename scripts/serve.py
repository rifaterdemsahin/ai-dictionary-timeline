#!/usr/bin/env python3
"""
CORS-enabled HTTP development server for Claude Associate Engine.
Runs on port 30085 by default and sends Access-Control-Allow-Origin headers
so that local and remote browser sessions can freely fetch JSON data payloads.
"""

import sys
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT_DIR), **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, HEAD, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Origin, Accept, Authorization')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.end_headers()

def run(port=30085):
    server_address = ('0.0.0.0', port)
    httpd = ThreadingHTTPServer(server_address, CORSRequestHandler)
    print(f"🚀 Claude Associate Server running on port {port} with CORS enabled:")
    print(f"   http://localhost:{port}/")
    print(f"   http://localhost:{port}/pages/json-viewer.html")
    httpd.serve_forever()

if __name__ == '__main__':
    p = int(sys.argv[1]) if len(sys.argv) > 1 else 30085
    run(p)
