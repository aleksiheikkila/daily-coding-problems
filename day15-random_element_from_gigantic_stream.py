"""
Given a stream of elements too large to store in memory, 
pick a random element from the stream with uniform probability.

####################

This is called reservoir sampling



"""

import random
from collections import defaultdict

def pick_random(stream: list):
    pick = None

    for i, elem in enumerate(stream):
        if random.randint(1, i+1) == 1:
            pick = elem
    
    return pick

"""
With this logic, we can observe the following:

with 1 elem, that will always be picked
with 2 elems, second element will have 50% of chance being picked.
with 3 elems:
    - P(1) = 1 * 1/2 * 2/3 = 1/3
    - P(2) = 1/2 * 2/3 = 1/3
    - P(3) = 1/3
with 4 elems:
    - P(1) = 1 * 1/2 * 2/3 * 3/4 = 6/24 = 1/4
    - P(2) = 1/2 * 2/3 * 3/4 = 1/4
    - P(3) = 1/3 * 3/4 = 3/12 = 1/4
    - P(4) = 1/4
etc.
"""

# TEST CASES
assert pick_random([]) == None
assert pick_random([2]) == 2
assert pick_random(["pick me"]) == "pick me"

# lets see that it seems to draw things with uniform probability
random.seed(123)
NUM_TRIALS = 100_000
counts = defaultdict(int)
for _ in range(NUM_TRIALS):
    counts[pick_random([1,2,3,4])] += 1

print(counts)
# Looks good: {3: 24997, 1: 25036, 4: 24878, 2: 25089}


# EXTRA: pick k random elements from the same stream.

def pick_random_k(stream: list, k: int):
    # this is unknown:
    # N = len(stream)
    picked_elements = []

    for i, elem in enumerate(stream):
        if i < k:
            picked_elements.append(elem)
        else:
            idx = random.randint(0, i)
            if idx < k:
                picked_elements[idx] = elem

    return picked_elements
