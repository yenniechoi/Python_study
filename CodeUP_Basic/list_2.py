"""
리스트
6096 ~
"""

# 6096 -- 바둑알 십(+)자 뒤집기
# 모든 가로줄 반대로 (1->0 / 0->1) ----> 그 다음 모든 세로줄 돌 반대로
# 고른 위치를 제외한 가로줄과 세로줄의 색이 모두 반대로 바뀜

# 바둑알이 깔려 있는 상황이 19 * 19 크기의 정수값으로 입력된다.
# 십자 뒤집기 횟수(n)가 입력된다.
# 십자 뒤집기 좌표가 횟수(n) 만큼 입력된다. 단, n은 10이하의 자연수이다.

# '''
d = [list(map(int, input().split())) for _ in range(19)]
n = int(input("2"))
for _ in range(n):
    x, y = map(int, input().split())

    # 좌표 (1,1) 은 배열 인덱스로 (0,0)
    x -= 1
    y -= 1

    for i in range(19):
        if i != x:
            d[i][y] = int(not d[i][y])
        if i != y:
            d[x][i] = int(not d[x][i])

for row in d:
    print(' '.join(map(str, row)))
# '''

# 6097 -- 설탕과자 뽑기

# 첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
# 두 번째 줄에 놓을 수 있는 막대의 개수(n)
# 세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.
# 1 <= w, h <= 100
# 1 <= n <= 10
# d = 0 or 1 (가로 or 세로)
# 1 <= x <= 100-h
# 1 <= y <= 100-w

# 모든 막대를 놓은 격자판의 상태를 출력한다.
# 막대에 의해 가려진 경우 1, 아닌 경우 0으로 출력

h, w = map(int, input().split())
# grid = [[0] * h for _ in range(w)]
grid = [[0] * w for _ in range(h)]
n = int(input())
for _ in range(n):
    # x 가 세로, y 가 가로 ...
    l, d, x, y = map(int, input().split())

    x -= 1
    y -= 1

    for i in range(l):
        # 가로 방향으로 값을 변경할거니까.. y 값이 바뀌어야 함..
        if d == 0 and y + i < w:
            grid[x][y + i] = 1

        elif d == 1 and x + i < h:
            grid[x + i][y] = 1

for row in grid:
    print(' '.join(map(str, row)))


