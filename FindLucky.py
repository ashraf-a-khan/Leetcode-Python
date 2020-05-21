"""
1394. Find Lucky Integer in an Array

"""

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky_integers = []
        for i in arr:
            if arr.count(i) == i:
                lucky_integers.append(i)

        if lucky_integers:
            return max(lucky_integers)
        else:
            return -1