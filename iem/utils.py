import io, csv
import time, functools, logging
from contextlib import contextmanager

def timeit(func):
    @functools.wraps(func)
    def newfunc(*args, **kwargs):
        startTime = time.time()
        ret = func(*args, **kwargs)
        elapsedTime = time.time() - startTime
        logging.debug('function [{}] finished in {} ms'.format(
            func.__name__, int(elapsedTime * 1000)))
        return ret
    return newfunc

@contextmanager
def timeit_context(name):
    startTime = time.time()
    yield
    elapsedTime = time.time() - startTime
    logging.debug('[{}] finished in {} ms'.format(name, int(elapsedTime * 1000)))

def to_csv(rows, fieldnames):
    f = io.StringIO()
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
    return f.getvalue()