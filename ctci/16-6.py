"""
This solution can be bruteforced with O(a*b).
If we sort both arrays we can use pointers
and go through it all in a single pass.

Final solution O(a log a + b log b)
"""


def smallest(a, b):
    a.sort()
    b.sort()
    diff = float('inf')
    i = j = 0

    while i < len(a) and j < len(b):
        if abs(a[i] - b[j]) < diff:
            diff = abs(a[i] - b[j])

        if a[i] > b[j]:
            j += 1
        else:
            i += 1

    return diff


res = smallest(
    a=[1, 3, 15, 11, 2],
    b=[23, 127, 235, 19, 8]
)
print(res)
