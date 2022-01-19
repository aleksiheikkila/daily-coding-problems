""" DAY 7. Medium.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, 
count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

######

Smells like a dynamic programming.

First character can be decoded in one ways

The second one can be decoded in one way
first and second could be 


###################
Example "6789"
INP [6,7,8,9]
DP  [1,1,1,1]

from 2nd onwards, we need to check if the last two vals are 1or2 and 0to6

###################
Example "111"
INP [1,1,1]
DP  [1,2,3]

sol = 3
1 1 1
1 11
11 1


###################
Example "1111"
INP [1,1,1,1]
DP  [1,2,3,5]

sol = 5
1 1 1 1
1 1 11
1 11 1
11 1 1
11 11

###################
Example "5117"
INP [5,2,1,7]
DP  [1,1,2,2]

sol=2
5 1 1 7
5 11 7


###################
Example "11111"
INP [1,1,1,1,1]
DP  [1,2,3,5,8]

sol=8
1 1 1 1 1
1 1 1 11
1 1 11 1
1 11 1 1
11 1 1 1
11 11 1
11 1 11
1 11 11

"""


def get_num_ways(msg: str) -> int:
    """[summary]

    """
    if not msg or len(msg) == 0:
        return 0

    msg_ints = [int(c) for c in msg]
    ways = [0] * (len(msg_ints) + 1)
    ways[0], ways[1] = 1, 1

    for i in range(1, len(msg_ints)):
        if 0 < msg_ints[i-1] < 3 and msg_ints[i] <= 6:
            ways[i+1] = ways[i] + ways[i-1]
        else:
            ways[i+1] = ways[i]

    return ways[-1]


# Test cases
assert get_num_ways("111") == 3
assert get_num_ways("48496046960") == 1
assert get_num_ways("1") == 1
assert get_num_ways("") == 0