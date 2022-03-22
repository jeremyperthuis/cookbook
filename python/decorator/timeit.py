import time

def timeit(f):
    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print(f"Finish function : {f.__name__}{args} after {te-ts} seconds.")
        return result

    return timed


@timeit
def compute_magic(arg):
    time.sleep(3)
    print(arg)

compute_magic("test ok")
