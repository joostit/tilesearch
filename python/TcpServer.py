import socket
import sys
from threading import Thread
import time
import traceback


class TcpServer:

    def __init__(self):
        self.listener_thread = Thread
        self.clients = []
        self.run = True
        self.serverport = 10000
        self.server_address = ('', 10000)

    def start(self):
        self.run = True
        self.listener_thread = Thread(target=self.__listener_thread_method)
        self.listener_thread.daemon = True
        self.listener_thread.start()

    def stop(self):
        print("Closing server socket")
        self.run = False
        self.listener.close()

        for client in self.clients:
            client.close()
        self.clients.clear()

    def send(self, data):
        client: socket
        toRemove = []
        for client in self.clients:
            try:
                client.sendall(data.encode())
            except:
                toRemove.append(client)

        for clientToRemove in toRemove:
            print("Removing client after send error: ", clientToRemove.getpeername())
            self.clients.remove(clientToRemove)

    def __listener_thread_method(self):
        while self.run:
            try:
                self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                host = socket.gethostname()
                self.listener.bind(('', self.serverport))
                self.listener.listen(1)
                print("Started listening om port ", self.serverport)
                connection, client_address = self.listener.accept()
                self.clients.append(connection)
                print("Client connected from: ", client_address)

            except OSError as exc:
                if self.run:
                    print("Exception while listening to socket: ", exc)
                    traceback.print_exc()

            time.sleep(1)
