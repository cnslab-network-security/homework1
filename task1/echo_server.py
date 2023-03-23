import socket

IP = '0.0.0.0'
PORT = 9999
BUF_SIZE = 4096

#TODO: make a server-socket
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # To make the port nuber reusable
#TODO: bind the IP, port number to the server-socket
server.bind((IP, PORT))
#TODO: make the socket a listening state

client, addr = server.accept()
print(f"Connected from {addr}")

try:
    while True:
      response = client.recv(BUF_SIZE)
      if not response: break
      #TODO: send the response back to the client

      print(buf.decode())
except:
    client.close()
    server.close()

