import time, functools

def retry(max_attempts=3, delay=1.0):
    def dec(fn):
        @functools.wraps(fn)
        def wrapper(*a, **kw):
            for i in range(max_attempts):
                try:
                    return fn(*a, **kw)
                except Exception:
                    if i == max_attempts-1: raise
                    time.sleep(delay * 2**i)
        return wrapper
    return dec
