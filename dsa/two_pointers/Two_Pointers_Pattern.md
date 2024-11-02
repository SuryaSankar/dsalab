
# Two Pointers Pattern in Data Structures & Algorithms

The Two Pointers pattern is useful for solving problems where we search for pairs in a sorted array or iterate over elements in opposite directions. This pattern is particularly efficient when dealing with sorted arrays or strings.

### How the Two Pointers Pattern Works
In the Two Pointers pattern, we use two pointers (often called `left` and `right`) to iterate from different ends of the array or meet at a common point based on the condition in the problem.

## Example Problems

### 1. Pair with Target Sum

**Problem**: Given a sorted array of integers and a target sum, find two numbers that add up to the target.

#### Solution
Use two pointers starting from the beginning and end of the array. Move them toward each other based on whether the sum is greater or smaller than the target.

#### Code

```python
def pair_with_target_sum(arr, target_sum):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [left, right]
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1
    return []

# Example
arr = [1, 2, 3, 4, 6]
target_sum = 6
print("Indices of pair with target sum:", pair_with_target_sum(arr, target_sum))
```

### 2. Remove Duplicates from Sorted Array

**Problem**: Given a sorted array, remove duplicates in-place such that each element appears only once and return the new length.

#### Solution
Use one pointer to track unique elements while iterating with another pointer.

#### Code

```python
def remove_duplicates(arr):
    if not arr:
        return 0

    unique_index = 1
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[unique_index] = arr[i]
            unique_index += 1
    return unique_index

# Example
arr = [2, 3, 3, 3, 6, 9, 9]
print("Length of array after removing duplicates:", remove_duplicates(arr))
```

### 3. Squaring a Sorted Array

**Problem**: Given a sorted array, create a new array containing squares of all numbers sorted in non-decreasing order.

#### Solution
Use two pointers to square values from both ends of the array, placing the larger squares in the result array from the end.

#### Code

```python
def make_squares(arr):
    n = len(arr)
    squares = [0] * n
    left, right = 0, n - 1
    highest_square_index = n - 1

    while left <= right:
        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]
        if left_square > right_square:
            squares[highest_square_index] = left_square
            left += 1
        else:
            squares[highest_square_index] = right_square
            right -= 1
        highest_square_index -= 1

    return squares

# Example
arr = [-2, -1, 0, 2, 3]
print("Squares of the array in sorted order:", make_squares(arr))
```

### 4. Triplet Sum to Zero

**Problem**: Given an array of unsorted numbers, find all unique triplets that add up to zero.

#### Solution
Sort the array, then iterate each element and use two pointers to find pairs that sum up to the negative of the current element.

#### Code

```python
def search_triplets(arr):
    arr.sort()
    triplets = []
    
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:  # Skip same element to avoid duplicates
            continue
        left, right = i + 1, len(arr) - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == 0:
                triplets.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return triplets

# Example
arr = [-3, 0, 1, 2, -1, 1, -2]
print("Triplets with zero sum:", search_triplets(arr))
```

## Conclusion
The Two Pointers pattern provides a way to optimize solutions by using two pointers to work toward the center or towards each other. It can simplify problems involving pairs or triplets and improve performance in problems involving sorted arrays.

---

These examples should give you a good understanding of how the Two Pointers pattern works in different scenarios!
