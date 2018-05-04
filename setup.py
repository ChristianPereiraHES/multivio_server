#!/usr/bin/env python3
from setuptools import setup, Extension
import os
poppler_install_path = '/usr/local'
import multivio

try:
    from Cython.Build import cythonize
except ImportError:
    print('You need to install cython first - sudo pip install cython', file=sys.stderr)
    sys.exit(1)

poppler_ext = Extension('multivio.poppler._mypoppler', ['multivio/poppler/mypoppler.pyx'],
                        language='c++',
                        extra_compile_args=['-I%s/include/poppler' % poppler_install_path],
                        extra_link_args=['-lpoppler'],
                        )

setup(
    name='multivio',
    version=multivio.__version__,
    description='Multivio server.',
    long_description='''Multivio is a project...''',
    license=multivio.__license__,
    url='http://www.multivio.org',
    py_modules=['multivio.poppler.mypoppler'],
    ext_modules=cythonize([poppler_ext]),
    packages=[
        'multivio'
    ],
    scripts=[
        'tools/multivio_server.py', 'tools/mvo_config_example.py'
    ],
    package_data={'multivio.mypoppler': ['*.so.*', 'multivio.mypoppler/*.so.*']},
    keywords=['multivio'],
    classifiers=[
        'Development Status :: Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Internal',
    ],
    install_requires=[]
)
