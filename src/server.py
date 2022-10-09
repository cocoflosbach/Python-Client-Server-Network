"""A simple Python server using the socket and threading modules"""

import socket
import threading
import pickle
#import json

HEADER = 64
PORT = 5050

#Get the IP address on which the server will run using socket package
SERVER = socket.gethostbyname(socket.gethostname())

ADDR = (SERVER, PORT)

#Define the encode/decode format for message recived from client
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    """A function to handle individual client connections to the server"""
    print(f"[NEW CONNECTION] {addr} connected.")

    #The dunction checks for a connection.
    connected = True
    while connected:
        try:
            msg = conn.recv(32768)
            unpickled_msg = pickle.loads(msg)
            print(f"[{addr}] {unpickled_msg}")
        #To disconnect a client from the server, set msg to disconnected message
            if msg == DISCONNECT_MESSAGE:
                connected = False
            conn.send("Msg received".encode(FORMAT))
        except IOError:
            print("Error: Can't find or read file/data")

    #Close a connection between a client and server.
    conn.close()

def start_listening():
    """A function for the server to start listening for client connections"""
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    #This starts an infinite loop that allows the server to pick up new
    #connection requests
    while True:
        conn, addr = server.accept()

        #This starts individual threads for each successful client connection.
        #This thread calls the handle client funtion and takes the client's connection,
        #IP address and Port as arguments.
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start_listening()
