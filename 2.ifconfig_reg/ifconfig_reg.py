import itertools
import os
import re
netinfo = {}
def get_ip():
    f = os.popen('ifconfig')
    for iface in [' '.join(i) for i in iter(lambda: list(itertools.takewhile(lambda l: not l.isspace(),f)), [])]:
        keys = re.findall('^(eth|wlan)[0-9]',iface)
        for netname in keys :
            ip = re.findall('(?<=inet\saddr:)[0-9\.]+',iface)
            if ip:
                netinfo[netname] = ip
    return False

if __name__ == '__main__':
	get_ip()