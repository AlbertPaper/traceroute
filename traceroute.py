#!/usr/bin/env python
import logging         
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
import json
import sys
import os

if len(sys.argv) != 2:
    print "error. syntax: trace 192.168.1.1"
    exit(1)
else:
    hostname = sys.argv[1]
    hosts = []

    for ttl in range(1, 30):
        p = sr1(IP(dst=hostname,ttl=ttl)/ICMP(id=os.getpid()), verbose=0, timeout=10)

        if p == None:
            break

        if p[ICMP].type == 11 and p[ICMP].code == 0:
            hosts.append({ "ttl": ttl, "src": p.src })
        elif p[ICMP].type == 0:
            hosts.append({ "ttl": ttl, "src": p.src })
            break

    print json.dumps(hosts)
