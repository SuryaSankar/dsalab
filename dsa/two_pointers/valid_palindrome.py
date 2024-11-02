# https://leetcode.com/problems/valid-palindrome/description/

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


class Solution:
    def is_valid_palindrome(word: str) -> bool:
        left = 0
        right = len(word) - 1
        newstr = "".join(l for l in word.lower() if l.isalnum())
        if newstr == "":
            return True
        while left <= right:
            if newstr[left] != newstr[right]:
                return False
            left += 1
            right -= 1
        return True
    
if __name__ == '__main__':
    sol = Solution()

