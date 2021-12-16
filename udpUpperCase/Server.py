#coding=utf-8
import socket

MAX_SIZE_BYTES = 65535 # Mazimum size of a UDP datagram

# socket.socket(family, type, proto, fileno)

# AF_INET ipv4
# AF_INET6 ipv6
# AF_UNIX 在符合 POSIX 的系统上可用,本机通信

# SOCK_DGRAM UDP
# SOCK_STREAM TCP

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

port = 3000
hostname = '127.0.0.1'
s.bind((hostname, port))

print('Listening at {}'.format(s.getsockname()))

while True:
    # The code to handle clients will go here
    data, clientAddress = s.recvfrom(MAX_SIZE_BYTES)
    # decode the message from the byte stream to ASCII
    message = data.decode('ascii')
    upperCaseMessage = message.upper()
    print('The client at {} says {!r}'.format(clientAddress, message))
    # encode the capitalized ASCII message to bytes 
    data = upperCaseMessage.encode('ascii')
    s.sendto(data, clientAddress)  
