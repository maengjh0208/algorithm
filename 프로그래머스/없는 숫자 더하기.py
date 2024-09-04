def solution(numbers: list):
    return 45 - sum(numbers)


result = solution([1, 2, 3, 4, 6, 7, 8, 0])
print(result)
print(result == 14)
