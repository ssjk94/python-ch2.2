# 객체 대소비교 연산(python은 모든 것이 객체이다.)
print(1 > 3)
print(2 < 4)
print(4 <= 5)
print(4 >= 5)
print(6 == 9)
print(6 != 9)

# 복합 관계식
a = 6
print(0 < a < 10)
print(0 < a and a< 10)

# 수치형 객체 외에도 다른 객체 비교 가능(tuple, list 갯수 등)
print("abcd" > "abd")
print((1, 2, 4) < (1, 3, 1))
print([1, 3, 2] > [1, 2, 0])

# 동질성 비교 : ==, 동일성 비교 : is연산자
a = 10
b = 20
c = a
print(a == b)
print(a is b)
print(a is c)
print(a == c)
