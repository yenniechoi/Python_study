'''
16) n 의 배수
17) 공배수
18) 홀짝에 따라 다른 값 반환하기
19) 조건 문자열
20) flag에 따라 다른 값 반환하기
'''


# 16)
def multiple(num, n):
    return 1 if num % n == 0 else 0

'''
# True is converted to 1 and False is converted to 0 
# when passed to int().
return int(num % n == 0)
'''
print(multiple(98, 2))


# 17)
def common_multiple(number, n, m):
    return int(number % n == 0 and number % m == 0)
print(common_multiple(60, 2, 3))


# 18)
# n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합
# n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합
def odd_even(n):
    answer = 0
    flag = int(n % 2 == 0)

    for i in range(flag + 1, n + 1, 2):
        if flag:
            answer += i * i
        else:
            answer += i
    return answer

'''
return sum(x ** (2 - x % 2) for x in range(n + 1) if n % 2 == x % 2)

if n%2:
        return sum(range(1,n+1,2))
    return sum([i*i for i in range(2,n+1,2)])
'''
print(odd_even(7))


# 19)
def ineq_eq(ineq, eq, n, m):
    eq = eq if eq == "=" else ""
    return int(eval(f"{n} {ineq}{eq} {m}"))
'''
eq.replace('!', '')
'''
print(ineq_eq(">", "!", 41, 78))


# 20)
def flag_value(a, b, flag):
    return a + b if flag else a - b

print(flag_value(-4, 7, True))