import socket

#소켓 연결
in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#www.google.co.kr 접속함. https의 기본 접속 포트는 443임
in_addr.connect(("www.google.co.kr",443))
#연결된 소켓의 이름을 출력함
print(in_addr.getsockname()[0])
#10.10.60.127
