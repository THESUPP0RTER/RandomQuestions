#Determine whether an integer is a palindrome.
#An integer is a palindrome when it reads the same backward as forward
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x > 0:
        return False
    old_input = x
    reverse: int = 0
    while x > 0:
        digit = x % 10
        reverse *= 10
        reverse += digit
        x //= 10

    return old_input == reverse
