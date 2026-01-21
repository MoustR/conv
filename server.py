import http.server
import socketserver
import os
import mimetypes
import json

PORT = 3000

# MIME types
MIME_TYPES = {
    '.html': 'text/html',
    '.js': 'application/javascript',
    '.css': 'text/css',
    '.svg': 'image/svg+xml',
    '.webp': 'image/webp',
    '.woff2': 'font/woff2',
    '.json': 'application/json',
    '.webmanifest': 'application/manifest+json',
    '.txt': 'text/plain'
}

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Clean path
        path = self.path.split('?')[0]
        
        # Default to index.html
        if path == '/':
            path = '/index.html'
        
        # Remove leading slash
        file_path = path[1:] if path.startswith('/') else path
        
        # Check if file exists
        if os.path.exists(file_path):
            self.send_file(file_path)
        else:
            # Check common alternatives
            alternatives = [
                file_path,
                'assets/' + file_path,
                'cdn-assets/' + file_path,
                'fonts/' + file_path
            ]
            
            for alt in alternatives:
                if os.path.exists(alt):
                    self.send_file(alt)
                    return
            
            # File not found
            self.send_error(404, f"File not found: {path}")
    
    def send_file(self, file_path):
        ext = os.path.splitext(file_path)[1].lower()
        content_type = MIME_TYPES.get(ext, 'application/octet-stream')
        
        try:
            with open(file_path, 'rb') as f:
                content = f.read()
            
            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.send_header('Content-Length', len(content))
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(content)
            
            print(f"✅ 200: {file_path}")
            
        except Exception as e:
            self.send_error(500, str(e))
    
    def log_message(self, format, *args):
        # Custom log format
        pass

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print("=" * 50)
    print("Converty Shop - Local Development Server")
    print("=" * 50)
    print(f"📂 Directory: {os.getcwd()}")
    print(f"🌐 URL: http://localhost:{PORT}")
    print("=" * 50)
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 Server stopped")

if __name__ == '__main__':
    main()