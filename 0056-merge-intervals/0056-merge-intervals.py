class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if merged[-1][-1] >= intervals[i][0]:
                new_interval = [min(merged[-1][0],intervals[i][0]),max(merged[-1][-1], intervals[i][-1])]
                merged.pop(-1)
                merged.append(new_interval)
            else:
                merged.append(intervals[i])

        return merged