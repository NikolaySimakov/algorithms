# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

import random

def rand7():
    return random.choice(range(1, 8))


class Solution:
    def rand10(self):
        return sum([rand7() for _ in range(9)]) % 10 + 1