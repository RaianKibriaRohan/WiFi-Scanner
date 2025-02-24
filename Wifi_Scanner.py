import scapy.all as scapy
# We need to create regular expressions to ensure that the input is correctly formatted.
import re

# Basic user interface header
print(r"""    _        _        _           _     _ 
   / \   ___| | _____| | __ _  __| | __| |
  / _ \ / __| |/ / _ \ |/ _` |/ _` |/ _` |
 / ___ \\__ \   <  __/ | (_| | (_| | (_| |
/_/   \_\___/_|\_\___|_|\__,_|\__,_|\__,_|
""")
print("        ▂▃▅▆█ WiFi SCANNER █▆▅▃▂     ")
print("\n****************************************************************")
print("\n* Constructed on 04 February, 2025                              *")
print("\n* https://github.com/RaianKibriaRohan                          *")
print("\n* https://www.linkedin.com/in/raian-kibria-rohan-89997a323/    *")
print("\n****************************************************************")

# Regular Expression Pattern to recognise IPv4 addresses.
ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

# Put an correct address range
while True:
    ip_add_range_entered = input("\nPlease enter the ip address and range that you want to send the ARP request to (ex 192.168.1.0/24): ")
    if ip_add_range_pattern.search(ip_add_range_entered):
        print(f"{ip_add_range_entered} is a valid ip address range")
        break
    
arp_result = scapy.arping(ip_add_range_entered)
