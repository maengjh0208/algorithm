# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/142086
# 유형: 문자열

def solution(s: str) -> list:
    char_locations = dict()
    answer = []

    for idx, c in enumerate(s):
        if c in char_locations:
            answer.append(idx - char_locations[c])
        else:
            answer.append(-1)

        char_locations[c] = idx

    return answer


print(solution("banana"))  # 정답: [-1, -1, -1, 2, 2, 2]
