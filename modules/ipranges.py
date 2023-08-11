from ipaddress import IPv4Address
from modules.print import *

def get_ranges():
	with open("settings/ranges.txt", "r") as ranges:
		return ranges.read().splitlines()
		
def get_ips():
	ranges = get_ranges()
	debug("Got ranges from ranges.txt")
	
	ips = []
	for ip_range in ranges:
		start = IPv4Address(ip_range.split("-")[0])
		end = IPv4Address(ip_range.split("-")[1])
		for ip in range(int(start), int(end)):
			ip = str(IPv4Address(ip))
			ips.append(ip)
			
	return ips