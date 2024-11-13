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



print()


# 74) ==========================================================================



print()


# 75) ==========================================================================



print()

