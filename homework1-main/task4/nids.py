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

    rules = line.split()
    action = rules[0]
    protocol = rules[1]
    src_ip = rules[2]
    src_port = rules[3]
    direction = rules[4]
    dst_ip = rules[5]
    dst_port = rules[6]
    options = {}

    for rule in rules[7:]:
        if ':' in rule:
            key, value = rule.split(':')
            options[key] = value

    msg_start_index = line.find('msg:"') + len('msg:"')
    msg_end_index = line.find('";', msg_start_index)
    msg = line[msg_start_index:msg_end_index]

    return Rule(action, protocol, src_ip, src_port, direction, dst_ip, dst_port, options, msg, line)


def parse_packet(packet, rule_set):
    #TODO: your code here

    if Ether in packet:
        ether = packet[Ether]

        if IP in packet:
            ip = packet[IP]
            src_ip = ip.src
            dst_ip = ip.dst
            
            if TCP in packet:
                tcp = packet[TCP]
                src_port = tcp.sport
                dst_port = tcp.dport
                protocol = 'tcp'
            elif UDP in packet:
                udp = packet[UDP]
                src_port = udp.sport
                dst_port = udp.dport
                protocol = 'udp'
            else:
                src_port = None
                dst_port = None
                protocol = None

        for rule in rule_set:
            if (rule.protocol == protocol or rule.protocol == 'ip') and \
                    (rule.src_ip == 'any' or ipaddress.ip_address(src_ip) in ipaddress.ip_network(rule.src_ip)) and \
                    (rule.dst_ip == 'any' or ipaddress.ip_address(dst_ip) in ipaddress.ip_network(rule.dst_ip)) and \
                    (rule.src_port == 'any' or str(src_port) in rule.src_port.split(',')) and \
                    (rule.dst_port == 'any' or str(dst_port) in rule.dst_port.split(',')):
                print(f"{datetime.now().strftime('%Y/%m/%d %H:%M:%S')} {rule.msg} {protocol} {src_ip} {src_port} -> {dst_ip} {dst_port}")

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

