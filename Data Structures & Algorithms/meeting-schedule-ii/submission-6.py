"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key = lambda i: i.start)
        rooms = [intervals[0]]
        res = 0

        for i in range(1, len(intervals)):
            for j in range(len(rooms)):
                if intervals[i].start < rooms[j].end:
                    if j+1 >= len(rooms):
                        rooms.append(intervals[i])
                        break
                else:
                    rooms[j] = intervals[i]
                    break
        return len(rooms)