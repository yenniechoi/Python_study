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



print()


# 54) ===========================================================================



print()


# 55) ===========================================================================



print()

