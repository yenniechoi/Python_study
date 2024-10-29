'''
문자열
# 46) 문자열의 앞의 n글자
# 47) 접두사인지 확인하기
# 48) 문자열 뒤집기
# 49) 세로 읽기
# 50) qr code
'''

# 46)===============================================================

def return_nlen_str(my_string, n):
    return my_string[:n]

print(return_nlen_str("ProgrammerS123", 11))    # "ProgrammerS"


# 47)===============================================================

def check_perfix(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))

print(check_perfix("banana",	"ban"))     # 1

'''
return int(my_string[:len(is_prefix)] == is_prefix)
'''


# 48)===============================================================

def reverse_part(my_string, s, e):
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]

print(reverse_part("Progra21Sremm3",	6,	12))    # "ProgrammerS123"


# 49)===============================================================
# my_string을 한 줄에 m 글자씩 가로로 적었을 때 왼쪽부터 세로로 c번째 열에 적힌 글자들

def vertical_str(my_string, m, c):
    return my_string[c-1::m]

print(vertical_str("ihrhbakrfpndopljhygc",	4,	2)) # "happy"


# 50)===============================================================
# code의 각 인덱스를 q로 나누었을 때 나머지가 r인 위치의 문자

def QRCode(q, r, code):
    return ''.join(char if idx % q == r else '' for idx, char in enumerate(code))

'''
# index = x * q + r 임을 알 수 있고, 우리가 필요한 index는 [0q+r, 1q+r, 2q+r... xq+r]입니다. 
# 즉 [r, q+r, 2q+r... xq+r]임을 알 수있고, r로 시작해서 q씩 커지는 index만 가져오면 됩니다 :)
return code[r::q]
'''

print(QRCode(3,	1,	"qjnwezgrpirldywt"))    # jerry
print(QRCode(1,	0,	"programmers"))         # programmers