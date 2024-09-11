def solution(s):
    answer = True

    # 문자열 길이 체크
    if len(s) not in (4, 6):
        answer = False

    # 숫자로만 구성되었는지 체크
    if not s.isnumeric():
        answer = False

    return answer


result = solution("a234")
print(result)
print(result is False)