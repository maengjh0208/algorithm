def solution(a, b):
    answer = 0

    for i, j in zip(a, b):
        answer += i * j

    return answer


# TEST
result = solution([1, 2, 3, 4], [-3, -1, 0, 2])
print(result)
print(result == 3)
