""" DAY 275 "Look and say". MEDIUM
The "look and say" sequence is defined as follows: 
beginning with the term 1, each subsequent term visually describes the digits appearing in the previous term. 
The first few terms are as follows:

1
11
21
1211
111221
As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.

Given an integer N, print the Nth term of this sequence.
"""

def get_look_and_say_gen():
    """Returns a generator object yielding next elements in the sequence"""
    def get_next(curr:str) -> str:
        if not curr or len(curr) == 0:
            return ""
        rst = []
        char, count = None, 0
        for c in curr:
            if c == char:
                count += 1
                continue
            else:  # None case also covered
                if char is not None:
                    rst.append(f"{str(count)}{char}")
                char, count = c, 1
                continue

        # something in the buffer
        rst.append(f"{str(count)}{char}")
        return "".join(rst)

    curr = "1"
    yield curr

    while True:
        curr = get_next(curr)
        yield curr


def look_and_say(n: int):
    elements_gen = get_look_and_say_gen()
    for _ in range(n):
        print(next(elements_gen))
