import os
import platform
from datetime import datetime

def debug(*args):
	now = str(datetime.now())
	text = f"[{now}] "
	for arg in args:
		text += str(arg) + " "
	
	print(text)
