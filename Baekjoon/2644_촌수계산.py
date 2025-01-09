'''
부모와 자식 사이를 1촌으로 정의하고 이로부터 사람들 간의 촌수를 계산한다.
예를 들면 나와 아버지, 아버지와 할아버지는 각각 1촌으로
나와 할아버지는 2촌이 되고,
아버지 형제들과 할아버지는 1촌,
나와 아버지 형제들과는 3촌이 된다.
여러 사람들에 대한 부모 자식들 간의 관계가 주어졌을 때, 주어진 두 사람의 촌수를 계산하는 프로그램을 작성하시오.

사람들은 1, 2, 3, …, n (1 ≤ n ≤ 100)의 연속된 번호로 각각 표시된다.
입력 파일의 첫째 줄에는 전체 사람의 수 n이 주어지고,
둘째 줄에는 촌수를 계산해야 하는 서로 다른 두 사람의 번호가 주어진다.
그리고 셋째 줄에는 부모 자식들 간의 관계의 개수 m이 주어진다.
넷째 줄부터는 부모 자식간의 관계를 나타내는 두 번호 x,y가 각 줄에 나온다.
이때 앞에 나오는 번호 x는 뒤에 나오는 정수 y의 부모 번호를 나타낸다.
각 사람의 부모는 최대 한 명만 주어진다.

입력에서 요구한 두 사람의 촌수를 나타내는 정수를 출력한다.
어떤 경우에는 두 사람의 친척 관계가 전혀 없어 촌수를 계산할 수 없을 때가 있다. 이때에는 -1을 출력해야 한다.
'''

import sys
from collections import deque

sys.stdin = open("input.txt", "r")

N = int(input())                    # 전체 사람 수
A, B = map(int, input().split())    # 촌수 계산 필요한 가족 구성원 2
M = int(input())                    # 총 관계 수

adj = [[] for _ in range(N + 1)]    # 부모 자식 쌍
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    adj[x].append(y)

# 최단거리는 BFS
def BFS(a, b):
    queue = deque([a])  # 큐 선언 및 초기화
    v = []              # 방문처리 스택 선언

    while queue:
        now = queue.popleft()
        if now not in v:
            v.append(now)           # 방문하지 않은 노드이면 방문 처리
            if b in adj[now]:       # 해당 노드의 자식 중 b 가 있으면 촌수 반환
                return len(v)
            for i in range(1, N+1):
                if now in adj[i]:   # 현재 노드의 부모를 찾았으면 큐에 삽입
                    queue.append(i)

    return -1   # 연결된 가족이 없을 경우 -1 리턴

print(BFS(A, B)) # 틀렸음..........





'''
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6

# 3

9
8 6
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6

# -1
'''