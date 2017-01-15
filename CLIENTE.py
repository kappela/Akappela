import socket
HOST = ''  
PORT = 4545       
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print 'Para sair use CTRL+X\n'
msg = raw_input()
for i in range(80):
    tcp.send (msg)
    msg = raw_input()
tcp.close()