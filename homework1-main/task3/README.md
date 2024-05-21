# Task 3: Implementing Subnet Scanner

In our class, we've learned that an attacker can perform subnet scanning to discover alive hosts in a given subnet range. This task requires you to implement the subnet scanner. The `subnet_scanner.py` script takes a network prefix (e.g., 10.0.100.0/24) as input and performs UDP scanning to discover all possible hosts in the subnet (i.e., 254 hosts). 

## Requirement

In the script `subnet_scanner.py`, you need to implement two methods: `sniffer()` and `udp_sender()`.

`sniffer()` captures all packets come to your host by using a raw socket. The raw socket is a special socket that allows us to modify TCP/IP headers, which are originally controlled by Linux kernel. By doing so, we can parse the header information of any incoming packet. When you send an UDP packet to an alive host, it replies with an **ICMP Port Unreachable** message, letting us know that the host is currently up. This means that when `sniffer()` captures a packet via raw socket, it needs to analyze its ICMP header information. You may need to refer [this document](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Datagram_structure) to know what ICMP packet looks like. Note that you can utilize `IP` and `ICMP` classes in `subnet_scanner.py`.

`udp_sender()` sends UDP packets (whose destination port is 19999) to all the hosts of a given subnet, which is taken from the parameter `subnet` from the command line. What you need to do is to get all the valid IP addresses belong to the subnet. For example, there are 254 valid hosts starting from 10.0.100.1 to 10.10.100.254 in 10.0.100.0/24.

In order to execute the script, we type the following command:

```
$ python3 subnet_scanner.py [target_subnet]
```

When we type `Ctrl+C`, the program stops and prints out all the hosts discovered so far.

You can test your subnet scanner in your home network (i.e., wifi subnet) or the given script `run_tester.sh`.
When you type the following command (in your host), it prints out subnet information (which will be 10.0.100.0/24) and executes 5 containers:

```
jinwoo@MacBook-Pro task3 % ./run_tester.sh
                    "Subnet": "10.0.100.0/24"
[+] Running 5/0
 ⠿ Container task3-ubuntu1-1  Created                                                                    0.0s
 ⠿ Container task3-ubuntu2-1  Created                                                                    0.0s
 ⠿ Container task3-ubuntu3-1  Created                                                                    0.0s
 ⠿ Container task3-ubuntu5-1  Created                                                                    0.0s
 ⠿ Container task3-ubuntu4-1  Created                                                                    0.0s
Attaching to task3-ubuntu1-1, task3-ubuntu2-1, task3-ubuntu3-1, task3-ubuntu4-1, task3-ubuntu5-1
```

Note that those 5 containers will run on the same network that you have previously run with `run_docker.sh` in the parent directory.
If you correctly implement your scanner, it will find 7 IP addresses there (five for the above containers, one for the scanner where your scanner is running, and one for the Docker bridge interface.).

## Writing-up 

When writing a report, you need to include the answers for the following questions:

1. Describe how your subnet scanner works. You need to mention a *thread*.
2. In the case of subnet scanning, which protocol would be best between UDP and TCP? Explain why you think so.

## Ethical Issue

Similar to the port scanning case, performing subnet scanning for public networks is NOT recommended.
