# https://leetcode.com/problems/3sum/description/
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
# i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

class Solution:

    def _two_sum_sorted(self, nums, start_idx, end_idx, target):
        left = start_idx
        right = end_idx

        pairs = []

        while left < right:
            if nums[left] + nums[right] == target:
                pairs.append((left, right))
                left += 1
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return pairs
            
            


    def three_sum_sub_optimal(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            target = - nums[i]
            for idx1, idx2 in self._two_sum_sorted(nums, i + 1, len(nums) - 1, target):
                triplet = [nums[i], nums[idx1], nums[idx2]]
                if triplet not in result:
                    result.append(triplet)
        return result

    def three_sum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1
        return result




if __name__ == '__main__':
    solution = Solution()
    # Test 1
    nums = [-1, 0, 1, 2, -1, -4]
    # The solution set is:
    # [
    #   [-1, -1, 2],
    #   [-1, 0, 1]
    # ]
    print(solution.three_sum(nums))
    assert solution.three_sum(nums) == [[-1, -1, 2], [-1, 0, 1]]
    # Test 2
    nums = []
    assert solution.three_sum(nums) == []
    print(solution.three_sum(nums))
    # Test 3
    nums = [0]
    print(solution.three_sum(nums))
    assert solution.three_sum(nums) == []
    print("All test cases passed successfully.")