""" Day 343 - Medium

Given a binary search tree and a range [a, b] (inclusive), 
return the sum of the elements of the binary search tree within the range.
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node(val:{self.val}"

# Construct a test tree
TEST_ROOT = Node(5)
TEST_ROOT.left = Node(3, left=Node(2), right=Node(4))
TEST_ROOT.right = Node(8, left=Node(6), right=Node(10))


def range_sum(root:Node, lo, hi):
    assert lo <= hi
    rst = 0
    stack = [root]

    while stack:
        node = stack.pop()

        if node.val < lo:
            if node.right is not None:
                stack.append(node.right)

        elif node.val > hi:
            if node.left is not None:
                stack.append(node.left)
        
        else:
            # in range
            assert lo <= node.val <= hi
            rst += node.val

            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)

    return rst


assert range_sum(TEST_ROOT, 4, 9) == 23
