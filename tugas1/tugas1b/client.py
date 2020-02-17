import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
namafile = input("Nama file : ")
namafile = namafile.strip("\n")
print ('connecting')
sock.connect(server_address)

try:
    # Send data
    pesan = namafile
    print ("sending", pesan)
    print("nama filenya", pesan)
    sock.sendall(pesan.encode())
    # Look for the response
    while 1:
        data = sock.recv(1024)
        pesanakhir = open("finale" + pesan, 'a+b')
        if not data:
            pesanakhir.close()
            break
        pesanakhir.write(data)
finally:
    print ('closing socket')
    sock.close()