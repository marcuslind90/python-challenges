def search(haystack, needle):
    """
    Return index of first occurance of needle in sorted haystack.
    """
    left = 0
    right = len(haystack)-1
    res = -1
    while left <= right:
        mid = (right+left)//2
        if needle < haystack[mid]:
            right = mid-1
        elif needle > haystack[mid]:
            left = mid+1
        else:
            # Instead of returning the key whenever we match,
            # we keep searching to the left to make sure
            # that we return the first occurance of the needle.
            right = mid-1
            res = mid

    return res


print(search([1, 1, 1, 3, 3, 10, 12, 13, 15], 3))
