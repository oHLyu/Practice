#region Print
'''
print(5)
print(-5)
print(3.14)
print(100000)
print(5 + 3)
print(5 * 10)
print(3 * (3+1))
print('풍선')
print("나비")
print('ㄹㅇㅋㅋ')
print('ㄹㅇㅋㅋ'* 4)
print(1>10)
print(1<10)
print(True)
print(False)
print(not 1>10)
print(not 1<10)
'''
#endregion
#region Variable
'''
name = "정수용"
sex = "남"
age = 24
hight = 178
weight = 73
is_adult = age >= 20

print("내이름은" , name)
print("나이는" , age , "이고")
print("어른인가?" , is_adult)
'''
#endregion
#region Quiz1
'''
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")
'''
#endregion
#region Calculation
'''
print(2**10)
print(100//5)
'''
#endregion
#region Maxminrandom
'''
print(abs(-1))      #절댓값
print(pow(2, 4))    #지수
print(max(5, 10))   #최댓값
print(min(1, 5))    #최솟값
print(round(3.14))  #반올림
print(round(3.99))
print(round(3.14))  
from math import *  #math 라이브러리
print(floor(3.99))  #내림
print(ceil(3.14))   #올림
print(sqrt(16))     #제곱근
'''
'''
from random import *

print(random())             #0.0 ~ 1.0미만
print(random() *10)         #0.0 ~ 10.0미만
print(int(random() *10))    #0 ~ 10미만  

print(randrange(1, 46))     #1 ~ 46미만
print(randrange(1, 45))     #1 ~ 45
'''
#endregion
#region Quiz2
'''
from random import *

print("오프라인 스터디 모임 날짜는 매월"+ str(randrange(4, 29)) +"일로 선정되었습니다")
'''
#endregion
#region Sentence
'''
se = '가나다라마바사'
se2 = "가나다라마바사"
se3 = """
가나다라마바사
아자차카타파하
에헤
"""
print(se)
print(se2)
print(se3)
'''
#endregion
#region Slicing
'''
per = "980119-1118011"

print("성별 : " + per[7])
print("생년 : " + per[0:2])         #0 ~ 2 직전까지
print("월 : " + per[2:4])
print("일 : " + per[4:6])
print("생년월일 : " + per[:6])      #처음부터
print("뒷자리 : " + per[7:])        #끝까지
print("뒷자리 : " + per[-7:])       #뒤부터
'''
#endregion
#region Sentence_function
'''
python = "Python is Greatn"
print(python.lower())       #전부 소문자
print(python.upper())       #전부 대문자
print(python[0].isupper())  #해당글자 논리
print(len(python))          #문자열 길이
print(python.replace("Python", "Java")) #치환
index = python.index("n")   #문자 찾기
print(index)
index = python.index("n", index + 1) #그다음번째
print(index)
print(python.find("java"))  #문자찾기(없다면 -1을 반환)
print(python.count("n"))    #문자횟수
'''
#endregion
#region Sentence_format
'''
print("%d" % 30)
print("%s" % "정수용")
print("%c" % "a")

print("%s" % 30)
print("%s %s" % ("하나", "둘"))

print("{}".format(20))
print("{} {}".format(20, 10))
print("{1} {0}".format(20, 10))

print("{color} {age}".format(age = 20, color = "하나"))

age = 20
color = "하나"
print(f"{color} {age}")

print("\"\"\"\"")
print("\\")
#\r = 커서를 앞으로
print("asdasd\rdddddddd")
#\b = 백스페이스
#\t = 탭
'''
#endregion
#region Quiz3
'''
site = "https://www.naver.com"
site_1 = site[site.index(".") + 1:site.index(".",site.index(".") + 1)]

PW = site_1[:3] + str(len(site_1)) + str(site_1.count('e')) + "!"
print(site_1)
print(PW)
'''
#endregion
#region List
'''
subway = [0,2,3]
print(subway.index(2))
subway.append(4)
print(subway)
subway.insert(1,1)
print(subway)

print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)

subway.append(1)
print(subway.count(1))

num = [3,4,2,5,1]
num.sort()
print(num)

num.reverse()
print(num)

# num.clear()
# print(num)

num.extend(subway)
print(num)
'''
#endregion
#region Cabinet
'''
cabinet = {3:"정수용", 100:"홍길동"}
# print(cabinet[3])   #값이 없는경우 프로그램 종료
# print(cabinet[100])

# print(cabinet.get(3)) #값이 없는경우 넘어감

print(3 in cabinet)
print(5 in cabinet)

cabinet[50] = "신규"
print(cabinet)

del cabinet[100]  # 지우기
print(cabinet)

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

cabinet.clear()
print(cabinet)
'''
#endregion
#region Tuple
'''
menu = ("제육", "라면")
print(menu[0])
print(menu[1])

name, age, hobby = "정수용", 24, "코딩"
print(name, age, hobby)
'''
#endregion
#region Set
#중복 안됨, 순서 없음
'''
my_set = {1,2,3,3,3}
print(my_set)

java = {"갑", "을", "병", "정"}
python = set(["을", "정"])
#교집합
print(java & python)
print(java.intersection(python))
#합집합
print(java | python)
print(java.union(python))
#차집합
print(java - python)
print(java.difference(python))
#추가
python.add("무")
print(python)
#삭제
java.remove("을")
print(java)
'''
#endregion
#region Change
'''
menu = {"커피", "우유", "쥬스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))
'''
#endregion
#region Quiz4
'''
from random import *
ID = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#ID = range(1, 21) 1부터 20까지 숫자를 생성
#ID = list(ID) list형으로 변환
shuffle(ID)
print("-- 당첨자 발표 --")
print("치킨 당첨자 : ", ID.pop())
print("커피 당첨자 : ", sample(ID, 3))
print("-- 축하합니다 --")
print(ID)
'''
#endregion
#region If
'''
weather = input("today weather?")
if weather == "rain" or weather == "snow":
    print("umbrella")
elif weather == "dust":
    print("mask")
else:
    print("-")

temp = int(input("temp?"))

if 30 <= temp:
    print("too hot")
elif 10 <= temp < 30:
    print("good")
else:
    print("too cold")
'''
#endregion
#region For
'''
for ex in range(6):
    print("number : {0}".format(ex))
for ex in [0,1,2,3,4,5]:
    print("number : {0}".format(ex))
for ex in range(1,6):
    print("number : {0}".format(ex))

user = ["A","B","C"]
for customer in user:
    print("{0}, thanks.".format(customer))
    '''
