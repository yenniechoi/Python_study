'''
리스트(배열)
# 66) 홀수 vs 짝수
# 67) 5명씩
# 68) 할 일 목록
# 69) n보다 커질 때까지 더하기
# 70) 수열과 구간 쿼리1
'''

# 66) ====================================================================
# 가장 첫 번째 원소를 1번 원소라고 할 때, 홀수 번째 원소들의 합과 짝수 번째 원소들의 합 중 큰 값을 return

def odd_vs_even(num_list):
    odd, even = 0, 0
    odd = sum(num for num in num_list[1::2])
    even = sum(num for num in num_list[::2])

    return max(odd, even)

'''
return max(sum(num_list[::2]), sum(num_list[1::2]))
'''
'''
JS

num_list.map((val, idx) => { !(idx % 2) ? even += val : odd += val })
return odd > even ? odd : even;

num_list.forEach((val, idx) => idx % 2 == 0 ? even += val : odd += val);
return Math.max(odd, even);
'''

print(odd_vs_even([4, 2, 6, 1, 7, 6]))  # 17


# 67) ====================================================================
# 앞에서 부터 5명씩 묶은 그룹의 가장 앞

def group_leader(names):
    return names[::5]


# ["nami", "vex"]
print(group_leader(["nami", "ahri", "jayce", "garen", "ivern", "vex", "jinx"]))


# 68) ====================================================================
#  아직 마치지 못한 일들을 순서대로

def todo(todo_list, finished):
    return [t for t, r in zip(todo_list, finished) if not bool(r)]

'''
return [work for idx, work in enumerate(todo_list) if not finished[idx]]

return [x for x, b in zip(todo_list, finished) if not b]
'''
'''
JS
return todo_list.filter((e,i) => !finished[i]);

Java
for(int i=0; i<finished.length; i++){
    str = finished[i]==false ? str+todo_list[i]+"," : str;
}
return str.split(",");
'''

# ["practiceguitar", "studygraph"]
print(todo(["problemsolving", "practiceguitar", "swim", "studygraph"],	[True, False, True, False]))


# 69) ====================================================================
# 앞에서부터 하나씩 더하다가 그 합이 n보다 커지는 순간 리턴

def add_num(numbers, n):
    answer = 0
    for num in numbers:
        answer += num
        if answer > n:
            return answer

'''
return next(sum(numbers[:i + 1]) for i in range(len(numbers)) if sum(numbers[:i + 1]) > n)

from itertools import accumulate
def find_first_exceeding_sum(numbers, n):
    return next((s for s in accumulate(numbers) if s > n), None)
'''

print(add_num([34, 5, 71, 29, 100, 34],	123))   # 139
print(add_num([58, 44, 27, 10, 100],	139))       # 239


# 70) ====================================================================
#  s ≤ i ≤ e인 모든 i에 대해 arr[i]에 1을 더합니다.

def section_query(arr, queries):
    for s, e in queries:
        for i in range(s, e+1):
            arr[i] += 1
    return arr

'''
JS
queries.forEach(([s, e]) => {
    while (s <= e) arr[s++]++;
});
'''


# [1, 3, 4, 4, 4]
print(section_query([0, 1, 2, 3, 4],	[[0, 1],[1, 2],[2, 3]]))

