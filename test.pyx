import numpy as np
import time


def hi(name):
    print("Hello {}".format(name))


if __name__ == "__main__":
    tic = time.time()
    hi('bleh')
    toc = time.time()
    res = toc-tic
    print("result: {:.6f} sec".format(res))
