"""
6025 ~ 6031
"""
# 입력되는 값은 기본적으로 문자열로 인식


# 6025 -- 정수 2개를 입력받아 합을 출력
d1, d2 = input("123 -123 -- ").split()
print(int(d1) + int(d2))


# 6026 -- 실수 2개를 입력받아 합을 출력
f1 = float(input("0.1 -- "))
f2 = float(input("0.9 -- "))
print(float(f1) + float(f2))


# 6027 -- 10진수를 입력받아 16진수(hexadecimal)로 출력
d3 = int(input("255 -- "))
print('%x' % d3)


# 6028 -- 10진수 -> 16진수 대문자
d4 = int(input("255 -- "))
print('%X' % d4)


# 6029 -- 16진수를 입력받아 8진수(octal)로 출력
x1 = int(input("f -- "), 16)
print('%o' % x1)


# 6030 -- 영문자 1개를 입력받아 10진수 유니코드(Unicode) 값으로 출력
u1 = ord(input("A -- "))
print(u1)


# 6031 -- 10진 정수 1개를 입력받아 유니코드 문자(character)로 출력
d5 = int(input("65 -- "))
print(chr(d5))