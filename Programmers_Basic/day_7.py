'''
31) 수열과 구간 쿼리 4
32) 배열 만들기 2
33) 카운트 업
34) 콜라츠 수열 만들기
35) 배열 만들기 4
'''


# 31)
def sequence_4(arr, queries):
    for s, e, k in queries:
        '''
        if k == 0:
            continue
        '''
        for i in range(s, e + 1):
            if i % k == 0:
                arr[i] += 1

    return arr


# [3, 2, 4, 6, 4]
print(sequence_4([0, 1, 2, 4, 3], [[0, 4, 1], [0, 3, 2], [0, 3, 3]]))


# 32)
# l 이상 r이하의 정수 중에서 (1 ≤ l ≤ r ≤ 1,000,000)
# 숫자 "0"과 "5"로만 이루어진 모든 정수를
# 오름차순으로 저장한 배열
def make_array(l, r):
    # BFS/queue-based generation approach
    answer = []
    queue = ["5"]

    while queue:
        current = queue.pop(0)
        num = int(current)

        if l <= num <= r:
            answer.append(num)

        num1 = current + "0"
        num2 = current + "5"

        if int(num1) <= r:
            queue.append(num1)
        if int(num2) <= r:
            queue.append(num2)

    return answer if answer else [-1]

'''
# the iterative check approach
answer = []
for num in range(l, r + 1):
    if not set(str(num)) - set(['0', '5']):
        answer.append(num)
return answer if answer else [-1]


ret = []
def f(lim, val):
    if lim == 0:
        ret.append(val)
        return
    f(lim - 1, val * 10 + 5)
    f(lim - 1, val * 10)
f(6, 0)
return list(i for i in ret if l <= i <= r)[::-1] or [-1]
'''

print(make_array(5, 555))  # [5, 50, 55, 500, 505, 550, 555]
print(make_array(10, 20))  # [-1]


# 33)
def count_up(start_num, end_num):
    return list(num for num in range(start_num, end_num + 1))

'''
return list(range(start, end + 1))
'''

# [3, 4, 5, 6, 7, 8, 9, 10]
print(count_up(3, 10))


# 34)
# x가 짝수일 때는 2로 나누고, x가 홀수일 때는 3 * x + 1
# 계속해서 반복하면 언젠가는 반드시 x가 1이 되는지 묻는 문제 = 콜라츠 문제
# 위 과정에서 거쳐간 모든 수를 기록한 수열을 콜라츠 수열
def collatz_conjecture(n):
    answer = []
    while n != 1:
        answer.append(int(n))
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
    answer.append(int(n))
    return answer


# [10, 5, 16, 8, 4, 2, 1]
print(collatz_conjecture(10))


# 35)
# stk가 빈 배열이라면 arr[i]를 stk에 추가하고 i에 1을 더합니다
# stk의 마지막 원소가 arr[i]보다 작으면 arr[i]를 stk의 뒤에 추가하고 i에 1을 더합니다.
# stk의 마지막 원소가 arr[i]보다 크거나 같으면 stk의 마지막 원소를 stk에서 제거

def make_arr_stk(arr):
    stk = []
    i = 0
    while i < len(arr):
        if not stk:
            stk.append(arr[i])
            i += 1
            continue

        if stk[-1] >= arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])
            i += 1

    return stk

'''
# runtime error
# in Python, the value of i is automatically managed by the loop itself.
# Because the manual incrementing of i is not properly managed
stk = []
    for i in range(len(arr)):
        if not stk:
            stk.append(arr[i])
            i += 1

        if stk[-1] >= arr[i]:
            stk.pop()

        if stk[-1] < arr[i]:
            stk.append(arr[i])
            i += 1

    return stk
'''
'''
stk = []
for i in range(len(arr)):
    while stk and stk[-1] >= arr[i]:
        stk.pop()
    stk.append(arr[i])
return stk
'''

# [1, 2, 3]
print(make_arr_stk([1, 4, 2, 5, 3]))





