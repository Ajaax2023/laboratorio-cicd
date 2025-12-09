from http.server import BaseHTTPRequestHandler, HTTPServer


# --- LÓGICA DE NEGOCIO (Separada para poder testearla) ---
def obtener_mensaje_html():
    # Aquí puedes cambiar el texto o el color cuando quieras
    mensaje = """
    <html>
    <head>
        <meta charset="UTF-8">
    </head>
    <body>
        <h1 style="color:red;">¡Versión 2.2 verificada con Test Unitario!</h1>
        <p>Si ves esto, es que el test pasó correctamente.</p>
    </body>
    </html>
    """
    return mensaje.encode("utf-8")


# --- SERVIDOR WEB ---
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        # Llamamos a la función que genera el contenido
        self.wfile.write(obtener_mensaje_html())


def run():
    print("Iniciando servidor...")
    server_address = ("0.0.0.0", 80)
    httpd = HTTPServer(server_address, SimpleHandler)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
