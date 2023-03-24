# Task 3: Implementing Subnet Scanner

In our class, we've learned that an attacker can perform subnet scanning to discover alive hosts in a given subnet range. This task requires you to implement the subnet scanner. The `subnet_scanner.py` script takes a network prefix (e.g., 172.17.0.0/24) as input and performs UDP scanning to discover all possible hosts in the subnet (i.e., 254 hosts). 

## Requirement

In the script `subnet_scanner.py`, you need to implement two methods: `sniffer()` and `udp_sender()`.

`sniffer()` captures all packets come to your host by using a raw socket. The raw socket is a special socket that allows us to modify TCP/IP headers, which are origianlly controlled by Linux kernel. By doing so, we can parse the header information of any incoming packet. When you send an UDP packet to an alive host, it replies with an **ICMP Port Unreachable** message, letting us know that the host is currently up. This means that when `sniffer()` captures a packet via raw socket, it needs to analyze its ICMP header information. You may need to refer [this document](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Datagram_structure) to know what ICMP packet looks like. Note that you can utilize `IP` and `ICMP` classes in `subnet_scanner.py`.

`udp_sender()` sends UDP packets (whose destination port is 19999) to all the hosts of a given subnet, which is taken from the parameter `subnet` from the command line. What you need to do is to get all the valid IP addresses belong to the subnet. For example, there are 254 valid hosts starting from 172.17.0.1 to 172.17.0.254 in 172.17.0.0/24.

In order to execute the script, we type the following command:

```
$ python3 subnet_scanner.py 172.17.0.0/24
```

When we type `Ctrl+C`, the program stops and prints out all the hosts discovered so far.

You can test your subnet scanner in your home network (i.e., wifi subnet) or 

## Writing-up 

When writing a report, you need to include the answers for the following questions:

1. Describe how your subnet scanner works. You need to mention a *thread*.
2. In the case of subnet scanning, which protocol would be best between UDP and TCP? Explain why you think so.
3.  

## Ethical Issue

Similar to the port scanning case, performing subnet scanning for public networks is NOT recommended.
