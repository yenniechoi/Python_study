"""
리스트
6092 ~ 6095
"""
# d = [] -- 어떤 데이터 목록(list) 을 순서대로 저장하기 위해 아무것도 없는 리스트 변수 만들기
# d.append(값) -- d 리스트의 마지막에 원하는 값을 추가(append)해 넣음
# d[a[i]] += 1 -- 2중 리스트 참조 : 만약 a[i]의 값이 1이었다면? d[1] += 1 이 실행되는 것이다. 1번 카운트 1개 증가..

# 6092 -- n번 무작위로 불렀을 때, 각 번호(1 ~ 23)가 불린 횟수를 각각 출력
n = int(input("10 -- "))
l = list(map(int, input("1 3 2 2 5 6 7 4 5 9 -- ").split()))

result = []
for _ in range(24):
    result.append(0)
for i in range(n):
    result[l[i]] += 1
for i in range(1, 24):
    print(result[i], end=' ')
print()

# 간단한 버전
result = [0] * 24
for num in l:
    result[num] += 1
print(' '.join(map(str, result[1:])))


# 6093 -- 출석 번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력
n = int(input("10 -- "))
k = list(map(int, input("10 4 2 3 6 6 7 9 8 5 -- ").split()))
for i in range(n-1, -1, -1):
    print(k[i], end=' ')
print()
# 역순으로 슬라이싱
print(' '.join(map(str, k[::-1])))


# 6094 -- n번 무작위로 불렀을 때, 가장 빠른 번호를 출력
n = int(input("10 -- "))
k = list(map(int, input("10 4 2 3 6 6 7 9 8 5 -- ").split()))
print(min(k))


# 6095 -- 바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때, n개의 흰 돌이 놓인 위치를 출력
d = [[0] * 20 for _ in range(20)]
n = int(input("5 -- "))     # 바둑돌 개수
for _ in range(n):
    x, y = map(int, input().split())    # 바둑돌 위치 입력
    d[x][y] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=' ')     # 수열 형태로 출력
    print()
print()
# 리스트 내포와 join을 사용해 출력
print('\n'.join(' '.join(map(str, d[i][1:20])) for i in range(1, 20)))

