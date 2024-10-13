'''
26) 마지막 두 원소
27) 수 조작하기 1
28) 수 조작하기 2
29) 수열과 구간 쿼리 3
30) 수열과 구간 쿼리 2
'''



# 26)
def last_two(num_list):
    last, before = num_list[-1], num_list[-2]
    new = last - before if last > before else last * 2
    num_list.append(new)
    return num_list

# [5, 2, 1, 7, 5, 10]
print(last_two([5, 2, 1, 7, 5]))


# 27)
# w -> n + 1
# s -> n - 1
# d -> n + 10
# a -> n - 10
def wasd(n, control):
    for value in control:
        n = {
            'w' : n + 1,
            's' : n - 1,
            'd' : n + 10,
            'a' : n - 10
          }.get(value, n)

    return n

'''
key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
return n + sum([key[c] for c in control])

c = { 'w':1, 's':-1, 'd':10, 'a':-10}
for i in control:
    n += c[i]

return n + 10*(control.count('d')-control.count('a')) + (control.count('w')-control.count('s'))
'''

# -1
print(wasd(0, "wsdawsdassw"))


# 28)
def return_wasd(numLog):
    answer = ''
    num_dict = { 1 : 'w', -1 : 's', 10 : 'd', -10 : 'a'}
    for i in range(len(numLog)-1):
        cal = numLog[i+1] - numLog[i]
        answer += num_dict[cal]
    return answer

# wsdawsdassw
print(return_wasd([0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]))


# 29)
def sequence(arr, queries):
    for i, j in queries:
        arr[i], arr[j] = arr[j], arr[i]
    return arr

# [3, 4, 1, 0, 2]
print(sequence([0, 1, 2, 3, 4], [[0, 3],[1, 2],[1, 4]]))


# 30)
def sequence_2(arr, queries):
    answer = []
    for query in queries:
        pre_answer = []
        for i, value in enumerate(arr):
            if query[0] <= i <= query[1] and value > query[2]:
                pre_answer.append(value)

        if len(pre_answer) == 0:
            answer.append(-1)
        else:
            answer.append(min(pre_answer))

    return answer

'''
for s, e, k in queries:
    tmp = []
    for x in arr[s:e+1]:
        if x > k:
            tmp.append(x)
    answer.append(-1 if not tmp else min(tmp))

l = [i for i in arr[s:e+1] if i > k]
'''

# [3, 4, -1]
print(sequence_2([0, 1, 2, 4, 3], [[0, 4, 2],[0, 3, 2],[0, 2, 2]]))