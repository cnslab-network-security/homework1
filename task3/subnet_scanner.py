import socket
import ipaddress
import struct
import sys
import time
import threading

# used for parsing an IP header
class IP:
    def __init__(self, buf=None):
        header = struct.unpack('<BBHHHBBH4s4s', buf)
        self.ver = header[0] >> 4
        self.ihl = header[0] & 0xF

        self.tos = header[1]
        self.len = header[2]
        self.id = header[3]
        self.offset = header[4]
        self.ttl = header[5]
        self.protocol_num = header[6]
        self.sum = header[7]
        self.src = header[8]
        self.dst = header[9]

        # human readable IP addresses
        self.src_address = ipaddress.ip_address(self.src)
        self.dst_address = ipaddress.ip_address(self.dst)

        # map protocol constants to their names
        self.protocol_map = {1: "ICMP", 6: "TCP", 17: "UDP"}
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except Exception as e:
            print('%s No protocol for %s' % (e, self.protocol_num))
            self.protocol = str(self.protocol_num)

# used for parsing an ICMP header
class ICMP:
    def __init__(self, buff):
        header = struct.unpack('<BBHHH', buff)
        self.type = header[0]
        self.code = header[1]
        self.sum = header[2]
        self.id = header[3]
        self.seq = header[4]

# sniffer: used to capture all ICMP packets come to this host.
def sniffer():
    socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    socket.bind(("0.0.0.0", 0))
    socket.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    discovered_hosts = set([])
    try:
        while True:
            raw_buffer = socket.recvfrom(1500)[0]

            #TODO: your code here

    except KeyboardInterrupt:
        print(f'\n\nSummary: Discovered Hosts')
        for host in sorted(discovered_hosts):
            print(f'{host}')
        sys.exit()

# udp_sender: used to send UDP packets to all the hosts of a given subnet.
def udp_sender(subnet):
    STRING="SCAN"
    PORT=19999
    #TODO: your code here

if __name__ == '__main__':
       subnet = sys.argv[1]
       time.sleep(3)

       # execute a udp sender thread
       t = threading.Thread(target=udp_sender, args=(subnet,))
       t.start()

       # start sniffing
       sniffer()
