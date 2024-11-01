# 사이트에 접속하기 위해 requests 모듈 불러옴
import requests
# ip 주소 찾기 위한 정규식 사용하기 위해 re 모듈 불러옴
import re

# http://ipconfig.kr 사이트 접속
req = requests.get("http://ipconfig.kr")
# 정규식을 사용하여 ip 주소를 가져와 out_addr 변수에 바인딩함
out_addr = re.search(r'IP Address:\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]

# 외부 ip 주소를 출력함
print(out_addr)
