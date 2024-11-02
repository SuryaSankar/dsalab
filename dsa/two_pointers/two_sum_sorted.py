# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
        return []
    
if __name__ == '__main__':
    solution = Solution()
    # Test 1
    numbers = [2, 7, 11, 15]
    target = 9
    # The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
    assert solution.twoSum(numbers, target) == [1, 2]
    # Test 2
    numbers = [2, 3, 4]
    target = 6
    # The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3.
    assert solution.twoSum(numbers, target) == [1, 3]
    print("All test cases passed successfully.")