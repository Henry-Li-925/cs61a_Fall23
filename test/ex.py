def average(x, y):
    return (x + y) / 2

def improve(update, close, guess = 1):
    while not close(guess):
        guess = update(guess) 
    return guess

def sqrt(a):
    def sqrt_update(x): #refrain from adding another positional argument "a" that misleads the equation to require another argument 
        return average(x, a/x)
    def sqrt_close(x): #refrain from adding another positional argument "a" that misleads the equation to require another argument 
        return approx_eq(x * x, a)
    return improve(sqrt_update, sqrt_close)


def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance

result = sqrt(256)

