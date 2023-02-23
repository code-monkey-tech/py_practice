from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

from io import BytesIO


class ManyaServer(BaseHTTPRequestHandler):

    def get_request(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"This is Manya's server")

    def post_request(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        response = BytesIO
        response.write('Post request')
        response.write('Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())


httpd = HTTPServer(('localhost', 8080), ManyaServer)
httpd.serve_forever()
