# HARD

# Given an array of integers, return a new array such that each element at index i 
# of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

def products_without_current(nums: list, verbose=False) -> list:
    """
    Generate left and right product arrays.
    At index i: 
        The left array contains the product of nums from left up to i element.
        The right array contains the product of nums from i+1 element to the right end.
    """

    # if 0 or 1 numbers, let's return empty array
    if len(nums) < 2:
        return []

    leftprods = []
    rightprods = []

    # left
    running_prod = 1
    for i, num in enumerate(nums):
        running_prod *= num
        if i == 0:
            leftprods.append(num)
        else:
            leftprods.append(running_prod)

    # right
    running_prod = 1
    for i, num in enumerate(nums[::-1]):
        running_prod *= num
        if i == 0:
            rightprods.append(num)
        else:
            rightprods.append(running_prod)

    rightprods.reverse()

    if verbose:
        print("Left:", leftprods)
        print("Right:", rightprods)

    prods_without = []
    for i in range(len(nums)):
        if i == 0:
            prods_without.append(rightprods[i+1])
        elif i == len(nums) - 1:
            prods_without.append(leftprods[i-1])
        else:
            prods_without.append(leftprods[i-1] * rightprods[i+1])

    if verbose:
        print("Result: ", prods_without)
    return prods_without

assert products_without_current([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
assert products_without_current([3, 2, 1]) == [2, 3, 6]
