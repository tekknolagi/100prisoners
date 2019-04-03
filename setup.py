import setuptools
from distutils.core import Extension

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="prisoners_problem",
    version="0.0.8",
    description="Simulate the 100 prisoners problem.",
    ext_modules=[
        Extension(
            "simulate_fast", sources=["prisoners_problem/simulate_fast.cpp"],
            extra_compile_args=['-std=c++11', '-Wall', '-Wextra'],
            language='c++',
            )
        ],
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
