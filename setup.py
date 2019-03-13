from Cython.Build import cythonize

# ------------------------------------------------------------------------------
# distutils
# compile with:  python setup.py build_ext --inplace
# use `annotate` to get html files for investigating code.
# ------------------------------------------------------------------------------

from distutils.core import setup

exts = ['example.pyx', 'example_py_cy.py', 'calc_pi.pyx']

setup(
    ext_modules=cythonize(exts, annotate=True),
)


# ------------------------------------------------------------------------------
# setuptools
# ------------------------------------------------------------------------------

#from setuptools import setup
#from setuptools.extension import Extension
#
#ext_modules = [
#    Extension('test', ['test.pyx']),
#]
#
#setup(
#    name='test',
#    ext_modules=cythonize(ext_modules),
#    zip_safe=False,
#)
