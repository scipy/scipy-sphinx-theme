needs_sphinx = '1.1'

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.pngmath', 'numpydoc',
              'sphinx.ext.intersphinx', 'sphinx.ext.coverage',
              'sphinx.ext.autosummary', 'matplotlib.sphinxext.plot_directive']

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'scipy-sphinx-theme'
copyright = u'2013, Surya Kasturi and Pauli Virtanen'
version = '0.1'
release = '0.1'
exclude_patterns = ['_build']
pygments_style = 'sphinx'


# -- Options for HTML output ---------------------------------------------------

html_theme = 'scipy'
html_theme_path = ['_theme']

pngmath_latex_preamble = r"""
\usepackage{color}
\definecolor{textgray}{RGB}{51,51,51}
\color{textgray}
"""
pngmath_use_preview = True
pngmath_dvipng_args = ['-gamma 1.5', '-D 96', '-bg Transparent']

#------------------------------------------------------------------------------
# Plot style
#------------------------------------------------------------------------------

plot_pre_code = """
import numpy as np
import scipy as sp
np.random.seed(123)
"""
plot_include_source = True
plot_formats = [('png', 100), 'pdf']
plot_html_show_formats = False

import math
phi = (math.sqrt(5) + 1)/2

plot_rcparams = {
    'font.size': 8,
    'axes.titlesize': 8,
    'axes.labelsize': 8,
    'xtick.labelsize': 8,
    'ytick.labelsize': 8,
    'legend.fontsize': 8,
    'figure.figsize': (3*phi, 3),
    'figure.subplot.bottom': 0.2,
    'figure.subplot.left': 0.2,
    'figure.subplot.right': 0.9,
    'figure.subplot.top': 0.85,
    'figure.subplot.wspace': 0.4,
    'text.usetex': False,
}
