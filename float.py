a = 1.2
print(a, type(a))
print(isinstance(a,float))

b = 2.0
print(b, type(b))
# 객체 함수 is_integer()는 값이 정수인지 실수인지 확인하는 함수이다.(타입을 확인하지 않는다.)
print(b.is_integer())

# 부동 소수점 표기
b = 2e3
c = 0.2e-4
print(b, c)
