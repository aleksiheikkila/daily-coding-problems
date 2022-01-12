# MEDIUM

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
# and deserialize(s), which deserializes the string back into the tree.

import json
# Serialize to json string

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node(val: {self.val},\n left: {self.left},\n right: {self.right})\n"


def serialize(root: Node) -> str:
    if root is None:
        return None

    ser_root = {}
    ser_root["val"] = root.val

    ser_left = serialize(root.left)   # Node object, or None
    ser_right = serialize(root.right)

    if ser_left is not None:
        ser_root["left"] = ser_left
    if ser_right is not None:
        ser_root["right"] = ser_right

    return json.dumps(ser_root)


def deserialize(json_repr:str) -> Node:
    # read serialized string representation to dictionary
    ser_node = json.loads(json_repr)
    
    # create Node, recurse into left and right where needed
    node = Node(ser_node["val"])
    if "left" in ser_node:
        node.left = deserialize(ser_node["left"])
    if "right" in ser_node:
        node.right = deserialize(ser_node["right"])

    return node


#The following test should pass:
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

print("Repr of root")
print(node)

print("\nAfter serialising:")
serialized = serialize(node)
print(serialized)

print("\nAfter deserialising:")
deser = deserialize(serialized)
print(deser)
