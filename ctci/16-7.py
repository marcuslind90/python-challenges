"""
Find the max between 2 numbers without
using comparison operators or if statements.
"""


def max_int(a, b):
    # The absolute difference, plus the sum, divided by 2
    # returns the max value of the two.
    diff = abs(a-b)
    s = a+b
    return (diff+s)//2


def max_bit(a, b):
    def flip(bit):
        return 1 ^ bit

    def sign(num):
        return flip((num >> 31) & 0x1)

    def get_max_naive(a, b):
        # We know that if a-b > 0 then a is larger than b.
        # k is either 1 or 0 indicating the positive or negative of
        # a-b. q is k inversed.
        k = sign(a - b)
        q = flip(k)

        # We multiply each value with their k or q which is either 0 or 1.
        # This means only 1 value remains, the other is set to 0.
        return a * k + b * q

    return get_max_naive(a, b)


print(max_bit(10, 50))
