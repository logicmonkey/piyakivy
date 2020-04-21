import socket

HOST = '192.168.1.104' # Enter IP or Hostname of your server
PORT = 62 # Pick an open Port (1000+ recommended), must match the server port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

r = ' '
while r!='x':
    a = 0
    while a<100:
        s.send(bytes('ask', 'utf-8'))
        reply = s.recv(1024)
        print(reply.decode('utf-8'))
        a = a+1
    r = input("What?")
