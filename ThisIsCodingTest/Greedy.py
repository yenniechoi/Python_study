'''
그리디 알고리즘
: 현재 상황에서 가장 좋은 것만 고르는 방법

# 1) 큰 수의 법칙
# 2) 숫자 카드 게임
# 3) 1이 될 때까지
'''

# 1)============================================================
# 배열의 수들을 M번 더하여 가장 큰 수를 만드는 법칙.
# 단, 특정 인덱스에 해당하는 수가 연속해서 K번 초과하여 더해질 수는 없음.
# 인덱스가 다른데 값이 같을 경우 서로 다른 값으로 간주함.
# N: 배열 크기, M: 숫자 더하는 횟수, K: 연속해서 더할 수 있는 횟수

def make_big_num():
    # N, M, K 공백으로 구분하여 입력 받기
    n, m, k = map(int, input().split())

    # N개의 자연수 공백으로 구분하여 입력 받기
    data = list(map(int, input().split()))

    max_value = max(data)   # 가장 큰 수
    data.remove(max_value)
    next_max = max(data)    # 두 번째로 큰 수

    result = 0
    cnt = k
    # 가장 큰 수를 더하는데, 연속해서 K번 더할 수는 없음
    for i in range(m):
        if cnt == 0:
            # 두 번째로 큰 수를 한 번 더하기
            result += next_max
            cnt = k
        else :
            # 가장 큰 수를 k번 더하기
            result += max_value
            # 더할 때마다 1씩 빼기
            cnt -= 1

    return result

# print(make_big_num())

'''
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()     # 입력받은 수들 정렬하기
first = data[n - 1]
second = data[n - 2]

# [1] 단순하게 푸는 방법

result = 0
while True:
    for i in range(k):  # 가장 큰 수 k번 더하기
        if m == 0:
            break
        result += first
        m -= 1  
    if m == 0:
        break 
    result += second
    m -= 1


# [2] 수학 공식 이용

# 가장 큰 수가 더해지는 횟수 계산
count = int(m/(k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first   # 가장 큰 수 더하기
result += (m-count) * second    # 두 번째로 큰 수 더하기

print(result)

'''

# 2)============================================================
# 여러 개의 숫자 카드 중 가장 높은 숫자가 쓰인 카드 한장을 뽑는 게임
# 행을 선택 -> 가장 숫자가 작은 카드 뽑음
# 행마다 가장 작은 숫자를 뽑지만, 최종적으로는 가장 높은 숫자를 뽑아야 한다.
# 즉, 각 행의 가장 작은 숫자들 중 가장 큰 수를 찾아야 한다.

def number_card_game():
    # n: 행, m: 열
    n, m = map(int, input().split())
    num = []

    # 한 줄 씩 입력을 받고, 거기서 가장 작을 수를 뽑는다.
    for _ in range(n):
        num.append(min(map(int, input().split())))

    # 가장 작은 수들 중에서 가장 큰 수를 리턴.
    # 이렇게 결과물을 모두 담고 한번에 계산할 경우, 메모리를 필요 이상으로 쓰게 된다.
    return max(num)

# print(number_card_game())

'''
## min() 함수 이용

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
    # 이렇게 하면 숫자를 전부 담지 않고 그때그때 값을 비교하므로 메모리 사용이 덜할 것 같다.
'''
'''
## 2중 반복문 구조 이용  

result = 0
for i in range(n):
    data = list(map(int, input().split()))

    # 각 숫자는 1 이상 10,000 이하의 자연수 
    # => 나올 수 없는 가장 큰 수(10001)를 설정하여 무조건 첫 비교 시 min_value 에 값 할당하도록 함.
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)

    result = max(result, min_value)
'''

# 3)============================================================
# N이 1이 될 떄까지 1 혹은 2 과정을 수행해야 하는 횟수의 최솟값
# 1) N-1
# 2) N/K -- N이 K로 나누어떨어질 떄에만 선택 가능

def until_one():
    n, k = map(int, input("25 5 --").split())
    cnt = 0
    while n != 1:
        if n % k == 0:
            n /= k
        else:
            n -= 1
        cnt += 1
    return cnt

print(until_one())

'''
# K로 가능한 한 많이 나눴을 때 가장 빠르게 N=1 만들 수 있다.
# N이 K의 배수가 되도록 효율적으로 한 번에 빼는 방식

# N, K를 공백으로 구분하여 입력받기
n, k = map(int, input("25 5 --").split())
result = 0

while True:
    # (N == K 로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k   # 25    # 5     # 0
    result += (n - target)  # 0     # 1+0   # 2+1
    n = target              # 25    # 5     # 0
    
    # N이 K보다 작을 때 (더이상 나눌 수 없을 때) 반복문 탈출
    if n < k:       # 25<5  # 5<5   # 0<5
        break       # result 가 3이 될 때 탈출
    
    # K로 나누기
    result += 1     # 1     # 2
    n //= k         # 5     # 1

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)   # 3-1
print(result)       # 2
'''