import os
from setuptools import setup
from scipy_sphinx_theme import __version__

HERE = os.path.abspath(os.path.dirname(__file__))

# README long description from README
with open(os.path.join(HERE, 'README.rst'), encoding='utf-8') as ff:
    long_description = ff.read()


setup(
    name="scipy-sphinx-theme",
    version=__version__,
    description="Scipy Sphinx theme",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    url="https://github.com/scipy/scipy-sphinx-theme",
    # Maintainer
    # Maintainer email
    # License
    py_modules = ['scipy_sphinx_theme'],
    packages=['scipy_sphinx_theme'],
    include_package_data=True,
    entry_points = {
        "sphinx.html_themes": ["scipy_sphinx_theme = scipy_sphinx_theme"],
    },
    install_requires=["sphinx"],
    # Classifiers
)
