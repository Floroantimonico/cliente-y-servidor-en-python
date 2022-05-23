import socket
import sys
import time 

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hosts = sys.argv[1]
puerto = sys.argv[2]

servidor_socket.bind((hosts, int(puerto)))

servidor_socket.listen(2)

mensaje, ip = servidor_socket.accept()


mensaje.send(b'QVFVSSBERUJFUyBERSBQT05FUiBVTiBNRU5TQUpFIERFIEJJRU5CRU5JREEgUEFSQSBFTCBTRVJWSURPUg==')
def mensaje_recividos():
    hora_1 = time.gmtime()
    while True:
        desempaquetar = mensaje.recv(4000).decode('utf8')
        mensaje_recividos_1 = [f"mensaje de [{ls[0]}] -> -({desempaquetar})- ({time.strftime('%x %I')}:{hora_1.tm_min} {time.strftime('%p')}) ip {ip}"]
        
        if desempaquetar == 'close':
            break
        
        with open('registro_de_usuarios_y_mensajes.txt', 'a') as agregar:
            for b in mensaje_recividos_1:
                agregar.write(b + str('\n'))
        
        
        print(mensaje_recividos_1)
        
datos = mensaje.recv(4000).decode("utf8")
    
ls = []
ls.append(datos)
    
with open("texto.txt", 'r') as r:
    leer = r.readlines()
        
    if f"{datos}\n" in leer:
        wolcom = f"bienbenido de nuevo [*]{ls[0]}"
        
        gallina = time.gmtime()
        
        registro = [f"usuario logeado {datos} ({time.strftime('%x %I')}:{gallina.tm_min} {time.strftime('%p')}) ip = [{ip}]"]
            
        print(registro)
            
        empaquetar = wolcom.encode(encoding='utf-8')
            
        mensaje.send(empaquetar)
        
        mensaje_recividos()
        
    if  not f"{datos}\n" in leer:
        with open("texto.txt", 'a') as a:
            for b in ls:
                a.write(b + '\n')
                
                hora = time.gmtime()
                
                en = str(ls[0])
                
                on = [f"usuario creado <{en}> ({time.strftime('%x %I')}:{hora.tm_min} {time.strftime('%p')}) ip {ip}"]
                
                print(on)
                
                txt = f"te has registrado satisfactoriamente con el usuario <{ls[0]}>"
                
                empaquetar_1 = txt.encode(encoding='utf-8')
                
                mensaje.send(empaquetar_1)
                
                mensaje_recividos()
    
    
