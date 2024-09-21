'''
1) 문자열 출력하기
2) a와 b 출력하기
3) 문자열 반복해서 출력하기
4) 대소문자 바꿔서 출력하기
5) 특수문자 출력하기
'''

# 1) 문자열 출력하기
str = input("HelloWorld! -- ")
print(str)


# 2) a와 b 출력하기
a, b = map(int, input("4 5 -- ").split())
print("a =", a)
print("b =", b)

'''
a, b = map(int, input().strip().split(' '))
print(f"a = {a}\nb = {b}")
'''


# 3) 문자열 반복해서 출력하기
str, n = input("string 5 -- ").strip().split(' ')
n = int(n)
print(''.join(str for _ in range(n)))

'''
print(str * int(n))
'''


# 4) 대소문자 바꿔서 출력하기
str = list(input("aBcDeFg -- "))

for i in range(len(str)):
    if str[i].isupper():
        str[i] = str[i].lower()
    elif str[i].islower():
        str[i] = str[i].upper()

print(''.join(str))

'''
print(input().swapcase())

print(''.join(x.upper() if x == x.lower() else x.lower() for x in input()))
'''


# 5) 특수문자 출력하기
# !@#$%^&*(\'"<>?:;
print("!@#$%^&*(\\'\"<>?:;")

'''
문자열 앞에 r을 붙이면 특수문자 그대로 출력할 수 있다.
print(r'!@#$%^&*(\'"<>?:;')
'''