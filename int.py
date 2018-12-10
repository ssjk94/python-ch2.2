# 2진법, 8진법, 10진법, 16진법 literal
a = 23
print(type(a))

b = 0b1101
o = 0o23
h = 0x23
print(b, o, h)

# 3.x버전은 int와 long이 합쳐졌다. int 표현범위가 무한대이다.
e = 2**1024
print(e)
print(e.bit_length())

# 변환함수
print(oct(38))
print(hex(38))
print(bin(38))