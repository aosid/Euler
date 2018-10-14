# memoization helper function
def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper

# recursively defined function that outputs the nth fibonacci number, with starting conditions fib(0) = 0 and fib(1) = 1.
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

fib = memoize(fib)

def count():
    sum = 0
    i = 0
    while fib(i) <= (4*10**6):
        if fib(i) % 2 == 0:
            sum += fib(i)
        i += 1
    print(sum)