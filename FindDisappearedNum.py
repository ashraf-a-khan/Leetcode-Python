"""
448. Find All Numbers Disappeared in an Array

"""


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        len_arr = len(nums)+1
        a = set([i for i in range(1, len_arr)])
        b = set(nums)
        return list(a-b)
        