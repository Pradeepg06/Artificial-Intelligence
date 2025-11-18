from collections import deque

# ----- Utility: Print Puzzle -----
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])
    print()

# ----- Allowed moves for blank (0) -----
moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

# ----- Generate children states -----
def generate_states(state):
    zero = state.index(0)
    new_states = []
    
    for move_pos in moves[zero]:
        new_state = list(state)
        new_state[zero], new_state[move_pos] = new_state[move_pos], new_state[zero]
        new_states.append(tuple(new_state))
    
    return new_states

# ----- DFS Search -----
def dfs(start, goal, limit=50000):
    stack = [(start, [start])]
    visited = set()
    
    while stack and len(visited) < limit:
        state, path = stack.pop()

        if state in visited:
            continue
        visited.add(state)

        if state == goal:
            return path

        for next_state in generate_states(state):
            if next_state not in visited:
                stack.append((next_state, path + [next_state]))

    return None


# ------------ MAIN PROGRAM WITH USER INPUT ---------------
def read_puzzle(prompt):
    print(prompt)
    arr = list(map(int, input().split()))
    if len(arr) != 9:
        raise ValueError("You must enter exactly 9 numbers.")
    return tuple(arr)

# User input
start = read_puzzle("Enter start state (9 numbers, 0 = blank):")
goal = read_puzzle("Enter goal state (9 numbers, 0 = blank):")

solution = dfs(start, goal)

if solution:
    print("\nSolution found in", len(solution)-1, "moves:\n")
    for s in solution:
        print_puzzle(s)
else:
    print("No solution found or depth limit reached.")

