import socket
import sys

def port_scanner(target_ip, start_portno, end_portno):

    for port_number in range(start_portno, end_portno):
        socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.settimeout(0.05)

        try:
            #TODO: your code here
        except ConnectionRefusedError:
            continue
        except TimeoutError:
            continue

if __name__ == '__main__':
        
       target_ip = sys.argv[1]
       start_portno = int(sys.argv[2])
       end_portno = int(sys.argv[3])

       port_scanner(target_ip, start_portno, end_portno)
