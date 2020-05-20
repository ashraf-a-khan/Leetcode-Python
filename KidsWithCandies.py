"""
1431. Kids With the Greatest Number of Candies

"""



class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        print(max_candy)
        bool_arr = []
        for i in candies:
            if i+extraCandies >= max_candy:
                bool_arr.append(True)
            else:
                bool_arr.append(False)

        return bool_arr