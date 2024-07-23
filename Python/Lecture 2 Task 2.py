import requests

ip_address = requests.get("https://api.ipify.org/?format=json").json()["ip"]
print(requests.get("https://ipinfo.io/%s/geo" % ip_address).json())
