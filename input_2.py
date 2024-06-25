"""
6016 ~ 6024
"""

# 6016 -- 2개의 문자가 공백으로 구분되어 입력 -> 순서 바꿔 출력
while True:
    try:
        c1, c2 = input("1 1 -- ").split()
        print(c2, c1)
        break
    except ValueError:
        print("Invalid input")


# 6017 -- 정수, 실수, 문자, 문자열 등 1개만 입력받아 한 줄로 3번 출력
c3 = input("1 -- ")
print(c3, c3, c3)


# 6018 -- 시:분 한 줄로 입력 -> 그대로 출력
t1, t2 = input("1:1 -- ").split(':')
print(t1, t2, sep=':')


# 6019 -- 2020.3.4 -> 4-3-2020
y, m, d = input("1111.1.1 -- ").split('.')
print(d, m, y, sep='-')


# 6020 -- 000907-1121112 -> 0009071121112
# 아무것도 없는 공(empty) 문자는 작은 따옴표(') 2개를 붙여서 '' 로 표현한다.
num1, num2 = input("111-111 -- ").split('-')
print(num1, num2, sep='')


# 6021 -- 알파벳과 숫자로 이루어진 단어 1개가 입력 -> 한 줄에 한 문자씩 분리해 출력
s1 = input("111 -- ")
for i in range(len(s1)):
    print(s1[i])


# 6022 -- 200304 -> 20 03 04
# s[a:b] 라고 하면, s라는 단어에서 a번째 문자부터 b-1번째 문자까지 잘라낸 부분
s2 = input("숫자 6자리 -- ")
print(s2[0:2], s2[2:4], s2[4:6])


# 6023 -- 17:23:57 -> 23
t3 = input("12:34:56 -- ").split(':')
print(t3[1])


# 6024 -- hello world -> helloworld
w1, w2 = input("asd asd -- ").split()
print(w1 + w2)