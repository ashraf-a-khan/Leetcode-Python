"""
1365. How Many Numbers Are Smaller Than the Current Number

"""


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = 0
        newArr = []
        for i in nums:
            for j in nums:
                if i>j:
                    count += 1

            newArr.append(count)
            count = 0

        return newArr