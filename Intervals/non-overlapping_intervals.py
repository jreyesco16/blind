class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort first
        intervals.sort()
        
        res = 0
        
        prev = intervals[0][1]
        
        for l, r in intervals[1:]:
            if l >= prev:
                prev = r
            # overlap
            else:
                res += 1
                prev = min(r, prev)

        return res