'''
6) 덧셈식 출력하기
7) 문자열 붙여서 출력하기
8) 문자열 돌리기
9) 홀짝 구분하기
10) 문자열 겹쳐쓰기
'''

# 6)
a, b = map(int, input("4 5 -- ").strip().split(' '))
print(f"{a} + {b} = {a + b}")

# 7)
str1, str2 = input("a b -- ").strip().split(' ')
print(str1 + str2)
'''
print(input().strip().replace(' ', ''))
'''

# 8)
s_list = list(input("abced -- "))
print(*s_list, sep='\n')
'''
s_list = [*input()]

print('\n'.join(input()))

for a in input():
    print(a)
'''

# 9)
a = int(input())
a_type = "even" if a % 2 == 0 else "odd"
print(f"{a} is {a_type}")


# 10)
def switch_string(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]

print(switch_string("Program29b8UYP", "merS123", 7))
