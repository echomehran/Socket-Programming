import socket


HEADER = 64
PORT = 5050
SERVER = ""
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT!"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send_msg(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    
    print(client.recv(2048).decode(FORMAT))


messages = [
    "Hello World!",
    "Socket programming is cool",
    "Python is great",
    "Networking is fun",
    "Linux is the best"
]

# [send_msg(msg) for msg in messages]
send_msg(input("Enter something to send a message: "))
send_msg(DISCONNECT_MESSAGE)
