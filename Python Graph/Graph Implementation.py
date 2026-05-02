import heapq
from collections import deque

graph = {
    'S': [('B_top', 4), ('B_bottom', 3), ('C', 2)],
    'B_top': [('E', 3), ('F', 5)],
    'B_bottom': [('E', 2), ('F', 4)],
    'C': [('E', 4), ('F', 3)],
    'E': [('G', 2)],
    'F': [('G', 3)],
    'G': []
}

heuristic = {
    'S': 4,
    'B_top': 3,
    'B_bottom': 3,
    'C': 3,
    'E': 2,
    'F': 2,
    'G': 0
}

def dfs(start, goal):
    """Depth-First Search using a stack"""
    stack = [(start, [start])]  # (current_node, path_so_far)
    visited = set()
    expanded = 0
    
    while stack:
        node, path = stack.pop()
        expanded += 1
        
        if node == goal:
            return path, expanded
        
        if node not in visited:
            visited.add(node)
            # Add neighbors to stack
            for neighbor, _ in graph[node]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    
    return None, expanded

def bfs(start, goal):
    """Breadth-First Search using a queue"""
    queue = deque([(start, [start])])  # (current_node, path_so_far)
    visited = set()
    expanded = 0
    
    while queue:
        node, path = queue.popleft()
        expanded += 1
        
        if node == goal:
            return path, expanded
        
        if node not in visited:
            visited.add(node)
            # Add neighbors to queue
            for neighbor, _ in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    
    return None, expanded

def a_star(start, goal):
    """A* Search using a priority queue"""
    # f = g + h
    pq = [(heuristic[start], 0, start, [start])]
    visited = set()
    expanded = 0
    g_values = {start: 0}
    
    while pq:
        f, g, node, path = heapq.heappop(pq)
        expanded += 1
        
        if node == goal:
            return path, expanded, g  # g is total cost
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node]:
                new_g = g + weight
                if neighbor not in g_values or new_g < g_values[neighbor]:
                    g_values[neighbor] = new_g
                    f = new_g + heuristic[neighbor]
                    heapq.heappush(pq, (f, new_g, neighbor, path + [neighbor]))    
    return None, expanded, 0

print("=" * 50)
print("DFS RESULT:")
path, expanded = dfs('S', 'G')
print(f"Path: {' -> '.join(path)}")
print(f"Nodes expanded: {expanded}")
print("\n" + "=" * 50)
print("BFS RESULT:")
path, expanded = bfs('S', 'G')
print(f"Path: {' -> '.join(path)}")
print(f"Nodes expanded: {expanded}")
print("\n" + "=" * 50)
print("A* RESULT:")
path, expanded, cost = a_star('S', 'G')
print(f"Path: {' -> '.join(path)}")
print(f"Total cost: {cost}")
print(f"Nodes expanded: {expanded}")
print("\n" + "=" * 50)
print("ALGORITHM COMPARISON")
print("=" * 50)