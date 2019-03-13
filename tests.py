"""Test cython code.
"""
import time

# First two here are exactly same except one is cython-compiled, other is pure
# python. The third thing is cython-compiled _with_ lots of 'cythonization'.
from example_py    import primes_python
from example_py_cy import primes_python_compiled
from example       import primes


def test(n):
    """With n=10k, I get:

    (py2-cython-tests) Daniels-MBP-6:cython-tests danielseita$ python tests.py
    python: 2.321
    python compiled: 1.221
    cythonized compiled: 0.002

    It's consistent across several runs, though I know time.time() is probably
    less accurate than timeit.
    """
    tic = time.time()
    primes_python(n)
    print("python: {:.3f}".format(time.time()-tic))

    tic = time.time()
    primes_python_compiled(n)
    print("python compiled: {:.3f}".format(time.time()-tic))

    tic = time.time()
    primes(n)
    print("cythonized compiled: {:.3f}".format(time.time()-tic))


if __name__ == "__main__":
    n=10000
    test(n)
