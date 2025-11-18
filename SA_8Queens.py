import random
import math

N = 8  # 8-Queens

def random_state():
    return [random.randint(0, N-1) for _ in range(N)]

def cost(state):
    attacks = 0
    for i in range(N):
        for j in range(i+1, N):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return attacks

def random_neighbor(state):
    neighbor = state[:]
    col = random.randint(0, N-1)
    new_row = random.randint(0, N-1)
    neighbor[col] = new_row
    return neighbor

def simulated_annealing():
    T = 100.0
    alpha = 0.99
    current = random_state()

    while T > 0.001:
        next_state = random_neighbor(current)
        delta = cost(next_state) - cost(current)

        if delta < 0:
            current = next_state
        else:
            prob = math.exp(-delta / T)
            if random.random() < prob:
                current = next_state

        T *= alpha

    return current

# ----- RUN SIMULATED ANNEALING -----
solution = simulated_annealing()
print("Final state:", solution)
print("Conflicts:", cost(solution))
