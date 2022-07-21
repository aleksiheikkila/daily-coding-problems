""" DAY 294. Medium

A competitive runner would like to create a route that starts and ends at his house, 
with the condition that the route goes entirely uphill at first, and then entirely downhill.

Given a dictionary of places of the form {location: elevation}, and a dictionary mapping paths 
between some of these locations to their corresponding distances, find the length of the shortest 
route satisfying the condition above. Assume the runner's home is location 0.

For example, suppose you are given the following input:

elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
paths = {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10
}  # hmm... (0,3) and (3,0) has different distance.

In this case, the shortest valid path would be 0 -> 2 -> 4 -> 0, with a distance of 28.

===========================================
BFS?

Tarkoittaa että tietyssä pisteessä voidaan käydä max kahdesti. Kerran ylös, kerran alas.
Ylös ja alas legeillä max kerran per paikka

need to go up at least once
need to go downhill at least once

Kotoa ylös. OK, mitkä mahdollisia.

Tämähän tarkoittaa

no need to consider elevators below home

"""


def shortest_distance(elevations: dict, paths: dict) -> int:
    home_elev = elevations[0]
    
    # reduce data
    # no need to consider elevations below home
    elevs = {k: v for k, v in elevations.items() if v >= home_elev}
    paths = {k: v for k, v in paths.items() if all((k[0] in elevs, k[1] in elevs))}

    min_dist = float("inf")
    s = []
    # stack to contain tuples of (location, direction, total_dist so far)
    # init with possible uphill options
    s = [(dest, "up", dist) for (orig, dest), dist in paths.items() 
            if orig == 0 and elevs[dest] > home_elev]

    # From this, we can either continue going up if that is the current direction
    # or revert to downpath (and never revert again)
    while s:
        curr_loc, direction, total_dist = s.pop()
        for (orig, dest), dist in paths.items():
            # use only those originating at the current location
            if orig != curr_loc:
                continue
            
            # have seen shorter route already, no need to continue (prune)
            if total_dist + dist >= min_dist:
                continue
            
            # add downhill options:
            if elevs[dest] < elevs[curr_loc]:
                # if destination is home, update min_dist and do not continue this route any more
                if dest == 0:
                    min_dist = min(min_dist, total_dist + dist)
                    continue
            
                # dest not home, add to stack
                s.append((dest, "down", total_dist + dist))
                continue
            
            # if we were going uphill, add possible uphill options:
            if direction == "up" and elevs[dest] > elevs[curr_loc]:
                s.append((dest, "up", total_dist + dist))

    # is it guaranteed that the loop will terminate in all cases?
    return min_dist


# Test case
TEST_ELEVATIONS = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
TEST_PATHS = {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10
}

print(shortest_distance(TEST_ELEVATIONS, TEST_PATHS))
assert shortest_distance(TEST_ELEVATIONS, TEST_PATHS) == 28
