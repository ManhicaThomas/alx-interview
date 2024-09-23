#!/usr/bin/python3
"""Island per computing mod.
"""


def island_perimeter(grid):
    """Calculates the perimeter of the island in the given grid.

    Args:
        grid: A list of lists of integers representing the island and water.

    Returns:
        The perimeter of the island.
    """

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check for adjacent water cells
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
