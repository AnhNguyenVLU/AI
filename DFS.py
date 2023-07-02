def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Đồ thị
graph = {
    '1': ['2'],
    '2': ['7', '4'],
    '3': ['4'],
    '4': ['6'],
    '5': ['4', '3'],
    '6': [],
    '7': ['5']
}

# Chạy thuật toán DFS từ đỉnh 1
dfs(graph, '1')
