# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

from typing import List

class Solution:
    def brute_force_solution(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
    def hashmap_solution(self, nums: List[int], target: int) -> List[int]:
        nums_map = {nums[i] : i for i in range(len(nums))}
        print(nums_map)
        for idx, num in enumerate(nums):
            complement = target - num
            if complement in nums_map and nums_map[complement] != idx:
                return [idx, nums_map[complement]]
        return []

    
if __name__ == '__main__':
    solution = Solution()
    # Test 1
    nums = [2, 7, 11, 15]
    target = 9
    assert solution.brute_force_solution(nums, target) == [0, 1]
    assert solution.hashmap_solution(nums, target) == [0, 1]
    # Test 2
    nums = [3, 2, 4]
    target = 6
    assert solution.brute_force_solution(nums, target) == [1, 2]
    assert solution.hashmap_solution(nums, target) == [1, 2]
    # Test 3
    nums = [3, 3]
    target = 6
    assert solution.brute_force_solution(nums, target) == [0, 1]
    assert solution.hashmap_solution(nums, target) == [0, 1]
    print("All test cases passed successfully.")

