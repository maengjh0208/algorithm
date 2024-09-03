def solution(num):
    count = 0
    while num != 1 and count < 500:
        count += 1

        # 입력된 수가 짝수라면 2로 나눠
        if num % 2 == 0:
            num = num // 2

        # 입력된 수가 홀수라면 3 곱하고 1 더해
        else:
            num = num * 3 + 1

    return count if num == 1 else -1


result = solution(6)
print(result)
print(result == 8)
