#!/usr/bin/env python3

import socket
import pigpio
from gpio_pin import gpio_pin

TCP_IP = '192.168.1.104'
TCP_PORT = 62
BUFFER_SIZE = 1024
ENCODING = 'utf-8'

GPIO_PIN = 2

device = pigpio.pi()
pin = gpio_pin(device, GPIO_PIN)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))

req_str = ''

while req_str != 'STOP':
    s.listen(1)

    conn, addr = s.accept()
    print('Connection address:', addr)
    while True:
         req = conn.recv(BUFFER_SIZE)
         req_str = req.decode(ENCODING)
         if (not req) or (req_str == 'STOP'): break
         resp = "{}:{}".format(pin._eventcount, pin._delta)
         conn.send(bytes(resp, ENCODING))

print('STOP command received')
conn.close()
pin.cancel()
device.stop()
