# Task 3: Implementing Subnet Scanner

In our class, we've learned that an attacker can perform subnet scanning to discover alive hosts in a given subnet range. This task requires you to implement the subnet scanner. The `subnet_scanner.py` script takes a network prefix (e.g., 172.17.0.0/24) as input and performs UDP scanning to discover hosts in the subnet (i.e., 254 hosts). The alive host will reply with a **ICMP Port Unreachable** message, letting us know that the host is currently up.

## Programming



## Writing-up 

## Ethical Issue

Similar to the port scanning case, performing subnet scanning too much for public networks is NOT recommended.
