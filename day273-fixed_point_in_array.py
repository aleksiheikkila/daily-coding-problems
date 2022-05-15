"""A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.

"""

def get_fixed_point(nums: list) -> list:
    # bin search
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == mid:
            return nums[mid]
        elif nums[mid] < mid:
            left = mid + 1
        else:
            right = mid - 1

    # no fixed point
    return False


# Tests
TEST_DATA_1 = [-6, 0, 2, 40]
TEST_DATA_2 = [1, 5, 7, 8]
TEST_DATA_3 = [-6, 0, 1, 2, 3, 4, 6, 22, 40]  

assert get_fixed_point(TEST_DATA_1) == 2
assert get_fixed_point(TEST_DATA_2) is False
assert get_fixed_point(TEST_DATA_3) == 6
