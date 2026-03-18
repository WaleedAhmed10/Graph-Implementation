import heapq
import copy

class PuzzleState:
    def __init__(self, board, parent=None, move="", depth=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.blank = self.find_blank()
    
    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)
    
    def heuristic(self):
        dist = 0
        for i in range(3):
            for j in range(3):
                val = self.board[i][j]
                if val != 0:
                    target_i = (val - 1) // 3
                    target_j = (val - 1) % 3
                    dist += abs(i - target_i) + abs(j - target_j)
        return dist
    
    def get_successors(self):
        successors = []
        i, j = self.blank
        moves = {'Up': (-1,0), 'Down': (1,0), 'Left': (0,-1), 'Right': (0,1)}
        
        for move, (di, dj) in moves.items():
            new_i, new_j = i + di, j + dj
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_board = copy.deepcopy(self.board)
                new_board[i][j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[i][j]
                successors.append(PuzzleState(new_board, self, move, self.depth + 1))
        
        return successors
    
    def is_goal(self):
        return self.board == [[1,2,3], [4,5,6], [7,8,0]]
    
    def __lt__(self, other):
        return False
    
    def __eq__(self, other):
        return self.board == other.board
    
    def __hash__(self):
        return hash(str(self.board))

class Agent:
    def solve(self, initial_board):
        start = PuzzleState(initial_board)
        open_set = [(start.heuristic(), 0, start)]
        closed_set = set()
        counter = 1        
        while open_set:
            f, _, current = heapq.heappop(open_set)            
            if current.is_goal():
                return self.get_path(current)
            
            closed_set.add(current)
            
            for successor in current.get_successors():
                if successor in closed_set:
                    continue                
                g = successor.depth
                h = successor.heuristic()
                f = g + h
                in_open = False
                for i, (old_f, _, state) in enumerate(open_set):
                    if successor == state:
                        in_open = True
                        if f < old_f:
                            open_set[i] = (f, counter, successor)
                            heapq.heapify(open_set)
                        break                
                if not in_open:
                    heapq.heappush(open_set, (f, counter, successor))
                    counter += 1
        return None
    
    def get_path(self, state):
        path = []
        while state.parent:
            path.append((state.move, state.board))
            state = state.parent
        return list(reversed(path))

def print_board(board):
    for row in board:
        print(" ".join(str(x) if x != 0 else " " for x in row))

if __name__ == "__main__":
    initial = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 0, 8]
    ]    
    print("Initial State:")
    print_board(initial)
    print("\nSolving...\n")    
    agent = Agent()
    solution = agent.solve(initial)
    
    if solution:
        print("Solution Path:")
        for i, (move, board) in enumerate(solution):
            print(f"Step {i+1}: Move {move}")
            print_board(board)
            print()
        print(f"Total moves (cost): {len(solution)}")
    else:
        print("No solution found")