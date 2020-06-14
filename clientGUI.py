import socket, tkinter as tk, threading, random as r


def getNameData(event=None):
    global name
    name = ename.get()
    name = name + "#" + str(r.randint(100000, 999999))
    root.destroy()


def recv():
    while 1:
        msg = clientsocket.recv(1024)
        ah = msg.decode()
        epic = ah.split(",")
        if epic[0] != name:
            tk.Label(framea, text=f"{epic[0][:-7]} : {epic[1]}").pack()


def send(event=None):
    if ent.get() != "":
        msg = ent.get()
        tk.Label(framea, text=f"{name[:-7]} : {msg}").pack()
        ent.delete(0, 'end')
        if msg == "quit":
            clientsocket.send(f"Disconnect#000000,{name} Has disconnected!".encode())
            clientsocket.close()
            root2.destroy()
        clientsocket.send(f"{name},{msg}".encode())


clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(("127.0.0.1", 1111))
root = tk.Tk()
tk.Label(root, text="Name: ").pack()
root.bind('<Return>', getNameData)
ename = tk.Entry(root)
ename.pack()

tk.Button(root, text="Next", command=getNameData).pack()
root.mainloop()

root2 = tk.Tk()
root2.geometry("300x1000")
root2.bind('<Return>', send)
framea = tk.Frame(root2).pack()
ent = tk.Entry(root2)
tk.Label(root2, text="If you want to quit, Just say \"quit\"").pack(side="bottom")
but = tk.Button(root2, text="Send message", command=send).pack(side="bottom")
ent.pack(side="bottom")
threading.Thread(target=recv).start()
root2.mainloop()
