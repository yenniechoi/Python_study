'''
조건문, 문자열
36) 간단한 논리 연산
37) 주사위 게임3
38) 글자 이어 붙여 문자열 만들기
39) 9로 나눈 나머지
40) 문자열 여러번 뒤집기
'''

#36)
# (x1 ∨ x2) ∧ (x3 ∨ x4)
# ∧ == and
# ∨ == or
def return_bool(x1, x2, x3, x4):
    return (x1 or x2) and (x3 or x4)

'''
# Logical Operators (or, and) | Bitwise Operators (|, &)
return (x1 | x2) & (x3 | x4)

solution=lambda w,x,y,z:(w or x)and(y or z)
'''

# True
print(return_bool(False, True,	True, True))


#37)
# case 1) 네 숫자가 모두 p로 같다면 1111 × p
# case 2) 세 숫자가 p로 같고 나머지 숫자가 q(p ≠ q)라면 (10 × p + q)2
# case 3) 두 개씩 같은 값이 나오고, 나온 숫자를 각각 p, q(p ≠ q)라고 한다면 (p + q) × |p - q|
# case 4) 두 숫자가 p로 같고 나머지 두 숫자가 각각 p와 다른 q, r(q ≠ r)이라면 q × r
# case 5) 네 숫자가 모두 다르다면 나온 숫자 중 가장 작은 숫자

def dice(a, b, c, d):
    dice_origin = [a, b, c, d]
    dice_set = list({a, b, c, d})   # set (중복 제거)
    check = len(dice_set)

    counts = [dice_origin.count(i) for i in dice_origin]
    print(counts)


    if check == 1:
        # case 1 --- 2222
        return 1111 * dice_set[0]

    elif check == 2:
        p, q = dice_set
        p_count = dice_origin.count(p)
        q_count = dice_origin.count(q)
        if p_count == q_count:
            # case 3 --- 27
            return (p + q) * abs(p - q)
        else:
            # case 2 --- 1681
            three = p if p_count > q_count else q
            one = q if p_count > q_count else p
            return (10 * three + one) ** 2

    elif check == 3:
        # case 4 --- 30
        q, r = [num for num in dice_set if dice_origin.count(num) == 1]
        return q * r

    else:
        # case 5 --- 2
        return min(dice_origin)

'''
# index -- 배열에서 찾고자 하는 값의 위치를 알려주는 함수
    l = [a,b,c,d]
    c = [l.count(x) for x in l]
    if max(c) == 4:
        return 1111*a
    elif max(c) == 3:
        return (10*l[c.index(3)]+l[c.index(1)])**2
    elif max(c) == 2:
        if min(c) == 1:
            return eval('*'.join([str(l[i]) for i, x in enumerate(c) if x == 1]))
        else:
            return (max(l) + min(l)) * abs(max(l) - min(l))
    else:
        return min(l)
'''

print(dice(2, 2, 2, 2))     # 2222
print(dice(4, 1, 4, 4))     # 1681
print(dice(6, 3, 3, 6))     # 27
print(dice(2, 5, 2, 6))     # 30
print(dice(6, 4, 2, 5))     # 2


#38)
# my_string의 index_list의 원소들에 해당하는 인덱스의 글자들을 순서대로 이어 붙인 문자열
def string_plus(my_string, index_list):
    return ''.join([my_string[i] for i in index_list])


# "programmers"
print(string_plus("cvsgiorszzzmrpaqpe", [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]))
# "pizza"
print(string_plus("zpiaz", [1, 2, 0, 0, 3]))


#39)
# 음이 아닌 정수를 9로 나눈 나머지는 그 정수의 각 자리 숫자의 합을 9로 나눈 나머지와 같은 것
def remainder(number):
    answer = 0
    for a in number:
        answer += int(a)
    return answer % 9

'''
return int(number) % 9

# "123" -> [1, 2, 3] -> 1+2+3
return sum(map(int, number)) % 9
'''

print(remainder("123"))     # 6
print(remainder("78720646226947352489"))    # 2


#40)
def flip_stc(my_string, queries):
    for s, e in queries:
        my_string = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    return my_string

# "programmers"
print(flip_stc("rermgorpsam", [[2, 3], [0, 7], [5, 9], [6, 10]]))