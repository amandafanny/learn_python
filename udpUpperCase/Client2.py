import socket

MAX_SIZE_BYTES = 65535 # Mazimum size of a UDP datagram

def client(port):
  host = '127.0.0.1'
  s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  s.connect((host, port))
  message = input('Input lowercase sentence:' )
  data = message.encode('ascii')
  s.send(data)
  print('The OS assigned the address {} to me'.format(s.getsockname()))
  data = s.recv(MAX_SIZE_BYTES) 
  text = data.decode('ascii')
  print('The server replied with {!r}'.format(text))