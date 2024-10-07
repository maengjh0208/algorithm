# DFS 구현 (재귀적)
def dfs(graph: dict, start: str, visited: set = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')  # 방문한 노드 출력

    # 인접한 노드 중 아직 방문하지 않은 노드를 재귀적으로 방문
    for next_node in graph[start]:
        if next_node not in visited:
            dfs(graph, next_node, visited)


# DFS 구현 (스택 사용)
def dfs_stack(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            print(node, end=' ')
            # stack.extend(graph[node]) 으로 해도 상관 없음. 위의 dfs()와 동일한 순서로 방문하게끔 하려고 reversed 추가한 것
            stack.extend(reversed(graph[node]))


# 예시 그래프 (인접 리스트 표현)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

dfs_stack(graph, 'A')
