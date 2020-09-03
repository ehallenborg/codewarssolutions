cache = {0: 0, 1: 1}

def fibonacci(n):
    if n in [0, 1]:
        return cache.get(n)
    else:
        if n in cache.keys():
            return cache.get(n)
        else:
            result = 0
            for i in range(2, n + 1):
                result = fibonacci(i - 1) + fibonacci(i - 2)
            cache[n] = result
    return cache.get(n)


'''
using an import
'''
from functools import lru_cache

@lru_cache(None)
def fibonacci_with_import(n):
    if n in [0, 1]:
        return n
    return fibonacci_with_import(n - 1) + fibonacci_with_import(n - 2)

'''
xrange solution - only in python2
so for python3 - use different solution since this will cause a timeout with just range
'''
def fibonacci_xrange(n):
    cache = [0,1]
    for i in xrange(2, n+1):
        cache.append(cache[i-1] + cache[i-2])
    return cache[n]

'''
def within a def
'''
def fibonacci_def(m):
    cache = {0:0, 1:1}
    def fib(n):
        if n not in cache:
            cache[n] = fib(n-1)+fib(n-2)
        return cache[n]
    return fib(m)