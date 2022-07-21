"""
Pascal's triangle is a triangular array of integers constructed with the following formula:

The first row consists of the number 1.
For each subsequent row, each element is the sum of the numbers directly above it, on either side.
For example, here are the first few rows:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
Given an input k, return the kth row of Pascal's triangle.

Bonus: Can you do this using only O(k) space?
"""

def get_kth_pascal_triangle_row(k: int):
    if k < 1:
        return None

    nums = [1] * k

    for row in range(2, k):
        prev_row = nums[:row].copy()  # get rid of this extra space req!
        for idx in range(1, row):
            nums[idx] = prev_row[idx-1] + prev_row[idx]

    return nums


for k in range(1, 10):
    print(get_kth_pascal_triangle_row(k))
