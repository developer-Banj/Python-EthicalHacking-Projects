## run with sudo on kali linux

import scapy.all as scapy
import re

# Regular Expression pattern for IPv4 addresses
ipaddress_rangepattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")


while True:
    ipaddress_range_entered = input("\nPlease enter the ip address and range that you want to send the ARP request to (ex 192.168.1.0/24): ")
    if ipaddress_rangepattern.search(ipaddress_range_entered):
        print(f"{ipaddress_range_entered} is a valid ip address range")
        break


arp_result = scapy.arping(ipaddress_range_entered)
