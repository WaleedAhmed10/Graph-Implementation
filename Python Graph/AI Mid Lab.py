import heapq

graph = {
    'S': [('A', 2), ('B', 5)],
    'A': [('C', 3), ('G', 10)],
    'B': [('D', 2), ('E', 4)],
    'C': [('G', 4), ('D', 1)] ,
    'D': [('G', 6)],
    'G': []
}

heuristics = {
    'S': 0,
    'A': 2,
    'B': 5,
    'C': 5,
    'D': 7,
    'E': 9,
    'G': 9
}

def a_star(start, goal):
    "A* Search using a priority queue"
    open_set = [(heuristics[start], start, [start])]
    closed_set = set()
    expanded = 0
    cost = 15
    while open_set:
        f_max, node, path = heapq.heappop(open_set)
        if node == goal:
            return path, expanded
        if node not in closed_set:
            closed_set.add(node)
            for neighbor, cost in graph[node]:
                if neighbor not in closed_set:
                    init_fuel = f_max - heuristics[node] + cost  # Initial fuel: Maximum fuel+ h(Last Digit of your ID)
                    f_max = init_fuel + heuristics[neighbor]  # Max fuel = Initialfuel + h(n)
                    heapq.heappush(open_set, (f_max, neighbor, path + [neighbor]))
                    expanded += 1
    return None, expanded


if __name__ == "__main__":
    path, expanded = a_star('S', 'G')
    print('path:', path)
    print('expanded:', expanded)
