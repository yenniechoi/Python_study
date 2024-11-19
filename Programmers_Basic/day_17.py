'''
문자열
# 81) 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기
# 82) 문자열이 몇 번 등장하는지 세기
# 83) ad 제거
# 84) 공백으로 구분하기 1
# 85) 공백으로 구분하기 2
'''

# 81) ====================================================================
# pat로 끝나는 가장 긴 부분 문자열
# pat은 반드시 myString의 부분 문자열로 주어집니다.
# 대문자와 소문자를 구분합니다.

def longest_pat_ending(myString, pat):
    return myString[: myString.rfind(pat)+len(pat)]

    # if myString.endswith(pat): return myString
    # answer = ''
    # arr = myString.split(pat)
    # for i in range(len(arr) - 1):
    #     if arr[i] == '': arr[i] = pat
    #     answer += arr[i]
    # return answer if answer.endswith(pat) else answer + pat

'''
solution=lambda x,y:x[:x.rindex(y)+len(y)]

return myString[:len(myString) - myString[::-1].index(pat[::-1])]

answer = ''
for ch in myString:
    answer += ch
    if mem.endswith(pat):
        return answer
'''

print(longest_pat_ending("AbCdEFG", "AbCdEFG"))     # "AbCdEFG"
print(longest_pat_ending("ancdnc", "nc"))           # "ancdnc"
print(longest_pat_ending("AAAAaaaa", "a"))          # "AAAAaaaa"

print(longest_pat_ending("abcdefghidj", "d"))       # "abcdefghid"
print(longest_pat_ending("AbCdEFG", "dE"))          # "AbCdE"

print(longest_pat_ending("asdf", "a"))              # "a"
print(longest_pat_ending("aasdf", "a"))             # "aa"
print(longest_pat_ending("aaaaAAAA", "a"))          # "aaaa"
print(longest_pat_ending("OxOOo", "Ox"))            # "Ox"


# 82) ====================================================================


print()


# 83) ====================================================================


print()


# 84) ====================================================================


print()


# 85) ====================================================================


print()

