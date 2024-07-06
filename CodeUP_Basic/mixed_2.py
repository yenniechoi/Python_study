"""
종합(2)
6081 ~ 6083
"""

# 6081 -- 입력된 16진수에 1~F까지 순서대로 곱한, 16진수 구구단을 줄을 바꿔 출력
# print('%X'%n)    #n에 저장되어있는 값을 16진수(hexadecimal) 형태로 출력
# 작은 따옴표 2개를 사용해서 print(..., sep='') 으로 출력하면, 공백없이 모두 붙여 출력된다.
n = int(input("B -- "), 16)
for i in range(1, 16):
    print("%X*%X=%X" % (n, i, (n*i)))
    # print("{:X}*{:X}={:X}".format(n, i, (n*i)))
    # print(f"{n:X}*{i:X}={n * i:X}")
    # print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')


# 6082 -- 1 ~ n(=1~29) 출력할 때, 3, 6, 9 대신 영문 대문자 X 를 출력
n = int(input("9 -- "))
for i in range(1, n+1):
    if (i % 10) % 3 == 0 and i % 10 != 0:
        print('X', end=' ')
    else:
        print(i, end=' ')
print()


# 6083 -- 만들 수 있는 rgb 색의 정보를 오름차순으로 줄을 바꿔 모두 출력하고, 마지막에 그 개수를 출력
# range(stop): 0부터 stop-1까지의 정수를 생성
r, g, b = map(int, input("2 2 2 -- ").split())
print('\n'.join(f"{i} {j} {z}" for i in range(r) for j in range(g) for z in range(b)))
print(r * g * b)


