'''
구현
Level.1
# 1) 최소직사각형
'''

# 1) =========================================================
def the_smallest_card(sizes):
    answer = 0
    w, h = 0, 0

    for card in sizes:
        # 카드의 w, h 를 오름차순으로 정렬
        card.sort()

        # w, h 각각의 최댓값을 변수로 할당
        if card[0] > w:
            w = card[0]
        if card[1] > h:
            h = card[1]

    # w, h의 최댓값을 곱해 최소한의 크기를 반환
    return w * h

print(the_smallest_card([[60, 50], [30, 70], [60, 30], [80, 40]]))  # 4000

'''
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

def solution(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col
'''