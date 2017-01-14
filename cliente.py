import socket


HOST = '192.168.1.102'#ip do meu pc
PORT = 8686

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print"conectando"

s.connect((HOST,PORT))

for i in range(100):
 msg = raw_input("mensagem: ")
 s.send(msg)
 
s.close()
