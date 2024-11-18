'''
문자열
# 76) 대문자로 바꾸기
# 77) 소문자로 바꾸기
# 78) 배열에서 문자열 대소문자 변환하기
# 79) A 강조하기
# 80) 특정한 문자를 대문자로 바꾸기
'''

# 76) =================================================================
def str_upper(myString):
    return myString.upper()

'''
solution = lambda n : n.upper()
'''
'''
JS
const solution = s => s.toUpperCase()

Java
return myString.toUpperCase();
'''

print(str_upper("aBcDeFg"))     # "ABCDEFG"


# 77) =================================================================
def str_lower(myString):
    return myString.lower()

print(str_lower("aBcDeFg"))     # "abcdefg"


# 78) =================================================================
# 홀수 인덱스 -> 소문자 변환, 짝수 인덱스 -> 대문자 변환
def odd_A_even_a(strArr):
    return [strArr[i].lower() if i%2==0 else strArr[i].upper() for i in range(len(strArr))]

'''
# range 보다 enumerate 를 사용하여 index 사용 권장
return [s.lower() if i % 2 == 0 else s.upper() for i, s in enumerate(strArr)]
'''

print(odd_A_even_a(["AAA","BBB","CCC","DDD"]))  # ["aaa","BBB","ccc","DDD"]


# 79) =================================================================
# a -> A, 나머지 모두 소문자 변환

def a_to_A(myString):
    return myString.lower().replace('a', 'A')

'''
JS
const solution = s => s.toLowerCase().replaceAll('a','A');
'''

print(a_to_A("abstract algebra"))   # "AbstrAct AlgebrA"


# 80) =================================================================
def find_alp_and_up(my_string, alp):
    return my_string.replace(alp, my_string[my_string.find(alp)].upper())

'''
return my_string.replace(alp, alp.upper())

return my_string.replace(alp, alp.swapcase())
'''

print(find_alp_and_up("programmers", "p"))   # "Programmers"

