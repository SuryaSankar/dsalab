# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. 
# The remaining elements of nums are not important as well as the size of nums.
# Return k.

from typing import List

class Solution:

    def _remove_duplicates(self, nums: List[int]) -> int:
        last_unique_idx = 0
        duplicates_count = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[last_unique_idx]:
                duplicates_count += 1
            else:
                last_unique_idx += 1
                nums[last_unique_idx] = nums[i]
        return len(nums) - duplicates_count



    def removeDuplicates(nums: List[int]) -> int:
        if not nums:
            return 0
            
        # slow pointer keeps track of where to place next unique element
        slow = 1
        
        # fast pointer finds next unique element
        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
        
        return slow
    
if __name__ == '__main__':
    solution = Solution()
    # Test 1
    nums = [1, 1, 2]
    # The first two elements of nums are 1, 2. Therefore the number of unique elements is 2.
    assert solution.removeDuplicates(nums) == 2
    # Test 2
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # The first five elements of nums are 0, 1, 2, 3, 4. Therefore the number of unique elements is 5.
    assert solution.removeDuplicates(nums) == 5
    print("All test cases passed successfully.")