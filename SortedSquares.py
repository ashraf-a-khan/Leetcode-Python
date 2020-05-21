"""
977. Squares of a Sorted Array

"""


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        sq_arr = []

        for i in A:
            sq_arr.append(i*i)

        sq_arr.sort()

        return sq_arr