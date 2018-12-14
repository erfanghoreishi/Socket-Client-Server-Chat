import json
import socket
import pickle
from _thread import *
from queue import Queue
import threading


class Client():

    def __init__(self):
        # self.address = port

        self.HOST = '127.0.0.1'
        self.PORT = 10000
        self.get_users()
        self.start_server()
        #self.connect(0)
        self.recieve_message()

    def get_users(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.HOST, self.PORT))
        self.port = self.s.getsockname()[1]
        clients_serialized = self.s.recv(2048)
        self.s.close()
        self.clients = pickle.loads(clients_serialized)
        print('users get:{}'.format(self.clients))

    def start_server(self):
        self.clients = []
        self.host = '127.0.0.1'
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.bind((self.host, self.port))
            print('server:{} '.format(self.s))
            self.s.listen(100)
            while True:
                self.client_socket, client_address = self.s.accept()
                client_port = self.client_socket.getpeername()
                print('user: {} is connected to you'.format(client_port))
                self.client_socket.close()

        except socket.error as e:
            print(str(e))

    def connect(self, user):
        user = self.clients[user]
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((str(user.get_host()), int(user.get_port())))

    def send_message(self, message):
        pass

    def recieve_message(self):
        pass


Client()
