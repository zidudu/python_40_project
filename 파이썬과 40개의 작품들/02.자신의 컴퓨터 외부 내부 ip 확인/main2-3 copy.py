import requests

# 공인 IP를 반환하는 API에 요청
req = requests.get("https://api.ipify.org")
out_addr = req.text

# 외부 IP 주소 출력
print(out_addr)

#115.140.89.82