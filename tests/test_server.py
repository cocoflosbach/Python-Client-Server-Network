"""Perform Unit Testing for server program connecting to the server"""

import unittest
import socket
import threading

import sys
sys.path.append("..")

from src.server import handle_client
from src.server import  start_listening


class TestServer(unittest.TestCase):
    """Test Class for server starting and listening for connection"""

    def server_start_listening(self):
        """This function starts the server"""

        #Create a test server connection using socket
        test_server = server.start_listening("192.168.1.35", 8080)
        thread = threading.Thread(target=test_server.start_listening)
        thread.start()
        thread.join()

    def connect_fake_client(self):
        """This function creates a test client to connect to server"""

        #create fake client to connect to server initialised above
        fake_client = socket.socket()
        thread = threading.Thread(target=server.handle_client)
        fake_client.connect(("192.168.1.35", 8080))
        fake_client.close()

        
if __name__ == '__main__':
    # Run the testing script
    unittest.main()
