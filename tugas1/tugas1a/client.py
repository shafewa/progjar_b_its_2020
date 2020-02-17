import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
filename = "logo.png"
f = open(filename, "rb")
print ('connecting')
sock.connect(server_address)

try:
    # Send data
    message = f.read()
    print ("sending", message)
    sock.sendall(message)
finally:
    print ('closing socket')
    sock.close()