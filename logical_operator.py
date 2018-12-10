a = 20
b = 30

print(not a < b)
print(a < b and a != b)
print(a != b or a > b)

# True = 1, False = 0 인식
print(True + 1)
print (a > b + 1)

# bool 캐스팅(0 이외에는 전부 True값이 나온다)
print(bool(10))
print(bool(0))
print(bool([1,2,3]), bool([]))
print(bool({"a" : 10}), bool({}))
print(bool(None))

# 논리식 연산순서 True가 먼저 나온다.
print([] or "hello")

# or 연산자
print("hello" or "world")
print("" or "world")

s = "HelloWorld"
# s = ""
s and print(s)
