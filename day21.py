"""Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

def get_min_roomcount(intervals) -> int:
    # An interval is a tuple (start_time: int, end_time: int)
    # we need the max nbr of overlapping intervals
    # kind of cumulative sum of leases and releases
    events = []  # (time, plus or minus 1)

    for interval in intervals:
        events.append((interval[0], 1))  # +1 means "needs one more room"
        events.append((interval[1], -1)) 

    events.sort()  # in asc order based primarily on the first elem

    max_room_need = curr_room_need =  0

    # go thru the events in time order
    for event in events:
        curr_room_need += event[1]
        max_room_need = max(max_room_need, curr_room_need)

    return max_room_need


assert get_min_roomcount([(30, 75), (0, 50), (60, 150)]) == 2
