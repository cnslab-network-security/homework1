import socket

IP = '0.0.0.0'
PORT = 9999
BUF_SIZE = 4096

#TODO: make a server-socket
# IPv4 주소 체계의 TCP 소켓을 생성
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# socket 옵션을 사용하여 주소 재사용을 허용
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#TODO: bind the IP, port number to the server-socket
server.bind((IP, PORT))

#TODO: make the socket a listening state
server.listen(5) # 인자는 대기 중인 연결의 최대 개수를 지정

client, addr = server.accept()
print(f"Connected from {addr}")

try:
    while True:
      response = client.recv(BUF_SIZE)
      if not response: break

      #TODO: send the response back to the client
      client.sendall(response)
      print(response.decode())
except:
    client.close()
    server.close()

