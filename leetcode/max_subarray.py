# https://leetcode.com/problems/maximum-subarray

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float("-inf")
        iSum = 0
        for i in range(len(nums)):
            iSum += nums[i]
            if iSum > maxSum:
                maxSum = iSum
            if iSum < 0:
                iSum = 0
        return maxSum
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSubArray([-2,-1,-3,-4,-1,-2,-1,-5,-4])) # -1

# The time complexity is O(n) and the space complexity is O(1).
# The time complexity is O(n) because we iterate through the list of numbers once.
# The space complexity is O(1) because we only use a constant amount of space to store the maximum sum and the current sum.
# The algorithm works by keeping track of the current sum of the subarray that we are considering.
# If the current sum becomes negative, we reset it to 0, since a negative sum will not contribute to the maximum sum.
# We also keep track of the maximum sum that we have seen so far, and update it whenever the current sum is greater than the maximum sum.
# At the end of the iteration, the maximum sum will be the maximum subarray sum.
# The algorithm is efficient because it only requires a single pass through the list of numbers, and does not require any additional space to store intermediate results.
# The algorithm is also correct, as it correctly computes the maximum subarray sum for any given list of numbers.
# The algorithm is optimal, as it achieves the maximum subarray sum in linear time and constant space.
# The algorithm is also easy to understand and implement, making it a good choice for solving the maximum subarray problem.
