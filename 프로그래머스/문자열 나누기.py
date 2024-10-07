def solution(s):
    same_count = 0
    diff_count = 0
    split_count = 0
    compare_char = None

    for char in s:
        if same_count == 0:
            compare_char = char
            same_count += 1
            continue

        if compare_char == char:
            same_count += 1
        else:
            diff_count += 1

        if same_count == diff_count:
            same_count = 0
            diff_count = 0
            split_count += 1

    if same_count != diff_count:
        split_count += 1

    return split_count


result = solution("aaabbaccccabba")
print(result)  # 정답: 3
