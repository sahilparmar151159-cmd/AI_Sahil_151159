CAP_A = 4
CAP_B = 3
GOAL = 2

def print_state(state):
    print("Jug A:", state[0], "liters")
    print("Jug B:", state[1], "liters")
    print()


def get_neighbors(state):
    neighbors = []
    a, b = state

    # 1. Fill Jug A
    if a < CAP_A:
        neighbors.append(((CAP_A, b), "Fill Jug A"))

    # 2. Fill Jug B
    if b < CAP_B:
        neighbors.append(((a, CAP_B), "Fill Jug B"))

    # 3. Empty Jug A
    if a > 0:
        neighbors.append(((0, b), "Empty Jug A"))

    # 4. Empty Jug B
    if b > 0:
        neighbors.append(((a, 0), "Empty Jug B"))

    # 5. Pour Jug A -> Jug B
    amount_ab = min(a, CAP_B - b)
    if amount_ab > 0:
        neighbors.append(
            ((a - amount_ab, b + amount_ab),
             "Pour Jug A -> Jug B")
        )

    # 6. Pour Jug B -> Jug A
    amount_ba = min(b, CAP_A - a)
    if amount_ba > 0:
        neighbors.append(
            ((a + amount_ba, b - amount_ba),
             "Pour Jug B -> Jug A")
        )

    return neighbors


# DFS
def dfs(start):
    stack = [(start, [])]
    visited = set()

    while stack:
        # DFS uses pop() from the end
        state, path = stack.pop()

        if state in visited:
            continue

        visited.add(state)

        # Check goal
        if state[0] == GOAL or state[1] == GOAL:
            return path + [(state, "Goal Reached")]

        for neighbor, action in get_neighbors(state):
            if neighbor not in visited:
                stack.append(
                    (neighbor, path + [(neighbor, action)])
                )

    return None


# Execute DFS
start = (0, 0)
solution = dfs(start)

if solution:
    print(f"Solution found in {len(solution) - 1} moves:\n")

    print("Initial State:")
    print_state(start)

    for state, action in solution:
        print(action)
        print_state(state)
else:
    print("No Solution found.")