import socket
import user
import json
import pickle


class Server():
    def __init__(self):

        self.clients = []
        self.host = '127.0.0.1'
        self.port = 10000
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.bind((self.host, self.port))
            print('host clients:{} '.format(self.s))
            self.s.listen(100)
            while True:
                self.client_socket, client_address = self.s.accept()
                client_port = self.client_socket.getpeername()
                print('port: {} is connected'.format(client_port))
                self.add_user(client_port)
                self.send_users()
                self.client_socket.close()

        except socket.error as e:
            print(str(e))

    def add_user(self, client_port):
        print('add user')
        client = user.User(port=client_port)
        self.clients.append(client)

    def send_users(self):
        self.serialized_clients = pickle.dumps(self.clients)
        print('users sent: {}'.format(self.clients))
        self.client_socket.send(self.serialized_clients)
        self.client_socket.close()


Server()
