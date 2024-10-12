# https://leetcode.com/problems/ipo/

# Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on 
# some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects 
# before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

# You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

# Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

# Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

# The answer is guaranteed to fit in a 32-bit signed integer.

# Example 1:
# Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
# Output: 4
# Explanation: Since your initial capital is 0, you can only start the project indexed 0.
# After finishing it you will obtain profit 1 and your capital becomes 1.
# With capital 1, you can either start the project indexed 1 or the project indexed 2.
# Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
# Therefore, output the final result, which is 0 + 1 + 3 = 4.

# Example 2:
# Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
# Output: 6

# Constraints:
# 1 <= k <= 10^5
# 0 <= w <= 10^9
# n == profits.length
# n == capital.length
# 1 <= n <= 10^5
# 0 <= profits[i] <= 10^4
# 0 <= capital[i] <= 10^9

# Approach:
# The key observation in this approach is that we can sort the projects based on their capital and then use a priority queue to select the projects with the maximum profit.
# We can iterate through the projects in increasing order of capital and add the projects that have the required capital to a priority queue.
# We can then select the project with the maximum profit from the priority queue and add the profit to the total capital.
# We can repeat this process k times to maximize the total capital.
# The time complexity of this approach is O(nlogn + klogn), where n is the number of projects and k is the maximum number of projects that can be selected.
# The space complexity is O(n) for the priority queue.
# The approach is efficient as it uses a priority queue to select the projects with the maximum profit, and iterates through the projects in increasing order of capital.
# The approach is correct as it selects the projects with the maximum profit that can be completed with the available capital.
# The approach is optimal as it maximizes the total capital by selecting the projects with the maximum profit.
# The approach is also easy to understand and implement, making it a good choice for solving the IPO problem.


from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, no_of_chooseable_projects: int, available_capital: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(profits, capital), key=lambda x: x[1])
        pq = []
        i = 0
        for _ in range(no_of_chooseable_projects):
            while i < len(projects) and projects[i][1] <= available_capital:
                heapq.heappush(pq, -projects[i][0]) # heapq is a min heap, so we negate the profit to make it a max heap
                i += 1
            if pq:
                available_capital -= heapq.heappop(pq)
            else:
                break
        return available_capital
    
if __name__ == '__main__':
    # Test 1
    solution = Solution()
    k = 2
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 1]
    # The projects are sorted based on their capital: [(1, 0), (2, 1), (3, 1)].
    # Since the initial capital is 0, we can only start the project indexed 0.
    # After finishing it, we will obtain a profit of 1 and our capital becomes 1.
    # With capital 1, we can either start the project indexed 1 or the project indexed 2.
    # Since we can choose at most 2 projects, we need to finish the project indexed 2 to get the maximum capital.
    # Therefore, the final result is 0 + 1 + 3 = 4.
    assert solution.findMaximizedCapital(k, w, profits, capital) == 4
    # Test 2
    k = 3
    w = 0
    profits = [1, 2, 3]
    capital = [0, 1, 2]
    # The projects are sorted based on their capital: [(1, 0), (2, 1), (3, 2)].
    # Since the initial capital is 0, we can only start the project indexed 0.
    # After finishing it, we will obtain a profit of 1 and our capital becomes 1.
    # With capital 1, we can start the project indexed 1 and obtain a profit of 2.
    # With capital 3, we can start the project indexed 2 and obtain a profit of 3.
    # Therefore, the final result is 0 + 1 + 2 + 3 = 6.
    assert solution.findMaximizedCapital(k, w, profits, capital) == 6
    # Test 3
    k = 1
    w = 1
    profits = [1, 2, 3]
    capital = [0, 1, 2]
    # The projects are sorted based on their capital: [(1, 0), (2, 1), (3, 2)].
    # Since the initial capital is 1, we can start the project indexed 1 and obtain a profit of 2.

