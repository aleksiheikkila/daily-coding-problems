""" DAY 4. HARD.
Given an array of integers, find the first missing positive integer 
in linear time and constant space. 

In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.


SOLUTION:

If nums has length of L, the first missing positive must be in range [1, L+1].

We could have and array of length L+1 to mark which positive integers 1...L+1 we have seen 
and grab the first missing. THis would be linear time but also linear (not constant) extra space

To get away with the space requirement, we need to use the original nums to mark which ones
we have seem while not losing the original values. This can be done by utilizing modulo.
"""


def find_first_missing_pos_int(nums: list):

    # edge case
    if not nums or len(nums) == 0:
        return 1

    # add one value to make this work nicer
    nums.append(0)
    N = len(nums)

    # Get rid of values that do not interest us
    for i in range(N):
        if nums[i] < 0 or nums[i] >= N:
            nums[i] = 0

    # Mark values we have seen
    for i in range(N):
        if nums[i] > 0:
            nums[nums[i]%N - 1] += N
    
    # Check whether we have seen value i+1 (we have if nums[i] >= N)
    for i in range(N):
        if nums[i] // N == 0:
            return i + 1

    # else we must have contiguous block and the missing one is the "next"
    return N


assert find_first_missing_pos_int([3, 4, -1, 1]) == 2
assert find_first_missing_pos_int([]) == 1
assert find_first_missing_pos_int([0, 0, 0]) == 1
assert find_first_missing_pos_int([1, 3]) == 2
assert find_first_missing_pos_int([2, 3, 4, 5]) == 1
assert find_first_missing_pos_int([9, 0, 0, 0, 9, 2, 1, 13, -33, 
                                  -6, 6, 3, 4, 5, 8,-4, 99, 10, 101]) == 7
