"""
1189. Maximum Number of Balloons

"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hash_map = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

        for i in text:
            if i in hash_map:
                if i == 'l' or i == 'o':
                    hash_map[i] += 0.5
                else:
                    hash_map[i] += 1

        return int(min(hash_map.values()))