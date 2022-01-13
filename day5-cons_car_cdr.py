""" DAY 5: Medium. Kind of functional programmming mindbender.

cons(a, b) constructs a pair, 
and car(pair) and cdr(pair) returns the first and last element of that pair. 

For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given the below implementation of cons, implement car and cdr

"""

# So this returns a function 'pair' that applies the parameter function f by calling f(a,b)

def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


def car(func):
    """Need to call func (returned by cons) with another function as parameter 
    that returns the first value"""
    return func(lambda x, y: x)  


def cdr(func):
    """Need to call func (returned by cons) with another function as parameter 
    that returns the second value"""
    return func(lambda x, y: y)   


assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4
assert cdr(cons(0, 0)) == 0
