# https://leetcode.com/problems/island-perimeter/

# Difficulty: Easy

# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

from typing import List

# class Solution:
#     def islandPerimeter(self, grid: List[List[int]]) -> int:
#         result = []
#         for row in range(len(grid)):
#             for col in range(len(grid[0])):
#                 if grid[row][col] == 1:
#                     top_edge = [(row, col), (row, col + 1)]
#                     right_edge = [(row, col+1), (row + 1, col+1)]
#                     bottom_edge = [(row + 1, col + 1), (row+1, col)]
#                     left_edge = [(row + 1, col), (row, col)]
#                     if top_edge not in result and list(reversed(top_edge)) not in result:
#                         result.append(top_edge)
#                     if right_edge not in result and list(reversed(right_edge)) not in result:
#                         result.append(right_edge)
#                     if bottom_edge not in result and list(reversed(bottom_edge)) not in result:
#                         result.append(bottom_edge)
#                     if left_edge not in result and list(reversed(left_edge)) not in result:
#                         result.append(left_edge)
#         print(result)
#         return len(result)

# Approach 1: Counting the number of edges
# Intuition
# The key observation in this approach is that the perimeter of the island can be counted by counting the number of edges that are connected to the water.

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    perimeter += 4
                    if row > 0 and grid[row-1][col] == 1:
                        perimeter -= 2 # subtract 2 because the two cells share an edge - one edge is counted twice
                    if col > 0 and grid[row][col-1] == 1:
                        perimeter -= 2
        return perimeter    

if __name__ == '__main__':
    solution = Solution()
    # Test 1
    grid = [
            [0, 1, 0, 0],
            [1, 1, 1, 0],
            [0, 1, 0, 0],
            [1, 1, 0, 0]
        ]
    # The perimeter is the sum of the lengths of the four edges of the island.
    # The perimeter is 16.
    print(solution.islandPerimeter(grid))  # Output: 16