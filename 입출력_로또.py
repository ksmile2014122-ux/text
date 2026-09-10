import random

def save_lottos(lotto, filename):
    with open(filename, "a", encoding="utf-8") as file:
        line = " ".join(lotto)
        file.write(line)
        file.write("\n")

def load_lottos(filename):
    lottos = []
    lotto = []

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip().split(" ")
        #print(line) #['8', '11', '24', '26', '29', '31']
        lotto= [int(i) for i in line]
        #print(lotto) # [8, 11, 24, 26, 29, 31]
        lottos.append(lotto)
    return lottos


def zadong() : 
    target = []
    count = 0
    while True : 
        if count == 6 : 
            break
        zz = random.randint(1,45)
        if zz not in target : 
            target.append(zz)
            count += 1 
    target.sort()
    target = [str(i) for i in target]
    save_lottos(target, "lottos.txt")

def sudong() : 
    target = []
    while len(target) < 6 :
        zz = int(input("1~45번 중에 로또번호를 입력하세요 : "))
        if zz in target :
            print("값이 중복되었습니다")
            continue
        else :
            target.append(zz)
    target.sort()
    target = [str(i) for i in target]
    save_lottos(target, "lottos.txt")

def banzadong() : 
    target = []
    while len(target) < 6 :
        zz = int(input("1~45번 중에 로또번호를 입력해주세요(자동추첨을 원할경우 0을 입력해주세요) : "))
        #범위검사 

        if zz in target : # 중복값제거
            print("값이 중복되었습니다.")
            continue
        elif zz != 0 : # 수동
            target.append(zz)

        elif zz == 0 : # 자동
            while len(target) <6 :
                zz = random.randint(1,45)
                if zz not in target : 
                    target.append(zz)
    target.sort()
    target = [str(i) for i in target]
    save_lottos(target, "lottos.txt")

def pastlotto() : 
    nuzac = load_lottos("lottos.txt")
    if len(nuzac) < 5 :
        print('이력이 충분하지 않습니다.')
    else :
        nuzac.reverse()
        count = len(nuzac)
        for i in range (5, 0, -1) :
            print(f"{count} 회 : {nuzac[i][0]} {nuzac[i][1]} {nuzac[i][2]} {nuzac[i][3]} {nuzac[i][4]} {nuzac[i][5]}")
            count -= 1

while True : 
    a = int(input("로또번호 추첨기: 숫자를 입력하세요(1.자동 2.수동 3.반자동 ,4.이력보기 ,5.종료하기 중에)"))
    if a==1 : 
        print("자동추첨")
        zadong()
        
    if a==2 :
        print("수동추첨")
        sudong()

    if a==3 :
        print("반자동 추첨")
        banzadong()

    if a==4 :
        print("이력보기")
        pastlotto()

    if a==5 : 
        print("종료하기")
        break
