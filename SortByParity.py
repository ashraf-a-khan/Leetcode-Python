"""
905. Sort Array By Parity

"""


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        final = []
        A.sort()

        for i in A:
            if i%2 == 0:
                even.append(i)
            else:
                odd.append(i)

        final = even+odd
        return final
