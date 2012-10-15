from distutils.core import setup, Extension
setup(
    name='fallocate',
    version='1.0',
    packages=[
        'fallocate',
        'fallocate.defines',
        'fallocate.ext',
        'fallocate.ext.cconst',
    ],
    ext_modules=[
        Extension('fallocate/defines/libfallocdefines', ['fallocate/defines/falloc_defines.c'])
    ],
)
