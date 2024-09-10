def solution(s):
    return "".join(sorted(list(s), reverse=True))


result = solution("Zbcdefg")
print(result)
print(result == "gfedcbZ")
