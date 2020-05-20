"""
283. Move Zeroes

"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroArr = []
        nonZero = []
        for i in nums:
            if i == 0:
                zeroArr.append(i)
            else:
                nonZero.append(i)
        nums[:] = (nonZero+zeroArr)
        