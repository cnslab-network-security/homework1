# Tester example. Build your own tester to verify your NIDS!
from scapy.all import *
import random

if __name__ == '__main__':
    packet = (Ether() / IP(dst = "192.168.1.100") / TCP(dport = random.randrange(1, 1024)))
    sendp(packet, iface='eth0')
