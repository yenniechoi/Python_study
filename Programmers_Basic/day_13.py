'''
리스트(배열)
# 61) n 번째 원소부터
# 62) 순서 바꾸기
# 63) 왼쪽 오른쪽
# 64) n 번째 원소까지
# 65) n 개 간격의 원소들
'''

# 61) ===================================================================
def from_n(num_list, n):
    return num_list[n-1:]

'''
JS
return num_list.slice(n - 1);
'''

print(from_n([2, 1, 6],	3))             # [6]
print(from_n([5, 2, 1, 7, 5],	2))     # [2, 1, 7, 5]



# 62) ===================================================================
def change_order(num_list, n):
    return num_list[n:] + num_list[:n]

'''
JS
# removing n elements starting from index 0
# The removed elements are returned as an array

num_list.push(...num_list.splice(0, n));
return num_list
'''

print(change_order([2, 1, 6], 1))       # [1, 6, 2]
print(change_order([5, 2, 1, 7, 5],	3)) # [7, 5, 5, 2, 1]


# 63) ===================================================================
# str_list에는 "u", "d", "l", "r" 네 개의 문자열이 여러 개 저장
# "l"과 "r" 중 먼저 나오는 문자 --> "l" 왼쪽 문자열 / "r" 오른쪽 문자열 / 없으면 빈 문자열

def left_right(str_list):
    for i, val in enumerate(str_list):
        if val == "l":
            return str_list[:i]
        if val == "r":
            return str_list[i:]
    return []

print(left_right(["u", "u", "l", "r"])) # ["u", "u"]
print(left_right(["l"]))                # []
print(left_right(["l", "u", "d", "r"]))  # Expected output: []
print(left_right(["r", "u", "d", "l"]))  # Expected output: ["r", "u", "d", "l"]
print(left_right(["u", "d", "u", "d"]))  # Expected output: []
print(left_right(["u", "d", "u", "l"]))  # Expected output: ["u", "d", "u"]
print(left_right(["u", "d", "u", "r"]))  # Expected output: ["r"]
print(left_right([]))  # Expected output: []
print(left_right(["l"]))  # Expected output: []
print(left_right(["r"]))  # Expected output: ["r"]
print(left_right(["u"]))  # Expected output: []



# 64) ===================================================================



print()


# 65) ===================================================================



print()

