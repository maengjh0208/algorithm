# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/12915
# 유형: 문자열

def solution(strings, n):
    result = sorted(strings, key=lambda x: (x[n], x))
    return result


result = solution(strings=["sun", "bed", "car"], n=1)
print(result)  # 정답: ["car", "bed", "sun"]
