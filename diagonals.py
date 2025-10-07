def extract_four_element_diagonals(grid):
    """Extracts all four-element diagonals from a 2D grid (list of lists).
    Includes diagonals in all four directions:
    
    - Down-right (↘)
    - Up-right (↗)
    - Down-left (↙)
    - Up-left (↖)
    
    Assumes the grid is rectangular and at least 4x4 in size.
    
    Returns:
        A list of lists, where each inner list is a four-element diagonal.

        This function was generated from Co-pilot, September 24th 2025. (Paul Barry).
    """
    diagonals = []

    rows = len(grid)
    cols = len(grid[0])

    # Down-right (↘)
    for row in range(rows - 3):
        for col in range(cols - 3):
            diagonals.append([grid[row + i][col + i] for i in range(4)])

    # Up-right (↗)
    for row in range(3, rows):
        for col in range(cols - 3):
            diagonals.append([grid[row - i][col + i] for i in range(4)])

    # Down-left (↙)
    for row in range(rows - 3):
        for col in range(3, cols):
            diagonals.append([grid[row + i][col - i] for i in range(4)])

    # Up-left (↖)
    for row in range(3, rows):
        for col in range(3, cols):
            diagonals.append([grid[row - i][col - i] for i in range(4)])

    return diagonals
