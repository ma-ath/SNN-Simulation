import SimpleHTTPServer
import SocketServer

def startServer():
    print "iniciando servidor!"
    PORT = 8080
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "serving at port", PORT
    httpd.serve_forever()

startServer();
