import socketserver
from config.utils import decrypt

class ConnectionHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print('{} wrote:'.format(self.client_address[0]))
        print(decrypt(self.data))

def listen():
    HOST, PORT = "localhost", 9999
    server = socketserver.TCPServer((HOST, PORT), ConnectionHandler)
    print('Bonandos:/# Waiting for data...')
    server.serve_forever()    

if __name__ == '__main__':
    print('You should not run this file! Run App.py instead.')    