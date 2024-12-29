'''
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
더 이상 방문할 수 있는 점이 없는 경우 종료한다.
정점 번호는 1번부터 N번까지이다.

# 입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력
첫째 줄에 DFS를 수행한 결과를,
그 다음 줄에는 BFS를 수행한 결과를 출력한다.
V부터 방문된 점을 순서대로 출력하면 된다.
'''



from sys import stdin as s
from collections import deque

# 정점의 개수, 간선의 개수, 시작 정점 입력받기
n, m, v = map(int, s.readline().split())

# 그래프 생성
graph = [[] for _ in range(n + 1)]  # 1부터 n까지의 정점 초기화
for _ in range(1, m + 1):
    a, b = map(int, s.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 그래프 오름차순 정렬
for nodes in graph:
    nodes.sort()

def DFS(v):
    visited_dfs.append(v)   # 현재 정점 방문 처리

    # 현재 정점과 연결된 정점 정렬 후 방문
    for node in graph[v]:
        if node not in visited_dfs:
            DFS(node)


def BFS(v):
    queue = deque()
    queue.append(v)

    visited_bfs.append(v)   # 현재 정점 방문 처리

    # queue 가 다 빌 때까지 그래프 방문
    while queue:
        q = queue.popleft()     # 최하단 노드 뽑기

        for node in graph[q]:
            if node not in visited_bfs:
                visited_bfs.append(node)    # 방문처리
                queue.append(node)      # 큐에 미방문 노드 넣기


# 방문할 정점을 기록할 리스트
visited_dfs = []
DFS(v)
print(*visited_dfs)

visited_bfs = []
BFS(v)
print(*visited_bfs)



'''
예제 1

4 5 1
1 2
1 3
1 4
2 4
3 4

1 2 4 3
1 2 3 4
'''

'''
예제 2

5 5 3
5 4
5 2
1 2
3 4
3 1

3 1 2 5 4
3 1 4 2 5
'''

'''
예제 3

1000 1 1000
999 1000

1000 999
1000 999
'''