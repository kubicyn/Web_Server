from http.server import HTTPServer, BaseHTTPRequestHandler


class Server1(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'

        try:
            open_file = open(self.path[1:]).read()
            self.send_response(200)
        except:
            open_file = 'File not found.'
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(open_file, 'utf-8'))


httpd = HTTPServer(('localhost', 8080), Server1)
httpd.serve_forever()
