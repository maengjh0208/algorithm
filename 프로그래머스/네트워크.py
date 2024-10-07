from collections import deque


def solution(n, computers):
    # 방문 노드 관리
    visited = set()

    # 네트워크 갯수
    network_count = 0

    # 그래프
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i].append(j)

    # 컴퓨터 하나씩 순회 하면서 연결성 찾기
    for node in range(n):
        queue = deque([])

        if node not in visited:
            visited.add(node)
            network_count += 1
            queue.extend(graph[node])

        while queue:
            next_node = queue.popleft()

            if next_node not in visited:
                visited.add(next_node)
                queue.extend(graph[next_node])

    return network_count


# TEST
result = solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
print(result) # 정답: 2
