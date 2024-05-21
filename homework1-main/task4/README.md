# Task 4: Implementing a simple NIDS

In our class, we've learned that NIDS (Network Intrusion Detection System) is used for detecting malicious traffic in practice and some open-source NIDSs are widely used. In this task, we will implement a Snort-like NIDS to understand how it works.


# Requirement

We will develop a simple NIDS that reads a Snort rule file and parses it to extract detection policies. 
It should operate with three steps:
1. Parse a Snort rule file and generate a rule set.
2. Parse an incoming packet and match it with the rule set.
3. Print a message if matched.

For example, if you type the following command:

```
$ python3 nids.py test.rules
```

Then, it should read the rule file `test.rules` and wait for incoming packets to match them with the Snort rules. 
If your NIDS captures a packet and it is matched with a rule set, your NIDS prints out a message like following:

```
2023/03/25 11:57:03 r1 packet for subnet 192.168.1.0 tcp 10.0.100.2 12345 -> 192.168.1.100 9999
```
## Parsing Snort Rule

Your first job is to parse a Snort rule file to build a rule set.
The rule file contains several Snort rules like following:

```
alert tcp any any -> 192.168.1.0/24 any (msg:"r1 packet for subnet 192.168.1.0";)
alert tcp any any -> any 23,25,21 (msg:"r2 packet for Telnet, FTP, and SSH";)
alert udp any any -> any 10000:20000 (msg:"r3 udp ports from 10000 to 20000";)
...
```

Each row is a single Snort rule and it consists of two parts: **rule header** and **rule body**. 

The **rule header** includes action, protocol, IP addresses, port numbers, and direction of packets. The action indicates how Snort should work when an incoming packet is matched with a certain rule. For example, if the action is `alert`, your NIDS should print out a message (specified in `msg` field in the rule body) to a console.


The **rule body** defines various options, such as the message being printed and packet details being analyzed.
It's important to note that except for the `msg` field, others indicate specific packet fields (e.g., flags, itype) and payload (i.e., content). Also, your NIDS should take an action only if both the rule header and rule body are matched. For example, the following rule should be taken when a TCP packet whose destination port is 80 and its payload contains the string "GET".

```
alert tcp any any -> any 80 (content:"GET"; msg:"r5 HTTP GET message";)
```

For more information about the Snort rule syntax, please refer to the [Snort official document](https://docs.snort.org/rules/).

## Parsing Packets  

Your NIDS should captures an incoming a packet and analyzes its headers and payload. Packet capturing and parsing are not a easy task if we only use pure Python code. So, we utilize [Scapy](https://scapy.net/), a powerful packet manipulation tool that allows us to develop those code very easily.

In order to use Scapy, we need to import Scapy library:

```
from scapy.all import *
```

If we want to capture a packet, we can use `sniff()`:

```
sniff(iface='eth0', prn=lambda p: parse_packet(p), filter='ip')
```

The above code captures all packets detected at the interface `eth0` (inside the container). Note that we use the `prn` option, so whenever a packet `p` is captured, it invokes `parse_packet()`, which is the method we'll implement. `filter='ip'` indicates that we'll only see IP packets.

When a packet is captured, we need to parse it to extract its information. We can utilize Scapy again to do so very easily.
For example, see the following code:

```
# Assume that the packet variable is `packet` and the captured packet is TCP packet.
ip = packet[IP]
print(f"{ip.src}, {ip.dst})
tcp = packet[TCP]
print(f"{tcp.sport}, {tcp.dport})
```

The above code extracts IP and TCP headers from the capture packet and accesses its fields.
For more information, see [this document](https://scapy.readthedocs.io/en/latest/usage.html#starting-scapy).

## Printing Messages

If an incoming packet is matched with one of Snort rules, your NIDS must print out a message. The message should follow the following format.

```
[detection_date_and_time] [msg] [protocol] [src_ip] [src_port] [direction] [dst_ip] [dst_port]
```

# Writing-up

When writing a report, include the answers for the following questions:

1. Describe how your NIDS work and how to implement it.
2. What method did you use for implementing NIDS efficiently?
3. Do you think that your NIDS can be used for a large network?
