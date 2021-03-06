"""Running python profiler on this gives:


(py2-cython-tests) Daniels-MBP-6:cython-tests danielseita$ python profile.py 
Wed Mar 13 12:43:14 2019    Profile.prof

         10000004 function calls in 3.005 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    1.537    1.537    3.005    3.005 calc_pi.py:7(approx_pi)
 10000000    1.248    0.000    1.248    0.000 calc_pi.py:4(recip_square)
        1    0.220    0.220    0.220    0.220 {range}
        1    0.000    0.000    3.005    3.005 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


The most important columns here are tottime (total time spent in this function
not counting functions that were called by this function) and cumtime (total
time spent in this function also counting the functions called by this
function).

If you do nothing but add in a few type declarations, it's this:


(py2-cython-tests) Daniels-MBP-6:cython-tests danielseita$ python profile.py 
Wed Mar 13 13:02:33 2019    Profile.prof

         10000004 function calls in 1.749 seconds

   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    1.284    1.284    1.749    1.749 calc_pi.pyx:11(approx_pi)
 10000000    0.465    0.000    0.465    0.000 calc_pi.pyx:8(recip_square)
        1    0.000    0.000    1.749    1.749 {calc_pi.approx_pi}
        1    0.000    0.000    1.749    1.749 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


(I used a different file for this, and compiled with setup.py. I moved this file
to an `old` directory so the names wouldn't conflict.)

TL;DR: `approx_i` improved a little bit, `recip_square` improved more.
"""
import time

def recip_square(i):
    return 1. / i ** 2

def approx_pi(n=10000000):
    val = 0.
    for k in range(1, n + 1):
        val += recip_square(k)
    return (6 * val) ** .5


if __name__ == "__main__":
    tic = time.time()
    approx_pi()
    toc = time.time()
    print("{:.3f} s".format(toc-tic))
