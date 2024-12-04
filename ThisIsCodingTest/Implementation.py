'''
구현 알고리즘
: 풀이를 떠올리는 것은 쉽지만 소스 코드로 옮기기 어려운 문제.
: 프로그래밍 문법 정확히 숙지 + 라이브러리 사용 경험 풍부

# 1 ) 상하좌우
# 2 ) 시각
# 3 ) 왕실의 나이트
# 4 ) 게임 개발     # Level.2 문제라 많이 헤매고 결국 답지 봄. 꼭 나중에 다시 풀 것.
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

# print(*up_down_left_right())

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
# 정수 N이 입력되면
# 00시 00분 00초 부터 N시 59분 59초까지의 모든 시각 중에서
# 3이 하나라도 포함되는 모든 경우의 수를 구하라
# hour : 00 ~ N
# minute : 00 ~ 59
# second : 00 ~ 59

def case_include_3():
    cnt = 0
    num = input("5 -- ")

    for h in range(int(num)+1):
        for m in range(60):
            for s in range(60):
                # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
                if '3' in str(h)+str(m)+str(s):
                    cnt += 1
    return cnt

# print(case_include_3())     # 5 -> 11475

# 3 ) ================================================================
# 행 (1~8), 열 (a~h)
# 나이트는 8X8 밖으로 나갈 수 없다.
# 1. 수평 2칸 -> 수직 1칸 이동
# 2. 수직 2칸 -> 수평 1칸 이동
def royal_knight():
    # 8X8 좌표 평면 상 현재 나이트의 좌표 문자열 입력 -- 열+행 (a1)
    x, y = input("a1 -- ")
    x = ord(x) - ord('a') + 1
    y = int(y)
    steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]
    cnt = 0

    for step in steps:
        x, y = x + step[0], y + step[1]
        if 1 <= x <= 8 and 1 <= y <= 8:
            cnt += 1

    # 나이트가 이동할 수 있는 경우의 수 반환
    return cnt

# print(royal_knight())

'''
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2) (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_col = col + step[1]
    
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        result += 1

return result


# 8x8 좌표 평면 상 현재 나이트의 좌표 문자열 입력 -- 열+행 (예: "a1")
position = input("Enter the knight's position (e.g., a1): ")
x, y = ord(position[0]), int(position[1])  # x는 문자('a'-'h'), y는 숫자(1-8)
cnt = 0

# 나이트가 이동할 수 있는 8가지 방향 정의 (수평2칸+수직1칸 / 수직2칸+수평1칸)
moves = [
    (-2, -1), (-2, 1),  # 수직 2칸, 수평 1칸
    (-1, -2), (-1, 2),  # 수직 1칸, 수평 2칸
    (1, -2), (1, 2),    # 수직 1칸, 수평 2칸
    (2, -1), (2, 1)     # 수직 2칸, 수평 1칸
]

# 모든 방향에 대해 이동 가능 여부 확인
for move in moves:
    nx = x + move[0]  # 새로운 x좌표 (열)
    ny = y + move[1]  # 새로운 y좌표 (행)
    
    # 새로운 좌표가 8x8 체스판 범위를 벗어나지 않으면 카운트 증가
    if ord('a') <= nx <= ord('h') and 1 <= ny <= 8:
        cnt += 1
        
# 나이트가 이동할 수 있는 경우의 수 반환
return cnt
'''

# 4 ) ================================================================
# N X M -- 육지(0) or 바다(1) (바다는 못 감)
# (A, B)
# 상하좌우 -- 순서가 되면
# 0. 일단 왼쪽으로 몸을 돌려
# 1. 아직 가보지 않은 칸 -> 앞으로 한 킨
# 2. 가본 칸 -> 멈추고 0번으로
# 3. 네 방향 모두 가봤거나, 앞이 바다일 경우 -> 한칸 뒤로 가고 0번으로
# 4. 3번일 때, 뒤가 바다라면 멈추기
# 캐릭터가 방문한 칸 수 출력

def game_map():
    # 맵 크기 N x M
    n, m = map(int, input("4 4 -- ").split())
    # 캐릭터 서있는 위치 A, B, 방향(북동남서 0123)
    a, b, d = map(int, input("1 1 0 -- ").split())
    # 전체 맵 정보 입력 -- 육지(0), 바다(1)
    field = [list(map(int, input().split())) for _ in range(n)]

    ''' 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화 '''
    done = [[0] * m for _ in range(n)]
    # 북동남서
    steps = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    ''' 서있는 곳 가본 곳으로 체크 '''
    done[a][b] = 2

    ''' 방문한 칸 수 -> 시작점도 방문했다고 생각해야 함 '''
    result = 1
    ''' 네 방향 모두 가봤는 지 체크 '''
    turn_time = 0

    while True:
        # 왼쪽으로 회전
        d = 0 if d == 3 else d + 1
        # 한 칸 앞 위치
        new_a, new_b = a + steps[d][0], b + steps[d][1]

        # 맵 안에서만 움직이기
        if 0 <= a <= n and 0 <= b <= m:
            ''' 조건을 순서대로 생각하지 말고 그룹화를 잘 해야 함 '''
            # 정면에 가보지 않은 칸이 있다면
            if done[new_a][new_b] == 0 and field[new_a][new_b] == 0:
                done[new_a][new_b] = 2     # 가본 곳으로 체크
                a, b = new_a, new_b         # 앞으로 한 칸 가기
                result += 1
                turn_time = 0
                continue

            # 정면에 가보지 않은 칸이 없거나 바다인 경우
            else:
                turn_time += 1

            # 네 방향 모두 갈 수 없는 경우
            if turn_time == 4:
                new_a, new_b = a - steps[d][0], b - steps[d][1]
                # 뒤쪽이 바다가 아니라면 한 칸 뒤로 가기
                if field[new_a][new_b] == 1:
                    a, b = new_a, new_b  # 뒤로 한 칸 가기
                else:
                    break
                turn_time = 0

        else:
            break

    return result


# 입력 예시
"""
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
"""
print(game_map())  # 출력: 3


'''
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())

# 현재 좌표 방문 처리
d[x][y] = 1

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회번
def turn_left():
    global direction    # 전역변수 불러옴
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x, y = nx, ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0
        
# 정답 출력
print(count)
'''
