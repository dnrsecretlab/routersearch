import socket
import threading
from modules.ipranges import *
from modules.print import *
from modules.webparser import *

ports = [80, 8080] # кто нахуй юзает порт 8080 в 2023 веке
good = []
scans = 0
max_scans = 1000_000
reconnections = 1
timeout = 0.1
routers = ["asus", "totolink", "netis", "tl-"]

def is_working(ip, port):
	try:
		sock = socket.socket()
		sock.connect((ip, port))
	except:
		return False
	else:
		sock.close(); return True
		
def scan_ip(ip):
	global scans
	for port in ports:
		# тут заспавнился костыль из-за уебищных роутеров asus (todo)
		for _ in range(reconnections):
			if is_working(ip, port):
				address = "http://" + ip + ":" + str(port)
				if address not in good:
					html = get_html(address)
					title = get_title(html)
						
					for router in routers:
						try:
							if router in title:
								print(address + " " + title)
						except:
							continue
							
					good.append(address)
			
			scans += 1
		
def scan_ips():
	ips = get_ips()
	
	debug("Got all IPs. Started scanning.")
	debug("Max Scans =", max_scans)
	debug("Socket Timeout =", timeout)
	debug("Requests Timeout =", 100)
	debug("Reconnections =", reconnections)
	debug("IPs to scan =", len(ips))
	print("\nRouters:")
	
	socket.setdefaulttimeout(timeout)
	for ip in ips:
		thread = threading.Thread(target=lambda: scan_ip(ip))
		thread.daemon = True
		thread.start()
		
		if scans >= max_scans:
			break