from gtts import gTTS
from playsound import playsound
import os

#경로를 .py파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#텍스트 저장해놓은 경로이름 할당
file_path = '나의텍스트.txt'
#'나의텍스트.txt'는 현재 스크립트가 실행되는 경로에 있는 파일을 참조하기 위한 상대 경로입니다.
#코드에서 os.chdir()을 사용하여 스크립트의 위치로 작업 디렉토리를 변경했기 때문에, 스크립트와 같은 경로에 해당 파일이 있어야 코드가 파일을 찾고 열 수 있습니다.

#상대 경로: file_path = '나의텍스트.txt'는 현재 작업 디렉토리를 기준으로 해당 파일을 찾습니다. 
#os.chdir(os.path.dirname(os.path.abspath(__file__))) 코드를 통해 현재 작업 디렉토리를 스크립트가 실행되는 위치로 변경하였기 때문에, 
#이 위치에 '나의텍스트.txt' 파일이 있다고 인식하고 파일을 열 수 있습니다.

#파일을 f의 이름으로 열음. 한글로 작성된 파일을 열기 때문에 'rt', encoding='UTP8'형식으로 열어 글자가 깨지지 않게 함
with open(file_path, 'rt', encoding='UTF8') as f :
    #파일의 전체 내용을 읽어 read_file 변수에 할당함
    #파일 객체 f의 read() 메서드는 파일의 내용을 한 번에 모두 읽어서 문자열로 반환합니다.

    #open() 함수:
    #Python에서 open() 함수는 파일을 열고 파일 객체를 반환합니다.
    #file_path는 열고자 하는 파일의 경로(여기서는 나의텍스트.txt)입니다.
    #'rt'는 읽기 모드('r')와 텍스트 모드('t')를 결합한 모드입니다. 기본적으로 'r'만 써도 텍스트 모드가 디폴트지만, 명시적으로 나타내기 위해 'rt'를 사용한 것입니다.
    read_file = f.read() # txt 파일의 텍스트들을 read_file에 저장
#with는 파일을 열고 종료되면 자동으로 파일을 닫음. 파일을 열때 with를 사용하면 코드가 간결해짐.
print(read_file)
#[myText.mp3]파일 생성 후 음성으로 출력함
tts = gTTS(text=read_file, lang='ko')
#gTTS 클래스를 사용하여 read_file에 저장된 텍스트를 한국어('ko')로 음성 변환하여 tts 객체에 저장합니다.
tts.save("myText.mp3")
#tts 객체에 저장된 음성을 myText.mp3 파일로 저장합니다.
playsound("myText.mp3")
#playsound 함수를 사용하여 myText.mp3 파일을 재생합니다.
