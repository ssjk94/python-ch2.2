# 한줄 문자열 정의
s = ""
str1 = "Hello World"
str2 = "Hello World"
print(type(s), type(str1), type(str2))

# 여러줄 문자열 정의
str3 = """ABC
DEF
가나다라마바사
아자차카타파하
"""
print(str3)

# 여러줄 주석의 경우
"""
주석1
주석2
주석3
"""
"주석주석해"
# escape \
print("Hello\nWorld\nI say \"Hello World\"")

# 문자열 연산
str1 = "First String"
str2 = "Second String"

# 인덱싱
print(str1[0], str1[2], str1[4])

print(str1[2])
print(str2[2:5])


# 문자열 객체만 + 연결 연산을 할 수 있다.
print(str1 + " " + str2)
name = "정세윤"
age = 25
print(name + " " + str(age))

# 반복연산(*)
print(str1*3)

# len함수
print(len(str2))

# in, not in
print("S" in str1)
print("S" not in str2)

# 문자열 객체 변경 불가
# str1[0] = "F"

# 서식(Formating) / format함수
print("name : " + name + ", age : " + format(age,"d"))
print("name : " + format(name, "s") + ", age : " + format(age,"d"))

# tuple 이용 서식
f = "name : %s, agd : %d"
print(f % ("둘리", 20))

# Dic 이용 서식
f = 'name: %(name)s, age: %(age)d'
print(f)
print(f % {'name': '둘리', 'age': 30})
