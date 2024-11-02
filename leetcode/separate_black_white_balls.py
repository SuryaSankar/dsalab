# https://leetcode.com/problems/separate-black-and-white-balls/

# There are n balls on a table, each ball has a color black or white.

# You are given a 0-indexed binary string s of length n, where 1 and 0 represent black and white balls, respectively.

# In each step, you can choose two adjacent balls and swap them.

# Return the minimum number of steps to group all the black balls to the right and all the white balls to the left.

# The adjacent balls are considered the ones indexed i and i + 1 (0-indexed) with |i| < n - 1.

from typing import List

class Solution:
    def minimumOperations(self, s: str) -> int:
        n = len(s)
        white_count = s.count('0')
        black_count = s.count('1')
        if white_count == 0 or black_count == 0:
            return 0
        whites_seen = 0
        blacks_seen = 0
        min_swaps = float('inf')
        for i in range(n):
            if s[i] == '0':
                whites_seen += 1
            else:
                blacks_seen += 1
            min_swaps = min(min_swaps, whites_seen + black_count - blacks_seen)
        return min_swaps
    