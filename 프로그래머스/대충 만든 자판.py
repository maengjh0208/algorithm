def solution(keymap, targets):
    alphabets = {}
    for key in keymap:
        for i in range(len(key)):
            if key[i] in alphabets:
                alphabets[key[i]] = min(alphabets[key[i]], i + 1)
            else:
                alphabets[key[i]] = i + 1

    result = []
    for target in targets:
        sum_value = 0
        for char in target:
            if char not in alphabets:
                sum_value = -1
                break

            sum_value += alphabets[char]

        result.append(sum_value)

    return result


result = solution(
    keymap=["AA"],
    targets=["B"],
)

print(result)
print(result == [-1])
