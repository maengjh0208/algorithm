# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/134240
# 유형: 문자열

def solution(food):
    answer = []

    for i in range(1, len(food)):
        count = food[i] // 2

        if count == 0:
            continue

        answer.append(str(i) * count)

    answer.extend(['0'])
    answer.extend(answer[::-1][1:])

    return "".join(answer)


# TEST
result = solution([1, 3, 4, 6])
print(result)  # 정답: "1223330333221"
