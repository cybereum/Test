# Client
import socket
import json
import urllib.request as request

HOST = '192.168.1.89'
PORT = 63755


class Ui_ClientWindow():

    def json_message(self, direction):
        data = {
            'sender': socket.gethostbyname(socket.gethostname()),
            'instruction': direction,
        }
        with request.urlopen(
            'http://blockchainforprojects.com/wp-content/uploads/2019/12/use2.txt'
        ) as f:
            datastore = json.loads(f.read())

        json_data = json.dumps(datastore, sort_keys=False, indent=2)
        print("data %s" % json_data)
        self.send_message(json_data + ";")
        return json_data

    def send_message(self, data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(data.encode())
            response = s.recv(1024)
        print('Received', repr(response))
        return response
