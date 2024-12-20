#컴퓨터가 연결된 접속정보를 받아올때 사용하는 모듈을 불러옴
import socket

#연결된 소켓의 이름을 가져와 in_addr 변수와 바인딩함(소켓을 특정 IP 주소와 포트 번호에 연결하는 것을 바인딩이라고 합니다. 즉, 소켓이 해당 IP와 포트를 사용하도록 설정하는 과정입니다.
#즉, in_addr 변수는 socket.gethostbyname(socket.gethostname())의 결과인 IP 주소와 바인딩됩니다(연결됩니다).)
in_addr = socket.gethostbyname(socket.gethostname()) #socket.gethostbyname(socket.gethostname())은 현재 컴퓨터의 호스트 이름을 가져온 후, 이를 사용해 해당 호스트 이름의 IP 주소를 조회합니다.
#in_addr은 로컬 네트워크 상의 IP 주소를 저장


#in_addr을 출력하여 내부 ip를 확인함
print(in_addr)
#192.168.124.1
#=> 이 방법으로 진행하여 내부 ip 확인할 경우 가상 환경 등을 사용하여 여러 개의 환경이 있을 경우 다른 환경의 ip가 출력될 수 있음
# 정확한 ip를 알 수 없을 수 있음

#이 방법으로 IP 주소를 확인할 경우, 가상 환경(VM)이나 도커 컨테이너 등 여러 개의 네트워크 인터페이스가 있을 때 정확한 IP 주소를 가져오지 못할 수도 있습니다. 
# socket.gethostbyname()은 종종 기본 인터페이스의 IP 주소만 반환하기 때문입니다.
#만약 컴퓨터가 
#여러 개의 네트워크 인터페이스(예: 가상 네트워크 어댑터)를 갖고 있다면, 다른 인터페이스의 IP 주소가 반환될 수 있습니다. 
# 이로 인해 로컬 네트워크의 정확한 IP를 알기 어려운 경우가 발생할 수 있습니다.