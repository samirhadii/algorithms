# simple recursive factorial function below

# def factorial_recursive(n):
#     print("bleh ", n)
#     if n == 0:
#         return 1
#     return n * factorial_recursive(n-1)

# we can use dynamic programming to optimize this recursion where there are a lot of repeated calculations,

memoize = {}  # empty dict to store reseults


def dp_factorial(n):
    if n in memoize:  # optimization from above using memoization
        return memoize[n]

    if n == 1 or n == 0:  # base case
        result = 1
    else:
        result = n * dp_factorial(n - 1)  # recursive call

    memoize[n] = result
    return result


# this is a top-down memoization dynamic proggraming approach to factorial problem
# O(N) space and O(N) time
