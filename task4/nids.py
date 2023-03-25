# Skeleton code for NIDS
import socket
import sys
import ipaddress
from scapy.all import *
from datetime import datetime

protocol_dict = {1:'icmp', 6:'tcp', 17: 'udp'}
option_dict = {'tcp': ['seq', 'ack', 'window', 'flags'],
               'ip': ['id', 'tos', 'ttl'],
               'icmp': ['itype', 'icode']}

# You can utilize this class to parse the Snort rule and build a rule set.
class Rule:
    def __init__(self, action, protocol, src_ip, src_port, direction, dst_ip, dst_port, options, msg, original_rule):
        self.action = action
        self.protocol = protocol
        self.src_ip = src_ip
        self.src_port = src_port
        self.direction = direction
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.options = options
        self.msg = msg

        self.original_rule = original_rule

    def __str__(self):
        return (f"action: {self.action}\n"
                 f"protocol: {self.protocol}\n"
                 f"src_ip: {self.src_ip}\n"
                 f"src_port: {self.src_port}\n"
                 f"direction: {self.direction}\n"
                 f"dst_ip: {self.dst_ip}\n"
                 f"dst_port: {self.dst_port}\n"
                 f"options: {self.options}")

def parse_rule(line):
    #TODO: your code here
    pass

def parse_packet(packet, rule_set):
    #TODO: your code here
    pass

    # example codes:
    # ether = packet[Ether]
    # ip = packet[IP]
    # tcp = packet[TCP]
    # ip.show()
    # tcp.summary()

if __name__ == '__main__':
    rule_file = sys.argv[1] 

    f = open(rule_file, 'r')

    rule_set = []
    lines = f.readlines()
    for line in lines:
        rule = parse_rule(line)
        rule_set.append(rule)

    print("Start sniffing")
    sniff(iface='eth0', prn=lambda p: parse_packet(p, rule_set), filter='ip')

    f.close()

