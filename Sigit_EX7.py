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
