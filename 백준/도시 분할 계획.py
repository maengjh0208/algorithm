import sys


def get_parent(parent: list, node: int):
    if parent[node] != node:
        parent[node] = get_parent(parent, parent[node])

    return parent[node]


def union(parent: list, parent_a: int, parent_b: int) -> None:
    parent[max(parent_a, parent_b)] = min(parent_a, parent_b)


def solution(house: int, connections: list) -> int:
    parent = [i for i in range(house + 1)]

    total_cost = 0
    connected_edge_count = 0

    connections.sort(key=lambda x: x[2])

    for node_a, node_b, cost in connections:
        if connected_edge_count == house - 2:
            break

        parent_a = get_parent(parent, node_a)
        parent_b = get_parent(parent, node_b)

        if parent_a != parent_b:
            union(parent, parent_a, parent_b)
            total_cost += cost
            connected_edge_count += 1

        if connections == house - 2:
            break

    return total_cost


if __name__ == "__main__":
    house, road = map(int, input().split())

    connections = []
    for _ in range(road):
        connections.append(list(map(int, sys.stdin.readline().split())))

    result = solution(house, connections)
    print(result)
