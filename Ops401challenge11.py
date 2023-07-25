#!/usr/bin/env python3
# Script:  OpsChallenge11.py                     
# Author:  Marcelo Clark                      
# Date of latest revision:   7/25/2023 
from scapy.all import *

def scan_tcp_port_range(host, port_range):
    open_ports = []
    closed_ports = []

    for port in port_range:
        response = sr1(IP(dst=host)/TCP(dport=port, flags="S"), timeout=1, verbose=0)
