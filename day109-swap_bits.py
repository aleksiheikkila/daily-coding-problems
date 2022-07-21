""" Day 109. Medium
Given an unsigned 8-bit integer, swap its even and odd bits. The 1st and 2nd bit should be swapped, 
the 3rd and 4th bit should be swapped, and so on.

For example, 10101010 should be 01010101. 11100010 should be 11010001.
Bonus: Can you do this in one line?

Own example:
10011011
->
Expected
01100111

Approach:
A. Take 1st, 3rd, 5th and 7th bits, zero others --> 10001010
B. Take 2nd, 4th, 6th and 8th bits, zero others --> 00010001

Shift A to right by one --> 01000101
Shift B to left by one  --> 00100010

Bitwise OR
01000101
00100010
=>
01100111
"""

def swap_bits(num: int) -> int:
    mask = 85   # as bin: 01010101

    #print(f"Number given: {num}")
    #print(f"as binary: {bin(num)}")
    odd_bits = (num & mask)
    even_bits = (num & (mask << 1))

    #print(f"odd bits : {bin(odd_bits)}")
    #print(f"even bits: {bin(even_bits)}")

    return (odd_bits << 1) | (even_bits >> 1)


# Test cases:
assert swap_bits(num=int("0b10011011", 2)) == int("0b01100111", 2)
assert swap_bits(0) == 0
assert swap_bits(2) == 1
assert swap_bits(3) == 3
assert swap_bits(4) == 8
assert swap_bits(100) == 152  # 01100100  --> 10011000 = 152