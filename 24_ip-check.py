from ipaddress import ip_address, ip_network

target = input("Enter IP address =")
ip_add = ip_address(target)

ip_list = ["10.0.0.0/30" , "10.0.0.4/30"]
for prefix in ip_list:
    net = ip_network(prefix)
    if ip_add in net:
        print(f"{ip_add} is in the {net} range")
