from distutils.core import setup, Extension

luckybit_hash_module = Extension('luckybit_hash',
                                 sources = ['luckybitmodule.c',
                                            'luckybit.c',
                                            'sha3/neoscrypt.c'],
                               include_dirs=['.', './sha3'])

setup (name = 'luckybit_hash',
       version = '1.3.1',
       description = 'Binding for luckybit Neoscrypt proof of work hashing.',
       ext_modules = [luckybit_hash_module])
