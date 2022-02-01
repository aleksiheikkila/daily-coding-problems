""" DAY 16
You run an e-commerce website and want to record the last N order ids in a log. 
Implement a data structure to accomplish this, with the following API:
    record(order_id): adds the order_id to the log 
    get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N. 
    
You should be as efficient with time and space as possible.

#############

If it is OK to use abstract data type (defined by what you can do with it; what operations it supports 
but not the actual data structure details)
--> deque is an easy option.

If a data structure (defined by how it is represented in memory, 
and how its state should be manipulated to fulfil the deque operations) 
needs to be put together --> e.g. circular buffer would be fine

"""

from collections import deque

class OrderLog_deque:
    """OrderLog based on deque"""
    def __init__(self, N):
        self.N = N
        self.deque = deque(maxlen=self.N)
        # lets add to the right and pop from the left, if needed

    def record(self, order_id) -> None:
        self.deque.append(order_id)

    def get_last(self, i: int):
        if i < 1 or i > len(self.deque):
            return None
        else:
            return self.deque[-i]

    def print_data(self):
        print(self.deque)


class OrderLog_circbuff:
    """OrderLog based on circular buffer"""
    def __init__(self, N):
        self.N = N
        self.circular_buffer = [None for _ in range(N)]
        self.pos = 0  # pointer to the write loc

    def record(self, order_id) -> None:
        self.circular_buffer[self.pos] = order_id
        self.pos = (self.pos + 1) % self.N

    def get_last(self, i: int):
        if i < 1 or i > self.N:
            return None
        return self.circular_buffer[self.pos - i]

    def print_data(self):
        print(self.circular_buffer)


# TEST CASES
logs = [("deque-based", OrderLog_deque(N=3)), 
        ("circular buffer based", OrderLog_circbuff(N=3))]

for label, log in logs:
    print(label)
    # Store some data
    for i in range(1, 6):
        log.record(i)

    #log.print_data()
    assert log.get_last(0) is None
    assert log.get_last(-111) is None
    assert log.get_last(1) == 5
    assert log.get_last(3) == 3
    assert log.get_last(4) is None
