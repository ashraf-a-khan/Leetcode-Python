"""
1198. Find Smallest Common Element in All Rows

"""
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        h_map = {}

        for m in mat:
            for i in m:
                if i in h_map:
                    h_map[i] += 1
                else:
                    h_map[i] = 1

        res = []

        for k, v in h_map.items():
            if v == len(mat):
                res.append(k)
    
        if len(res) == 0:
            return -1
        else:
            return min(res)