""" Day 10. Medium.

Implement a job scheduler which takes in a function f and an integer n, 
and calls f after n milliseconds.

Using sleep kinda works, but it's blocking.
Let's use a Timer from threading.

It represents an action that should be run only after a certain amount of time has passed 
(exactly what we need). It creates a thread to run in the background, i.e. non-blocking.
"""

from typing import Callable
from time import sleep
from threading import Timer


def job_scheduler(function: Callable, delay: int, 
                  verbose=False, blocking=False) -> None:
    """Simple job scheduler, basically implementing a timer.

    Args:
        function (Callable): Function that is to be scheduled
        delay (int): Delay in ms after which the function will be called
    """

    if verbose:
        print(f"Taking a nap for {delay} ms...")

    if blocking:    
        sleep(delay / 1000.)
        if verbose:
            print("Calling the function now!")
        function()
    else:
        t = Timer(delay / 1000., function)
        t.start()


# For testing
def say_hi() -> None:
    print("Hi!")

# These will overlap
job_scheduler(say_hi, 2000, verbose=True)
job_scheduler(say_hi, 3000, verbose=True, blocking=True)