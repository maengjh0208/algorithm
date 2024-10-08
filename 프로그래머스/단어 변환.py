# https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque


def is_can_transform(word1: str, word2: str) -> bool:
    count = 0
    for w1, w2 in zip(word1, word2):
        if w1 != w2:
            count += 1

        if count > 1:
            break

    return count == 1


def bfs(begin, target, words):
    result = 0
    queue = deque([[begin, 0]])
    visited = [False] * (len(words))

    while queue:
        current_word, count = queue.popleft()
        if current_word == target:
            result = count

        for idx in range(len(words)):
            if visited[idx]:
                continue

            word = words[idx]

            if is_can_transform(current_word, word):
                visited[idx] = True
                queue.append([word, count + 1])

    return result


def solution(begin, target, words):
    if target not in words:
        return 0

    return bfs(begin, target, words)


# TEST
result = solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
print(result == 4, result) # True 4
