#   This file is responsible for the web server.
#   It will be used to send data to the web server.
#   It will also be used to receive data from the web server.
import base64
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import cgi
from apiCalls import getCityWeatherImage

hostName = ""
hostPort = 80


#function to call CJ's function to get the weather image
def requestWeatherImage(city, state):
    return getCityWeatherImage(city,state)


class WeatherWebServer(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    #	GET is for clients geting the predi
    def do_GET(self):
        print(self.path)
        self.send_response(200)
        try:
            with open("."+self.path.replace("%20"," "), "rb") as f:
                webPage=f.read()
            self.wfile.write(webPage)
        except:
            with open("index.html", "r") as f:
                webPage=f.read()
            self.wfile.write(bytes(webPage, "utf-8"))

    #	POST is for submitting data.
    def do_POST(self):
        #Handle post request body
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
        tagList=False
        a=""
        #Output all fields
        for i in form:
            print(i)
        #handle different requests

        #Handle get weather request
        if form['type'].value == "getWeather":
            #Setup the HTML response template
            weatherImage,memo=requestWeatherImage(form['city'].value,form['state'].value)
            #return weatherImage
            self.respond(bytes(f'<!DOCTYPE html><html><head><meta http-equiv="refresh" content="2;url=.?state={form["state"].value}&city={form["city"].value}&memo=The%20weather%20in%20{form["city"].value},%20{form["state"].value}%20is%20currently%20{memo}."></head><body></body></html>', "utf-8"))

        print("incomming http: ", self.path)
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        self.send_response(200)
        print(self.rfile.read())

    #Tbh, idk what this is, but I see it in other servers set up like this, so whatever.
    def respond(self, response, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-length", len(response))
        self.end_headers()
        self.wfile.write(response)


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