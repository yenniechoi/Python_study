"""
종합 (1)
6077 ~ 6080
"""

# 6077 -- 정수(1 ~ 100) 1개를 입력받아 1부터 그 수까지 짝수의 합
a = int(input("5 -- "))
n = 0
while n <= a:
    n += 2
print(n)

n = 0
for i in range(1, a + 1):
    if i % 2 == 0:
        n += i
print(n)

# 6078 -- 영문 소문자 'q'가 입력될 때까지 입력한 문자를 계속 출력
while True:
    a = input("q -- ")
    if a != "q":
        print(a)
    else:
        print(a)
        break
# 할당 표현식 (:=) -- input("q -- ")의 결과를 a에 할당하고, 그 값을 반환
while (a := input("q -- ")) != "q":
    print(a)
print(a)


# 6079 -- 1, 2, 3, 4, 5 ... 를 순서대로 계속 더해 합을 만들어가다가,
# 입력된 정수와 같거나 커졌을 때, 마지막에 더한 정수를 출력
a = int(input("55 -- "))
n = 0
for i in range(1, a + 1):
    n += i
    if n >= a:
        print(i)
        break

n, i = 0, 0
while n < a:
    i += 1
    n += i
print(i)



# 6080 -- 서로 다른 주사위 2개를 던졌을 때, 나올 수 있는 모든 경우를 출력
# 서로 다른 주사위 2개의 면의 개수
a, b = input("2 3 -- ").split()
a, b = int(a), int(b)
for i in range(1, a + 1):
    for j in range(1, b + 1):
        print(f"{i} {j}")

a, b = map(int, input("2 3 -- ").split())
# 리스트 내포(List Comprehension) -- [expression for item in iterable if condition]
print('\n'.join(f"{i} {j}" for i in range(1, a + 1) for j in range(1, b + 1)))


