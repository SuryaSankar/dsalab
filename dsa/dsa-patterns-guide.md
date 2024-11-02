# Common Data Structure & Algorithm Patterns in Coding Interviews

## 1. Two Pointers Pattern
Used when dealing with sorted arrays or linked lists to find pairs of elements that satisfy certain conditions.

### Example Problems:
1. **Two Sum II (Sorted Array)**
```python
def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    
    while left < right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum == target:
            return [left + 1, right + 1]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    
    return []
```

2. **Container With Most Water**
```python
def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        width = right - left
        max_area = max(max_area, width * min(height[left], height[right]))
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area
```

## 2. Sliding Window Pattern
Used for problems involving arrays or strings where you need to find/calculate something among all subarrays of a given size.

### Example Problems:
1. **Maximum Sum Subarray of Size K**
```python
def maxSubArraySum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

2. **Longest Substring Without Repeating Characters**
```python
def lengthOfLongestSubstring(s):
    seen = {}
    start = max_length = 0
    
    for end, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        else:
            max_length = max(max_length, end - start + 1)
        seen[char] = end
    
    return max_length
```

## 3. Fast & Slow Pointers (Floyd's Cycle Finding)
Used in linked lists or arrays to find cycles or solve problems that require finding a pattern.

### Example Problems:
1. **Linked List Cycle Detection**
```python
def hasCycle(head):
    if not head or not head.next:
        return False
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False
```

2. **Find the Duplicate Number**
```python
def findDuplicate(nums):
    slow = fast = nums[0]
    
    # Find intersection point
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Find cycle start
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow
```

## 4. Merge Intervals Pattern
Used when dealing with overlapping intervals or ranges.

### Example Problems:
1. **Merge Intervals**
```python
def merge(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)
    
    return merged
```

## 5. Dynamic Programming Patterns
Common patterns include:
- 0/1 Knapsack
- Unbounded Knapsack
- Longest Common Subsequence
- Palindromic Subsequence

### Example Problem:
1. **0/1 Knapsack**
```python
def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w-weights[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]
```

## 6. Tree Traversal Patterns
Common approaches include:
- DFS (Preorder, Inorder, Postorder)
- BFS (Level Order)
- Path Finding

### Example Problem:
1. **Binary Tree Level Order Traversal**
```python
from collections import deque

def levelOrder(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level = []
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

## 7. Graph Patterns
Common approaches include:
- DFS/BFS Traversal
- Topological Sort
- Union Find
- Shortest Path Algorithms

### Example Problem:
1. **Course Schedule (Topological Sort)**
```python
from collections import defaultdict, deque

def canFinish(numCourses, prerequisites):
    # Build adjacency list
    graph = defaultdict(list)
    indegree = [0] * numCourses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1
    
    # Find all courses with no prerequisites
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    courses_taken = 0
    
    while queue:
        prereq = queue.popleft()
        courses_taken += 1
        
        for course in graph[prereq]:
            indegree[course] -= 1
            if indegree[course] == 0:
                queue.append(course)
    
    return courses_taken == numCourses
```

## Tips for Practice:
1. Start with easier problems in each pattern
2. Focus on one pattern at a time
3. Try to solve problems without looking at solutions first
4. After solving, look at other solutions to learn different approaches
5. Pay attention to edge cases and time/space complexity
6. Practice explaining your thought process out loud
