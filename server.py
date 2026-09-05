import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000

# Cambiar al directorio donde se encuentra este script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Permitir reutilizar el puerto
socketserver.TCPServer.allow_reuse_address = True

def run_server():
    port = PORT
    handler = http.server.SimpleHTTPRequestHandler

    for attempt in range(5):
        try:
            httpd = socketserver.TCPServer(("", port), handler)
            break
        except OSError:
            print(f"  Puerto {port} ocupado, intentando {port + 1}...")
            port += 1
    else:
        print("No se pudo encontrar un puerto disponible.")
        sys.exit(1)

    url = f"http://localhost:{port}"
    print("=" * 50)
    print(f"  Servidor de Caseritos iniciado exitosamente")
    print(f"  URL: {url}")
    print("  Abriendo en tu navegador...")
    print("  Presiona Ctrl + C para detenerlo")
    print("=" * 50)

    webbrowser.open(url)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido. ¡Hasta luego!")
        httpd.server_close()
        sys.exit(0)

if __name__ == "__main__":
    run_server()
