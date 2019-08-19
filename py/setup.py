from setuptools import setup, find_packages
import os
import io

with io.open(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                          "..", 'README.rst')), encoding="utf-8") as f:
    long_description = f.read()

with io.open(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                          "..", 'LICENSE.txt')), encoding="utf-8") as f:
    license = f.read()

setup(
    name='sophus',
    version='1.0.0',
    description='c++ implementation of Lie groups',
    long_description=long_description,
    author='Hauke Strasdat',
    author_email='strasdat@example.com',
    url="https://github.com/strasdat/Sophus",
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
)
