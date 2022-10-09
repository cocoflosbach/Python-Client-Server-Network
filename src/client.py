"""A simple Python client program that connects to and sends data to a server"""

import socket
import pickle
#import json


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


def text_file():
    """A Function to create a txt file to be sent to the server"""
    txt_file = open("encoded_text.txt", "wb")
    txt_file.close()
    return txt_file

def send(msg):
    """A function to send pickled data to a server"""
    try:
        # file = open("encoded_dict.json", "wb")
        try:
            #  # message = json.dump(msg, file)
            message = pickle.dumps(msg)
            client.sendall(message)
        finally:
            #file = open("encoded_dict.txt", "wb")
            print(f"This is a picked dictionary \n {message}")
            print(client.recv(2048).decode(FORMAT))
    except EOFError:
        print("[CONNECTION ERROR] A connection to the server could not be made")



# send("Hello World")
# send("My name is Coco")
# send("I am a software engineer")
send(dict_data())

#send(DISCONNECT_MESSAGE)
