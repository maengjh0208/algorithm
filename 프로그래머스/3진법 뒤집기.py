def solution(n):
    remains = []

    while n >= 3:
        remains.append(str(n % 3))
        n = n // 3

    remains.append(str(n))

    answer = 0
    multiply = 1
    for num in remains[::-1]:
        answer += int(num) * multiply
        multiply *= 3

    return answer


result = solution(45)
print(result)
print(result == 7)
