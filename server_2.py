import pickle
import select
import socket


class EasySocketServer:
    HEADER_LENGTH = 10

    IP = "127.0.0.1"
    PORT = 1234
    SERVER_SOCKET = None
    sockets_list = []
    clients = {}

    def __init__(self):
        self.SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.SERVER_SOCKET.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.SERVER_SOCKET.bind((self.IP, self.PORT))

        self.SERVER_SOCKET.listen()

        self.sockets_list = [self.SERVER_SOCKET]

    print(f'Listening for connections on {IP}:{PORT}...')

    def receive_message(self, client_socket):
        try:

            message_header = client_socket.recv(self.HEADER_LENGTH)

            if not len(message_header):
                return False

            message_length = int(message_header.decode('utf-8').strip())

            return {'header': message_header, 'data': pickle.loads(client_socket.recv(message_length))}

        except:
            return False

    def listen(self):
        while True:
            read_sockets, _, exception_sockets = select.select(self.sockets_list, [], self.sockets_list)

            for notified_socket in read_sockets:

                if notified_socket == self.SERVER_SOCKET:

                    client_socket, client_address = self.SERVER_SOCKET.accept()

                    user = self.receive_message(client_socket)

                    if user is False:
                        continue

                    self.sockets_list.append(client_socket)

                    self.clients[client_socket] = client_address

                    yield user['data'], client_socket

                    print('Accepted new connection from {}:{}'.format(*client_address))

                else:

                    message = self.receive_message(notified_socket)

                    if message is False:
                        print(
                            'Closed connection from: {}:{}'.format(*self.clients[notified_socket]))

                        self.sockets_list.remove(notified_socket)

                        del self.clients[notified_socket]

                        continue

                    user = self.clients[notified_socket]

                    yield message['data'], notified_socket

                    print('Received message from {}:{}'.format(*user))

            for notified_socket in exception_sockets:
                self.sockets_list.remove(notified_socket)

                del self.clients[notified_socket]

    def send(self, client_socket: socket, mensg):
        message = pickle.dumps(mensg)
        message_header = f"{len(message):<{self.HEADER_LENGTH}}".encode('utf-8')
        client_socket.send(message_header + message)


sock = EasySocketServer()
for data, clint_socket in sock.listen():
    print(data)
    sock.send(clint_socket, {'vitor': "Buenas"})
