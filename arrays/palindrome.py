def longest_palindrome(s, left, right):
    """
    Gets the longest palindrome from an index in a string.
    """
    longest = ''
    while left >= 0 and right < len(s) and s[left] == s[right]:
        longest = s[left:right+1]
        left -= 1
        right += 1

    return longest


def is_palindrome(s):
    """
    Gets the longest palindrome from the mid of a string
    and compare it to the original string to confirm if
    the original string was a Palindrome or not.
    """
    mid = len(s)//2
    if len(s) % 2 == 0:
        # Even string...
        longest = longest_palindrome(s, mid, mid+1)
    else:
        # Uneven string...
        longest = longest_palindrome(s, mid, mid)

    return longest == s


print(is_palindrome("abad"))
print(longest_palindrome("abad", 1, 1))
