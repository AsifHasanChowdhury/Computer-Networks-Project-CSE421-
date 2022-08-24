import socket
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
            else:
                print(msg)
                conn.send('Message is delivered'.encode(format))

    conn.close()