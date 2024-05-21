import socket
import sys

def port_scanner(target_ip, start_portno, end_portno):

    for port_number in range(start_portno, end_portno):
        #TODO: your code here
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # 타임아웃을 설정하여 연결 시도를 제한

        try:
            #TODO: your code here
            # 대상 IP 주소와 포트 번호로 연결을 시도
            sock.connect((target_ip, port_number))
            print(port_number)

        except ConnectionRefusedError:
            continue
        except TimeoutError:
            continue

if __name__ == '__main__':
        
       target_ip = sys.argv[1]
       start_portno = int(sys.argv[2])
       end_portno = int(sys.argv[3])

       port_scanner(target_ip, start_portno, end_portno)
