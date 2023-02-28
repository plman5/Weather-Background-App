#   This file is responsible for the web server.
#   It will be used to send data to the web server.
#   It will also be used to receive data from the web server.


import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = ""
hostPort = 80

class WeatherWebServer(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    #	GET is for clients geting the predi
    def do_GET(self):
        self.send_response(200)
        self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))

    #	POST is for submitting data.
    def do_POST(self):
        print("incomming http: ", self.path)
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        self.send_response(200)
        print(self.rfile.read())


#Start running the server
def run(server_class=HTTPServer, handler_class=WeatherWebServer, port=8080):
    weatherServer = HTTPServer((hostName, hostPort), WeatherWebServer)
    print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))
    try:
        weatherServer.serve_forever()
    except KeyboardInterrupt:
        pass
    weatherServer.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))


#It's being run via command line
if __name__ == '__main__':
    from sys import argv
    #Give the user the option of choosing the port
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()