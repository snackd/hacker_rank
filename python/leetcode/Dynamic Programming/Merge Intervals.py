class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return [[]]

        intervals.sort(key=lambda x: x[0])

        result = []
        for i, interval in enumerate(intervals):
            if i == 0:
                prev = interval
                continue
            # end < start
            if prev[1] < interval[0]:
                result.append(prev)
                prev = interval
            else:
                prev[0] = min(prev[0], interval[0])
                prev[1] = max(prev[1], interval[1])

        result.append(prev)

        return result
