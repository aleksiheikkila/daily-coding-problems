""" Day 165. Medium.
Given an array of integers, return a new array where each element in the new array is 
the number of smaller elements to the right of that element in the original input array.

For example, given the array [3, 4, 9, 6, 1], return [1, 1, 2, 1, 0], since:
    - There is 1 smaller element to the right of 3
    - There is 1 smaller element to the right of 4
    - There are 2 smaller elements to the right of 9
    - There is 1 smaller element to the right of 6
    - There are no smaller elements to the right of 1
"""

def get_num_smaller_to_right(nums: list) -> list:
    """ Naive O(N^2) runtime approach.
    TODO: Can we do better?
    """
    rst = []

    if not nums or len(nums) == 0:
        return rst

    for i, num1 in enumerate(nums):
        num_smaller = 0
        for j, num2 in enumerate(nums[i+1:]):
            if num2 < num1:
                num_smaller += 1
        rst.append(num_smaller)

    return rst


# TEST CASES
get_num_smaller_to_right([3, 4, 9, 6, 1]) == [1, 1, 2, 1, 0]
get_num_smaller_to_right([5]) == [0]
get_num_smaller_to_right([5, 5, 5, 5]) == [0, 0, 0, 0]
get_num_smaller_to_right([-4, -1, -1, 0, 4, 5]) == [0, 0, 0, 0, 0, 0]
get_num_smaller_to_right([-4, -10, -100]) == [2, 1, 0]
