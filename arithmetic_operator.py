print(2 * 3)
print(2 + 3)
print(2 - 3)
print(2 / 3)
print(2 / 3.0)
print(2.0 / 3)
print(2.0 / 3.0)

# //(몫), **(지수승), %(나머지)
print(2 // 3)
print(2 ** 3)
print(2 % 3)

# divmod : 몫과 나머지 연산을 같이 하는 tuple
print(divmod(2,3))

# 연산자 우선순위
# *,/가 +,-보다 우선이다
print(2 + 3 * 4)
print(-2 + 3 * 4)
print(-(2+3) * 4)
# 왼쪽부터 차례대로 간다.
print(4 / 2 * 2)
print(4 / (2 * 2))
# 지승의 경우 뒤에부터 진행된다.
print(2 ** 3 ** 4)
print((2 ** 3) ** 4)
print(2 ** (3 ** 4))
