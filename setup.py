from Cython.Build import cythonize

# distutils alternative (let's avoid for now)
# from distutils.core import setup
from setuptools import setup
from setuptools.extension import Extension

ext_modules = [
    Extension('test', ['test.pyx']),
]

setup(
    name='Test',
    ext_modules=cythonize(ext_modules),
    zip_safe=False,
)
