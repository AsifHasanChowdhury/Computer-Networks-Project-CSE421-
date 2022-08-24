import socket
import time
header= 16
port= 5050
server= socket.gethostbyname(socket.gethostname())
Addr= (server,port)
format='utf-8'
disconnect_message='end'
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(Addr)
server.listen()
print(f'{"Server is Running"}')
print(f'{"Hello"}{23}')

while True:
    conn, addr = server.accept()
    connected=True
    while connected:
        msg_length=conn.recv(header).decode(format)
        if msg_length:
            msg_length=int(msg_length)
            msg=conn.recv(msg_length).decode(format)
            if msg==disconnect_message:
                connected=False
                conn.send('tata'.encode(format))
                break
            else:
                hours=int(msg)
                salary=0
                print(f'{"Client hour Count"}')
                if(hours==0):
                    salary=0
                    salaryResponse='Hello! You Worked '+ str(salary)+' Hours No Work No Payment\n'
                    conn.send(salaryResponse.encode(format))
            
                elif(hours<=40):
                    salary=int(hours)*200
                    salaryResponse='Hello! You worked '+ str(hours) +' Hours that is less than 40 Hours. Salry is '+str(salary)+'\n'                    
                    conn.send(salaryResponse.encode(format))                
                
                elif(hours>40):
                    salary=int(hours)*300
                    salary=salary+8000
                    salaryResponse='Hello! You worked '+ str(hours) +' Hours that is More than 40 Hours. Salry is '+str(salary)+'\n'          
                    conn.send(salaryResponse.encode(format))    

                
                
                #conn.send('Message is delivered'.encode(format))

    conn.close()
