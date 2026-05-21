class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        for s, e in intervals:
            if res and s <= res[-1][1]:
                s = min(s, res[-1][0]) 
                e = max(e, res[-1][1])
                res.pop()
            res.append([s, e])

        return res