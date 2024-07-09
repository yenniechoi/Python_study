"""
종합(3)
6084 ~ 6087
"""


# 6084 -- 소리 파일 저장용량 MB 단위로 바꾸어 계산
# h -- 1초 동안 마이크로 소리강약을 체크하는 횟수
# b -- 한 번 체크한 값을 저장할 때 사용하는 비트수
# c -- 좌우 등 소리를 저장할 트랙 개수인 채널 개수
# s -- 녹음할 시간(초)
# 8bit=1Byte, 1024Byte=1KB
# 44100*16*2*1/8/1024/1024
h, b, c, s = map(int, input("44100 16 2 10 -- ").split())
volume = (h * b * c * s) / 8 / 1024 / 1024
print(format(float(volume), ".1f"), "MB", sep=" ")



# 6085 -- 그림 파일 저장용량 계산, MB 단위로 바꾸어, 둘째 자리까지 출력
# 이미지의 가로 해상도 w, 세로 해상도 h, 한 픽셀을 저장하기 위한 비트 b
# 1024 * 768 사이즈(해상도)의 각점에 대해 24비트(rgb 각각 8비트씩 3개)로 저장
# -> 1024*768*24/8/1024/1024 로 계산하면 약 2.25 MB 정도가 필요
w, h, b = map(int, input("1024 768 24 -- ").split())
volume = (w * h * b) / 8 / 1024 / 1024
print(format(float(volume), ".2f"), "MB", sep=" ")



# 6086 -- 1부터 순서대로 더하다가, 그 합 >= 정수 경우, 그때까지의 합을 출력
d = int(input("57 -- "))
result = 0
for i in range(1, d+1):
    result += i
    if result >= d:
        break
print(result)

"""
# 리스트 내포를 활용한 방법

result = sum(i for i in range(1, d+1) if (result := result + i) < d)
print(result + (result >= d) * (d - result))

# sum(...): 리스트 내포에서 생성된 값들의 합계를 계산
# i for i in range(1, d+1): 1부터 d까지의 숫자 i를 생성
# if (...) < d: 각 i에 대해 조건에 만족한 i 만 포함
# (result := result + i): result 변수에 result + i 값을 할당

# result >= d:조건식으로, result가 d보다 크거나 같은지를 확인 -- True(1), False (0)
"""

"""
# while 문을 활용한 방법

result, i = 0, 1
while result < d:
    result += i
    i += 1
print(result)
"""


# 6087 -- 1부터 입력한 정수까지 1씩 증가시켜 출력, 3의 배수는 통과
d = int(input("10 -- "))
for i in range(1, d+1):
    if (i % 3 != 0):
        print(i, end=' ')
print()


