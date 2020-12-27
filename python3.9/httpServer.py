#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        path = urlparse(self.path).path
        print(query_components)
        print(path)
        password = query_components.get('pass')
        cmd = query_components.get('cmd')
        print(password)
        print(cmd)

        if cmd is not None:
            cmd = cmd[0]

        print(cmd)

        if path != '/' or password is None or '123abc' not in password:
            self.send_response(401)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            message = "Unauthorized!"
            self.wfile.write(bytes(message, "utf8"))
            return

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        if cmd == 'sal':
            message = 'Zora Robot ti saluta'
        else:
            message = "Ok!"

        self.wfile.write(bytes(message, "utf8"))

        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('127.0.0.1', 10000)
        sock.settimeout(1)
        sock.connect(server_address)

        try:
            message = (cmd[:3]).encode('utf-8')
            sock.sendall(message)

        except:
            print("Socket error")
            sock.close()
            return

        finally:
            print('closing socket')
            sock.close()
        return


def run():
    print('Avvio del server...')
    # hostname = socket.gethostname()
    # local_ip = socket.gethostbyname(hostname)
    local_ip = '192.168.1.125'
    server_address = (local_ip, 8008)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('Server in esecuzione...')
    print('Ip = ', local_ip)
    httpd.serve_forever()


run()
