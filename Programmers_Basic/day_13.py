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
            return str_list[i+1:]
    return []

'''
JS
for(let i = 0; i < arr.length; i++) {
     if (arr[i] === 'l') return arr.slice(0, i);
     if (arr[i] === 'r') return arr.slice(i + 1);
 }
 return [];
'''

print(left_right(["u", "u", "l", "r"])) # ["u", "u"]
print(left_right(["l"]))                # []



# 64) ===================================================================
# num_list의 첫 번째 원소부터 n 번째 원소까지의 모든 원소를 담은 리스트

def to_n(num_list, n):
    return num_list[:n]

'''
JS
return num_list.slice(0, n);

Java
return Arrays.copyOfRange(num_list,0,n);
'''

print(to_n([2, 1, 6],	1))     # [2]


# 65) ===================================================================
# 첫 번째 원소부터 마지막 원소까지 n개 간격

def interval_n(num_list, n):
    return num_list[::n]

'''
JS
const solution = (num_list, n) => num_list.filter((_, i) => !(i % n))

Java
int N = num_list.length % n == 0 ? num_list.length / n : num_list.length / n + 1;
int idx = 0;
int[] answer = new int[N];
for (int i = 0;i < num_list.length;i+=n)
    answer[idx++] = num_list[i];
return answer;
'''

print(interval_n([4, 2, 6, 1, 7, 6],	2))     # [4, 6, 7]

