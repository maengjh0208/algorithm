# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42748
# 유형: Brute Force

def solution(numbers: list) -> list:
    answer = set()

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            answer.add(numbers[i] + numbers[j])

    answer = sorted(list(answer))
    return answer


# TEST
result = solution([2, 1, 3, 4, 1])
print(result)  # 정답: [2, 3, 4, 5, 6, 7]
