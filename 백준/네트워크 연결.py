# https://www.acmicpc.net/problem/1922
import sys


def get_parent_node(parent_table: list, node: int) -> int:
    if parent_table[node] != node:
        return get_parent_node(parent_table, parent_table[node])
    else:
        return parent_table[node]


def is_cycle(parent_table: list, node_a: int, node_b: int) -> bool:
    parent_a = get_parent_node(parent_table, node_a)
    parent_b = get_parent_node(parent_table, node_b)

    return parent_a == parent_b


def union(parent_table: list, node_a: int, node_b: int) -> None:
    a_parent = get_parent_node(parent_table, node_a)
    b_parent = get_parent_node(parent_table, node_b)

    parent_table[max(a_parent, b_parent)] = min(a_parent, b_parent)


def solution(computer_cnt: int, edge_cnt: int, costs: list) -> int:
    parent_table = [i for i in range(computer_cnt + 1)]

    total_cost = 0
    selected_edge_cnt = 0

    costs.sort(key=lambda x: x[0])

    for cost, node_a, node_b in costs:
        if not is_cycle(parent_table, node_a, node_b):
            union(parent_table, node_a, node_b)
            total_cost += cost
            selected_edge_cnt += 1

            if selected_edge_cnt == computer_cnt - 1:
                break

    return total_cost


if __name__ == "__main__":
    computer_cnt = int(input())
    edge_cnt = int(input())
    costs = []

    for _ in range(edge_cnt):
        node_a, node_b, cost = map(int, sys.stdin.readline().split())

        if node_a != node_b:
            costs.append([cost, node_a, node_b])

    result = solution(computer_cnt, edge_cnt, costs)
    print(result)
