import platform
import setuptools
import sys
from distutils.ccompiler import new_compiler
from distutils.core import Extension
from distutils.sysconfig import customize_compiler


if sys.version_info[0] >= 3:
    from subprocess import getoutput
else:
    from commands import getoutput

def using_clang():
    """Will we be using a clang compiler?"""
    compiler = new_compiler()
    customize_compiler(compiler)
    compiler_ver = getoutput("{0} -v".format(compiler.compiler[0]))
    return 'clang' in compiler_ver

cpp_extra_compile_args = ['-stdlib=libc++', '-std=c++11', '-Wall', '-Wextra']
cpp_extra_link_args = ['-stdlib=libc++']
if platform.system() == 'Darwin' and using_clang():
        cpp_extra_compile_args.append('-stdlib=libc++')
        cpp_extra_compile_args.append('-mmacosx-version-min=10.9')
        cpp_extra_link_args.append('-stdlib=libc++')
        cpp_extra_link_args.append('-mmacosx-version-min=10.7')

with open("README.md", "r") as f:
    long_description = f.read()

simulate_extension = Extension(
    "simulate_fast", sources=["prisoners_problem/simulate_fast.cpp"],
    extra_compile_args=cpp_extra_compile_args,
    extra_link_args=cpp_extra_link_args,
    language='c++')

setuptools.setup(
    name="prisoners_problem",
    version="0.0.8",
    description="Simulate the 100 prisoners problem.",
    ext_modules=[simulate_extension],
    url="https://github.com/tekknolagi/100prisoners",
    author="Maxwell Bernstein",
    packages=setuptools.find_packages(),
    author_email="python@bernsteinbear.com",
    install_requires=[
        'numpy==1.16.2',
        'matplotlib==3.0.3',
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
