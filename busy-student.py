"""
1450. Number of Students Doing Homework at a Given Time

"""

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        left = 0
        right = len(startTime)

        counter = 0

        while left < right:
            if endTime[left] >= queryTime >= startTime[left]:
                counter += 1

            left += 1
            
        return counter
