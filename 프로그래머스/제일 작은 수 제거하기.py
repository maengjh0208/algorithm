def solution(arr):
    arr.remove(min(arr))
    return arr if arr else [-1]


result = solution([4, 3, 2, 1])
print(result)
print(result == [4, 3, 2])
