from time import process_time


def logger(func):
    def wrapper(*args, **kwargs):
        a = ", ".join(map(str, args))
        ka = ", ".join(f"{key}={value}" for key, value in kwargs.items())
        msg = f'{func.__name__}({a}'
        if ka:
            msg += ', {ka})'
        else:
            msg += ')'
        print(msg)
        result = func(*args, **kwargs)
        print(msg, '=', result)
        return result

    return wrapper


def timeit(func):
    def wrapper(*args, **kwargs):
        start = process_time()
        result = func(*args, **kwargs)
        print(process_time() - start)
        return result

    return wrapper


@logger
@timeit
def f(a, b):
    return a + b


print(f(132135468765436532513654, 132135468476876873564687))
