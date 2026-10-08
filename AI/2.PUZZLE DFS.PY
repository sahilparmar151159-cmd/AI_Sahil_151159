goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()


def get_neighbours(state):
    neighbors = []

    zero = state.index(0)
    row, col = divmod(zero, 3)

  
    moves = [
        (-1, 0),  
        (1, 0),   
        (0, -1),  
        (0, 1)    
    ]

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


def dfs(start):
    stack = [(start, [start])]
    visited = set()

    while stack:
        state, path = stack.pop()

        
        if state in visited:
            continue

        visited.add(state)

        
        if state == goal:
            return path

        
        for neighbor in get_neighbours(state):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None



start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)



solution = dfs(start)



if solution:
    print("Solution found!")
    print("Number of moves:", len(solution) - 1)
    print()

    for step, state in enumerate(solution):
        print("Step", step)
        print_board(state)
else:
    print("No solution found.")
