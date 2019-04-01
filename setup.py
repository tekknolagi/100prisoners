import setuptools
from distutils.core import Extension

simulate_fast_module = Extension(
        "simulate_fast", sources=["prisoners_problem/simulate_fast.cpp"]
)

setuptools.setup(
    name="prisoners_problem",
    version="0.0.1",
    description="Simulate the 100 prisoners problem.",
    ext_modules=[simulate_fast_module],
    url="https://github.com/tekknolagi/100prisoners",
    author="Maxwell Bernstein",
    packages=setuptools.find_packages(),
    author_email="python@bernsteinbear.com",
)
