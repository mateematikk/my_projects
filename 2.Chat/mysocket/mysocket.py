import socket
import threading


def read_socket():
    while True:
        data = socket1.recv(1024)
        print(data.decode('utf-8'))


server = '192.168.0.1', 5050
login1 = input('Input login1')
socket1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket1.bind(('', 0))
socket1.sendto((login1 + ' Connect to server').encode('utf-8'), server)
t1 = threading.Thread(target=read_socket)
t1.start()
while True:
    login2 = input('Input login2')
    socket1.sendto(('[' + login1 + ']' + login2).encode('utf-8'), server)
