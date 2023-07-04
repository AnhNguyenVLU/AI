G = [[0, 2, 2, 5, 3],
     [2, 0, 1, 4, 4],
     [2, 1, 0, 3, 5],
     [5, 4, 3, 0, 9],
     [3, 4, 5, 9, 0]]

INF = float('inf')
N = len(G)
S = []  # Visited nodes
dist = [INF] * N  # Shortest distances from the source
dist[0] = 0  # Distance from source to itself is 0
previous = [None] * N  # Previous node in the shortest path

def get_min_distance(dist, visited):
    min_dist = INF
    min_node = None
    for v in range(N):
        if not visited[v] and dist[v] < min_dist:
            min_dist = dist[v]
            min_node = v
    return min_node

def dijkstra(G, source):
    visited = [False] * N

    for _ in range(N):
        u = get_min_distance(dist, visited)
        if u is None:
            break
        visited[u] = True

        for v in range(N):
            if G[u][v] != 0 and not visited[v]:
                new_dist = dist[u] + G[u][v]
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    previous[v] = u

# Run Dijkstra's algorithm
dijkstra(G, 0)
# Print the shortest path and distance for each vertex
for v in range(N):
    path = []
    current = v
    while current is not None:
        path.insert(0, current)
        current = previous[current]
    print("Shortest path to vertex", v, ":", path)
    print("Distance:", dist[v])
