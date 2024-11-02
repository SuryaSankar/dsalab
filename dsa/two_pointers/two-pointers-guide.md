# Two Pointers Pattern - Comprehensive Guide

## Overview
The Two Pointers pattern uses two pointers to traverse an array or linked list, usually moving them towards each other or in the same direction based on certain conditions. This pattern is especially useful for:
- Searching pairs in a sorted array
- Finding triplets or subarrays that meet specific conditions
- Comparing strings
- Linked list operations

## Common Variations

### 1. Opposite Direction Pointers
Pointers start from opposite ends and move toward each other.

#### Example 1: Valid Palindrome
```python
def isPalindrome(s: str) -> bool:
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    left, right = 0, len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Example usage:
# isPalindrome("A man, a plan, a canal: Panama") -> True
# isPalindrome("race a car") -> False
```

#### Example 2: 3Sum (Finding triplets that sum to zero)
```python
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue
            
        left, right = i + 1, len(nums) - 1
        target = -nums[i]
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return result

# Example usage:
# threeSum([-1,0,1,2,-1,-4]) -> [[-1,-1,2],[-1,0,1]]
```

### 2. Same Direction Pointers
Both pointers move in the same direction with different speeds or conditions.

#### Example 1: Remove Duplicates from Sorted Array
```python
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

# Example usage:
# removeDuplicates([1,1,2]) -> 2, nums becomes [1,2,_]
```

#### Example 2: Remove Element
```python
def removeElement(nums: List[int], val: int) -> int:
    slow = 0
    
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    
    return slow

# Example usage:
# removeElement([3,2,2,3], 3) -> 2, nums becomes [2,2,_,_]
```

### 3. Sliding Window with Two Pointers
Using two pointers to maintain a window of elements.

#### Example: Minimum Window Substring
```python
def minWindow(s: str, t: str) -> str:
    if not s or not t:
        return ""

    # Initialize character frequency dictionary for t
    char_count = {}
    for char in t:
        char_count[char] = char_count.get(char, 0) + 1
    
    required = len(char_count)
    formed = 0
    
    # Dictionary to keep count of characters in current window
    window_counts = {}
    
    # Initialize result variables
    ans = float("inf"), None, None
    left = right = 0
    
    while right < len(s):
        # Add one character from the right
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        # Check if this character completes a required character count
        if char in char_count and window_counts[char] == char_count[char]:
            formed += 1
            
        # Try to minimize window by moving left pointer
        while left <= right and formed == required:
            char = s[left]
            
            # Save smallest window
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
                
            # Remove the left character
            window_counts[char] -= 1
            if char in char_count and window_counts[char] < char_count[char]:
                formed -= 1
                
            left += 1
        
        right += 1
    
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]

# Example usage:
# minWindow("ADOBECODEBANC", "ABC") -> "BANC"
```

### 4. Partition Arrays
Using two pointers to partition arrays based on certain conditions.

#### Example: Sort Colors (Dutch National Flag Problem)
```python
def sortColors(nums: List[int]) -> None:
    # Three pointers: left (0s), current (traversing), right (2s)
    left = current = 0
    right = len(nums) - 1
    
    while current <= right:
        if nums[current] == 0:
            nums[left], nums[current] = nums[current], nums[left]
            left += 1
            current += 1
        elif nums[current] == 2:
            nums[current], nums[right] = nums[right], nums[current]
            right -= 1
        else:
            current += 1

# Example usage:
# sortColors([2,0,2,1,1,0]) -> [0,0,1,1,2,2]
```

## Tips for Solving Two Pointer Problems

1. **Identify the Pattern**
   - Is the array/string sorted?
   - Are we looking for pairs/triplets?
   - Do we need to compare elements from both ends?
   - Are we tracking a window of elements?

2. **Common Techniques**
   - Sort the array first if order doesn't matter
   - Use while loops for opposite direction pointers
   - Use for loops with a slower pointer for same direction
   - Handle duplicates carefully
   - Consider edge cases (empty input, single element)

3. **Optimization Tips**
   - Avoid unnecessary comparisons
   - Skip duplicate values when possible
   - Use early termination conditions
   - Consider space complexity (in-place modifications)

4. **Common Pitfalls**
   - Off-by-one errors in pointer movements
   - Not handling edge cases
   - Forgetting to update pointers
   - Infinite loops due to incorrect pointer updates
