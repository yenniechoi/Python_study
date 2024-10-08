'''
21) 코드 처리하기
22) 등차수열의 특정한 항만 더하기
23) 주사위 게임 2
24) 원소들의 곱과 합
25) 이어 붙인 수
'''



# 21)
# mode == 0 -> idx가 짝수일 때만 ret
# mode == 1 -> idx가 홀수일 때만 ret
# code[idx]가 "1"이면 mode 바꿈 (0->1 or 1->0)
# 시작할 때 mode는 0이며,
# return 하려는 ret가 만약 빈 문자열이라면 대신 "EMPTY"를 return
def turn_mode(code):
    ret = ''
    mode = 0
    for idx in range(len(code)):
        if code[idx] == '1':
            mode = 1 - mode
            continue

        if idx % 2 == mode:
            ret += code[idx]

    return ret if ret else "EMPTY"

'''
# default start(0), default end(len), step size of 2
return "".join(code.split("1"))[::2] or "EMPTY"

# xor 연산. 서로 같으면 0, 다르면 1
mode ^= 1
'''
print(turn_mode("abc1abc1abc"))     # acbac


# 22)
def arithmetic_sequence(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i]:
            answer += a + (d * i)
    return answer

'''
return sum(a + i * d for i, f in enumerate(included) if f)
'''
# 37
print(arithmetic_sequence(3, 4, [True, False, False, True, True]))


# 23)
def three_dices(a, b, c):
    one = a + b + c
    two = pow(a, 2) + pow(b, 2) + pow(c, 2)
    three = pow(a, 3) + pow(b, 3) + pow(c, 3)

    if a == b == c:
        return one * two * three
    elif a != b and a != c and b != c:
        return one
    else:
        return one * two

'''
# set(list) - 중복 요소 제거
check=len(set([a,b,c]))
    if check==1:
        return 3*a*3*(a**2)*3*(a**3)
    elif check==2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return (a+b+c)

unique_count = len(set([a, b, c]))
for i in range(4 - unique_count):
    answer *= (a ** (i + 1) + b ** (i + 1) + c ** (i + 1))
'''

print(three_dices(2, 6, 1))     # 9
#print(three_dices(5, 3, 3))
#print(three_dices(4, 4, 4))


# 24)
import math
def multiply_plus(num_list):
    return int(math.prod(num_list) < sum(num_list) ** 2)

'''
def compare_product_sum(num_list):
    product = 1
    total_sum = 0

    for num in num_list:
        product *= num
        total_sum += num

    return int(product < total_sum ** 2)
'''

print(multiply_plus([3, 4, 5, 2, 1]))       # 1


# 25)
# 홀수만 이어붙임 + 짝수만 이어붙임
def concatenate_num(num_list):
    odd, even = '', ''
    for num in num_list:
        if num % 2 == 0:
            even += str(num)
        else:
            odd += str(num)
    return int(even) + int(odd)

print(concatenate_num([5, 7, 8, 3]))        # 581
