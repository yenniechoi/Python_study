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



print()


# 69) ====================================================================



print()


# 70) ====================================================================



print()

