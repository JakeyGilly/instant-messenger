import socket
name = input("Please enter your name: ")
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(("", 1234))
while 1:
    message = input("> ")
    clientsocket.send(name.encode() + ": ".encode() + message.encode())
clientsocket.close()
