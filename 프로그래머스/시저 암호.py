# https://school.programmers.co.kr/learn/courses/30/lessons/12926
# 유형: 문자열

def solution(s, n):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    alphabets_dict = {c: idx for idx, c in enumerate(alphabets)}

    answer = []
    for c in s:
        if c != " ":
            idx = alphabets_dict[c.lower()]
            next_idx = (idx + n) % 26

            next_c = alphabets[next_idx]
            c = next_c if c.islower() else next_c.upper()

        answer.append(c)

    return "".join(answer)


# TEST
print(solution("a B z", 4) == "e F d")
