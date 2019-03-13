# cython-tests

Testing cython and python, also with numpy

See:

- https://cython.readthedocs.io/en/latest/src/quickstart/index.html
- https://github.com/cython/cython/wiki


## Installation and Steps to Reproduce

[Missing step, make an alias for cython virtualenv]


```
Daniels-MBP-6:~ danielseita$ virtualenv --python python2 seita-venvs/py2-cython-tests
Running virtualenv with interpreter /usr/local/bin/python2
New python executable in /Users/danielseita/seita-venvs/py2-cython-tests/bin/python2.7
Also creating executable in /Users/danielseita/seita-venvs/py2-cython-tests/bin/python
Installing setuptools, pip, wheel...
done.
Daniels-MBP-6:~ danielseita$ source ~/seita-venvs/py2-cython-tests/bin/activate
(py2-cython-tests) Daniels-MBP-6:~ danielseita$ vim ~/.bashrc
(py2-cython-tests) Daniels-MBP-6:~ danielseita$ . ~/.bashrc
(py2-cython-tests) Daniels-MBP-6:~ danielseita$ . ~/.bash_profile
(py2-cython-tests) Daniels-MBP-6:~ danielseita$ source ~/.bashrc
(py2-cython-tests) Daniels-MBP-6:~ danielseita$ cython
(py2-cython-tests) Daniels-MBP-6:~ danielseita$ pip list --local
DEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 won't be maintained after that date. A future version of pip will drop support for Python 2.7.
Package    Version
---------- -------
pip        19.0.3
setuptools 40.8.0
wheel      0.33.1
(py2-cython-tests) Daniels-MBP-6:~ danielseita$ pip install cython
DEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 won't be maintained after that date. A future version of pip will drop support for Python 2.7.
Collecting cython
  Downloading https://files.pythonhosted.org/packages/1e/b1/efbba7bc4856a3819db764c711ed71265287a4e3cb54fc2f00ce66fe2a11/Cython-0.29.6-cp27-cp27m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (2.8MB)
    100% |████████████████████████████████| 2.8MB 6.3MB/s
Installing collected packages: cython
Successfully installed cython-0.29.6
(py2-cython-tests) Daniels-MBP-6:~ danielseita$ pip install numpy
DEPRECATION: Python 2.7 will reach the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 won't be maintained after that date. A future version of pip will drop support for Python 2.7.
Collecting numpy
  Downloading https://files.pythonhosted.org/packages/bc/90/3e71b5392bd81d8559917ee38857bb2e4b92c88e87211a68e339127b86f5/numpy-1.16.2-cp27-cp27m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (13.9MB)
    100% |████████████████████████████████| 13.9MB 1.5MB/s
Installing collected packages: numpy
Successfully installed numpy-1.16.2
(py2-cython-tests) Daniels-MBP-6:~ danielseita$
```


## Other Helpful Resources

(Besides the official documentation, obviously.)

- https://stackoverflow.com/questions/2697275/cython-speed-boost-vs-usability
- https://stackoverflow.com/questions/22936413/why-there-is-a-huge-performance-difference-between-these-two-codes-in-python-and?
- https://stackoverflow.com/questions/44875043/attempting-to-build-a-cython-extension-to-a-python-package-not-creating-shared
