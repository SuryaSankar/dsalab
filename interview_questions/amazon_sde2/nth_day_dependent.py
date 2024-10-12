# Data analysts at Amazon are analyzing time-series data. It was concluded that the data of the nth item was dependent 
# on the data of some xth day if there is a positive integer k such that floor(n/k) = x, where floor(z) represents the 
# largest integer less than or equal to z.

# Given n, find the sum of all the days' numbers on which the data of the xth ( 0≤ x ≤n) will be dependent.

from typing import List

class Solution:
    def sum_dependent_numbers(self, nums: List[int], n: int) -> int:
        valid_indices = set()
        for i in range(1, n+1):
            valid_indices.add(n//i - 1)
        print(valid_indices)
        sum = 0
        for idx in valid_indices:
            sum += nums[idx]
            print(f"summing {nums[idx]}")
        return sum


 # 8/7 =    

if __name__ == '__main__':
    solution = Solution()

    assert solution.sum_dependent_numbers([1, 3, 4, 5, 8, 9, 11, 13, 6], 6) == 19