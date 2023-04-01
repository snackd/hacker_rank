class Solution:

    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        if not intervals and newInterval:
            return [[]]
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals
        result = []

        for interval in intervals:
            # head
            if newInterval[0] > interval[1]:
                result.append(interval)
            # tail
            elif newInterval[1] < interval[0]:
                print(newInterval)
                result.append(newInterval)
                newInterval = interval
            # merge
            else:
                newInterval = [
                    min(interval[0], newInterval[0]),
                    max(interval[1], newInterval[1])
                ]

        result.append(newInterval)

        return result
