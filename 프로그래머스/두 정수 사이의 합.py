def solution(a, b):
    answer = 0

    if a == b:
        answer = a
    else:
        min_value = min(a, b)
        max_value = max(a, b)

        sum_max_value = max_value * (max_value + 1) / 2
        sum_min_value = min_value * (min_value - 1) / 2

        answer = int(sum_max_value - sum_min_value)

    return answer


result = solution(3, 5)
print(result)
print(result == 12)
