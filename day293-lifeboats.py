""" Day 293. How many lifeboats are needed? Medium.
An imminent hurricane threatens the coastal town of Codeville. If at most two people can fit in a rescue boat, 
and the maximum weight limit for a given boat is k, determine how many boats will be needed to save everyone.

For example, given a population with weights [100, 200, 150, 80] and a boat limit of 200, the smallest number of boats 
required will be three.
"""


def num_lifeboats(weights: list, boat_limit: int):
    if len(weights) == 0:
        return 0

    weights = sorted(weights)
    if weights[-1] > boat_limit:
        return None

    left, right = 0, len(weights) - 1
    num_boats = 0

    while left <= right:
        # get the biggest person to a boat, check if we can pair it with a smallest person
        if weights[right] + weights[left] <= boat_limit:
            left += 1
        right -= 1
        num_boats += 1

    return num_boats

# Test cases
TEST_WEIGHTS_1 = [100, 200, 150, 80]
assert num_lifeboats(TEST_WEIGHTS_1, 200) == 3

TEST_WEIGHTS_2 = [1, 10, 9, 10, 10, 2, 8, 6]
assert num_lifeboats(TEST_WEIGHTS_2, 10) == 6

assert num_lifeboats([1, 2, 3, 4, 111], 100) is None
assert num_lifeboats([], 42) == 0