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
# name = "정수용"
# sex = "남"
# age = 24
# hight = 178
# weight = 73
# is_adult = age >= 20

# print("내이름은" , name)
# print("나이는" , age , "이고")
# print("어른인가?" , is_adult)

# station = "사당"
# print(station + "행 열차가 들어오고 있습니다.")
# station = "신도림"
# print(station + "행 열차가 들어오고 있습니다.")
# station = "인천공항"
# print(station + "행 열차가 들어오고 있습니다.")

# print(2**10)
# print(100//5)
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

# from random import *

# print("오프라인 스터디 모임 날짜는 매월"+ str(randrange(4, 29)) +"일로 선정되었습니다")
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

# per = "980119-1118011"

# print("성별 : " + per[7])
# print("생년 : " + per[0:2])         #0 ~ 2 직전까지
# print("월 : " + per[2:4])
# print("일 : " + per[4:6])
# print("생년월일 : " + per[:6])      #처음부터
# print("뒷자리 : " + per[7:])        #끝까지
# print("뒷자리 : " + per[-7:])       #뒤부터

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

# print("%d" % 30)
# print("%s" % "정수용")
# print("%c" % "a")

# print("%s" % 30)
# print("%s %s" % ("하나", "둘"))

# print("{}".format(20))
# print("{} {}".format(20, 10))
# print("{1} {0}".format(20, 10))

# print("{color} {age}".format(age = 20, color = "하나"))

# age = 20
# color = "하나"
# print(f"{color} {age}")

# print("\"\"\"\"")
# print("\\")
# #\r = 커서를 앞으로
# print("asdasd\rdddddddd")
# #\b = 백스페이스
# #\t = 탭

'''
site = "https://www.naver.com"
site_1 = site[site.index(".") + 1:site.index(".",site.index(".") + 1)]

PW = site_1[:3] + str(len(site_1)) + str(site_1.count('e')) + "!"
print(site_1)
print(PW)
'''

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
'''
cabinet = {3:"정수용", 100:"홍길동"}
print(cabiner[3])
'''
#region II

#endregion
