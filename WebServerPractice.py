from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

from io import BytesIO


class PythonSimpleWebServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"This is Manya's server")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        post_body = self.rfile.read(content_length)
      #  self.wfile.write("received post request:<br>{}".format(post_body))
        self.wfile.write(post_body)


httpd = HTTPServer(('localhost', 8080), PythonSimpleWebServer)
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.server_close()
