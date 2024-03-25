#CSCE 3550 - Alex Trumble

#Submodule imports
from main import MyServer
from http.server import HTTPServer
from unittest.mock import patch

#Base module import
import unittest

class serverTest(unittest.TestCase):
    def start(self):
        #Start copy server on different port
        self.server = HTTPServer(('localhost', 8787), MyServer)

    def stop(self):
        #Ends copy server
        sef.server.server_close()

    def authTest(self, mock_log_message):
        #Mock auth query
        query = unittest.mock.Mock()
        query.path = "/auth"
        query.headers = {'Content-Length': '2'}
        query.rfile.read.return_value = b'{}'

        #Mock Server Response
        response = unittest.mock.Mock()

        #Call for do_POST from main.py
        self.server.RequestHandlerClass(query, ('localhost', 8787), self.server).do_POST()

        #Confirmation that the log was called for
        mock_log_message.assert_called_once_with(expected_argument)

    def expiredAuth(self, mock_log_message):
        query = unittest.mock.Mock()
        #Mock auth query using expired parameter
        query = unittest.mock.Mock()
        query.path = "/auth?expired=true"
        query.headers = {'Content-Length': '2'}
        query.rfile.read.return_value = b'{}'

        #Mock Server Response
        response = unittest.mock.Mock()

        #Call for do_POST from main.py
        self.server.RequestHandlerClass(query, ('localhost', 8787), self.server).do_POST()

        #Confirmation that the log was called for
        mock_log_message.assert_called_once_with(expected_argument)

if __name__ == '__name__':
    unittest.main()
