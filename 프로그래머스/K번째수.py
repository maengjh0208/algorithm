# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42748
# 유형: 정렬

def solution(array: list, commands: list) -> list:
    answer = []

    for i, j, k in commands:
        answer.append(sorted(array[i - 1 : j])[k - 1])

    return answer


result = solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
print(result == [5, 6, 3])
