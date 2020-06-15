import socket,_thread,threading,datetime
now = datetime.datetime.now()


clients = []

def recv(clientsocket,addr):
    while True:
        now = datetime.datetime.now()
        msg = clientsocket.recv(1024)
        ah = msg.decode()
        epic = ah.split(",")
        if epic[0] == "Disconnect#000000":
            clients.remove(clientsocket)
            print(f'[{now.strftime("%Y-%m-%d %H:%M:%S")}][DISCONNECT] Disconnected  {addr}')
            with open('log.csv', mode='a') as log:
                log.writelines("\n" + str([{now.strftime("%Y-%m-%d %H:%M:%S")} ,"[DIS]", addr, "N/A", "N/A"]))
        elif epic[0] == "INFO#000000":
             ah = f"[SERVER]#000000,{epic[1]} has joined the chat!"
             with open('log.csv', mode='a') as log:
                log.writelines("\n" + str([{now.strftime("%Y-%m-%d %H:%M:%S")} ,"[CON]", addr, epic[1], "N/A"]))
        else:
            print(f'[{now.strftime("%Y-%m-%d %H:%M:%S")}][MESSAGE] Message received: {epic[0]} saying {epic[1]}')
        with open('log.csv', mode='a') as log:
            log.writelines("\n" + str([{now.strftime("%Y-%m-%d %H:%M:%S")} , "[MSG]" ,addr ,  epic[0], epic[1]]))
        for i in range(len(clients)):
            client = clients[i]
            try:
             client.sendall(ah.encode())
            except BrokenPipeError:
                clients.remove(clients[i])
                print(f'[{now.strftime("%Y-%m-%d %H:%M:%S")}][IDC] Illegal Disconnect (Check Log)')
                with open('log.csv', mode='a') as log:
                    log.writelines("\n" + str([{now.strftime("%Y-%m-%d %H:%M:%S")} ,"[IDC]", "N/A","N/A",client]))
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
    print(f'[{now.strftime("%Y-%m-%d %H:%M:%S")}][CONNECT] Accepted new connection from {addr}')

    clients.append(c)



s.close()
