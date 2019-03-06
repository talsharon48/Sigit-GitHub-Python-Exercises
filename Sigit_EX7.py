# the cache function that gets function and return memoized function
def cache_dec(func):
    cache = {}

    # function that runs func and put its result into the cache
    def cache_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return cache_func


# heavy function such as: fibonacci
# the parameter b is unused parameter, just to check the generic memoization
@cache_dec
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# main function that call the functions above
def main():
    print(fibonacci(320))

if __name__ == '__main__':
    main()
