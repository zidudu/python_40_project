from gtts import gTTS
from playsound import playsound
import os

#1. 입력하고 2. 입력한 문자를 출력과 동시에 재생시켜주고, 3. 예 아니오를 통해 사용자 편의성을 높이게 함
control = "Y"

while control == "Y":
    #1.입력
    printing = input("입력문자: ")

    #경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    #2.출력 및재생
    print("=>",printing)

    tts = gTTS(text=printing, lang='ko')
    #gTTS 클래스를 사용하여 read_file에 저장된 텍스트를 한국어('ko')로 음성 변환하여 tts 객체에 저장합니다.
    tts.save("myText.mp3")
    #tts 객체에 저장된 음성을 myText.mp3 파일로 저장합니다.
    playsound("myText.mp3")
    #playsound 함수를 사용하여 myText.mp3 파일을 재생합니다.
    
    #음성 파일 삭제
    # 재생 후 파일 삭제
    os.remove("myText.mp3")


    #3. 계속 입력 여부
    while True:
            try:
                # Y/N 입력
                control = input("계속 입력하시겠습니까? [Y/N]")

                # 만약 입력한 값이 알파벳이 아니라면 raise 실행하고 valueError 값 받아옴. 그리고 except 실행하고 valueError에 있는 예외 객체 ve를 가져와서 ve를 출력함
                if not control.isalpha():
                    raise ValueError("문자만 입력해 주세요.")
                # 만약 입력한 값이 알파벳이 맞다면 r을 반환시킴
                if control == "Y":
                    print("재시작!")
                    break
                elif control == "N":
                    print("프로그램 종료")
                    break
                else:
                    print("다시 입력해주세요")
            except ValueError as ve:
                print(ve)

    
