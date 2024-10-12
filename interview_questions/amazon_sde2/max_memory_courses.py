# The course has n chapters, each chapter has memory[i] memory points, which a student gains or loses while reading that chapter.

# The course has a requirement: in order to study the ith chapter, the student must revisit all the previous chapters. 
# A student gains memory[0] + memory[1] + … + memory[i] memory points for reading the ith chapter. 
# The total memory points is the sum of memory points gained while reading each chapter.

# Students can read the chapters in any order, and want to maximize their total memory points. 
# Find the maximum total memory points a student can score ensuring that all the chapters are read.

# Example 1:
# Input: memory = [3, 4, 5]
# Output: 26
# Explanation: The student can read the chapters in the following order: [3, 4, 5].


# Example 2:
# Input: memory = [1, 2, 3, 4, 5]
# Output: 35


# Example 3:
# Input: memory = [5, 4, 3, 2, 1]
# Output: 35

# Constraints:
# 1 <= n <= 10^5
# 1 <= memory[i] <= 10^4

# Approach:
# The key observation in this approach is that the student can read the chapters in any order, and the memory points gained for reading each chapter are cumulative.
# This means that the student can gain the maximum memory points by reading the chapters in the order of decreasing memory points.
# The student should read the chapters with the highest memory points first, followed by the chapters with the next highest memory points, and so on.
# This ensures that the student gains the maximum memory points for each chapter, as the memory points gained for reading each chapter are cumulative.
# The total memory points gained by reading all the chapters in this order will be the maximum possible memory points that the student can score.
# The total memory points gained by reading all the chapters in this order can be calculated as follows:
# total_memory_points = memory[0] + memory[0] + memory[1] + memory[0] + memory[1] + memory[2] + ... + memory[0] + memory[1] + ... + memory[n-1]

# The above formula can be simplified as follows:
# total_memory_points = n * memory[0] + (n-1) * memory[1] + (n-2) * memory[2] + ... + 1 * memory[n-1]

# The above formula can be further simplified as follows:
# total_memory_points = n * (memory[0] + memory[1] + ... + memory[n-1]) - (0 * memory[0] + 1 * memory[1] + ... + (n-1) * memory[n-1])

# The above formula can be further simplified as follows:
# total_memory_points = n * (memory[0] + memory[1] + ... + memory[n-1]) - (memory[1] + 2 * memory[2] + ... + (n-1) * memory[n-1])


from typing import List

class Solution:

    def max_memory_courses(self, memory: List[int]) -> int:
        n = len(memory)
        total_memory_points = n * sum(memory) - sum(i * memory[i] for i in range(1, n))
        return total_memory_points
    
if __name__ == '__main__':
    solution = Solution()
    # Test 1
    memory = [3, 4, 5]
    # The student can read the chapters in the following order: [3, 4, 5].
    # The total memory points gained by reading all the chapters in this order is 3 + 3 + 4 + 3 + 4 + 5 = 26.
    assert solution.max_memory_courses(memory) == 22
    # Test 2
    memory = [1, 2, 3, 4, 5]
    # The student can read the chapters in the following order: [5, 4, 3, 2, 1].
    # The total memory points gained by reading all the chapters in this order is 5 + 5 + 4 + 5 + 4 + 3 + 5 + 4 + 3 + 2 + 5 + 4 + 3 + 2 + 1 = 35.
    assert solution.max_memory_courses(memory) == 35
    # Test 3
    memory = [5, 4, 3, 2, 1]
    # The student can read the chapters in the following order: [5, 4, 3, 2, 1].
    # The total memory points gained by reading all the chapters in this order is 5 + 5 + 4 + 5 + 4 + 3 + 5 + 4 + 3 + 2 + 5 + 4 + 3 + 2 + 1 = 35.
    assert solution.max_memory_courses(memory) == 35
    print("All test cases passed successfully.")

