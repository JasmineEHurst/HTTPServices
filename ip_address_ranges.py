import ipaddress
net = ipaddress.ip_network(u'123.45.67.64/27')
net
IPv4Network(u'192.0.2.1')
for a in net:
    print(net)