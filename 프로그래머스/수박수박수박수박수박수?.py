def solution(n):
    array = ["수" if i % 2 == 0 else "박" for i in range(n)]
    return "".join(array)


result = solution(3)
print(result)
print(result == "수박수")
