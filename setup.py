from distutils.core import setup, Extension

simulate_fast_module = Extension('simulate_fast',
                           sources = ['simulate_fast.cpp'])

setup(name = '100prisoners',
      version = '1.0',
      description = '',
      ext_modules = [simulate_fast_module],

      url='https://bernsteinbear.com',
      author='Maxwell Bernstein',
      author_email='python@bernsteinbear.com')
