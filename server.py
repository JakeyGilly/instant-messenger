import socket,_thread,threading


clients = []

def recv(clientsocket,addr):
    while True:
        msg = clientsocket.recv(1024)
        ah = msg.decode()
        epic = ah.split(",")
        if epic[0] == "Disconnect":
            clients.remove(clientsocket)
            print(f'[CONNECT] Disconnected  {addr}')
        else:
            print(f"[MESSAGE] Message received: {epic[0]} saying {epic[1]}")
        for i in range(len(clients)):
            client = clients[i]
            client.sendall(ah.encode())
    clientsocket.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = "127.0.0.1"
PORT = int(input("port? "))


print("           Thanks for choosing PyChat!")
print("                Server started!")
print("------------------------------------------------")
print(f"Listening for connections on {IP}:{PORT}...")

s.bind((IP, PORT))

while True:
    s.listen(5)
    c, addr = s.accept()
    _thread.start_new_thread(recv, (c, addr))
    print(f'[CONNECT] Accepted new connection from {addr}')
    clients.append(c)



s.close()
