"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. 
Numbers can be 0 or negative.

For example, 
[2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 
[5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?


################

Linear scan, keep track of max sum so fat including or excluding the current number.
At each position, we have a choice. Either include that number of not.

Include if that improves the sum.
Do not include otherwise (if it goes negative, set the sum to zero)

"""


def max_nonadjacent_sum(nums: list) -> int:
    sum_incl_curr = sum_excl_curr = 0

    for num in nums:
        sum_incl_curr, sum_excl_curr = (max(num, sum_excl_curr + num), 
                                        max(sum_incl_curr, sum_excl_curr))

    return max(sum_incl_curr, sum_excl_curr)


# Test cases
assert max_nonadjacent_sum([2, 4, 6, 2, 5]) == 13
assert max_nonadjacent_sum([5, 1, 1, 5]) == 10
assert max_nonadjacent_sum([-10, -10, -10, -10, 5, 1, 1, 5, -1, -1]) == 10
assert max_nonadjacent_sum([-10, -10, -2, 0, -10, 0, -10, -1, -1]) == 0