import socket
import codecs
import base64
import sys
import time

from colorama import Fore, Back, Style

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = sys.argv[1]

puerto = sys.argv[2]

cliente_socket.connect((host, int(puerto)))


print(base64.b64decode(cliente_socket.recv(4000)))

name = input("\nnombre: ")
empaquetar_1 = name.encode(encoding='utf-8')
    
cliente_socket.send(empaquetar_1)
    
desempaquetar = cliente_socket.recv(4000).decode('utf8')
    
print(desempaquetar)


while True:   
    ava = input(f"\n{name}: ")
    
    mensaje = f"""
    {name}:
    {ava}

          """
         
    print(ava)
    empaquetar_2 = ava.encode(encoding='utf-8')
    
    cliente_socket.send(empaquetar_2)
    
    if ava == 'close':
        break