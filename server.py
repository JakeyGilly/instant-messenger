import socket,_thread,threading


clients = []

def recv(clientsocket,addr):
    while True:
        msg = clientsocket.recv(1024)
        ah = msg.decode()
        epic = ah.split(",")
        if epic[0] == "Disconnect#000000":
            clients.remove(clientsocket)
            print(f'[DISCONNECT] Disconnected  {addr}')
        elif epic[0] == "INFO#000000":
             ah = f"[SERVER]#000000,{epic[1]} has joined the chat!"
        else:
            print(f"[MESSAGE] Message received: {epic[0]} saying {epic[1]}")
        for i in range(len(clients)):
            client = clients[i]
            try:
             client.sendall(ah.encode())
            except BrokenPipeError:
                clients.remove(clients[i])
                break

    clientsocket.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
IP = socket.gethostbyname(host_name)
ipcorrect = input(f"Is your private IP: {IP}? [Y/N]")
answered = False

while not answered:
    if ipcorrect.lower() == "y":
        IP = IP
        answered = True
    elif ipcorrect.lower() == "n":
        IP = input("What is your private IP")
        answered = True
    else:
        print("Please enter Y/N")


PORT = int(input("port? "))


print("           Thanks for choosing PyChat!")
print("              PyChat Server V0.1.1")
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
