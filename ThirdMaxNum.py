"""
414. Third Maximum Number

"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort()
        unique_nums = []

        for i in nums:
            if i not in unique_nums:
                unique_nums.append(i)
          
        if len(unique_nums) >= 3:
            return unique_nums[-3]
        elif len(unique_nums) == 2:
            return unique_nums[1]
        else:
            return unique_nums[0]
            
