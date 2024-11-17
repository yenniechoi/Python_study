'''
리스트(배열), 문자열
# 71) 조건에 맞게 수열 변환하기 1
# 72) 조건에 맞게 수열 변환하기 2
# 73) 1로 만들기
# 74) 길이에 따른 연산
# 75) 원하는 문자열 찾기
'''

# 71) ==========================================================================
# 50보다 크거나 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면 2를 곱합니다.

def compare_50(arr):
    for i, n in enumerate(arr):
        if n >= 50 and n % 2 == 0:
            arr[i] = int(n/2)
        elif n < 50 and n % 2 != 0:
            arr[i] = n * 2
    return arr

'''
n % 2 == 0
(=) not n % 2

0 == False
'''


print(compare_50([1, 2, 3, 100, 99, 98]))   # [2, 2, 6, 50, 99, 49]


# 72) ==========================================================================
# 값이 50보다 크거나 같은 짝수라면 2로 나누고, 50보다 작은 홀수라면 2를 곱하고 다시 1을 더합니다.
# arr(x) = arr(x + 1)인 x 중 가장 작은 값 반환

def compare_50_x(arr):
    # debugging & tracking states

    all_result = [arr[:]]
    i = 0
    while True:
        for j, n in enumerate(arr):
            if n >= 50 and not n % 2:
                arr[j] = n // 2
            elif n < 50 and n % 2:
                arr[j] = n * 2 + 1
        all_result.append(arr[:])

        if all_result[i] == all_result[i + 1]:
            break
        else:
            i += 1
    return i

'''
# efficiency & simplicity

answer = 0
old = arr
while True:
    new = []
    for i in old:
        if i >= 50 and i % 2 == 0:
            i = i / 2
        elif i < 50 and i % 2 == 1:
            i = i * 2 + 1
        new.append(int(i))
    if old == new:
        break
    else:
        old = new
        answer += 1
return answer
'''

print(compare_50_x([1, 2, 3, 100, 99, 98]))     # 5


# 73) ==========================================================================
# 짝수라면 반으로 나누고, 홀수라면 1을 뺀 뒤 반으로 나누면, 마지막엔 1이 됩니다.
# num_list의 모든 원소를 1로 만들기 위해서 필요한 나누기 연산의 횟수 총합 리턴.

def count_for_one(num_list):
    answer = 0
    for n in num_list:
        count = 0
        while n != 1:
            if n % 2 == 0:
                n = n // 2
                count += 1
            else:
                n = (n - 1) // 2
                count += 1
        answer += count

    return answer

'''
# 바이트 연산
return sum(len(bin(i)) - 3 for i in num_list)

# 홀수일 때 1을 빼고 2로 나눈다는 것 = 몫을 구하겠다는 것
for n in num_list:
    while n != 1:
        n //= 2
        answer += 1
'''
'''
JS
return num_list.map(v => v.toString(2).length - 1).reduce((a, c) => a + c);

Java
return Arrays.stream(num_list).map(i -> Integer.toBinaryString(i).length() - 1).sum();
'''


print(count_for_one([12, 4, 15, 1, 14]))    # 11


# 74) ==========================================================================
# 리스트의 길이가 11 이상이면 리스트에 있는 모든 원소의 합을, 10 이하이면 모든 원소의 곱을 return

def if_list_11(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        mul = 1
        for n in num_list:
            mul *= n
        return mul

'''
return eval('*'.join(map(str, num_list)))

from functools import reduce
return reduce(lambda x, y: x * y, num_list)

from math import prod
def solution(num_list):
    return sum(num_list) if len(num_list)>=11 else prod(num_list)
'''
'''
JS
const solution = n => n.reduce((a, v) => n.length > 10 ? a + v : a * v)

const mult = (acc, v) => acc * v;
const add = (acc, v) => acc + v;
return num_list.length > 10
    ? num_list.reduce(add, 0)
    : num_list.reduce(mult, 1);
'''

print(if_list_11([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]))  # 51
print(if_list_11([2, 3, 4, 5]))          # 120


# 75) ==========================================================================
# myString의 연속된 부분 문자열 중 pat이 존재하면 1을 그렇지 않으면 0

def is_there_pat(myString, pat):
    return int(pat.lower() in myString.lower())


'''
JS
return +(myString.toUpperCase().includes(pat.toUpperCase()));
'''

print(is_there_pat("AbCdEfG", "aBc"))   # 1
print(is_there_pat("aaAA", "aaaaa"))    # 0

