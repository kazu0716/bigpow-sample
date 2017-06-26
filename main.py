# coding: utf-8

import time
from sys import argv


class Bigpower(object):

    @classmethod
    def power(cls, a, n):
        if n == 0:
            return 1
        if n % 2 == 1:
            return a * cls.power(a, n - 1)
        else:
            return cls.power(a * a, n / 2)

if __name__ == '__main__':
    since = time.time()
    print(Bigpower.power(int(argv[1]), int(argv[2])))
    print("time spent in this proc: " + str(round((time.time() - since), 4)) + " ms")
