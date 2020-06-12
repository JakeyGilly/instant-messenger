import threading
import socket
import time as t

name = input("Please enter your name: ")
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((input("IP of server? (eg: 127.0.0.1)"), int(input("Port of server? (eg: 1111)"))))
clientsocket.setblocking(True)
print("     		      PyChat 0.1")
print("                Connected to Server!")
print(f"			Type /exit to disconnect!")
print("------------------------------------------------")

def get_input():
		while True:
			msg = clientsocket.recv(1024)
			ah = msg.decode()
			epic = ah.split(",")
			if epic[0] != name:
				print(f"\n{epic[0]}) {epic[1]}")


input_thread = threading.Thread(target=get_input)
input_thread.start()

# Run your game now
while True:
	message = input(f"")
	toSend = name + "," + message
	if message == "/exit":
		toSend = f"Disconnect,{name} Has disconnected!"
	clientsocket.send(toSend.encode())