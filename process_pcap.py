# -*- coding: utf-8 -*-
"""
Created on Wed May 26 20:33:21 2021

@author: Dion
"""

from scapy import utils
from scapy.all import IP
    

def get_ips_simple(pcap):
    paths = set()
    ips = set()
    for p in utils.PcapReader(pcap):   
        if p.haslayer(IP):
            src = p[IP].src
            dst = p[IP].dst
            ips.update([src, dst])
            paths.add((src, dst))

    return ips, paths

if __name__ == '__main__':
    pcap = 'test/http.pcap'
    nodes, paths = get_ips_simple(pcap)
    nodes
    
    pcap = 'test/infection.pcap'
    nodes, paths = get_ips_simple(pcap)
    nodes
