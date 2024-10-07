def solution(numbers: list, target: int) -> int:
    array = [numbers[0], -numbers[0]]

    for i in range(1, len(numbers)):
        next_array = []
        for num in array:
            next_array.append(num + numbers[i])
            next_array.append(num - numbers[i])

        array = next_array

    return array.count(target)


def solution2(numbers: list, target: int) -> int:
    def dfs(idx, sum_value):
        if idx == len(numbers):
            return 1 if sum_value == target else 0

        add = dfs(idx + 1, sum_value + numbers[idx])
        minus = dfs(idx + 1, sum_value - numbers[idx])

        return add + minus

    return dfs(0, 0)


result = solution([1, 1, 1, 1, 1], 3)
print(result)
print(result == 5)

result = solution2([1, 1, 1, 1, 1], 3)
print(result)
print(result == 5)
