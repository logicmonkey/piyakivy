import socket

HOST = '192.168.1.104' # Enter IP or Hostname of your server
PORT = 62 # Pick an open Port (1000+ recommended), must match the server port

ENCODING = 'utf-8'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

req = ''
while not(req=='x' or req=='STOP'):
    req = input('>')
    if req=='': break
    s.send(bytes(req, ENCODING))
    resp = s.recv(1024)
    print(resp.decode(ENCODING))
