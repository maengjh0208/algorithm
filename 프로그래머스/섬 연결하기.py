"""
최소의 비용으로 모든 섬이 서로 통행 가능하도록 만든다.
최소 비용을 반환한다.
"""


def get_parent(parents, node):
    if parents[node] != node:
        return get_parent(parents, parents[node])

    return parents[node]


def union_parent(parents, node_a, node_b):
    parents[max(node_a, node_b)] = min(node_a, node_b)


def solution(n, costs):
    parents = [i for i in range(n)]
    total_costs = 0
    connected_edges = 0

    costs.sort(key=lambda x: x[2])

    for node_a, node_b, cost in costs:
        parent_a = get_parent(parents, node_a)
        parent_b = get_parent(parents, node_b)

        if parent_a != parent_b:
            union_parent(parents, parent_a, parent_b)
            connected_edges += 1
            total_costs += cost

        if connected_edges == n - 1:
            break

    return total_costs


result = solution(5, [[0, 1, 5], [2, 3, 3], [1, 2, 3], [3, 1, 2], [3, 0, 4], [2, 4, 6], [4, 0, 7]])
print(result)  # 실행결과: 15
