import pyttsx3

def V_def():
    while True:
        setting = input("[소리 음성 제어(속도,볼륨):1][소리 정보: 2][목소리 설정: 3][종료: 4]")
        if setting == "1":
            Controller()
        elif setting =="2":
            voice_Check()
        elif setting == "3":
            Set_Voice()
        elif setting == "4":
            print("[소리 설정] 종료")
            break
        else:
            print("다시 입력해주세요")

#소리 제어 함수
def Controller():
    print("[음성 설정]")
    V_Speed = int(input("음성속도: "))
    V_Volume = int(input("음성볼륨: "))

    # 속도 및 볼륨 설정
    engine.setProperty('rate', V_Speed)  # 말하는 속도 조정
    engine.setProperty('volume', V_Volume)  # 볼륨 조정

# 소리 정보 함수
def voice_Check():
    # 각 목소리의 상세 정보 출력
    for voice in voices:
        print(f"ID: {voice.id}")
        print(f"이름: {voice.name}")
        print(f"성별: {voice.gender}")
        print(f"언어: {voice.languages}")
        print("-" * 30)
# 목소리 설정 함수
def Set_Voice():

    # 목소리 찾기 
    
    # 목소리 설정 여부 변수
    voice_set = None
    #소리 찾기 변수
    voice_Search = ' '
    voice_Search = input("목소리 찾기: ")

    # 목소리 내장되있는 것들 중 하나씩 가져와서 입력한 이름과 대조해서 이름이 들어가있는지 확인
    for voice in voices:
        # 목소리의 이름이나 ID에 'zira'이라는 단어가 있는지 확인
        if voice_Search in voice.name.lower() or voice_Search in voice.id.lower():
            #있다면 그 id를 set에 넣음
            voice_set = voice.id
            break
    # 들어있다면 그 이름의 목소리로 설정함
    if voice_set:
        engine.setProperty('voice', voice_set)
        print(f"{voice_Search} 의 목소리로 설정합니다")

    #아니라면 기본 목소리로 설정
    else:
        print(f"{voice_Search}의 목소리를 찾을 수 없습니다. 기본 목소리로 설정됩니다.")

# 엔진 초기화
engine = pyttsx3.init()


# 사용 가능한 목소리 리스트 가져오기
voices = engine.getProperty('voices')

# 소리 설정
Set_Voice()


# 소리 속도 변수
V_Speed = 200
#소리 볼륨 변수
V_Volume = 1.0


#소리 제어 함수
Controller()

# 반복 제어 변수
control = "Y"

# 프로그램 실행 루프
while control.upper() == "Y":
    # 입력 받기
    printing = input("입력문자: ")

    # 입력 받은 텍스트 출력
    print(printing)

    # 텍스트를 음성으로 변환하여 재생
    engine.say(printing)
    engine.runAndWait()  # 음성 재생

    # 계속 입력 여부 확인
    while True:
        try:
            control = input("계속 입력하시겠습니까? [Y/N][소리 설정:C]").upper()
            
            if not control.isalpha():
                raise ValueError("문자만 입력해 주세요.")
            if control == "Y":
                print("재시작!")
                break
            elif control == "N":
                print("프로그램 종료")
                break
            elif control == "C":
                V_def()
                control = "Y"
                print("{음성 설정 종료}")
                continue
            else:
                print("다시 입력해주세요")
        except ValueError as ve:
            print(ve)
