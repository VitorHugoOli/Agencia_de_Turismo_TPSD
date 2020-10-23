import socket
import sys
import errno
import pickle


class EasySocketClient:
    HEADER_LENGTH = 10

    IP = "127.0.0.1"
    PORT = 1234

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((IP, PORT))

    client_socket.setblocking(False)

    def send(self, data):
        body = pickle.dumps(data)
        body_header = f"{len(body):<{self.HEADER_LENGTH}}".encode('utf-8')
        self.client_socket.send(body_header + body)

        while True:
            try:
                message_header = self.client_socket.recv(self.HEADER_LENGTH)
                message_length = int(message_header.decode('utf-8').strip())
                mens = pickle.loads(self.client_socket.recv(message_length))
                yield mens

            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print('Reading error: {}'.format(str(e)))
                    sys.exit()

            except Exception as e:
                print('Reading error: '.format(str(e)))
                sys.exit()


client = EasySocketClient()
message = input(f'Client > ')
for i in client.send(message):
    print(i)
    break
