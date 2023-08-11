import requests

# genius code)0)
def get_title(html):
	try:
		return html.lower().split("<title>")[1].split("<")[0]
	except:
		return False
	
def get_html(address):
	try:
		response = requests.get(address, timeout=100, auth=("admin", "admin"))
		html = response.text
		return html
	except:
		return False