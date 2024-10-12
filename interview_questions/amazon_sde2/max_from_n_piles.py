# Amazon Fresh is a new grocery store designed from the ground up to offer a seamless grocery shopping experience to consumers.

# As part of a stock clearance exercise at the store, given many piles of fresh products, follow the rules given below to stack 
# the products in an orderly manner.

# There are a total of n piles of products. The number of products in each pile is represented by the array numProducts. 
# Select any subarray from the array numProducts and pick up products from each pile. The number of products you pick from 
# the i th pile is strictly less than the number of products you pick from the (i+1) th pile for all indices i of the subarray. 
# Find the maximum number of products that can be picked

# Constraints:
# 1 <= n <= 10^5
# 1 <= numProducts[i] <= 10^4

# Approach:
# The key observation in this approach is that the maximum number of products that can be picked is obtained by selecting
# the subarray of piles with the maximum number of products. This is because the number of products picked from each pile
# must be strictly less than the number of products picked from the next pile. Therefore, the maximum number of products
# that can be picked is the sum of the maximum subarray of the piles array.

from typing import List

class Solution:
    
        def max_from_n_piles(self, numProducts: List[int]) -> int:
            max_sum = 0
            for start_idx in range(len(numProducts)):
                 for end_idx in range(start_idx, len(numProducts)):
                    subarr_sum = numProducts[end_idx]
                    prev_val = numProducts[end_idx]
                    for curr_idx in range(end_idx, start_idx -1 , -1):
                        val_to_add = min(numProducts[curr_idx], prev_val - 1)
                        if val_to_add <= 0:
                             break
                        subarr_sum += val_to_add
                        prev_val = val_to_add
                    max_sum = max(max_sum, subarr_sum)
            return max_sum
                         
                        
                         

if __name__ == '__main__':
     # Test 1
    solution = Solution()

    assert solution.max_from_n_piles([7, 4, 5, 2, 6, 5]) == 12
    assert solution.max_from_n_piles([2,9,4,7,5,2]) == 16
    assert solution.max_from_n_piles([7, 4, 5, 2, 6, 5, 12, 13, 8, 20]) == 53