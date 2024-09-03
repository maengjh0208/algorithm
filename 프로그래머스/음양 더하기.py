def solution(absolutes, signs):
    answer = 0

    for num, sign in zip(absolutes, signs):
        if sign:
            answer += num
        else:
            answer -= num

    return answer


result = solution([4, 7, 12], [True, False, True])
print(result)
print(result == 9)
