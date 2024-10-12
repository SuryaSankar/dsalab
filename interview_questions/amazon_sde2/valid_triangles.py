# https://leetcode.com/problems/valid-triangle-number/

# Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them 
# as side lengths of a triangle.

# Example 1:
# Input: nums = [2,2,3,4]
# Output: 3

# Explanation: Valid combinations are:
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3

# Example 2:
# Input: nums = [4,2,3,4]
# Output: 4

# Constraints:
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 1000

# Approach:
# The key observation in this approach is that the sum of the lengths of any two sides of a triangle must be greater than the length of the third side.
# Therefore, we can iterate through all possible combinations of three sides of the triangle and check if the sum of the lengths of any two sides is greater than the length of the third side.
# If the above condition is satisfied, we increment a counter to count the number of valid triangles.

# Optimal approach:
# The above approach has a time complexity of O(n^3), where n is the number of elements in the input array.
# We can optimize the above approach by sorting the input array and using the two-pointer technique to find the valid triangles in O(n^2) time complexity.
# The two-pointer technique involves iterating through the input array and using two pointers to find the valid triangles.



from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        num_triangles = 0
        for k in range(2, len(nums)):
            left, right = 0, k-1
            while left < right:
                if nums[left] + nums[right] > nums[k]:
                    num_triangles += right - left
                    right -= 1
                else:
                    left += 1
        return num_triangles


# class Solution:
#     def triangleNumber(self, nums: List[int]) -> int:
#         num_triangles = 0
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 for k in range(j+1, len(nums)):
#                     sides = [nums[i], nums[j], nums[k]]
#                     sides.sort()
#                     if sides[0] + sides[1] > sides[2]:
#                         num_triangles += 1
#         return num_triangles
    
if __name__ == '__main__':
    solution = Solution()
    # Test 1
    nums = [2, 2, 3, 4]
    # Valid combinations are:
    # 2,3,4 (using the first 2)
    # 2,3,4 (using the second 2)
    # 2,2,3
    assert solution.triangleNumber(nums) == 3
    # Test 2
    nums = [4, 2, 3, 4]
    # Valid combinations are:
    # 4,2,3
    # 4,3,4
    # 2,3,4
    # 3,4,4
    assert solution.triangleNumber(nums) == 4
    print("All test cases passed successfully.")