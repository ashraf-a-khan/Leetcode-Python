"""
1464. Maximum Product of Two Elements in an Array

"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod = []


        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                prod.append((nums[i]-1)*(nums[j]-1))

        return max(prod)