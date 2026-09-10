file=open("test.txt","w",encoding="utf-8") # w: 쓰기, a : 추가 , 
file.write("안녕하세요") # 파일에 내용 쓰기
file.close() # 파일 닫기

with open("test.txt","w",encoding="utf-8")as file: # 쓰기 모드
	file.write("1일차 학습\n")
	file.write("2일차 학습\n")
	file.write("3일차 학습\n")

with open("test.txt","r",encoding="utf-8")as file: #읽기 모드
	content=file.read()

print(content) # 이스케이프 문자 때문에 빈공간이 더 

# 파일 읽기 방식 3가지
# 1) read()  - 전체를 하나의 문자열로 읽습니다.

with open("test.txt","r",encoding="utf-8")as file:
	content=file.read()

print(content)

# 2) readline()  - 한 줄씩 읽습니다.
with open("test.txt","r",encoding="utf-8")as file:
	line1=file.readline()
	line2=file.readline()

print(line1)
print(line2)

# readlines()  - 여러 줄을 읽습니다.
with open("test.txt","r",encoding="utf-8")as file:
	lines=file.readlines()

print(lines)

for line in lines:
	print(line.strip()) # 양쪽 끝에 공백을 삭제하고 , 리스트 반복문을 통해서 print 해주기 

#  파일에 내용 추가하기: a 
with open("test.txt","a",encoding="utf-8")as file:
	file.write("4일차 학습\n")

for line in lines:
	print(line.strip()) # 양쪽 끝에 공백을 삭제하고 , 리스트 반복문을 통해서 print 해주기 

#사용자 입력을 메모장에 저장하기
# 다만 w 냐, a냐에 따라 결과물이 달라질 수 있다. 
memo=input("메모를 입력하세요: ")

with open("test.txt","w",encoding="utf-8")as file:
	file.write(memo)

# 여러 메모 계속 추가하기 
while True:
	memo=input("메모를 입력하세요. 종료하려면 q 입력: ").strip()

	if memo.lower()=="q":
		break
	
	with open("test.txt","a",encoding="utf-8")as file:
		file.write(memo+"\n")
	
	print("메모 저장이 완료되었습니다.")

# 업앤다운 결과도 하나의 메모에 위의 기능을 활용해 저장할 수 있음 
# 학생 점수 txt 파일 저장하기
students= [
    {"name":"민수","score":85},
    {"name":"지수","score":92},
    {"name":"영희","score":55}
]

with open("students.txt","w",encoding="utf-8")as file:
	for student in students:
		file.write(f"{student['name']},{student['score']}\n")

### 주의 : 메모장에 적힌 글씨는 모두다 String 으로 인식 한다.
# 만약 숫자로 인식 하고 싶다면 아래 처럼 코딩이 가능하다. 
students = []
with open("students.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

for line in lines: # \n ["민수", "85"] 공백 제거   
    data = line.strip().split(",")

    student = {
        "name": data[0],
        "score": int(data[1]) # {"name": "민수", "score" : 85}
    }

    students.append(student)

print(students)


# 파일이 없지만 무조건 실행해야하는 상황이 있다면, 파일 예외처리 가능 
try:
    with open("students.txt", "r", encoding="utf-8") as file:
        content = file.read()

except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")

else:
    print(content)

# 숫자 변환 실패 처리
line = "민수,팔십오"

try:
    data = line.strip().split(",")
    name = data[0]
    score = int(data[1])

except ValueError:
    print("점수는 숫자로 입력해야 합니다.")

else:
    print(name, score)

# 파일 입출력 함수로 묶기 
def save_students(students, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for student in students:
            line = f"{student['name']},{student['score']}\n"
            file.write(line)

save_students(students,"test.txt")

students= [
    {"name":"민수","score":85},
    {"name":"지수","score":92},
    {"name":"영희","score":55}
]

save_students(students,"students.txt")

# 학생 데이터 읽기 함수 
def load_students(filename):
    students = []

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(",") #공백제거, "," 기준으로 분류

        student = {
            "name": data[0],
            "score": int(data[1])
        }

        students.append(student)

    return students

# 현재 작업 폴더와 파일 존재 여부 확인
# 파일이 어디에 생성되는지 확인할 때는 os 라이브러리를 사용할 수 있습니다.
import os

d = os.getcwd() # 문자열로 받은 데이터 값을 활용해서 변수화해서 사용 할 수도 있다. 
print(os.getcwd())

# 파일이 있는지 확인
import os

if os.path.exists("ranking.txt"):
    print("랭킹 파일이 있습니다.")
else:
    print("랭킹 파일이 없습니다.")

# try-except를 이미 배웠다면 파일을 직접 열어보고 오류를 처리하는 방식도 사용할 수 있습니다.
# 없다면 파일 생성하는 예외 처리도 가능함 
# 랭킹 한 건 저장 
def save_ranking(name, count):
    with open("ranking.txt", "a", encoding="utf-8") as file:
        file.write(f"{name},{count}\n")

# 업앤다운 랭킹 파일 다시 불러오기
def load_ranking():
    players = []

    try:
        with open("ranking.txt", "r", encoding="utf-8") as file: # 파일 읽기
            lines = file.readlines()

        for line in lines:
            data = line.strip().split(",")

            player = {
                "name": data[0],
                "시도횟수": int(data[1])
            }

            players.append(player) # 리스트화 

    except FileNotFoundError:
        print("아직 저장된 랭킹이 없습니다.")

    return players

# 기존 로또 과거 이력을 TXT로 저장하기
def save_lotto(lotto):
    line = ""

    for i in range(len(lotto)):
        line += str(lotto[i])

        if i < len(lotto) - 1:
            line += ","

    with open("lotto_history.txt", "a", encoding="utf-8") as file:
        file.write(line + "\n")
# 사용
lotto = [3, 7, 12, 20, 31, 42]

save_lotto(lotto)
# 파일 내용
# 3,7,12,20,31,42
#1,5,11,22,33,44

# 프로그램이 언제 시작되서, 종료되는가? 
""" 프로그램 시작
→ 기존 랭킹 파일 읽기
→ 기존 로또 이력 파일 읽기
→ 게임 실행
→ 새 결과 저장
→ 프로그램 종료 """

# 다른 파일 형식 사용하기
# TXT 파일입출력 원리를 이해하기 좋음
# 표 형태 데이터는 CSV가 더 편리
