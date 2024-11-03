# 사이트에 접속하기 위해 requests 모듈 불러옴
#requests 모듈은 Python에서 HTTP 요청을 보내고 응답을 받을 수 있는 라이브러리입니다. 웹사이트에 접속하고 데이터를 가져오기 위해 사용됩니다.
import requests
# ip 주소 찾기 위한 정규식 사용하기 위해 re 모듈 불러옴
#re 모듈은 정규식을 사용하기 위한 라이브러리입니다. 문자열에서 특정 패턴을 검색하거나 추출할 때 사용됩니다.
import re

# http://ipconfig.kr 사이트 접속
req = requests.get("http://ipconfig.kr")
#requests.get() 메서드를 사용하여 http://ipconfig.kr 웹사이트에 접속하고, 응답을 req 변수에 저장합니다.
#req.text는 웹사이트의 HTML 콘텐츠를 문자열로 반환합니다.
#http://ipconfig.kr와 같은 사이트는 사용자가 따로 IP를 입력하지 않아도 접속하는 요청을 보낸 클라이언트의 공인 IP 주소를 자동으로 감지하여 반환합니다.
# 이러한 사이트들은 접속한 기기의 공인 IP를 확인하는 서비스로 설계되어 있습니다.



# 정규식을 사용하여 ip 주소를 가져와 out_addr 변수에 바인딩함
out_addr = re.search(r'IP Address:\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]

# 외부 ip 주소를 출력함
print(out_addr)


#2/2

#ChatGPT의 말:
#ChatGPT
#코드가 실행되지 않는 가장 큰 이유는 http://ipconfig.kr 사이트의 구조나 접근 방법이 변경되었을 가능성이 큽니다. 
#정규식으로 IP Address:라는 패턴을 찾고 있지만, 해당 페이지의 HTML이 변경되어 더 이상 이 패턴을 포함하지 않을 수 있습니다.
