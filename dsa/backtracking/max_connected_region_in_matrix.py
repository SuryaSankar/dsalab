# Given a matrix, each of which may be 1 or 0. The filled cells that are connected form a region. 
# Two cells are said to be connected if they are adjacent to each other horizontally, vertically or diagonally. 
# There may be several regions in the matrix. How do you find the largest region (in terms of number of cells) in the matrix?

# Example:
# Input:
# 1 0 1 1 0
# 1 1 0 1 0
# 0 0 1 0 0
# 0 0 0 1 1
# Output:
# 6

# Solution:
# The problem can be solved using Depth First Search (DFS) algorithm.
# The idea is to start from each cell that contains 1 and do DFS traversal of the matrix.
# The DFS traversal will be done for each cell that contains 1.

# The following steps are followed to find the largest region:
# 1. Create a variable maxRegion to store the maximum region size.
# 2. Traverse the matrix and for each cell that contains 1, do the following:
#     a. Create a variable size to store the size of the current region.
#     b. Call the DFS function with the current cell and size as arguments.
#     c. Update the maxRegion with the maximum of maxRegion and size.
# 3. The DFS function is defined as follows:
#     a. Check if the current cell is valid and contains 1.
#     b. Increment the size of the region.
#     c. Mark the current cell as visited.
#     d. Recursively call the DFS function for all the adjacent cells.
# 4. Return the maxRegion as the result.

# Complexity Analysis:
# The time complexity for this approach is O(m*n), where m is the number of rows and n is the number of columns in the matrix.
# The space complexity is O(m*n) for the visited array and the recursive stack.

# How to remember the pattern ?
# First define a max_size. This will be compared with the connected region size of each cell and max(size, max_size) will be stored in max_size.
# Then define a visited array to keep track of visited cells.
# Then define a is_valid function to check if the cell is valid or not.
# Then define a dfs function to do the DFS traversal of the matrix.
# In the dfs function, check if the cell is valid, contains 1 and not visited. If yes, mark it as visited and increment the size.
# Then do the DFS traversal for all the adjacent cells.
# Finally, iterate over the matrix and call the dfs function for each cell that contains 1 and update the max_size.



def max_connected_region(matrix):
    def is_valid(row, col):
        return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])
    
    def dfs(row, col):
        if not is_valid(row, col) or matrix[row][col] == 0 or visited[row][col]:
            return 0
        visited[row][col] = True
        size = 1
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]:
                size += dfs(row+x, col+y)
        return size

    max_size = 0
    visited = [[False for col in range(len(matrix[0]))] for row in range(len(matrix))]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1 and not visited[row][col]:
                size = dfs(row, col)
                max_size = max(size, max_size)
    return max_size

if __name__ == '__main__':
    # Test the function
    matrix = [
            [1, 0, 1, 1, 0],
            [1, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1]
        ]
    print(max_connected_region(matrix))  # Output: 6
    matrix = [
            [1, 0, 1, 1, 0],
            [1, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0]
        ]
    print(max_connected_region(matrix))  # Output: 5

