from collections import deque

CAP_A = 4
CAP_B = 3
GOAL = 2


def print_state(state):
    print("Jug A:", state[0], "liters")
    print("Jug B:", state[1], "liters")
    print()


def get_neighbours(state):
    neighbours = []

    a, b = state

    
    if a < CAP_A:
        neighbours.append(((CAP_A, b), "Fill Jug A"))

    
    if b < CAP_B:
        neighbours.append(((a, CAP_B), "Fill Jug B"))

    
    if a > 0:
        neighbours.append(((0, b), "Empty Jug A"))

  
    if b > 0:
        neighbours.append(((a, 0), "Empty Jug B"))

   
    amount = min(a, CAP_B - b)
    if amount > 0:
        neighbours.append(((a - amount, b + amount), "Pour A -> B"))

    
    amount = min(b, CAP_A - a)
    if amount > 0:
        neighbours.append(((a + amount, b - amount), "Pour B -> A"))

    return neighbours


def bfs():
    start = (0, 0)

    queue = deque()
    queue.append((start, []))

    visited = set()
    visited.add(start)

    while queue:
        state, path = queue.popleft()

       
        if state[0] == GOAL or state[1] == GOAL:
            print("Solution:")
            print()

            print_state((0, 0))

            for action, new_state in path:
                print(action)
                print_state(new_state)

            return

        
        for new_state, action in get_neighbours(state):

            if new_state not in visited:
                visited.add(new_state)

                new_path = path + [(action, new_state)]

                queue.append((new_state, new_path))

    print("No solution found")


bfs()
