"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
Given N, write a function that returns the number of unique ways you can climb the staircase. 
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:
    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of 
positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

#### SOL:

Kind of "1D DP"


ways [1, 0, 0, 0, 0]
ways [1, 1, 0, 0, 0]
ways [1, 1, 2, 0, 0]
ways [1, 1, 2, 3, 0]
ways [1, 1, 2, 3, 5]


ways [1, 0, 0, 0, 0]
ways [1, 1, 0, 0, 0]
ways [1, 1, 2, 0, 0]
ways [1, 1, 2, 4, 0]
ways [1, 1, 2, 4, 7]

"""

from collections import deque

def count_ways(total_steps: int, 
               possible_step_sizes: set = {1,2}) -> int:
    """ O(N) for both runtime and mem"""
    
    # we start "before the first step"
    ways = [1] + [0]*total_steps
    # We do not need to keep all of this history! Could be optimized

    for i in range(1, len(ways)):
        for d in possible_step_sizes:
            if i - d >= 0:
                ways[i] += ways[i-d]

    return ways[-1]


# TEST CASES
assert count_ways(4) == 5
assert count_ways(4, possible_step_sizes={1,2,3}) == 7
assert count_ways(10, possible_step_sizes={1}) == 1
    