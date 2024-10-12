# https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
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

if __name__ == '__main__':
    sol = Solution()
    print(sol.sortedSquares([-4, -1, 0, 3, 10])) # [0, 1, 9, 16, 100]