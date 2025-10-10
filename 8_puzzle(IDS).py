from collections import deque
# Manhattan Distance Heuristic
def manhattan_distance(state, goal):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            current_row, current_col = i // 3, i % 3
            goal_index = goal.index(state[i])
            goal_row, goal_col = goal_index // 3, goal_index % 3
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

# Define goal state
goal_state = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)  # 0 represents the blank tile

# Helper function to print puzzle in 3x3 grid
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

# Function to find possible moves (neighbors)
def get_neighbors(state):
    neighbors = []
    index = state.index(0)
    row, col = index // 3, index % 3
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for dx, dy in moves:
        new_row, new_col = row + dx, col + dy
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_index = new_row * 3 + new_col
            new_state = list(state)
            # Swap blank with target tile
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append(tuple(new_state))
    return neighbors

# Depth-Limited Search (DLS)
def depth_limited_search(state, goal, depth_limit, path, visited):
    print(f"Exploring state with Manhattan Distance = {manhattan_distance(state, goal)}")
    print_puzzle(state)

    if state == goal:
        return path

    if depth_limit == 0:
        return None

    visited.add(state)

    for neighbor in get_neighbors(state):
        if neighbor not in visited:
            result = depth_limited_search(neighbor, goal, depth_limit - 1, path + [neighbor], visited)
            if result is not None:
                return result

    return None


# Iterative Deepening Search (IDS)
def iterative_deepening_search(start, goal):
    depth = 0
    while True:
        visited = set()
        print(f"🔹 Searching at depth limit: {depth}")
        result = depth_limited_search(start, goal, depth, [start], visited)
        if result is not None:
            return result
        depth += 1

# Main function
def main():
    print("8-Puzzle Problem using Iterative Deepening Search (IDS)\n")
    print("Enter the start state as 9 numbers (0 for blank):")
    # Example input: 1 2 3 4 0 6 7 5 8
    start = tuple(map(int, input().strip().split()))

    print("\nStart State:")
    print_puzzle(start)
    print("Goal State:")
    print_puzzle(goal_state)

    solution_path = iterative_deepening_search(start, goal_state)

    if solution_path:
        print(f"✅ Solution found in {len(solution_path) - 1} moves:\n")
        for step, state in enumerate(solution_path):
            print(f"Step {step}:")
            print_puzzle(state)
    else:
        print("❌ No solution found.")

if __name__ == "__main__":
    main()
