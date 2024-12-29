'''
DFS & BFS 알고리즘
: 스택, 큐 알고리즘 사용하여 선택지 탐색

1) 음료수 얼려 먹기
2) 미로 탈출
'''


from collections import deque



# 1) ================================================================================
# 얼음틀 N X M
# 구멍 뚫린 부분 0, 막힌 부분 1
# 구멍 뚫린 부분끼리 붙어 있는 경우 서로 연결되어 있는 것으로 간주
# 한 번에 만들 수 있는 아이스크림 개수 출력

def DFS_frozen_icecream():
    # 그래프 크기 입력받기
    n, m = map(int, input().split())
    # 2차원 리스트의 맵 정보 입력받기
    graph = [list(map(int, input())) for _ in range(n)]

    # DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
    def dfs(x, y):
        # 주어진 범위를 벗어나는 경우 즉시 종료
        if x <= -1 or x >= n or y <= -1 or y >= m:
            return False

        # 현재 노드를 아직 방문하지 않았다면
        if graph[x][y] == 0:
            # 현재 노드 방문 처리
            graph[x][y] = 1

            # 인접 노드 방문 처리
            dfs(x+1, y)
            dfs(x, y+1)
            dfs(x-1, y)
            dfs(x, y+1)
            return True

        return False

    # 모든 노드에 대하여 음료수 채우기
    icecream = 0
    for i in range(n):
        for j in range(m):
            # 현재 위치에서 DFS 수행
            if dfs(i, j) == True:
                icecream += 1

    return icecream


def BFS_frozen_icecream():
    # 그래프 크기 입력받기
    n, m = map(int, input().split())
    # 2차원 리스트의 맵 정보 입력받기
    graph = [list(map(int, input())) for _ in range(n)]

    # BFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
    def bfs(x, y):
        # BFS를 위한 큐 생성
        queue = deque()
        queue.append((x, y))

        # 현재 노드 방문 처리
        graph[x][y] = 1

        # 이동할 네 방향 정의 (상, 하, 좌, 우)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            curr_x, curr_y = queue.popleft()
            # 현재 위치에서 네 방향으로 이동
            for dx, dy in directions:
                next_x, next_y = curr_x + dx, curr_y + dy
                # 주어진 범위를 벗어나지 않고, 방문하지 않은 노드라면
                if 0 <= next_x < n and 0 <= next_y < m and graph[next_x][next_y] == 0:
                    graph[next_x][next_y] = 1  # 방문 처리
                    queue.append((next_x, next_y))

    # 모든 노드에 대하여 음료수 채우기
    icecream = 0
    for i in range(n):
        for j in range(m):
            # 현재 위치에서 BFS 수행
            if graph[i][j] == 0:
                bfs(i, j)
                icecream += 1

    return icecream


'''
4 5
00110
00011
11111
00000
'''
# print(DFS_frozen_icecream())
print(BFS_frozen_icecream())



# 2) ================================================================================



