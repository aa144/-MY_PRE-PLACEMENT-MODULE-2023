class Solution:
    # example:
    # [
    #  [0,0,1,0,0,0,0,1,0,0,0,0,0],
    #  [0,0,0,0,0,0,0,1,1,1,0,0,0],
    #  [0,1,1,0,1,0,0,0,0,0,0,0,0],
    #  [0,1,0,0,1,1,0,0,1,0,1,0,0],
    #  [0,1,0,0,1,1,0,0,1,1,1,0,0],
    #  [0,0,0,0,0,0,0,0,0,0,1,0,0],
    #  [0,0,0,0,0,0,0,1,1,1,0,0,0],
    #  [0,0,0,0,0,0,0,1,1,0,0,0,0]
    # ]
        
    def traverse_island(self, x, y):
        self.grid[x][y] = 0 # mark as visited
        cells_num = 1
        
        # top
        if 0 <= x < self.rows_num and 0 < y <= self.columns_num and self.grid[x][y-1]:
            cells_num += self.traverse_island(x, y-1)
            
        # left
        if 0 < x <= self.rows_num and 0 <= y < self.columns_num and self.grid[x-1][y]:
            cells_num += self.traverse_island(x-1, y)
        
        # bottom
        if 0 <= x < self.rows_num and 0 <= y < self.columns_num - 1 and self.grid[x][y+1]:
            cells_num += self.traverse_island(x, y+1)
        
        # right
        if 0 <= x < self.rows_num - 1 and 0 <= 0 < self.columns_num and self.grid[x+1][y]:
            cells_num += self.traverse_island(x + 1, y)
            
        return cells_num

            
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.rows_num = len(grid)
        max_area = 0
        for i in range(self.rows_num):
            self.columns_num = len(grid[i])
            for j in range(self.columns_num):
                if self.grid[i][j]: # found unvisited island
                    cells_num = self.traverse_island(i, j)
                    if cells_num > max_area:
                        max_area = cells_num
                        
        return max_area