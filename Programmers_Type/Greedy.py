'''
# 1 ) 체육복
# 2 ) 예산
'''

# 1 )  =======================================================================
def distribute_clothes(n, lost, reserve):
    answer = 0

    # 여벌 체육복 중 하나만 도난당했을 경우
    for l in lost[:]:
        if l in reserve:
            lost.remove(l)
            reserve.remove(l)

    if len(lost) > 1: lost.sort()

    # 체육복 나누기
    for num in lost:
        # 여벌 학생이 없으면 반복문 탈출
        if not reserve:
            break

        # 앞 뒤로 도난 학생 여부 파악 -> 나눠주고 여벌 학생 리스트 제거
        if (num - 1) in reserve:
            reserve.remove(num - 1)
        elif (num + 1) in reserve:
            reserve.remove(num + 1)
        else:
            continue

        answer += 1

    answer += n - len(lost)

    return answer

print(distribute_clothes(5, [2, 4], [1, 3, 5]))     # 5
print(distribute_clothes(5, [1], [5]))              # 4
print(distribute_clothes(5, [3, 4], [4, 3]))        # 5
print(distribute_clothes(5, [1, 2], [2, 3]))        # 4

'''
def solution(n, lost, reserve):
    # Convert lists to sets for efficient operations
    lost_set = set(lost)
    reserve_set = set(reserve)
    
    # Remove students who have both lost and reserved a uniform
    overlap = lost_set & reserve_set
    lost_set -= overlap
    reserve_set -= overlap

    answer = n - len(lost_set)  # Start with the number of students who already have uniforms

    # Distribute uniforms
    for student in sorted(lost_set):
        if student - 1 in reserve_set:
            reserve_set.remove(student - 1)
            answer += 1
        elif student + 1 in reserve_set:
            reserve_set.remove(student + 1)
            answer += 1

    return answer
'''

# 2 )  =======================================================================

# 각 부서가 신청한 금액만큼을 모두 지원
# 최대 몇 개의 부서
def department_budget(d, budget):
    total = 0

    for i, req in enumerate(sorted(d)):
        total += req

        # total 이 budget 을 넘을 경우
        if total > budget:
            return i

    # total 이 budget 보다 작을 경우
    return len(d)

print(department_budget([1, 3, 2, 5, 4], 9))    # 3
print(department_budget([2, 2, 3, 3], 10))      # 4


