"""
125. Valid Palindrome

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        
        s = s.lower()
        
        left = ""
        right = ""
        
        for i in range(0, len(s)):
            if s[i].isalpha() or s[i].isdigit():
                left += s[i]
                
        for j in range(len(s) - 1, -1, -1):
            if s[j].isalpha() or s[j].isdigit():
                right += s[j]
                
        return left == right