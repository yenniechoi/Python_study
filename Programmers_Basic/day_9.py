'''
문자열
41) 배열 만들기 5
42) 부분 문자열 이어 붙여 문자열 만들기
43) 문자열 뒤의 n 글자
44) 접미사 배열
45) 접미사인지 확인하기
'''

# 41)
def trans_intStrs(intStrs, k, s, l):
    answer = []
    for intstr in intStrs:
        num = int(intstr[s:s+l])
        if num > k:
            answer.append(num)
    return answer

'''
return [int(intstr[s:s+l]) for intstr in intStrs if int(intstr[s:s+l]) > k]

return list(filter(lambda x: x > k, map(lambda x: int(x[s:s + l]), intStrs)))
'''


# [56789, 99999]
print(trans_intStrs(["0123456789","9876543210","9999999999999"], 50000, 5, 5))


# 42)
def assemble_str(my_strings, parts):
    return ''.join(string[s:e+1] for string, [s, e] in zip(my_strings, parts))

# "programmers"
print(assemble_str(["progressive", "hamburger", "hammer", "ahocorasick"], [[0, 4], [1, 2], [3, 5], [7, 7]]))


# 43)
def return_str_n(my_string, n):
    return my_string[len(my_string)- n : len(my_string) + 1]

'''
return my_string[-n:]
'''

print(return_str_n("ProgrammerS123", 11))   # "grammerS123"
print(return_str_n("He110W0r1d", 5))        # "W0r1d"


# 44)
# 모든 접미사를 사전순으로 정렬한 문자열 배열
def every_suffix(my_string):
    answer = []
    for i in range(len(my_string)):
        answer.append(my_string[-i:])
    answer.sort()
    return answer

'''
return sorted(my_string[i:] for i in range(len(my_string)))
'''

# ["a", "ana", "anana", "banana", "na", "nana"]
print(every_suffix("banana"))


# 45)
def check_suffix(my_string, is_suffix):
    return int(is_suffix in list((my_string[-i:] for i in range(len(my_string)))))

'''
return int(my_string[-len(is_suffix):] == is_suffix)

return int(my_string.endswith(is_suffix))
'''

print(check_suffix("banana","ana"))     # 1






