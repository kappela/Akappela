#tai ta tuudo no basico mesmo

import socket

HOST = '192.168.1.102'              
PORT = 8686

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    while True:
        msg = con.recv(1024)
        if not msg: break
        print cliente, msg
    con.close()
