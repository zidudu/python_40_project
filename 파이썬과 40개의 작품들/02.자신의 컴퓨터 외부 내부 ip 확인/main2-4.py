import socket
import requests

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr",443))
print("내부 IP: ",in_addr.getsockname()[0])

req = requests.get("https://api.ipify.org")
out_addr = req.text
print("외부 IP: ", out_addr)
