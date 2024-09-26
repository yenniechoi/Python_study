'''
11) 문자열 섞기
12) 문자 리스트를 문자열로 변환하기
13) 문자열 곱하기
14) 더 크게 합치기
15) 두 수의 연산값 비교하기
'''


# 11
def mix_str(str1, str2):
    answer = ''
    list_1, list_2 = [*str1], [*str2]

    for i in range(len(list_1)):
        answer += list_1[i] + list_2[i]
    return answer

'''
# strings in Python are iterable, and you don't need to convert them to lists.
for i in range(len(str1)):
    answer += str1[i] + str2[i]

# list comprehension 
answer = ''.join([str1[i] + str2[i] for i in range(len(str1))])

for s1,s2 in zip(str1,str2):
    answer += s1 + s2

return ''.join(i + j for i , j in zip(str1,str2))
'''
print(mix_str("aaaaa", "bbbbb"))


# 12
def list_to_str(arr1):
    return ''.join(arr1)


print(list_to_str(["a","b","c"]))


# 13
def multiply_str(my_string, k):
    return ''.join(my_string) * k

'''
# Just multiply the string directly
return my_string*k
'''
print(multiply_str("string", 3))


# 14
def add_bigger(a, b):
    ab = int(str(a) + str(b))
    ba = int(str(b) + str(a))
    return ba if ab < ba else ab

'''
# strings can be compared in Python based on their Unicode values.
return int(max(f"{a}{b}", f"{b}{a}"))
'''
print(add_bigger(9, 91))


# 15
def compare_two(a, b):
    return max(int(f"{a}{b}"), 2 * a * b)

print(compare_two(2, 91))