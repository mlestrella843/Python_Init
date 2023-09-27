import http.server
import socketserver

# Define el puerto en el que se ejecutará el servidor
PORT = 8000

# Configura el manejador de solicitudes para servir el contenido del directorio actual
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Servidor en el puerto", PORT)
    # Ejecuta el servidor
    httpd.serve_forever()
