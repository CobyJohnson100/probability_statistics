from setuptools import setup, find_packages

setup(
    name="probability_statistics",
    version="0.1.0",
    author="CobyJohnson100",
    description="A library for probability and statistics calculations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/CobyJohnson100/probability_statistics",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",  # Adjust if you have a specific license
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.8",
)