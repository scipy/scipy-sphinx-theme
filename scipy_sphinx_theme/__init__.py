from os import path

__version__ = "0.0.1-dev"

def get_html_theme_path():
    return path.abspath(path.dirname(path.dirname(__file__)))

def setup(app):
    app.add_html_theme('scipy_sphinx_theme', path.abspath(path.dirname(__file__)))
