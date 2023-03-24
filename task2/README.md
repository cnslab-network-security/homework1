# Task 2: Implementing Port Scanner

We have learned that port scanning is one of effective methods to identify which services are currently running on a target host. In this task, you will implement a toy port scanner that scans a certain range of TCP ports for a given host. 

## Programming

In this directory, `port_scanner.py` is given. This script takes `target_ip`, `start_portno`, `end_portno` as inputs. Thus, if you give the script a target IP address and TCP port range, it performs TCP scanning and prints out open ports. In order to make the script work, replace the `TODO:` comment with your code.

To test your scanner, you can use  

Hint: We will simply invoke the `connect()` method for sending a TCP SYN packet. However, it often blocks until a SYN-ACK or RST packet comes from the target, so scanning time will be too long. How can we resolve this situation? Find a hint from [here](https://docs.python.org/ko/3/library/socket.html).

## Writing-up

When writing a report, include the answers for the following questions:

1. Describe how your scanner works. Concretely, describe how your logic scans open/closed ports of a target host.
2. If you want to perform UDP scannig instead of TCP, which part of this script should be modified?
3.  

## Note: Ethical Issue

Do only test your scanner against your home router, your local host, VMs, and containers. Please do **NOT** test this program against public networks, such as university and cafe. Performing TCP scans indiscriminately could be detected by security devices (e.g., IDS/IPS/firewall), and then your host can be blocked by them.
