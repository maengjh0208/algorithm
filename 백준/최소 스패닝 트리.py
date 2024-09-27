import sys


def get_parent(parent_table: list, node_a: int) -> int:
    if parent_table[node_a] != node_a:
        return get_parent(parent_table, parent_table[node_a])

    return parent_table[node_a]


def union_parent(parent_table: list, parent_a: int, parent_b: int) -> None:
    parent_table[max(parent_a, parent_b)] = min(parent_a, parent_b)


def solution(node_count: int, edges: list) -> int:
    parent_table = [i for i in range(node_count + 1)]
    total_cost = 0
    selected_edge_count = 0

    edges.sort(key=lambda x: x[2])

    for node_a, node_b, cost in edges:
        parent_a = get_parent(parent_table, node_a)
        parent_b = get_parent(parent_table, node_b)

        if parent_a != parent_b:
            union_parent(parent_table, parent_a, parent_b)
            total_cost += cost
            selected_edge_count += 1

            if selected_edge_count == node_count - 1:
                break

    print(parent_table)
    return total_cost


if __name__ == "__main__":
    node_count, edge_count = map(int, input().split())

    edges = []
    for _ in range(edge_count):
        edges.append(list(map(int, sys.stdin.readline().split())))

    print(solution(node_count, edges))
