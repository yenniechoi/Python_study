"""
6009 ~ 6015
"""

# 6009
c = input()
print(c)


# 6010
while True:
    try:
        i_0 = input()
        print(int(i_0))
        break
    except ValueError:
        print("숫자를 입력하세요.")


# 6011
f = float(input())
print(f)


# 6012
i_1 = int(input())
i_2 = int(input())
print(f"{i_1}\n{i_2}")


# 6013
c_1 = input()
c_2 = input()
print("{}\n{}".format(c_2, c_1))


# 6014
ff = float(input())
for i in range(0, 3, 1):
    print(ff)


# 6015
i_3, i_4 = input("숫자+공백+숫자: ").split()
i_3, i_4 = int(i_3), int(i_4)
print("%d\n%d" % (i_3, i_4))