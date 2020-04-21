#!/usr/bin/env python3

import socket
import pigpio
from gpio_pin import gpio_pin

TCP_IP = '192.168.1.104'
TCP_PORT = 62
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

GPIO_PIN = 2

device = pigpio.pi()
pin = gpio_pin(device, GPIO_PIN)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))

while True:
    s.listen(1)

    conn, addr = s.accept()
    print('Connection address:', addr)
    while True:
         data = conn.recv(BUFFER_SIZE)
         if not data: break
         resp = "{}:{}".format(pin._eventcount, pin._delta)
         conn.send(bytes(resp, 'utf-8'))
    conn.close()
