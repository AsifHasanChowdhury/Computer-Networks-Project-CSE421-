import socket
header=16
port=5050
server=socket.gethostbyname(socket.gethostname())
Addr=(server,port)
format='utf-8'
disconnect_message='end'

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(Addr)


def send(msg):
    message=msg.encode(format)
    msg_length=len(message)
    send_length=str(msg_length).encode(format)
    send_length+=b' '*(header-len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(format))


send(f"Client IP Address is {server} Client device name is {socket.gethostname()}")
send(disconnect_message)