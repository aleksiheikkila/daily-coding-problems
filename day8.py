# EASY: Univalued binary tree

# Not the cleanest, but I believe it works

#A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
#Given the root to a binary tree, count the number of unival subtrees.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node(val: {self.val},\n left: {self.left},\n right: {self.right})\n"


def count_unival_trees(root:Node) -> int:
    #num_unival_trees = 0
    if root is None:
        return (True, None, 0)

    if root.left is None and root.right is None:
        # is unival
        return (True, root.val, 1)
    
    #if root.left:
    left_is_unival, left_unival, num_univals_left = count_unival_trees(root.left)
    #if root.right:
    right_is_unival, right_unival, num_univals_right = count_unival_trees(root.right)

    if (left_is_unival and right_is_unival) and \
        (num_univals_left == 0 or left_unival == root.val) and \
        (num_univals_right == 0 or right_unival == root.val):
        return (True, root.val, num_univals_left + num_univals_right + 1)
    else:
        return (False, None, num_univals_left + num_univals_right)



node = Node(3, Node(3, Node(3), Node(3)))
#    3
#   /
#  3
# / \
#3   3
_, _, num_unival_trees = count_unival_trees(node)
assert num_unival_trees == 4


node2 =  Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0) ) )
_, _, num_unival_trees = count_unival_trees(node2)
assert num_unival_trees == 5

# Idea:
# From the bottom.
# Leaf nodes are unival

# if node is unival, return (True, val, count). 
# Then check if the upper node has same val = left = right
# else return (False, None, count)

