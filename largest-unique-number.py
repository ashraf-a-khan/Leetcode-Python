"""
1133. Largest Unique Number

"""
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        dict_ = {}
        for i in A:
            if i in dict_:
                dict_[i] += 1
            else:
                dict_[i] = 1
        
        res = []
        
        for k, v in dict_.items():
            if v == 1:
                res.append(k)
                
        if len(res) == 0:
            return -1
        else:
            res.sort()
            return res[-1]