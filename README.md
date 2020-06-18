# PyChat (instant-messenger)
This is a instant messenger built in python by me and one of my friends. It runs in Python 3 either in the terminal, or in a GUI. You need a computer to run the server script, and people who want to join use the client script.
![Recordit GIF](http://g.recordit.co/JZGWUH97aT.gif)

## Getting Started (server.py)
How to get started with the server.
### Installing
First, you need to clone the repo:

```git clone https://github.com/JakeyGilly/instant-messenger```

Then, run the server script

```cd instant-messenger/```

```python3 server.py```
### Setup

When you start up the server script, it will try to guess your private IP.
 
 ```Is your private IP: XXX.X.X.X? [Y/N]```

If it says anything other than your private IP, then type 'N' and then put in your private IP.

Next, it will ask you for a port: 

```port? ```

We recommend a port of 1024 or greater, as this will have the least likeliness to interfere with any other programs.

Then, you will get the message:
````  
              PyChat Server V0.X.X
                Server started!
------------------------------------------------
Listening for connections on XXX.XXX.X.XXX:1111...
````
This means the server is now active.
If you want people to be able to connect from outside your network, you will need to port forward the port.

## Getting Started (clientGUI.py)
How to get started with the GUI based client.
### Installing
First, you need to clone the repo:

```git clone https://github.com/JakeyGilly/instant-messenger```

Then, run the script:

```cd instant-messenger/```

```python3 clientGUI.py```
### Setup
When setting up, you will see a a screen like this:

![Recordit GIF](http://g.recordit.co/Do4IaTjYym.gif)

This lets you type your name in to connect as. You will then be greeted with a screen to enter the IP and Port to connect to, like this:

![Recordit GIF](http://g.recordit.co/lEWIht5Hrl.gif)

After this, it will connect you to the server.

##Getting Started (clientTerminal.py)
How to get started with the GUI based client.

### Prerequisites
First, you need to install the package "npyscreen" for it to work:

```pip3 install npyscreen```
### Installing
Clone the repo:

```git clone https://github.com/JakeyGilly/instant-messenger```

Then, run the script:

```cd instant-messenger/```

```python3 clientTerminal.py```

### Setup
It will ask you for your name (What you want to connect as) , an IP address to connect to and the port on the IP. Then it will connect you in.
![Recordit GIF](http://g.recordit.co/JZGWUH97aT.gif)

There is also a basic terminal version (clientBasic.py) instead if you don't want to use any plugins

## Authors

- Jake Gillman - _Initial Idea, Basic Terminal and GUI client_ - [JakeyGilly](https://github.com/JakeyGilly/)
- Finn O'Neill - _Server, Basic Terminal and Terminal Client_ - [Explorer017](https://github.com/Explorer017/)

