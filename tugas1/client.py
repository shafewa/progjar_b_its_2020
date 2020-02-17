import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
print ('connecting')
sock.connect(server_address)

try:
    # Send data
    message = 'PEMROGRAMAN JARINGAN TEKNIK INFORMATIKA'
    print ("sending", message)
    sock.sendall(message.encode())
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(64)
        amount_received += len(data)
        print ("received", data.decode())
finally:
    print ('closing socket')
    sock.close()