#endregion
#region While
'''
user = "A"
index = 5
while index >= 1:
    print("{0}, ready. {1} number.".format(user, index))
    index -= 1
    if index == 0:
        print("user no.")
lndex = 1
while True:
    print("{0}, ready. {1} number.".format(user, lndex))
    lndex += 1
    if lndex == 5:
        print("user no.")
        break
    '''
#endregion
#region Continue
'''
absent = [2, 5]
for student in range(1,11):
    if student in absent:
        continue
    print("{0} student".format(student))
    '''
#endregion
#region One_Line_For
'''
students = range(1,6)
print(students)
students = [i+100 for i in students]
print(students)

students = ["QWRDASF", "QWFD AWEQWE", " QWES"]

students = [i.lower() for i in students]
print(students)

students = [len(i) for i in students]
print(students)
'''
#endregion
#region Quiz5
'''
from random import *
matching = 0
for coustomer_matching in range(50):
    i = randrange(5, 51)
    if i <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(coustomer_matching,i))
        matching += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(coustomer_matching,i))
print("총 탑승 승객 : {0}명".format(matching))
'''
#endregion
#region Function
'''
balance = 0
money = 0
def open_account():             #intro
    print("new account.")

def deposit(balance, money):    #입금함수
    print("balance : {0}$".format(balance + money))
    return balance + money

def withdraw(balance, money):   #출금함수
    if balance < money:
        print("insufficient cash. balance : {0}$".format(balance))
        return balance
    else:
        print("balance : {0}$".format(balance - money))
        return balance - money

open_account()
balance = deposit(balance, 1000)
balance = withdraw(balance, 300)
print(balance)
'''
#endregion
#region Default

def profile(name, age = 24, sex = "female"):
    print("name : {0}\nage : {1}\nsex : {2}".format(name, age, sex))
profile(name = "정수용", sex = "male")

#endregion
#region Variable_factor
'''
def profile(name, age, sex, *language):
    print("name : {0}\nage : {1}\nsex : {2}".format(name, age, sex))
    for i in language:
        print(i, end = " ")
    print()
profile("정수용", 24,  "male", "Java", "C", "C++", "Python")
'''
#endregion