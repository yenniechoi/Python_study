'''
리스트 (배열)
# 56) 리스트 자르기
# 57) 첫 번째로 나오는 음수
# 58) 배열 만들기 3
# 59) 2의 영역
# 60) 배열 조각하기
'''

# 56) ===========================================================================
def cut_list(n, slicer, num_list):
    a, b, c = slicer
    if n == 1: return num_list[:b+1]
    elif n == 2: return num_list[a:]
    elif n == 3: return num_list[a:b+1]
    elif n == 4: return num_list[a:b+1:c]
    return num_list

'''
return [num_list[:b + 1], num_list[a:], num_list[a:b + 1], num_list[a:b + 1:c]][n - 1]

slices = {
    1: num_list[:b+1],
    2: num_list[a:],
    3: num_list[a:b+1],
    4: num_list[a:b+1:c]
}
return slices.get(n, num_list)
'''

# [2, 3, 4, 5, 6]
print(cut_list(3, [1, 5, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9]))


# 57) ===========================================================================
def find_minus(num_list):
    for i, num in enumerate(num_list):
        if num < 0:
            return i
    return -1

'''
JS
const solution = num_list => num_list.findIndex(v => v < 0)
'''

print(find_minus([12, 4, 15, 46, 38, -2, 15]))  # 5
print(find_minus([13, 22, 53, 24, 15, 6]))      # -1


# 58) ===========================================================================
def two_arr(arr, intervals):
    answer = []
    for a, b in intervals:
        answer.extend(arr[a:b+1])
    return answer


'''
JS
const [[a,b],[c,d]] = intervals;
return [...arr.slice(a, b+1), ...arr.slice(c, d+1)];
'''

# [2, 3, 4, 1, 2, 3, 4, 5]
print(two_arr([1, 2, 3, 4, 5], [[1, 3], [0, 4]]))


# 59) ===========================================================================
def find_2_range(arr):
    index_list = list(filter(lambda i: arr[i] == 2, range(len(arr))))
    if not index_list:
        return [-1]
    return arr[index_list[0]:index_list[-1]+1]

'''
if 2 not in arr:
    return [-1]
return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]
'''

'''
JS
const from = arr.indexOf(2);
const end = arr.lastIndexOf(2);
return from === -1 ? [-1] : arr.slice(from, end+1);
'''

print(find_2_range([1, 2, 1, 2, 1, 10, 2, 1]))  # [2, 1, 2, 1, 10, 2]
print(find_2_range([1, 2, 1]))      # [2]
print(find_2_range([1, 1, 1]))      # [-1]


# 60) ===========================================================================
# 짝수 -- 인덱스 뒷부분 버리기
# 홀수 -- 인덱스 앞부분 버리기
def cut_arr(arr, query):
    for i, q in enumerate(query):
        if i % 2 == 0:
            arr = arr[:q+1]
        else:
            arr = arr[q:]
    return arr

'''
JS
query.map((v,i)=>i%2?arr.splice(0,v):arr.splice(v+1))
'''

print(cut_arr([0, 1, 2, 3, 4, 5],[4, 1, 2]))    # [1, 2, 3]

