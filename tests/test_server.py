
import unittest
import socket
import threading
import time

import sys
sys.path.append("..")

from src.server import handle_client
from src.server import  start_listening


class TestServer(unittest.TestCase):
    test_server = socket.socket()
    thread = threading.Thread(target=server.start_listening)
    thread.start()

    time.sleep(0.000001)

    fake_client = socket.socket()
    fake_client.settimeout(1)
    fake_client.connect((socket.gethostbyname(socket.gethostname), 8080))
    fake_client.close()

    thread.join()

        
if __name__ == '__main__':
    # Run the testing script
    unittest.main()
