#!/usr/bin/env python3
"""
Simple HTTP server with basic routing support for local development.
For full Vercel routing features, use: npm run dev (requires Vercel CLI)
"""

import http.server
import socketserver
import os
import urllib.parse
from pathlib import Path

PORT = 8000

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()
    
    def do_GET(self):
        # Parse the path
        parsed_path = urllib.parse.urlparse(self.path)
        request_path = parsed_path.path
        
        # Remove leading slash
        if request_path.startswith('/'):
            request_path = request_path[1:]
        
        # Handle root
        if request_path == '' or request_path == '/':
            request_path = 'index.html'
        
        # Get base directory (where server.py is located)
        base_dir = Path(__file__).parent.resolve()
        
        # Handle clean URLs (without .html extension)
        file_path = base_dir / request_path
        
        # If no extension, try adding .html
        if not file_path.suffix or file_path.suffix == '':
            html_path = base_dir / (request_path + '.html')
            if html_path.exists() and html_path.is_file():
                file_path = html_path
        
        # Check if file exists and is a file (not directory)
        if file_path.exists() and file_path.is_file():
            # Serve the file
            try:
                with open(file_path, 'rb') as f:
                    content = f.read()
                
                # Determine content type
                if file_path.suffix == '.html':
                    content_type = 'text/html'
                elif file_path.suffix == '.css':
                    content_type = 'text/css'
                elif file_path.suffix == '.js':
                    content_type = 'application/javascript'
                else:
                    content_type = 'application/octet-stream'
                
                self.send_response(200)
                self.send_header('Content-type', content_type)
                self.send_header('Content-length', str(len(content)))
                self.end_headers()
                self.wfile.write(content)
                return
            except Exception as e:
                self.send_error(500, f"Error reading file: {str(e)}")
                return
        else:
            # Try with .html extension one more time
            if not request_path.endswith('.html'):
                html_path = base_dir / (request_path + '.html')
                if html_path.exists() and html_path.is_file():
                    try:
                        with open(html_path, 'rb') as f:
                            content = f.read()
                        self.send_response(200)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Content-length', str(len(content)))
                        self.end_headers()
                        self.wfile.write(content)
                        return
                    except Exception as e:
                        self.send_error(500, f"Error reading file: {str(e)}")
                        return
            
            # 404
            self.send_error(404, f"File not found: {self.path}")
            return

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}/")
        print("Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
