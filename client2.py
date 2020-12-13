#Client:
import socket
import json
import urllib
from urllib.request import urlopen
import urllib.request as request

class Ui_ClientWindow():

    #Get IP Address
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    print("Your Computer Name is:" + hostname)
    print("Your Computer IP Address is:" + IPAddr)

    HOST = '192.168.1.89'  # The server's hostname or IP address
    #PORT = 8192         # The port used by the server
    PORT = 63755         # The port used by the server


    def json_message(direction):
        local_ip = socket.gethostbyname(socket.gethostname())
        data = {
            'sender': local_ip,
            'instruction': direction
        }
        with request.urlopen('http://blockchainforprojects.com/wp-content/uploads/2019/12/use2.txt') as filename2:
        #with request.urlopen('http://blockchainforprojects.com/wp-content/uploads/2018/11/106.txt') as filename2:
            source = filename2.read()
            datastore = json.loads(source)

        #filename2 = urlopen('http://blockchainforprojects.com/wp-content/uploads/2019/12/use.txt')

        #response = json.loads(requests.get("http://blockchainforprojects.com/wp-content/uploads/2019/12/use.txt").text)


     
        #filename = 'ProBloCh1.json'
        #with open(filename, 'r') as f:
            #datastore = json.load(f)

        json_data = json.dumps(datastore, sort_keys=False, indent=2)
        #json_data = json.dumps(data, sort_keys=False, indent=2)
        print("data %s" % json_data)

        send_message(json_data + ";")

        return json_data



    def send_message(data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(data.encode())
            data = s.recv(1024)

        print('Received', repr(data))

    json_message("SOME_DIRECTION")
