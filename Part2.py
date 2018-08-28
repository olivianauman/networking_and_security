from ipaddress import *
from utils import *

list_of_ips = []
list_of_active =[]

ips = ip_network('129.255.0.0/24', strict=False)
for ip in ips:
    list_of_ips.append(ip)
print(list_of_ips)
for value in list_of_ips:
    if check_host(str(value)):
        list_of_active.append(value)
    else:
        pass  
print(list_of_active)