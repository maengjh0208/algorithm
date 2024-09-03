def solution(x):
    sum_value = sum(map(int, str(x)))

    return True if x % sum_value == 0 else False


result = solution(10)
print(result)
