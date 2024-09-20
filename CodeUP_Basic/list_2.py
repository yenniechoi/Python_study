"""
리스트
6096 ~ 6098
"""

# 6096 -- 바둑알 십(+)자 뒤집기
# 모든 가로줄 반대로 (1->0 / 0->1) ----> 그 다음 모든 세로줄 돌 반대로
# 고른 위치를 제외한 가로줄과 세로줄의 색이 모두 반대로 바뀜

# 바둑알이 깔려 있는 상황이 19 * 19 크기의 정수값으로 입력된다.
# 십자 뒤집기 횟수(n)가 입력된다.
# 십자 뒤집기 좌표가 횟수(n) 만큼 입력된다. 단, n은 10이하의 자연수이다.


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



# 6098 -- 성실한 개미 미로찾기
# 0(갈 수 있는 곳), 1(벽 또는 장애물), 2(먹이)
# 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직여 가장 빠른 길로 움직
# 단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는
# 더이상 이동하지 않고 그 곳에 머무른다.
# 개미는 (2, 2)에서 출발
# 10*10 크기의 미로 상자의 구조와 먹이의 위치가 입력된다.
# 개미가 이동한 경로를 9로 표시해 출력

miro = [list(map(int, input().split())) for _ in range(10)]

x, y = 1, 1
miro[x][y] = 9

while True:
    # 먹이를 찾으면 가만히 있는다.
    if miro[x][y] == 2:
        miro[x][y] = 9
        break

    # 오른쪽이 0이면 오른쪽으로 간다.
    elif miro[x][y + 1] == 0:
        y += 1
        miro[x][y] = 9

    # 오른쪽이 2이면 오른쪽으로 가서 끝낸다.
    elif miro[x][y + 1] == 2:
        y += 1
        miro[x][y] = 9
        break

    # 오른쪽이 1인데, 아래가 0이면 아래로 간다.
    elif miro[x+1][y] == 0:
        x += 1
        miro[x][y] = 9

    # 오른쪽이 1인데, 아래가 2이면 아래로 가서 끝낸다.
    elif miro[x + 1][y] == 2:
        x += 1
        miro[x][y] = 9
        break

    else:
        break

for row in miro:
    print(' '.join(map(str, row)))


'''
while True:
    # Check for food (2), stop if found
    if miro[x][y] == 2:
        miro[x][y] = 9
        break
    
    # Move right if possible
    if miro[x][y+1] != 1:
        y += 1
    # Otherwise, move down if possible
    elif miro[x+1][y] != 1:
        x += 1
    else:  # If stuck, stop
        break
    
    # Mark the new position
    miro[x][y] = 9
'''


