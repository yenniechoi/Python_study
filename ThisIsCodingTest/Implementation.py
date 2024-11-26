'''
구현 알고리즘
: 풀이를 떠올리는 것은 쉽지만 소스 코드로 옮기기 어려운 문제.
: 프로그래밍 문법 정확히 숙지 + 라이브러리 사용 경험 풍부

# 1 ) 상하좌우
# 2 ) 시각
# 3 ) 왕실의 나이트
# 4 ) 게임 개발
'''

# 1 ) ================================================================
# N x N 크기의 정사각형 공간에서 입력 방향대로 움직임
def up_down_left_right():
    position = [1, 1]

    N = int(input("5 -- "))
    direction = list(input("R R R U D D -- ").split())

    for d in direction:
        if d == 'L':
            if position[1] > 1:
                position[1] -= 1
        elif d == 'R':
            if position[1] < N:
                position[1] += 1
        elif d == 'U':
            if position[0] > 1:
                position[0] -= 1
        elif d == 'D':
            if position[0] < N:
                position[0] += 1

    return position

print(*up_down_left_right())

'''
# N을 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D 에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            
    # 공간을 벗어나는 경우 무시
    if nx < 1 of ny < 1 or nx > n or ny > n:
        continue
    
    # 이동 수행
    x, y = nx, ny

print(x, y)
        
'''

# 2 ) ================================================================




# 3 ) ================================================================




# 4 ) ================================================================



