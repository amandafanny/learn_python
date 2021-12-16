import argparse, socket

MAX_SIZE_BYTES = 65535 # Mazimum size of a UDP datagram

def server(port):
    hostname = '127.0.0.1'
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((hostname, port))
    print('Listening at {}'.format(s.getsockname()))
    while True:
        data, clientAddress = s.recvfrom(MAX_SIZE_BYTES)
        message = data.decode('ascii')
        print('The client at {} says {!r}'.format(clientAddress, message))
        msg_to_send = input('Input message to send to client:' )
        data = msg_to_send.encode('ascii')
        s.sendto(data, clientAddress)

def client(port):
    host = '127.0.0.1'
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        s.connect((host, port))
        message = input('Input message to send to server:' )
        data = message.encode('ascii')
        s.send(data)
        print('The OS assigned the address {} to me'.format(s.getsockname()))
        data = s.recv(MAX_SIZE_BYTES) 
        text = data.decode('ascii')
        print('The server replied with {!r}'.format(text))

if __name__ == '__main__':
    funcs = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='UDP client and server')
    parser.add_argument('functions', choices=funcs, help='client or server')
    parser.add_argument('-p', metavar='PORT', type=int, default=3000,
                        help='UDP port (default 3000)')
    args = parser.parse_args()
    function = funcs[args.functions]
    function(args.p)