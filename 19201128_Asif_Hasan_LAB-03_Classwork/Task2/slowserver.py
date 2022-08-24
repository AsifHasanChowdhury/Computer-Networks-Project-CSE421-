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
                count=0
                print(msg)
                for char in msg:
                    if (char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
                        count=count+1
                    if(char=='A' or char=='E' or char=='I' or char=='O' or char=='U'):
                        count=count+1
               # print(count)
                if (count>2):
                    conn.send('Too many vowels \n'.encode(format))
                    count=0
                elif(count==0 or count==1):
                    conn.send('Not enough vowels \n'.encode(format))
                    count=0
                elif(count==2):
                    conn.send('Enough vowels I guess \n'.encode(format))
                    count=0
                time.sleep(2)
                #conn.send('Message is delivered'.encode(format))

    conn.close()
