"""Given an array of integers and a number k, where 1 <= k <= length of the array, 
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, 
we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)

Do this in O(n) time and O(k) space. 
You can modify the input array in-place and you do not need to store the results. 
You can simply print them out as you compute them.

"""

from collections import deque

def subarray_maxes(a: list, k: int) -> list:

    # Corner cases:
    if not a:
        return None
    if len(a) <= k:
        return [max(a)]

    maxes = []
    d = deque()  
    # leftmost element d[0] is the index for the maximum element within the current sliding window
    # d is purged when window slides past the element 
    # (in practice, d[0] is then removed... it's always the oldest/smallest index in d)
    # When new element is considered, indexes with value smaller than the value for current index 
    # are popped from the right end. Then the new index is added
    # Basically d has then the 1-k indexes, corresponding to the largest to smallest value

    # initial first k elements
    for i in range(k):
        # find the right place for the current index
        while d and a[d[-1]] < a[i]:
            d.pop()
        d.append(i)

    maxes.append(a[d[0]])  # we always read the current max from d[0]

    for i in range(k, len(a)):
        # out of the stored oldest values, the d[0] is the oldest, i.e. smallest index. 
        # There is always at least one value

        # check if we slide past the current max index
        if d and d[0] <= i - k:
            d.popleft()

        # then find the place for the current index
        while d and a[d[-1]] < a[i]:
            d.pop()
        d.append(i)

        maxes.append(a[d[0]])

    return maxes


# Test cases
assert subarray_maxes([10, 5, 2, 7, 8, 7], 3) == [10, 7, 8, 8]
assert subarray_maxes([5, 100, 2, 7, 8, 7, 5], 4) == [100, 100, 8, 8]
assert subarray_maxes([5, 100, 2, 7, 8, 7, 5], 2) == [100, 100, 7,  8, 8, 7]
assert subarray_maxes([10, 5, 2, 7, 8, 7], 1) == [10, 5, 2, 7, 8, 7]
assert subarray_maxes([10, 5, 2, 7, 8, 7], 10) == [10]
