# https://leetcode.com/problems/container-with-most-water/description/

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

from typing import List

class Solution:
    def brute_force(self, height: List[int]) -> int:
        for i in range(len(height) - 1):
            for j in range(i, len(height)):
                area = (j - i) * min(height[i], height[j])
                max_area = max(max_area, area)
        return max_area
    
    def two_pointers(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            width = right - left
            max_area = max(max_area, width * min(height[left], height[right]))
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            # Intuition behind the above if else is that we need to move one of the pointers
            # We also see that the area formed between the lines will always be limited by the height of the shorter line.
            # Whether left or right, any move will decrease width by 1, so only way to increase area is to increase height.
            # Assume left is < right
            # If we move the right ptr inward, there are 2 possibilities - the new right ptr is < left ptr or >= left ptr.
            # If it is < left ptr, that will become the new limiting height and hence area will be smaller than previous seen area.
            # If it is >= left ptr, the limiting height will still be left ptr and since width is smaller, area will be smaller.
            # So if we move right ptr, area will always decrease
            # If we move left ptr, there are 2 possibilities - the new left ptr is < prev left ptr or >= prev left ptr.
            # If it is < prev left ptr, the limiting height will be new left ptr and area will be smaller.
            # If it is >= prev left ptr, the limiting height could either be the right ptr or the new left ptr and there is a chance
            # that area could increase. So we move the left ptr.

        
        return max_area