"""
1313. Decompress Run-Length Encoded List

"""

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        
        if len(nums) % 2 != 0:
            return -1

        my_list = []
        for i in range(0,len(nums),2):
            freq = nums[i]
            value = nums[i+1]
            for i in range(freq):
                my_list.append(value)

        return my_list