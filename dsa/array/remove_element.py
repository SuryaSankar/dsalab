# https://leetcode.com/problems/remove-element
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
# The remaining elements of nums are not important as well as the size of nums.
# Return k.
from typing import List

class Solution:

    def remove_element(self, nums: List[int], val: int) -> int:
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                del nums[i]
        return len(nums)

if __name__ == '__main__':
    solution = Solution()
    # Test 1
    nums = [3, 2, 2, 3]
    val = 3
    # nums after removing 3 is [2, 2]. Therefore the number of elements in nums which are not equal to 3 is 2.
    assert solution.remove_element(nums, val) == 2
    # Test 2
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    # nums after removing 2 is [0, 1, 3, 0, 4]. Therefore the number of elements in nums which are not equal to 2 is 5.
    assert solution.remove_element(nums, val) == 5
    print("All test cases passed successfully.")