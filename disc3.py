def multiply(m, n):
    """Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m
    else:
        return m + multiply(m,n-1)

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 2 and n > 0:
        return n
    else:
        return n * skip_mul(n - 2)


def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    # the gist of this test is to find out whether n is divisible by any number greater than 1 and smaller than the square root of n. Therefore, we have to track two parameters, the dividend n and divisor x
    def helper(x): # define a helper function to track the divisor x
        if x > (n ** 0.5): # if divisor is incremented to the level greater than root n and no factor is found, we can conclude that n is a prime number
            return True
        elif n % x == 0: # As long as the divisor is within the interval, find out if it is a factor of n. If yes, then n is not prime.
            return False
        else:
            return helper(x+1) # recurse the helper function by incrementing the divisor, until a factor is found or the divisor reaches the limit
    return helper(2) # initiating the recursing by calling helper function on 2, which is the base case.



def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    if n == 1:
        print(n)
        return 1
    elif n % 2 == 0:
        print(n)
        return hailstone(int(n / 2)) + 1
    elif n % 2 != 0:
        print(n)
        return hailstone(int(n * 3) + 1) + 1


def merge(n1,n2):
    '''Merges two numbers with digits in descending order into a new number with digits in decreasing order.'''
    assert descending(n1) and descending(n2), "The number the function takes should be with digits in descending order."
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    elif n1 % 10 > n2 % 10:
        return merge(n1, n2 // 10) * 10 + n2 % 10
    else:
        return merge(n1 // 10, n2) * 10 + n1 % 10

    
# iteration method
def descending(n):
    while n > 10:
        second_to_last, last = n // 10 % 10, n % 10
        n = n // 10
        if last <= second_to_last:
            return True
        else:
            return False
    return True

# recursion method
def descending_rec(n):
    if n < 10:
        return True
    else:
        second_to_last, last = n // 10 % 10, n % 10
        if second_to_last >= last:
            return descending_rec(n // 10)
        else:
            return False 
 








        


