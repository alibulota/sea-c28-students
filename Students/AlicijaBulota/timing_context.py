import time
import sys


class Timer(object):
    def __init__(self, t=sys.stdout):
        self.t = t

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.elapsed = time.time() - self.start
        print('This code took (%s) seconds.' % self.elapsed
        return self.t
