"""
1119. Remove Vowels from a String

"""


class Solution:
    def removeVowels(self, S: str) -> str:
        modifiedS = ''
        vowels = ['a','e','i','o','u']
        
        for i in S:
            if i not in vowels:
                modifiedS += i
                
        return modifiedS