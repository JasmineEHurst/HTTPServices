import ipaddress

net = ipaddress.ip_network(u'123.45.67.64/27')
print(' IPv4 Network ranges:')
for a in net:
    print(a)

print('')

net6 = ipaddress.ip_network(u'12:3456:78:90ab:cd:ef01:23:30/125')
print('IPv6 Network ranges:')
for a in net6:
    print(a)