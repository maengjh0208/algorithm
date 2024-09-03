def solution(arr, divisor):
    answer = []

    for num in arr:
        if num % divisor == 0:
            answer.append(num)

    return sorted(answer) if answer else [-1]


result = solution([5, 9, 7, 10], 5)
print(result)
print(result == [5, 10])
