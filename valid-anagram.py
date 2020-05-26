"""
242. Valid Anagram

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = []
        list_t = []

        for i in s:
            list_s.append(i)

        for i in t:
            list_t.append(i)

        if sorted(list_s) == sorted(list_t):
            return True
        else:
            return False