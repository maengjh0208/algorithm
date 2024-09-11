def solution(price, money, count):
    total_price = price * (count * (count + 1) // 2)

    answer = 0
    if total_price > money:
        answer = total_price - money

    return answer


result = solution(3, 20, 4)
print(result)
print(result == 10)
