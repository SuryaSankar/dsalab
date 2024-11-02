# https://leetcode.com/problems/squares-of-a-sorted-array/description/
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

from typing import List

class Solution:
    def sorted_squares_using_stack(self, nums: List[int]) -> List[int]:
        stack = []
        idx = 0
        while idx < len(nums) and nums[idx] < 0:
            stack.append(nums[idx]**2)
            idx += 1
        result = []
        while idx < len(nums):
            candidate = nums[idx]**2
            if len(stack)==0:
                result.append(candidate)
                idx += 1
                continue
            
            while len(stack) > 0 and stack[-1] < candidate:
                result.append(stack.pop())
            result.append(candidate)
            idx += 1
        while len(stack) > 0:
            result.append(stack.pop())        
        return result
    
    def sorted_squares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        result = [0] * len(nums)
        result_idx = len(nums) - 1

        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            if left_square > right_square:
                result[result_idx] = left_square
                left += 1
            else:
                result[result_idx] = right_square
                right -= 1
            result_idx -= 1
        return result

    # def sorted_squares(self, nums: List[int]) -> List[int]:
    #     result = []
    #     right = 0
    #     while nums[right] < 0 and right < len(nums):
    #         right += 1
    #     left = right - 1
    #     while left >= 0 and right < len(nums):
    #         if nums[right]**2 < nums[left]**2:
    #             result.append(nums[right]**2)
    #             right += 1
    #         else:
    #             result.append(nums[left]**2)
    #             left -= 1
    #     if left == 0:
    #         while right < len(nums):
    #             result.append(nums[right]**2)
    #             right += 1
    #     if right == len(nums):
    #         while left >= 0:
    #             result.append(nums[left]**2)
    #             left -= 1
    #     return result


if __name__ == '__main__':
    solution = Solution()
    # Test 1
    nums = [-4, -1, 0, 3, 10]
    # The squares of the numbers are [16, 1, 0, 9, 100]. Therefore the sorted squares are [0, 1, 9, 16, 100].
    assert solution.sorted_squares(nums) == [0, 1, 9, 16, 100]
    # Test 2
    nums = [-7, -3, 2, 3, 11]
    # The squares of the numbers are [49, 9, 4, 9, 121]. Therefore the sorted squares are [4, 9, 9, 49, 121].
    assert solution.sorted_squares(nums) == [4, 9, 9, 49, 121]
    print("All test cases passed successfully.")