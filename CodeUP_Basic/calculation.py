"""
산술연산
6032 ~ 6045
"""

# 6032 -- 입력된 정수의 부호를 바꿔 출력
# 단항(unary) 연산자인 -(negative)를 변수 앞에 붙이면 부호가 반대
print(-int(input("1 -- ")))


# 6033 -- 문자 1개를 입력받아 그 다음 문자를 출력
# ord() -- 단일 문자를 입력받아 해당 문자의 유니코드(또는 아스키) 값을 반환
# chr() -- 유니코드 값을 입력받아 해당 유니코드 값에 해당하는 문자를 반환
print(chr(ord(input("a -- "))+1))


# 6034 -- 정수 2개(a b)를 입력받아 a에서 b를 뺀 차를 출력
d1, d2 = input("1 2 -- ").split()
print(int(d1) - int(d2))


# 6035 -- 실수 2개(f1 f2)를 입력받아 곱을 출력
f1, f2 = input("0.1 0.2 -- ").split()
print(float(f1) * float(f2))


# 6036 -- 단어와 반복 횟수를 입력받아 여러 번 출력
# 문자열 * 정수 또는 정수 * 문자열은 그 문자열을 여러 번 반복한 문자열을 만들어 준다
word, cnt = input("aaa 3 --").split()
print(word * int(cnt))


# 6037 -- 반복 횟수와 문장을 줄을 바꿔 입력받아 여러 번 출력
cnt1 = input("반복횟수 -- ")
word1 = input("문장 -- ")
print(int(cnt1) * word1)


# 6038 -- 정수 2개(a b)를 입력받아 a를 b번 곱한 거듭제곱을 출력
d3, d4 = input("3 4 -- ").split()
print(int(d3) ** int(d4))


# 6039 -- 실수 2개(f1, f2)를 입력받아 f1을 f2번 거듭제곱한 값을 출력
f3, f4 = input("0.3 0.4 -- ").split()
print(float(f3) ** float(f4))


# 6040 -- 정수 2개(a b) 를 입력받아 a를 b로 나눈 몫을 출력
# / -- 나눗셈
# // -- 나눗셈 몫
# % -- 나눗셈 나머지
d5, d6 = input("10 3 -- ").split()
print(int(d5) // int(d6))


# 6041 -- 정수 2개(a b) 를 입력받아 a를 b로 나눈 나머지를 출력
d7, d8 = input("10 3 -- ").split()
print(int(d7) % int(d8))


# 6042 -- 실수 1개를 입력받아 소숫점 이하 두 번째 자리까지의 정확도로 반올림한 값을 출력
f5 = float(input("3.6666 -- "))
print(format(f5, ".2f"))


# 6043 -- 실수 2개(f1 f2)를 입력받아 f1 을 f2 로 나눈 값을 출력
# 이 때 소숫점 넷째자리에서 반올림하여 무조건 소숫점 셋째 자리까지 출력
f6, f7 = input("10 3 -- ").split()
print(format(float(f6) / float(f7), ".3f"))


# 6044 -- 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산
# 단, b는 0이 아니다.
d9, d10 = input("10 3 -- ").split()
d9, d10 = int(d9), int(d10)
print(d9+d10, d9-d10, d9*d10, d9//d10, d9%d10, format(float(d9)/float(d10), ".2f"), sep='\n')


# 6045 -- 정수 3개를 입력받아 합과 평균을 출력
d, dd, ddd = input("1 2 3 -- ").split()
d, dd, ddd = int(d), int(dd), int(ddd)
allAdd = d + dd + ddd
print(allAdd, format(float(allAdd/3), ".2f"))