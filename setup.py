from setuptools import setup

setup(
    name='pip_package',
    version='0.0.1',
    description='My private package from private github repo',
    url='git://git@github.com/Goar/pip_package.git',
    author='Goar Orue Sanchez',
    author_email='goarorue@gmail.com',
    license='unlicense',
    packages=['pip_package'],
    zip_safe=False
)
