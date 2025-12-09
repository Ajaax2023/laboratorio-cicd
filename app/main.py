# app/main.py
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        # Este es el mensaje que cambiaremos para probar el pipeline
        mensaje = "<h1 style='color:red'>¡Versión 2.1 desplegada automáticamente con Jenkins! y con tildes arregladas</h1>"
        self.wfile.write(mensaje.encode("utf-8"))


def run():
    print("Iniciando servidor...")
    server_address = ("0.0.0.0", 80)
    httpd = HTTPServer(server_address, SimpleHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
