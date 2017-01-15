import socket
HOST = ''            
PORT = 4545
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    while True:
        msg = con.recv(1024)
        if not msg: break
    con.close()