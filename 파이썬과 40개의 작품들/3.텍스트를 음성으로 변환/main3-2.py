from gtts import gTTS
#playsound 모듈로부터 playsound를 불러와 사용
from playsound import playsound
#경로 이동하기 위해 os 라이브러리 불러옴
import os

#경로를 .py파일의 실행경로로 이동, 현재 경로로 이동(playsound에서 한글 인식 못해서 경로를 이동함)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#현재 스크립트 파일(.py 파일)이 실행되는 디렉토리로 경로를 이동합니다.
#os.path.abspath(__file__): 현재 스크립트의 절대 경로를 반환합니다.
#os.path.dirname(...): 해당 경로의 디렉토리 부분을 추출합니다.
#os.chdir(...): 지정된 디렉토리로 현재 작업 디렉토리를 변경합니다.
#이 코드가 필요한 이유는 playsound가 한글 경로를 제대로 인식하지 못하는 경우가 있으므로, 경로 문제를 피하기 위해 스크립트가 실행되는 디렉토리로 이동합니다.


text = "안녕하세요 파이썬과 40개의 작품들입니다"

tts=gTTS(text=text,lang='ko')
#gTTS 클래스를 사용하여 text 변수에 있는 텍스트를 음성으로 변환합니다. lang='ko'는 변환할 언어가 한국어임을 나타냅니다.
#tts 객체는 생성된 음성을 나타냅니다.

#hi.mp3 저장
tts.save("hi.mp3")
#hi.mp3 출력하여 소리재생
playsound("hi.mp3")