import socketserver

class ConnectionHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print('{} wrote:'.format(self.client_address[0]))
        print(self.data)

def run():
    HOST, PORT = "localhost", 9999
    server = socketserver.TCPServer((HOST, PORT), ConnectionHandler)
    print('Server is running on port {}'.format(PORT))
    server.serve_forever()    

if __name__ == '__main__':
    print('You should not run this file! Run App.py instead.')    