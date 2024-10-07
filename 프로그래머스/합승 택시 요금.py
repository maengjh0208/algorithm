from heapq import heappush, heappop


def dijkstra(n, start, graph):
    INF = 1e9

    distances = [INF] * (n + 1)
    distances[start] = 0

    queue = []
    for node, cost in graph[start]:
        heappush(queue, (cost, node))

    while queue:
        cost, node = heappop(queue)

        if cost <= distances[node]:
            distances[node] = cost

            for next_node, add_cost in graph[node]:
                next_cost = cost + add_cost

                if next_cost <= distances[next_node]:
                    heappush(queue, (next_cost, next_node))

    return distances


def solution(n: int, s: int, a: int, b: int, fares: list) -> int:
    min_value = 1e9

    graph = [[] for _ in range(n + 1)]
    for node_a, node_b, cost in fares:
        graph[node_a].append([node_b, cost])
        graph[node_b].append([node_a, cost])

    start_dijkstra = dijkstra(n, s, graph)
    a_dijkstra = dijkstra(n, a, graph)
    b_dijkstra = dijkstra(n, b, graph)

    for i in range(1, n + 1):
        min_value = min(min_value, start_dijkstra[i] + a_dijkstra[i] + b_dijkstra[i])

    return min_value


# n:지점개수 / s:출발지점 / a:A의 도착지점 / b:B의 도착지점 / fares:지점간 택시요금
result = solution(
    n=6,
    s=4,
    a=6,
    b=2,
    fares=[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
)

print(result == 82)
print(result)
