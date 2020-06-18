import npyscreen
import socket
import random as r
import threading
import time as t

global lastrefresh
global temp
global messages

messages = ["Welcome to PyChat for Terminal", "Type /exit to quit",""]
lastrefresh = ["Welcome to PyChat for Terminal", "Type /exit to quit",""]

name = input("Please enter your name: ")
name = name + "#" + str(r.randint(100000,999999))
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((input("IP of server? (eg: 127.0.0.1)"), int(input("Port of server? (eg: 1111)"))))
clientsocket.setblocking(True)
clientsocket.send(f"INFO#000000,{name}".encode())



class MessageBox(npyscreen.BoxTitle):
    _contained_widget = npyscreen.Textfield

def getMessages():
    msg = clientsocket.recv(1024)
    ah = msg.decode()
    epic = ah.split(",")
    messages.append(f"\n{epic[0][:-7]}) {epic[1]}")
    disploy = [f"\n{epic[0][:-7]}) {epic[1]}"]
    myDisplay.buffer(lines=disploy, scroll_end=True)


class MainForm(npyscreen.Form):
    def create(self):
        global myDisplay
        self.keypress_timeout = 1
        myDisplay = self.add(npyscreen.TitleBufferPager, name='Messages', height=20, max_height=30, autowrap=True,maxlen=30, footer="Connected to 127.0.0.1")
        myDisplay.buffer(lines=messages, scroll_end=True)
        self.myTextBox = self.add(MessageBox, name='Enter a message', max_height=5)
        #print(messages)

    def while_waiting(self):
        input_thread = threading.Thread(target=getMessages)
        input_thread.start()



#def getMesseges():
 #       msg = clientsocket.recv(1024)
  #      ah = msg.decode()
   #     epic = ah.split(",")
    #    if epic[0] != name:
     #       messages.append(f"\n{epic[0][:-7]}) {epic[1]}")


def GetInput(none):
    F = MainForm(name="PyChat for Terminal v0.2.1")
    F.edit()
    epic = F.myTextBox.value
    return epic

if __name__ == '__main__':
    while True:
        toSendRaw = npyscreen.wrapper_basic(GetInput)
        toSend = name + "," + toSendRaw
        if toSendRaw == "/exit":
            toSend = f"Disconnect#000000,{name} Has disconnected!"
            clientsocket.send(toSend.encode())
            clientsocket.close()
        clientsocket.send(toSend.encode())


