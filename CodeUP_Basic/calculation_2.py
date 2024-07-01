"""
비트시프트연산
6046 ~ 6047
"""
# 2진수 형태로 저장되어 있는 값들을 왼쪽(<<)이나 오른쪽(>>)으로
# 지정한 비트 수만큼 밀어주면 2배씩 늘어나거나 1/2로 줄어듦

# 6046 -- 1024 -> 2048
d = int(input("1024 -- "))
print(d << 1)

# 6047 --  정수 2개(a b)를 입력받아 a를 2의 b제곱한 값으로 출력
d1, d2 = input("1 3 -- ").split()
print(int(d1) << int(d2))


"""
비교연산
6048 ~ 6051
"""
# 비교/관계연산자는 <, >, <=, >=, ==(같다), !=(다르다)

# 6048 -- a가 b보다 작으면 True 를, a가 b보다 크거나 같으면 False
d3, d4 = input("1 9 -- ").split()
print(int(d3) < int(d4))
# 6049 -- 같으면 True
print(int(d3) == int(d4))
# 6050 -- b의 값이 a의 값 보다 크거나 같으면 True
print(int(d3) <= int(d4))
# 6051 -- a의 값이 b의 값과 서로 다르면 True
print(int(d3) != int(d4))


"""
논리연산
6052 ~ 6058
"""
# bool( ) -- 입력된 식이나 값을 평가해 True 또는 False
# 불(boolean) 값을 다루어주는 예약어는 not, and, or
# or -- 둘 중 하나라도 True이면 결과를 True로 반환

# 드모르간 법칙
# not (A or B) == not A and not B
# not (A and B) == not A or not B

# 6052 -- 입력된 값이 0이면 False, 0이 아니면 True
b = bool(int(input("0 -- ")))
print(b)
# 6053 -- 불 값을 반대로 출력
print(not b)

# 6054 -- 2개의 정수값의 불 값이 모두 True 일 때에만 True
b1, b2 = input("1 1 -- ").split()
b1 = bool(int(b1))
b2 = bool(int(b2))
print(b1 and b2)

# 5055 -- 하나라도 True 일 때에만 True
print(b1 or b2)

# 5056 -- 불 값(True/False) 이 서로 다를 때에만 True
# XOR(exclusive or, 배타적 논리합) 연산
print((b1 and (not b2)) or ((not b1) and b2))

# 5057 -- 불 값(True/False) 이 서로 같을 때에만 True
print((b1 and b2) or (not b1 and not b2))

# 5058 -- 모두 False 일 때에만 True
print(not (b1 or b2))



"""
비트단위 논리연산
6059 ~ 6062
"""
# 비트단위(bitwise) 연산자
# ~ : bitwise not, tilde, 틸드 -- 비트단위로 참/거짓을 바꾸기
# & : bitwise and, ampersand, 앰퍼센드 -- 비트단위로 and 연산 -- 둘 다 1인 자리를 1로
# | : bitwise or, vertical bar, 버티컬바 -- 비트단위로 or 연산 -- 둘 중 하나라도 1인 자리를 1로
# ^ : bitwise xor, circumflex/caret, 서컴플렉스/카릿
# <<(bitwise left shift), >>(bitwise right shift) 가 있다.

# 6059 -- 입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력
d5 = int(input("2 -- "))
print(~d5)

d6, d7 = input("3 5 -- ").split()
d6 = int(d6)
d7 = int(d7)
# 6060 -- & -- 같은 네트워크에 있는지 아닌지를 판단
# 그래픽처리에서 마스크연산(특정 부분을 가리고 출력하는)을 수행하는 데에도 효과적
print(d6 & d7)
# 6061
print(d6 | d7)
# 6062 -- ^ -- 그래픽처리 ->
# 두 그림에서 차이만 골라내 전체 그림을 구성하는 모든 점들의 색을 다시 계산해 입히지 않고 처리 가능
print(d6 ^ d7)


"""
3항 연산
6063 ~ 6064
"""
# "x if C else y" 의 형태로 작성이 된다.
# - C : True 또는 False 를 평가할 조건식(conditional expression) 또는 값
# - x : C의 평가 결과가 True 일 때 사용할 값
# - y : C의 평가 결과가 True 가 아닐 때 사용할 값

# 6063 -- 큰 값을 출력
d8, d9 = input("1 2 -- ").split()
d8, d9 = int(d8), int(d9)
print(d8 if (d8 > d9) else d9)

# 6064 -- 가장 작은 수
a, b, c = input("3 -1 5-- ").split()
a, b, c = int(a), int(b), int(c)
print((a if (a<b) else b) if ((a if (a<b) else b) < c) else c)