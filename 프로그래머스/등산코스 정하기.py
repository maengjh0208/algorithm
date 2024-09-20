"""
[문제 요구 사항]
- XX산은 n개의 지점으로 이뤄져 있다.
- 각 지점은 1 ~ n 번호가 붙어 있으며, 출입구, 쉼터, 혹은 산봉우리 이다.
- 각 지점은 양방향 통행이 가능한 등산로로 연결되어 있다.
- 다른 지점으로 이동 시 등산로를 이용해야 하며, 등산로별로 이동 비용이 존재한다.
- 등산코스는 방문할 지점 번호들을 순서대로 나열하여 표현할 수 있다. (ex: 1-2-3-2-1)
- intensity:
    -  등산코스를 따라 이동하는 중 쉼터 혹은 산봉우리를 방문할 때마다 휴식을 취할 수 있으며, 휴식 없이 이동해야 하는 시간 중 가장 긴 시간을 해당 등산코스의 intensity라 부른다.
- 출입구 중 한곳에서 출발 -> 산봉우리 중 한 곳만 방문한 뒤 -> 다시 원래 출입구로 돌아오는 등산코스를 정하려 한다.
- 산봉우리는 한 번만 포함되어야 한다.
- 반환값: [산봉우리 번호, intensity 최소값]
"""

from heapq import heappush, heappop


def solution(n: int, paths: list, gates: list, summits: list):
    INF = 1e9

    # intensity 거리 정보
    distance = [INF] * (n + 1)

    intensity_list = []

    # 연결 정보 및 업데이트
    graph = [[] for _ in range(n + 1)]

    for i, j, cost in paths:
        graph[i].append([cost, j])
        graph[j].append([cost, i])

    # 최단 거리를 추출할 수 있는 힙
    heap = []
    for gate in gates:
        heappush(heap, [0, gate])

    while (heap):
        cost, node = heappop(heap)

        if cost < distance[node]:
            distance[node] = cost

            if node in summits:
                intensity_list.append([cost, node])
                continue

            for cost2, next_node in graph[node]:
                next_cost = max(cost, cost2)

                if next_cost < distance[next_node]:
                    heappush(heap, [next_cost, next_node])

    return sorted(intensity_list)[0][::-1]


# TEST
result = solution(
    n=6,
    paths=[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]],
    gates=[1, 3],
    summits=[5],
)

print(result)
print(result == [5, 3])
