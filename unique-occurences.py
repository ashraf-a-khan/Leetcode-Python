"""
1207. Unique Number of Occurrences

"""


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict_ = {}
        for i in arr:
            if i in dict_:
                dict_[i] += 1
            else:
                dict_[i] = 1
        if len(set(dict_.values())) == len(dict_.values()):
            return True
        return False