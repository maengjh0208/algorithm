# https://school.programmers.co.kr/learn/courses/30/lessons/86491?language=python3
# 문제 유형: 그리디

def solution(sizes: list) -> int:
    max_width = 0 # 가로
    max_length = 0 # 세로

    # 가로에 큰 숫자를, 세로엔 작은 숫자를 옮겨두었다고 생각하자. (실제로 옮기는 게 아니라 가정만 하는 것)
    for i in range(len(sizes)):
        big = max(sizes[i])    # 가로에 배치된 숫자라고 가정한다.
        small = min(sizes[i])  # 세로에 배치된 숫자라고 가정한다.

        max_width = max(max_width, big)
        max_length = max(max_length, small)

    return max_width * max_length


# TEST
print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]) == 4000)
