from collections import deque

def min_time_to_exit(grid):
    rows, cols = len(grid), len(grid[0])

    # Find the starting position and the exits
    start_position = None
    exits = set()
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'S':
                start_position = (i, j)
            elif grid[i][j] == 'E' or ('a' <= grid[i][j] <= 'z'):
                exits.add((i, j))

    # Define the four possible directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Initialize the BFS queue with the starting position
    queue = deque([(start_position, 0)])

    # Mark the starting position as visited
    visited = set([start_position])

    while queue:
        (current_i, current_j), time = queue.popleft()

        # Check if the current position is an exit
        if (current_i, current_j) in exits:
            return time

        # Explore adjacent cells
        for di, dj in directions:
            new_i, new_j = current_i + di, current_j + dj

            # Check if the new position is within the grid and not a wall
            if 0 <= new_i < rows and 0 <= new_j < cols and grid[new_i][new_j] != '#':
                # If the new position is a portal, teleport to a cell with the same portal
                if 'a' <= grid[new_i][new_j] <= 'z':
                    portal_letter = grid[new_i][new_j]
                    for i in range(rows):
                        for j in range(cols):
                            if grid[i][j] == portal_letter:
                                new_position = (i, j)
                                if new_position not in visited:
                                    visited.add(new_position)
                                    queue.append((new_position, time + 1))
                else:
                    # Otherwise, move to the new position
                    new_position = (new_i, new_j)
                    if new_position not in visited:
                        visited.add(new_position)
                        queue.append((new_position, time + 1))

    # If no exit is reachable
    return -1

# Example usage:
grid = [
    "S.#.#",
    "#a#.#",
    "#...#",
    "#.E.#",
]
result = min_time_to_exit(grid)
print(result)
