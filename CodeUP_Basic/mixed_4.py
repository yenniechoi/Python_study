"""
종합(4) -- 수열, 최소공배수
6088 ~ 6091
"""

# 6088 -- 등차수열
# 시작 값(a), 등차의 값(d), 몇 번째 수 인지를 의미하는 정수(n)
a, d, n = map(int, input("1 3 5 -- ").split())
for i in range(n-1):
    a += d
print(a)
# result = a + (n - 1) * d


# 6089 -- 등비수열
# 시작 값(a), 등비(r), 몇 번째인지를 나타내는 정수(n)
a, r, n = map(int, input("2 3 7 -- ").split())
for i in range(n-1):
    a *= r
print(a)
# result = a * (r ** (n - 1))


# 6090 -- 1부터 시작해 이전에 만든 수에 -2를 곱한 다음 1을 더해 다음 수를 만든 수열
# 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째인지를 나타내는 정수(n)
a, m, d, n = map(int, input("1 -2 1 8 -- ").split())
# 변수 i를 사용하지 않기 때문에 _를 사용하여 반복 횟수만 제어
for _ in range(n-1):
    a = a * m + d
print(a)


# 6091 -- 3명이 다시 모두 함께 방문해 문제를 풀어보는 날(동시 가입/등업 후 며칠 후?)
a, b, c = map(int, input("3 7 9 -- ").split())
day = 0
while True:
    day += 1
    if day % a == 0 and day % b == 0 and day % c == 0:
        print(day)
        break

"""
d = 1
while d%a!=0 or d%b!=0 or d%c!=0 :
  d += 1
print(d)
"""

"""
# 두 수의 최소 공배수를 구하는 함수
## // -- 나눗셈 몫
## math.gcd(x, y) -- 두 수의 최대 공약수(GCD)를 구하는 함수
## 최소 공배수는 두 수의 곱을 최대 공약수로 나눈 값
def lcm(x, y):
    return x * y // math.gcd(x, y)

a, b, c = map(int, input("3 7 9 -- ").split())

# 세 수의 최소 공배수를 구함
result = lcm(lcm(a, b), c)
"""
