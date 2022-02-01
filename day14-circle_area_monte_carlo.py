""" DAY 14
The area of a circle is defined as r^2. 
Estimate \pi to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x^2 + y^2 = r^2.

###################

Imagine box with corner points (x,y) of
    * (-1, -1)
    * (-1, 1)
    * (1, -1)
    * (1, 1)

This has an area of 4.

The unit circle (r=1) has an area of pi*r^2 = pi.

So now we repeatedly generate random points inside the box and count how many fall inside the unit circle.
The proportion falling inside the circle tends to pi / 4 (the ratio of the areas).
So th estimate for pi is 4 * (num_points_inside_circle / all_points)

Could be made faster...

"""

from numpy.random import uniform 

def estimate_pi(num_iters: int = 1_000_000) -> float:
    num_inside_circle = 0
    for _ in range(num_iters):
        # draw a random point
        x, y = uniform(-1, 1), uniform(-1, 1)
        if x**2 + y**2 < 1:
            num_inside_circle += 1

    return 4 * num_inside_circle / num_iters
