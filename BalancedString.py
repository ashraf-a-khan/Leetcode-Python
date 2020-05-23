"""
1221. Split a String in Balanced Strings

"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        stack = 0
        
        for i in s:
            if i == 'L':
                stack -= 1
            elif i == 'R':
                stack += 1
            
            if stack == 0:
                count += 1
                
        return count