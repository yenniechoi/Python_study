'''
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다.
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다.
컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때,
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

1. 컴퓨터의 수 (100 이하인 양의 정수)
- 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
2. 컴퓨터 쌍의 수
3. 한 줄에 한 쌍씩, 컴퓨터의 번호 쌍

1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.
'''

import sys
from collections import deque

sys.stdin = open("input.txt", "r")

# 개수만 알면 되니까 DFS! (최단거리는 BFS)
def DFS(c):
    # c 방문 처리
    v.append(c)

    # c와 연결된 노드 모두 처리
    for n in adj[c]:
        if n not in v:
            DFS(n)

# BFS 연습
def BFS(c):
    queue = deque([c])

    # queue 가 빌 때까지 진행
    while queue:
        n = queue.popleft() # 최하단 노드 뽑아서
        if n not in v:
            v.append(n) # 방문하지 않은 노드일 경우 방문 처리
            for a in adj[n]:    # 해당 노드와 연결된 노드 모두 방문
                if a not in v:
                    queue.append(a) # 방문하지 않은 노드일 경우 queue 삽입

N = int(input())    # 컴퓨터 수
P = int(input())    # 컴퓨터 쌍의 수

adj = [[] for _ in range(N+1)]
for _ in range(P):
    a, b = map(int, sys.stdin.readline().split())
    # 컴퓨터 쌍 양방 처리
    adj[a].append(b)
    adj[b].append(a)

v = []  # 방문 노드 저장 리스트
DFS(1)  # 1번 컴퓨터부터 시작

# 1번 컴퓨터를 뺀 방문한 컴퓨러의 수
print(len(v) - 1)




'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
# 4
'''