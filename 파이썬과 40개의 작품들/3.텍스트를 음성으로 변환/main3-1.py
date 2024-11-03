#gtts 라이브러리로부터 gTTS를 불러옴
from gtts import gTTS
import os
print(os.getcwd()) 
#text 변수에 문자열 할당
text = "안녕하세요. 파이썬과 40개의 작품들입니다."
#text 변수의 문자열을 한글로 변환하여 tts 변수에 넣음   
tts = gTTS(text=text, lang='ko')
#[3.텍스트를 음성으로 변환 ]폴더에 hi.mp3의 파일이름으로 저장함.저장경로는 [3.텍스트를 음성으로 변환 ]폴더임. c드라이브에 저장하고 싶으면 C:/3.텍스트를 음성으로 변환 로 해야됨
#  r은 \ 두번 안쓰게 해줌. 원래는 두번 써야 폴더 안에 있다는게 표시됨
tts.save(r"3.텍스트를 음성으로 변환\hi.mp3")

