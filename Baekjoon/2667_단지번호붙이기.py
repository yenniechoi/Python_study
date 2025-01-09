'''
정사각형 모양의 지도가 있다.
1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다.
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다.
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다.
대각선상에 집이 있는 경우는 연결된 것이 아니다.
지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고,
그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

첫 번째 줄에는 총 단지수를 출력하시오.
그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.
'''

import sys
from collections import deque

sys.stdin = open("input.txt", "r")

# DFS 로 풀어도 됨! 다만, 맵이 커질 수록 반복 횟수가 커져서
# BFS 는 코드는 다소 길지만 효율적이어서 추천
def BFS(x, y):
    queue = deque([(x, y)]) # 큐 선언 및 초기데이터 삽입
    v[x][y] = 1             # 방문처리
    cnt = 1                 # 정답처리 관련 작업 -> 집 카운트

    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 4 방향 선언
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in d:
            nx, ny = cx + dx, cy + dy
            # 4 방향, 범위 내, 미방문, 1이면 큐 삽입
            if 0 <= nx < N and 0 <= ny < N and v[nx][ny] == 0 and adj[nx][ny] == 1:
                queue.append((nx, ny))  # 방문할 수 있는 집을 queue 에 넣기
                v[nx][ny] = 1           # 방문처리
                cnt += 1                # 단지 수 카운트
    return cnt

# 지도의 크기, 지도 정보 입력 받기
N = int(sys.stdin.readline())
adj = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

# 방문 여부 리스트, 카운트 담을 정답 리스트 초기화
v = [[0] * N for _ in range(N)]
ans = []

# 지도에서 집 탐방
for i in range(N):
    for j in range(N):
        # 집이 있고 방문하지 않았으면 BFS 시작
        if adj[i][j] == 1 and v[i][j] == 0:
            ans.append(BFS(i, j))

# 오름차순 정렬
ans.sort()

# 총 단지 수, 각 단지내 집의 수 출력
print(len(ans), *ans, sep="\n")


'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000

#
3
7
8
9
'''