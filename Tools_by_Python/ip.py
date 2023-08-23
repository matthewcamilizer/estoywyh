import requests

url="https://checkip.amazonaws.com"

request=requests.get(url)

print(request.text)
