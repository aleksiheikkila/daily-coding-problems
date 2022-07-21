""" DAY 26. Medium

Given a singly linked list and an integer k, remove the kth last element from the list. 
k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.

z -> 1 -> 2 -> 3 -> 4 -> 5
k = 3


z -> 1 -> 2 -> 3 -> 4 -> 5
k = 5

"""

class Node:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.nxt = nxt

    def __repr__(self):
        return f"Node(val:{self.val}, next: {self.nxt})"


def remove_kth_last_node(root: "Node", k: int):
    if not isinstance(k, int) or k < 1:
        raise ValueError("k must be an integer, at least 1")
    
    dummy = Node(None, root)

    curr = dummy
    for _ in range(k):
        curr = curr.nxt
        if curr is None:
            return root

    prev_to_kth_from_end = dummy
    kth_from_end = dummy.nxt

    # then go all the way to the end
    while curr.nxt is not None:
        curr = curr.nxt
        prev_to_kth_from_end = prev_to_kth_from_end.nxt
        kth_from_end = kth_from_end.nxt
    
    if kth_from_end == root:
        return kth_from_end.nxt
    
    prev_to_kth_from_end.nxt = kth_from_end.nxt
    
    return root


# Test case
# 1 -> 2 -> 3 -> 4 -> 5
TEST_ROOT_1 = Node(1, 
    Node(2, 
    Node(3, 
    Node(4,
    Node(5)))))

TEST_ROOT_2 = Node(1, 
    Node(2, 
    Node(3, 
    Node(4,
    Node(5)))))

TEST_ROOT_3 = Node(1, 
    Node(2, 
    Node(3, 
    Node(4,
    Node(5)))))

TEST_ROOT_4 = Node(1, 
    Node(2, 
    Node(3, 
    Node(4,
    Node(5)))))

TEST_ROOT_5 = Node(1, 
    Node(2, 
    Node(3, 
    Node(4,
    Node(5)))))


new1 = remove_kth_last_node(TEST_ROOT_1, 3)
print(new1)

new2 = remove_kth_last_node(TEST_ROOT_2, 5)
print(new2)

new3 = remove_kth_last_node(TEST_ROOT_3, 6)
print(new3)

new4 = remove_kth_last_node(TEST_ROOT_4, 1)
print(new4)

new5 = remove_kth_last_node(TEST_ROOT_5, 0)
print(new5)
