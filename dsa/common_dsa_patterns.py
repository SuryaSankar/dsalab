# 1. Two Pointers Pattern
def two_pointer_template(arr):
    left, right = 0, len(arr) - 1
    result = []
    
    while left < right:
        # Process elements from both ends
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            result.append([arr[left], arr[right]])
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return result

# Example: Find pairs that sum to target
def find_pairs(arr, target):
    arr.sort()  # Usually need to sort first
    left, right = 0, len(arr) - 1
    result = []
    
    while left < right:
        curr_sum = arr[left] + arr[right]
        if curr_sum == target:
            result.append([arr[left], arr[right]])
            left += 1
            right -= 1
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return result

# 2. Sliding Window Pattern
def sliding_window_template(arr, k):
    window_start = 0
    window_sum = 0
    max_sum = float('-inf')
    
    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # Add element to window
        
        if window_end >= k - 1:  # Window size is k
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]  # Remove element from window
            window_start += 1
    
    return max_sum

# Example: Maximum sum subarray of size k
def max_subarray_sum(arr, k):
    window_start = 0
    window_sum = 0
    max_sum = float('-inf')
    
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        
        if window_end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    
    return max_sum

# 3. Fast & Slow Pointers (Floyd's Cycle Detection)
def fast_slow_pointer_template(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:  # Cycle detected
            return True
    
    return False

# Example: Detect cycle in linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False

# 4. Merge Intervals Pattern
def merge_intervals_template(intervals):
    if not intervals:
        return []
        
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]:  # Overlapping intervals
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)
    
    return merged

# Example: Merge overlapping intervals
def merge_intervals(intervals):
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

# 5. Binary Search Pattern
def binary_search_template(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Not found

# Example: Search in rotated sorted array
def search_rotated(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
            
        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

# 6. DFS Pattern (Tree/Graph)
def dfs_template(root):
    if not root:
        return
        
    # Process current node
    result.append(root.val)
    
    # Recurse on children
    dfs_template(root.left)
    dfs_template(root.right)

# Example: Binary tree path sum
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def has_path_sum(root, target_sum):
    if not root:
        return False
        
    # Leaf node check
    if not root.left and not root.right:
        return root.val == target_sum
        
    # Recurse on non-leaf nodes
    return (has_path_sum(root.left, target_sum - root.val) or 
            has_path_sum(root.right, target_sum - root.val))

# 7. BFS Pattern
from collections import deque

def bfs_template(root):
    if not root:
        return []
        
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(current_level)
    
    return result

# Example: Level order traversal
def level_order(root):
    if not root:
        return []
        
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(current_level)
    
    return result

# 8. Backtracking Pattern
def backtrack_template(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path[:])
            return
            
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                continue
                
            path.append(candidates[i])
            backtrack(i, target - candidates[i], path)
            path.pop()
    
    result = []
    backtrack(0, target, [])
    return result

# Example: Combination Sum
def combination_sum(candidates, target):
    def backtrack(start, target, path):
        if target == 0:
            result.append(path[:])
            return
            
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                continue
                
            path.append(candidates[i])
            backtrack(i, target - candidates[i], path)
            path.pop()
    
    result = []
    candidates.sort()  # Optional optimization
    backtrack(0, target, [])
    return result