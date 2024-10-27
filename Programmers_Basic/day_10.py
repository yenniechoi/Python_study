'''
문자열
# 46) 문자열의 앞의 n글자
# 47) 접두사인지 확인하기
# 48) 문자열 뒤집기
# 49) 세로 읽기
# 50) qr code
'''

# 46)
def return_nlen_str(my_string, n):
    return my_string[:n]

print(return_nlen_str("ProgrammerS123", 11))    # "ProgrammerS"


# 47)
def check_perfix(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))

print(check_perfix("banana",	"ban"))     # 1

'''
return int(my_string[:len(is_prefix)] == is_prefix)
'''


# 48)
def reverse_part(my_string, s, e):
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]

print(reverse_part("Progra21Sremm3",	6,	12))    # "ProgrammerS123"

# 49)


print()


# 50)


print()




