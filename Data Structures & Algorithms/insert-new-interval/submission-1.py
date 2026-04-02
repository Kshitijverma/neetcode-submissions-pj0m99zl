class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals.append(newInterval)
        # intervals.sort(key=lambda x : x[0])
        # res = [intervals[0]]

        # for start, end in intervals[1:]:
        #     lastEnd = res[-1][1]
        #     if start <= lastEnd:
        #         res[-1][1] = max(end, lastEnd)
        #     else:
        #         res.append([start,end])
        
        # return res

        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        
        res.append(newInterval)
        return res
