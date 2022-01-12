# EASY

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

def two_nums_add_to(to: int, nums: list) -> bool:
    needed = set()
    for num in nums:
        if num in needed:
            return True
        needed.add(to - num)
    return False
    

assert two_nums_add_to(10, [10, 15, 3, 7]) == True
assert two_nums_add_to(11, [10, 15, 3, 7]) == False
assert two_nums_add_to(17, [10, 15, 3, 7]) == True
