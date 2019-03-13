from Cython.Build import cythonize

# ------------------------------------------------------------------------------
# distutils
# compile with:  python setup.py build_ext --inplace
# use `annotate` to get html files for investigating code.
# ------------------------------------------------------------------------------

from distutils.core import setup

setup(
    ext_modules=cythonize(['example.pyx', 'example_py_cy.py'], annotate=True),
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
