"""
A network consists of nodes labeled 0 to N. You are given a list of edges (a, b, t), 
describing the time t it takes for a message to be sent from node a to node b. 
Whenever a node receives a message, it immediately passes the message on to a neighboring node, if possible.

Assuming all nodes are connected, determine how long it will take for every node to receive a message that begins at node 0.

For example, given N = 5, and the following edges:

edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5)
]
You should return 9, because propagating the message from 0 -> 2 -> 3 -> 4 will take that much time.
"""

from collections import defaultdict

def get_time_to_each_node(edges: list) -> dict:
    """Lets generate the first time a message reaches each node.
    Could perhaps also terminate early (no need everytime to construct the whole thing)"""
    time_to_node = dict()
    adjs = defaultdict(list)
    # assume no duplicates
    for edge in edges:
        origin_node, dest_node, t = edge
        adjs[origin_node].append((dest_node, t))

    stack = [(0, 0)]  # starting point: node=0, curr_time=0
    while stack:  # dfs
        curr_node, curr_time = stack.pop()
        if curr_node not in time_to_node or curr_time < time_to_node[curr_node]:
            time_to_node[curr_node] = curr_time
            for (neighbor, ttd) in adjs[curr_node]:
                stack.append((neighbor, curr_time + ttd))
        # else we already have better time to this node, so no need to reconstruct

    return time_to_node


def get_time_to_node(edges: list, node: int) -> int:
    time_to_node = get_time_to_each_node(edges)
    return time_to_node.get(node)

    
TEST_EDGES = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5)
]

assert get_time_to_node(TEST_EDGES, 4) == 9
assert get_time_to_node(TEST_EDGES, 0) == 0
assert get_time_to_node(TEST_EDGES, 1) == 5
assert get_time_to_node(TEST_EDGES, 3) == 4

print(get_time_to_each_node(TEST_EDGES))
