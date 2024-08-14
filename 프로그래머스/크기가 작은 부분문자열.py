# https://school.programmers.co.kr/learn/courses/30/lessons/147355
# 유형: 문자열 (문자열 탐색)

def solution(t: str, p: str) -> int:
    length = len(p)
    count = 0
    for idx in range(0, len(t) - len(p) + 1):
        if t[idx: idx + length] <= p:
            count += 1

    return count


# TEST
print(solution("3141592", "271") == 2)
