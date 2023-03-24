# Task 3: Implementing Subnet Scanner

In our class, we've learned that an attacker can perform subnet scanning to discover alive hosts in a given subnet range. This task requires you to implement the subnet scanner. The `subnet_scanner.py` script takes a network prefix (e.g., 172.17.0.0/24) as input and performs UDP scanning to discover hosts in the subnet (i.e., 254 hosts). The alive host will reply with a **ICMP Port Unreachable** message, letting us know that the host is currently up.

## Requirement

In the script `subnet_scanner.py`, you need to implement two methods: `sniffer()` and `udp_sender()`. The `sniffer()` captures all packets come to this host by using a raw socket. The raw socket is a special socket that allows us to modify TCP/IP headers, which are origianlly controlled by Linux kernel. By doing so, we can parse the header information of any incoming packet. The `udp_sender()` sends UDP packets to all the hosts of a given subnet, which is taken from the parameter `subnet` from the command line. 

For example, to execute the script we type the follwoing command:

```
$ python3 subnet_scanner.py 172.17.0.0/24
```

When we type `Ctrl+C`, the program stops and prints out the discovered hosts.

## Writing-up 




## Ethical Issue

Similar to the port scanning case, performing subnet scanning too much for public networks is NOT recommended.
