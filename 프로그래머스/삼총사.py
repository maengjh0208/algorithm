# https://school.programmers.co.kr/learn/courses/30/lessons/131705
# 유형: 완전탐색 (조합 이용)

from itertools import combinations


# combinations를 이용한 풀이
# 일반적으로 시간복잡도는 n(=number 길이)의 r(=뽑는 개수)승
def solution(number: list) -> int:
    answer = 0
    for i, j, k in combinations(number, 3):
        if i + j + k == 0:
            answer += 1

    return answer


# TEST
print(solution([-2, 3, 0, 2, -5]) == 2)
print(solution([-3, -2, -1, 0, 1, 2, 3]) == 5)
