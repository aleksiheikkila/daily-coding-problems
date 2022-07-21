""" Day 276, Friend Groups / Transitive Closure. Easy
A classroom consists of N students, whose friendships can be represented in an adjacency list. 
For example, the following descibes a situation where 0 is friends with 1 and 2, 3 is friends with 6, and so on.

{0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3]} 

Each student can be placed in a friend group, which can be defined as the transitive closure of that student's friendship relations.
In other words, this is the smallest set such that no student in the group has any friends outside this group. 
For the example above, the friend groups would be {0, 1, 2, 5}, {3, 6}, {4}.

Given a friendship list such as the one above, determine the number of friend groups in the class.
"""

from collections import defaultdict


def get_groups(adj: dict) -> list:
    seen = set()
    groups = defaultdict(set)
    curr_grp_idx = 0

    for root_person, friend_list in adj.items():
        if root_person in seen:
            continue
        curr_grp_idx += 1
        groups[curr_grp_idx].add(root_person)
        stack = friend_list.copy()
        # dfs
        while stack:
            person = stack.pop()
            if person in seen:
                continue
            seen.add(person)
            groups[curr_grp_idx].add(person)
            stack.extend(adj[person])

    return groups

"""
def get_num_groups(adj: dict) -> int:
    num_groups = 0
    seen = set()

    for root_person, friend_list in adj.items():
        if root_person in seen:
            continue
        num_groups += 1
        stack = friend_list.copy()
        # dfs
        while stack:
            person = stack.pop()
            if person in seen:
                continue
            seen.add(person)
            stack.extend(adj[person])

    return num_groups
"""

TEST_DATA = {
    0: [1, 2],
    1: [0, 5],
    2: [0],
    3: [6],
    4: [],
    5: [1],
    6: [3]
 }


groups = get_groups(TEST_DATA)
assert len(groups) == 3
print(groups)
