# 목표:
# 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값을 return. 단, 상대 팀 진영에 도착할 수 없을 때는 -1을 return

# map: 0:벽, 1:통로
# 캐릭터 시작지점: (0, 0) / 캐릭터 도착 지점 (맵 맨 우측 하단)

from collections import deque


def solution(maps):
    INF = 1e9

    row_count = len(maps)
    col_count = len(maps[0])
    distance_graph = [[INF] * col_count for _ in range(row_count)]

    dxs = (0, 0, 1, -1)
    dys = (1, -1, 0, 0)

    result = -1

    queue = deque([[0, 0, 1]])
    while queue:
        x, y, cost = queue.popleft()

        if x == row_count - 1 and y == col_count - 1:
            result = cost
            break

        if cost >= distance_graph[x][y]:
            continue

        distance_graph[x][y] = cost

        for dx, dy in zip(dxs, dys):
            new_x = x + dx
            new_y = y + dy

            if new_x < 0 or new_x >= row_count:
                continue

            if new_y < 0 or new_y >= col_count:
                continue

            if maps[new_x][new_y] == 0:
                continue

            queue.append([new_x, new_y, cost + 1])

    return result


# TEST
result_1 = solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]])
print(result_1 == 11, result_1)

result_2 = solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]])
print(result_2 == -1, result_2)

result_3 = solution([[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1]])
print(result_3 == 9, result_3)

result_4 = solution([[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
print(result_4 == 9, result_4)

result_5 = solution([[1, 0, 1, 1, 1], [0, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 0, 0], [1, 1, 1, 0, 1]])
print(result_5 == -1, result_5)
