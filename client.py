"""A simple Python client program that connects to and sends data to a server"""

import socket
import pickle


HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def dict_data():
    """A Function to populate a dictionary from elements in two lists"""
    dicts = {}
    name = ["Andre", "Maya", "Noah", "Georgia", "Bianca", "Adele"]
    age = ["12", "14", "12", "13", "14", "13"]
    keys = range(len(name))

    for i in keys:
        dicts[name[i]]= age[i]
        return dicts
    print(dicts)
    # pickled_dict = pickle.dumps(dicts)   

def send(msg):
    """A function to send pickled data to a server"""
    #file = open("df.p", "wb")
    message = pickle.dumps(msg)

    #message = msg.encode(FORMAT)
    #msg_length = len(message)
    #send_length = struct.pack("!Q", msg_length)
    # send_length = str(msg_length).encode(FORMAT)
    # send_length += b" " * (HEADER - len(send_length))
    #client.send(send_length)
    client.send(message)
    print(f"This is a picked dictionary \n {message}")

    print(client.recv(2048).decode(FORMAT))



send("Hello World")
send("My name is Coco")
send("I am a software engineer")
send(dict_data())

send(DISCONNECT_MESSAGE)
