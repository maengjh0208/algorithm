def solution(s):
    n = len(s) // 2
    return s[n - 1: n + 1] if len(s) % 2 == 0 else s[n]


result = solution("abcde")
print(result)
print(result == "c")
