from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str], memo={}) -> bool:
        if s in memo:
            return memo[s]
        if s == "":
            return True
        for idx in range(1, len(s)+1):
            prefix = s[:idx]
            suffix = s[idx:]
            if prefix in wordDict and self.wordBreak(suffix, wordDict, memo):
                memo[s] = True
                return True
        memo[s] = False
        return False
    
if __name__ == '__main__':
    sol = Solution()
    # print(sol.wordBreak('leetcode', ['leet', 'code'])) # True
    # print(sol.wordBreak('applepenapple', ['apple', 'pen'])) # True
    # print(sol.wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat'])) # False
    # print(sol.wordBreak('catsanddog', ['cats', 'dog', 'sand', 'and', 'cat'])) # True
    print(sol.wordBreak('a', ['b'])) # False
