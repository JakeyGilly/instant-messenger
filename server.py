import socket,_thread

def recv(clientsocket,addr):
    while True:
        msg = clientsocket.recv(1024)
        print(msg.decode())
    clientsocket.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP = ""
PORT = 1234

print("                Server started!")
print("------------------------------------------------")
print(f"Listening for connections on {IP}:{PORT}...")

s.bind((IP, PORT))

while True:
    s.listen(5)
    c, addr = s.accept()
    _thread.start_new_thread(recv, (c, addr))
    print(f'Accepted new connection from {addr}')



s.close()
