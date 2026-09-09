class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        Calculate the perimeter of an island in a 2D grid.
      
        Args:
            grid: 2D list where 1 represents land and 0 represents water
          
        Returns:
            The total perimeter of the island
        """
        # Get grid dimensions
        rows, cols = len(grid), len(grid[0])
        total_perimeter = 0
      
        # Iterate through each cell in the grid
        for row in range(rows):
            for col in range(cols):
                # Check if current cell is land
                if grid[row][col] == 1:
                    # Each land cell contributes 4 sides initially
                    total_perimeter += 4
                  
                    # Check if there's land below (subtract shared edge)
                    if row < rows - 1 and grid[row + 1][col] == 1:
                        # Subtract 2 (1 from current cell, 1 from neighbor)
                        total_perimeter -= 2
                  
                    # Check if there's land to the right (subtract shared edge)
                    if col < cols - 1 and grid[row][col + 1] == 1:
                        # Subtract 2 (1 from current cell, 1 from neighbor)
                        total_perimeter -= 2
      
        return total_perimeter
