""" Day 268 - Is power of four? Medium.
Given a 32-bit positive integer N, determine whether it is a power of four in faster than O(log N) time.

Let's have a look how the sequence shapes up...

1
0b1

4
0b100

16
0b10000

64
0b1000000

256
0b100000000

1024
0b10000000000

4096
0b1000000000000

16384
0b100000000000000

65536
0b10000000000000000

262144
0b1000000000000000000
"""

def is_power_of_four(n: int) -> bool:
    """Nice trick using bit manipulation
    From: https://stackoverflow.com/questions/19607856/determining-whether-a-number-is-a-power-of-four-in-time-olog-log-n/"""
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be positive integer")
    
    mask = 0x55555554  # 1010101010 1010101010 1010101010 0, for 32 bit case
    return (n & (-n) & mask) == n
    # select least significant 1 bit, then keep it if it's in the correct position. Then check that that's all we have


def is_power_of_four_simple(n: int) -> bool:
    """keep dividing the number by 4, check the modulo"""
    if n < 4:
        return False

    while n != 1:
        if n % 4 > 0:
            return False
        n = n // 4

    return True


# Test cases for both functions
assert(is_power_of_four(1024))
assert(is_power_of_four(4))
assert(not is_power_of_four(1))
assert(not is_power_of_four(2000202002))


assert(is_power_of_four_simple(1024))
assert(is_power_of_four_simple(4))
assert(not is_power_of_four_simple(1))
assert(not is_power_of_four_simple(2000202002))