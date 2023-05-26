import sys
sys.dont_write_bytecode = True

import requests

url = input(r"Enter URL:")
response = requests.get(url, allow_redirects=False)
redirect_url = response.headers.get('location')

print(redirect_url)
