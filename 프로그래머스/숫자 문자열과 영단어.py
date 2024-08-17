# https://school.programmers.co.kr/learn/courses/30/lessons/81301
# 문제 유형: 문자열

def solution(s: str) -> int:
    numbers_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    idx = 0
    answer = []
    while idx < len(s):
        if s[idx].isalpha():
            if s[idx: idx + 3] in numbers_dict:
                answer.append(numbers_dict[s[idx: idx + 3]])
                idx += 3
            elif s[idx: idx + 4] in numbers_dict:
                answer.append(numbers_dict[s[idx: idx + 4]])
                idx += 4
            else:
                answer.append(numbers_dict[s[idx: idx + 5]])
                idx += 5
        else:
            answer.append(s[idx])
            idx += 1

    return int("".join(answer))


# TEST
print(solution("one4seveneight"))  # 정답: 1478
