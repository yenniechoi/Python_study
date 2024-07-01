"""
선택실행구조
6065 ~ 6070
"""


# 6065 -- 3개의 정수(a b c)가 입력되었을 때, 짝수만 출력
a, aa, aaa = input("1 2 4 -- ").split()
a, aa, aaa = int(a), int(aa), int(aaa)
if a % 2 == 0:
    print(a)
if aa % 2 == 0:
    print(aa)
if aaa % 2 == 0:
    print(aaa)

# 입력 값을 받아 정수로 변환
numbers = map(int, input("1 2 4 -- ").split())
for num in numbers:
    if num % 2 == 0:
        print(num)

# 6066 -- 3개의 정수(a b c)가 입력되었을 때, 짝(even)/홀(odd)을 출력
numbers = map(int, input("1 2 4 -- ").split())
for num in numbers:
    if num % 2 == 0:
        print("even")
    else:
        print("odd")

# 6067 -- 0이 아닌 정수 1개가 입력되었을 때, 음(-)/양(+)과 짝(even)/홀(odd)을 구분
b = int(input("2 -- "))
if b < 0:
    print("A" if (b % 2 == 0) else "B")
else:
    print("C" if (b % 2 == 0) else "D")

print("A" if b < 0 and b % 2 == 0 else "B" if b < 0 else "C" if b % 2 == 0 else "D")

# 6068 -- 점수(정수, 0 ~ 100)를 입력받아 평가를 출력
score = int(input("80 -- "))
if score >= 90:
    print("A")
elif score >= 70:
    print("B")
elif score >= 40:
    print("C")
else:
    print("D")
print("A" if score >= 90 else "B" if score >= 70 else "C" if score >= 40 else "D")

# 6069 -- 평가를 문자(A, B, C, D, ...)로 입력받아 내용을 다르게 출력
grade = input("A -- ")
print(
    "best!!!" if grade == "A" else "good!!" if grade == "B" else "run!" if grade == "C" else "slowly~" if grade == "D" else "what?")

# 6070 -- 월이 입력될 때 계절 이름이 출력
# // -- 나눗셈 몫
month = int(input("12 -- "))
print("spring" if month // 3 == 1 else "summer" if month // 3 == 2 else "fall" if month // 3 == 3 else "winter")




"""
반복실행구조
6071 ~ 6076
"""

# 6071 -- 0이 아니면 입력된 정수를 출력하고, 0이 입력되면 출력을 중단
n = 1
while n != 0:
    n = int(input("0 -- "))
    if n != 0:
        print(n)

# 6072 -- 정수(1 ~ 100) 1개가 입력되었을 때 카운트다운을 출력
countdown = int(input("3 -- "))
while countdown != 0:
    print(countdown)
    countdown -= 1

# 6073 -- 1만큼씩 줄이면서 카운트다운 수가 0이 될 때까지 한 줄에 1개씩 출력
countdown = int(input("3 -- "))
while countdown != 0:
    countdown -= 1
    print(countdown)

# 6074 -- a부터 입력한 영문소문자까지의 알파벳을 순서대로 출력
# ord() -- 단일 문자를 입력받아 해당 문자의 유니코드(또는 아스키) 값을 반환
# chr() -- 유니코드 값을 입력받아 해당 유니코드 값에 해당하는 문자를 반환
start = ord('a')
end = ord(input("d -- "))
while start <= end:
    print(chr(start), end=' ')
    start += 1
print()     # 엔터

# 6075 -- 정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력
d = int(input("3 -- "))
i = 0
while d >= i:
    print(i)
    i += 1

# range(3) 은 0, 1, 2 인 수열
# range(끝)
# range(시작, 끝)
# range(시작, 끝, 증감)
# 시작 수는 포함이고, 끝 수는 포함되지 않는다.
# 증감할 수를 작성하지 않으면 +1이 된다.
for j in range(d+1):
    print(j)