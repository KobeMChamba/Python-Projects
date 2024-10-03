
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals = sorted(intervals, key=lambda x: x [0])

        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                # condition is that ans empty or interval is past last interval in ans
                ans.append(interval)
            else:
                # new interval must start equal to or before end of last interval in ans
                ans[-1][1] = max(ans[-1][1], interval[1])

        return ans
            
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         result = []
#         if not intervals:
#             return result
#         start = intervals[0][0]
#         end = intervals[0][1]
#         for i in range(1, len(intervals)):
#             print("int: ", intervals[i])
#             if intervals[i][0] <= end:
#                 end = intervals[i][1]
#                 print("s: ", start)
#                 print("e: ", end)
#             else:
#                 result.append([start, end])
#                 start = intervals[i][0]
#                 end = intervals[i][1]
#         print("s: ", start)
#         print("e: ", end)
#         if [start, end] not in result:
#             result.append([start, end])
#         return result