goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()



def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row, col = divmod(zero, 3)

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col

            new_state = list(state)

            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors



def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_position = goal.index(state[i])

            current_row, current_col = divmod(i, 3)
            goal_row, goal_col = divmod(goal_position, 3)

            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)

    return distance



def astar(start):


    queue = [(heuristic(start), 0, start, [])]

    visited = set()

    while queue:

       
        queue.sort()

        f, g, state, path = queue.pop(0)

        if state in visited:
            continue

        visited.add(state)

        if state == goal:
            return path + [state]

        for neighbor in get_neighbors(state):

            if neighbor not in visited:

                new_g = g + 1
                new_h = heuristic(neighbor)
                new_f = new_g + new_h

                queue.append(
                    (new_f, new_g, neighbor, path + [state])
                )

    return None


start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)



solution = astar(start)



if solution:

    print("Solution found in", len(solution) - 1, "moves:\n")

    for step in solution:
        print_board(step)

else:
    print("No solution found.")