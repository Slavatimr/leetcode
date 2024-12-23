from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        index = 0
        intervals.sort()
        while index < len(intervals) - 1:
            if intervals[index][1] >= intervals[index+1][0]:
                a, b = intervals[index][0], max(intervals[index+1][1], intervals[index][1])
                for i in range(2):
                    intervals.pop(index)
                intervals.insert(index, [a, b])
            else:
                index += 1
        return intervals