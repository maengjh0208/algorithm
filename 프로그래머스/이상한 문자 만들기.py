# https://school.programmers.co.kr/learn/courses/30/lessons/12930
# 유형: 문자열

def solution(s: str) -> str:
    result = []
    num = 0

    for c in s:
        if c == " ":
            result.append(c)
            num = 0
        else:
            c = c.upper() if num % 2 == 0 else c.lower()
            result.append(c)
            num += 1

    return "".join(result)


# TEST
print(solution("try hello world"))  # 결과: "TrY HeLlO WoRlD"
