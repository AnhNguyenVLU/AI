# Hàm heuristic để ước lượng chi phí từ một điểm đến điểm khác
def heuristic(node, goal):
    # Sử dụng từ điển để lưu trữ các ước lượng heuristic
    heuristic_dict = {
        'A': 6,
        'B': 5,
        'C': 4,
        'D': 3,
        'E': 2,
        'F': 0
    }
    return heuristic_dict[node]

# Hàm heuristic search
def heuristic_search(graph, start, goal):
    # Khởi tạo hàng đợi ưu tiên và thêm điểm bắt đầu vào hàng đợi
    queue = [(0, start)]  #Sử dụng một danh sách thay cho hàng đợi ưu tiên
    visited = {}  #Sử dụng một từ điển để lưu trạng thái đã duyệt
    visited[start] = 0
    while queue:
        # Lấy điểm tiếp theo từ hàng đợi
        current_cost, current_node = queue.pop(0)
        # Nếu đã tìm thấy điểm đích, trả về chi phí tương ứng
        if current_node == goal:
            return current_cost
        # Xem xét các điểm kề của điểm hiện tại
        for neighbor, cost in graph[current_node].items():
            # Tính toán chi phí từ điểm bắt đầu đến điểm kề
            h_cost = heuristic(neighbor, goal)
            total_cost = current_cost + cost + h_cost
            # Nếu điểm kề chưa được duyệt hoặc có chi phí tốt hơn thì cập nhật
            if neighbor not in visited or total_cost < visited[neighbor]:
                visited[neighbor] = total_cost
                queue.append((total_cost, neighbor))
                # Sắp xếp lại hàng đợi dựa trên chi phí
                queue.sort(key=lambda x: x[0])
    # Nếu không tìm thấy đường đi từ điểm bắt đầu đến mục tiêu
    return None

# Đồ thị
graph = {
    'A': {'B': 2, 'C': 3},
    'B': {'D': 4, 'E': 3},
    'C': {'D': 1, 'E': 5},
    'D': {'F': 2},
    'E': {'F': 4},
    'F': {}
}
# Đường đi ngắn nhất từ 'A' đến 'F'
result = heuristic_search(graph, 'A', 'F')
print("Chi phí đường đi ngắn nhất:", result)
