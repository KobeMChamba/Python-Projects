class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        # Init merged list
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            last_merged = merged[-1]
            if intervals[i][0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], intervals[i][1])
            else:
                merged.append(intervals[i])

        return merged