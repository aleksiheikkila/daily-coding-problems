""" Day 6. XOR linked list. Hard.


An XOR linked list is a more memory efficient doubly linked list. 
Instead of each node holding next and prev fields, it holds a field named both, 
which is an XOR of the next node and the previous node. 

Implement an XOR linked list; it has 
 - an add(element) which adds the element to the end, and
 - a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), 
you can assume you have access to get_pointer and dereference_pointer functions 
that converts between nodes and memory addresses.


=======================
Need to fake a little in python.

In Python, could utilize id() (however it's not memory loc in all cases/implementations).

Or perhaps use list to represent memory, and list indices are the memory locations / addresses.
Let's use this.

=======================
In the XOR linked list, instead of storing actual memory addresses, 
every node stores the XOR of addresses of previous and next nodes.

While traversing the list we need to remember the address of the previously 
accessed node in order to calculate the next node’s address

Consider XOR Linked list of A - B - C - D.
For example: When we are at node B, we must have the address of A. 
XOR of address(A) and 'both' value of B gives us the address(D)

XOR has this property:
If T = num_a ^ num_b, then
T ^ num_a = num_b
T ^ num_b = num_a
"""

class XORNode():
    """In the XOR linked list, instead of storing actual memory addresses, 
    every node stores the XOR of addresses of previous and next nodes. Call this 'both'
    """
    def __init__(self, val, prev: int, next: int):
        """
            val (int): value to store in the node
            prev (int): "memory address" of the previous node (list index)
            next (int): "memory address" of the next node (list index)
        """
        self.val = val
        # the 'both' pointer will be formed by XORing prev and next
        self.both = prev ^ next

    # we need to do these on the XORLinkedList side
    #def add(self, val): 
    #    pass

    #def get(self, index):
    #    pass

    def get_next_idx(self, prev_idx: int) -> int:
        """Get the mem loc (list index) for the next node"""
        return self.both ^ prev_idx

    def get_prev_idx(self, next_idx: int) -> int:
        """Get the mem loc (list index) for the prev node"""
        return self.both ^ next_idx

    def set_pointers(self, prev_idx, next_idx) -> None:
        self.both = prev_idx ^ next_idx


class XORLinkedList():
    """ We need this for the add and get"""
    def __init__(self):
        # initialize memory with a dummy node
        # prev_idx of -1 indicates that the node is at the beginning of the list
        # next_idx of -1 indicates that the node is at the end of the list
        self.mem = [XORNode(None, -1, -1)]


    def __len__(self):
        return len(self.mem) - 1


    def alloc_mem_addr(self) -> int:
        """Used to ask for a new "memory address" (next list index)"""
        return len(self.mem)


    def add(self, val):
        # traverse to the end of the linked list
        prev_idx, curr_idx, curr_node = -1, 0, self.mem[0]
        while True:
            next_idx = curr_node.get_next_idx(prev_idx)
            if next_idx == -1: 
                # we are at the end
                break
            prev_idx, curr_idx, curr_node = curr_idx, next_idx, self.mem[next_idx]

        # add the new node to the end
        # get new "memory address"
        new_idx = self.alloc_mem_addr()
        # update curr_node pointers (the last node before addition)
        curr_node.set_pointers(prev_idx, new_idx)
        self.mem.append(XORNode(val, curr_idx, -1))


    def get(self, idx: int):
        """Returns the ith node value for XOR linked list"""
        # we ignore the dummy node in these... so return ith real, added value
        if idx > len(self) - 1 or idx < 0:
            raise IndexError("idx out of range")

        # init with the dummy
        prev_idx, curr_idx, curr_node = -1, 0, self.mem[0]

        for _ in range(idx + 1):
            next_idx = curr_node.get_next_idx(prev_idx)
            prev_idx, curr_idx, curr_node = curr_idx, next_idx, self.mem[next_idx]

        return curr_node.val

    
# Some tests
XOR_llist = XORLinkedList()

for i in range(5, 16):
    XOR_llist.add(i)

recv_vals = []
for i in range(5, 16):
    recv_vals.append(XOR_llist.get(i-5))
    
assert recv_vals == list(range(5, 16)), recv_vals
