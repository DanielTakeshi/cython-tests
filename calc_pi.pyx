# cython: profile=True

"""
The line above is needed to tell Cython that profiling is enabled.
"""
import time
cimport cython

@cython.profile(False)
cdef inline double recip_square(int i):
    return 1. / (i*i)

def approx_pi(int n=10000000):
    """Whew, you can type default values."""
    cdef double val = 0.
    cdef int k
    for k in range(1, n + 1):
        val += recip_square(k)
    return (6 * val) ** .5


if __name__ == "__main__":
    tic = time.time()
    approx_pi()
    toc = time.time()
    print("{:.3f} s".format(toc-tic))
