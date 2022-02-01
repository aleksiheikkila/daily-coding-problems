""" DAY 164. Medium.

You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}. 
By the pigeonhole principle, there must be a duplicate. 

Find it in linear time and space.
"""


def find_duplicate(nums: list) -> int:
    seen = set()

    for num in nums:
        if num in seen:
            return num
        seen.add(num)


# TEST CASES
assert find_duplicate([1,2,3,4,5,8,2,6,7]) == 2
assert find_duplicate([1,1]) == 1
assert find_duplicate([4,3,2,1,1]) == 1