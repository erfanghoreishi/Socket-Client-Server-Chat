class User():
    def __init__(self, port, host="127.0.0.1"):
        self.port = port
        self.host = host

    def get_port(self):
        return self.port

    def set_port(self, port):
        self.port = port

    def get_host(self):
        return self.host

    def set_host(self, host):
        self.host = host
