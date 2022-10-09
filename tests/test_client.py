"""Perform Unit Testing for client program connecting to the server"""

import unittest
import socket
import threading


class TestClient(unittest.TestCase):
    """Test Class for client conneection to server"""

    def start_fake_server(self):
        """This function creates and starts a fake server for the test case"""
        server = socket.socket()
        server.bind(("192.168.1.35", 8080))
        server.listen(0)
        server.accept()
        server.close()

    def test_client_connection(self):
        """This function tests the client connection to the fake server"""
        thread = threading.Thread(target=self.start_fake_server)
        thread.start()

        client = socket.socket()
        client.connect(("192.168.1.35", 8080))
        client.close()

        thread.join()


if __name__ == '__main__':
    # Run the testing script
    unittest.main()
