'''
리스트(배열)
# 51) 문자 개수 세기
# 52) 배열 만들기 1
# 53) 글자 지우기
# 54) 카운트 다운
# 55) 가까운 1 찾기
'''

# 51) ===========================================================================
# A의 개수 ~ z의 개수 == 총 52개의 정수 배열

def count_alphabet(my_string):
    answer = [0 for _ in range(58)]
    for char in my_string:
        answer[ord(char)-65] += 1
    return answer[:26] + answer[32:]

'''
answer=[0]*52
for x in my_string:
    if x.isupper():
        answer[ord(x)-65]+=1
    else:
        answer[ord(x)-71]+=1
return answer


answer = []
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    answer.append(len(my_string.split(i))-1)
return answer


return [my_string.count(alphabet) for alphabet in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz']
'''

# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0]
print(count_alphabet("Programmers"))


# 52) ===========================================================================
# 1 이상 n이하의 정수 중에서 k의 배수를 오름차순으로 저장한 배열
def make_arr(n, k):
    return [i for i in range(k, n+1, k)]

'''
return list(range(k, n + 1, k))
'''

print(make_arr(10,	3))     # [3, 6, 9]


# 53) ===========================================================================

def remove_char(my_string, indices):
    answer = list(my_string)

    for index in indices:
        answer[index] = ''

    return ''.join(answer)

'''
# 인덱스 없는 글자를 이어붙임
return "".join([v for i,v in enumerate(my_string) if i not in indices])

# 인덱스를 내림차순 정렬 후 뒤에서부터 리스트 값 삭제
my_string = list(my_string)
for i in sorted(indices, reverse=True):
    del my_string[i]
return ''.join(my_string)
'''

# "programmers"
print(remove_char("apporoograpemmemprs",	[1, 16, 6, 15, 0, 10, 11, 3]))


# 54) ===========================================================================
# start_num에서 end_num까지 1씩 감소하는 수
def countdown(start_num, end_num):
    return list(range(start_num, end_num-1, -1))

print(countdown(10, 3))     # [10, 9, 8, 7, 6, 5, 4, 3]


# 55) ===========================================================================

def near_one(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1

'''
answer = 0
try:
    answer = arr.index(1, idx)
except:
    answer = -1
return answer
'''


print(near_one([0, 0, 0, 1], 1))            # 3
print(near_one([1, 0, 0, 1, 0, 0],	4))     # -1
print(near_one([1, 1, 1, 1, 0],	3))         # 3

