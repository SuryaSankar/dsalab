# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Brute force solution

class BruteForceSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        for i in range(len(s)):
            sub = ""
            for j in range(i, len(s)):
                if s[j] in sub:
                    break
                sub += s[j]
                maxLen = max(maxLen, len(sub))
        return maxLen

# Optimized solution
    
class TwoPointerSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        left = 0
        right = 0
        lastSeen = {}
        for right in range(len(s)):
            if s[right] in lastSeen and left <= lastSeen[s[right]]:
                left = lastSeen[s[right]] + 1
            lastSeen[s[right]] = right
            l = right - left + 1
            maxLen = max(l, maxLen)
        return maxLen
    
class TwoPointerSolutionWithoutMap:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        i = 0
        j = 0
        sub = ""
        while i < len(s) and j < len(s):
            if s[j] not in sub:
                sub += s[j]
                j += 1
                maxLen = max(maxLen, len(sub))
            else:
                sub = sub[1:]
                i += 1
        return maxLen