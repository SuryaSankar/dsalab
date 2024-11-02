
# Sliding Window Pattern in Data Structures & Algorithms

The Sliding Window pattern is a useful technique in problems involving subarrays or substrings within a larger array or string. Typically, these problems involve finding a subarray with a specific property, like maximum/minimum sum, length, or unique elements.

### How the Sliding Window Pattern Works
The idea is to maintain a subset of elements within a "window" in the array or string. This window slides over the array as you progress. The size of the window can either be fixed or dynamic depending on the problem's requirements.

## Example Problems

### 1. Maximum Sum Subarray of Size K

**Problem**: Given an array of positive integers and a number `k`, find the maximum sum of any contiguous subarray of size `k`.

#### Solution
We use a fixed-size sliding window approach. We slide the window across the array and keep track of the maximum sum as we go.

#### Code

```python
def max_sum_subarray(arr, k):
    max_sum = 0
    window_sum = 0
    for i in range(len(arr)):
        window_sum += arr[i]  # Add the next element
        if i >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[i - (k - 1)]  # Subtract the element going out
    return max_sum

# Example
arr = [2, 1, 5, 1, 3, 2]
k = 3
print("Maximum sum of a subarray of size k:", max_sum_subarray(arr, k))
```

### 2. Smallest Subarray with Sum Greater Than or Equal to S

**Problem**: Given an array of positive integers and a number `S`, find the length of the smallest contiguous subarray whose sum is greater than or equal to `S`.

#### Solution
Here, we use a variable-size sliding window. We expand the window by moving the end pointer, then shrink it from the beginning until the window's sum is less than `S`.

#### Code

```python
import math

def smallest_subarray_sum(s, arr):
    window_sum = 0
    min_length = math.inf
    start = 0
    
    for end in range(len(arr)):
        window_sum += arr[end]
        while window_sum >= s:
            min_length = min(min_length, end - start + 1)
            window_sum -= arr[start]
            start += 1
    return min_length if min_length != math.inf else 0

# Example
arr = [2, 1, 5, 2, 3, 2]
S = 7
print("Smallest subarray length:", smallest_subarray_sum(S, arr))
```

### 3. Longest Substring with K Distinct Characters

**Problem**: Given a string, find the length of the longest substring that contains exactly `K` distinct characters.

#### Solution
We use a variable-sized sliding window. As we expand the window, we keep track of the character counts. If the count exceeds `K`, we shrink the window from the left until we have exactly `K` distinct characters again.

#### Code

```python
def longest_substring_k_distinct(s, k):
    start = 0
    max_length = 0
    char_count = {}
    
    for end in range(len(s)):
        right_char = s[end]
        char_count[right_char] = char_count.get(right_char, 0) + 1
        
        while len(char_count) > k:
            left_char = s[start]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            start += 1
            
        max_length = max(max_length, end - start + 1)
    
    return max_length

# Example
s = "araaci"
k = 2
print("Length of longest substring with k distinct characters:", longest_substring_k_distinct(s, k))
```

### 4. Maximum Sum Subarray of Size K (Alternative)

**Problem**: Find the maximum sum of any contiguous subarray of size `k` in an array of integers, where `k` is a given integer.

#### Solution
This is similar to the first problem, but here we use a slightly optimized approach with `window_sum`.

#### Code

```python
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # Slide the window forward
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Example
arr = [2, 3, 4, 1, 5]
k = 2
print("Maximum sum of subarray of size k:", max_sum_subarray(arr, k))
```

## Conclusion
The Sliding Window pattern is versatile and can be adapted to solve a variety of problems involving contiguous subarrays or substrings. By learning how to apply this pattern, you can tackle many coding interview questions more efficiently.

---

These examples should give you a good understanding of how the Sliding Window pattern works in different scenarios!
