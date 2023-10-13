def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    total = 1
    if k != 0:
        while k > 0:
            k -= 1
            total = total * (n-k)
        return total #required to return the value while k != 0
    else:
        return total



def divisible_by_k(n, k):
    """
    >>> a = divisible_by_k(10, 2)  # 2, 4, 6, 8, and 10 are divisible by 2
    2
    4
    6
    8
    10
    >>> a
    5
    >>> b = divisible_by_k(3, 1)  # 1, 2, and 3 are divisible by 1
    1
    2
    3
    >>> b
    3
    >>> c = divisible_by_k(6, 7)  # There are no integers up to 6 divisible by 7
    >>> c
    0
    """
    count = 0
    if n >= k:
        test = 1
        while test <= n:
            if test % k == 0:
                print(test)
                count += 1
            test += 1
        return count
    else:
        return count



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    divisor = 10
    total = 0
    while y // divisor != 0:
        total, y = total + y % divisor, y // divisor
    return total + y




def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    first_digit = 0
    second_digit = 0
    divisor = 10
    result = False
    while n // divisor != 0:
        first_digit, n= n % divisor, n // divisor
        second_digit = n % divisor
        if first_digit == 8 and second_digit == 8:
            result = True
    return result


    

