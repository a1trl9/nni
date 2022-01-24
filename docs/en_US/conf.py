# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import subprocess
import sys
sys.path.insert(0, os.path.abspath('../..'))


# -- Project information ---------------------------------------------------

project = 'NNI'
copyright = '2021, Microsoft'
author = 'Microsoft'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = 'v2.6'

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinxarg.ext',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'nbsphinx',
    'sphinx.ext.extlinks',
    'IPython.sphinxext.ipython_console_highlighting',
]

# Add mock modules
autodoc_mock_imports = ['apex', 'nni_node', 'tensorrt', 'pycuda', 'nn_meter']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ['.rst']

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'Release_v1.0.md', '**.ipynb_checkpoints']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

# -- Options for HTML output -------------------------------------------------

# HTML logo
html_logo = '../img/nni_icon.svg'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_material'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {

    # Set the name of the project to appear in the navigation.
    'nav_title': 'Neural Network Intelligence',

    # Set you GA account ID to enable tracking
    'google_analytics_account': 'UA-136029994-1',

    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    'base_url': 'https://nni.readthedocs.io/',

    # Set the color and the accent color
    # We can't have our customized themes currently
    # Remember to update static/css/material_custom.css when this is updated.
    'color_primary': 'indigo',
    'color_accent': 'pink',

    # Set the repo location to get a badge with stats
    'repo_url': 'https://github.com/microsoft/nni/',
    'repo_name': 'nni',

    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 3,

    'version_dropdown': True,
    'version_json': '../static/versions.json'
}

# Customizing html context, so that some keys inserted by readthedocs
# gets populated into other keys in the format of sphinx-material
class html_context_dict(dict):
    def update(self, *args, **kwargs):
        assert (len(args) == 1 and isinstance(args[0], dict)) or not args
        if len(args) == 1:
            return self.update(**args[0])

        # rename versions as theme_version_info
        if 'versions' in kwargs:
            kwargs['theme_version_info'] = dict(kwargs['version'])

        # support other logics here if needed
        return super().update(**kwargs)

# Declare html_context here, so that readthedocs can find it in the globals()
html_context = html_context_dict()

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

html_title = 'Neural Network Intelligence'

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'NeuralNetworkIntelligencedoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'NeuralNetworkIntelligence.tex', 'Neural Network Intelligence Documentation',
     'Microsoft', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'neuralnetworkintelligence', 'Neural Network Intelligence Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'NeuralNetworkIntelligence', 'Neural Network Intelligence Documentation',
     author, 'NeuralNetworkIntelligence', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# external links (for github code)
# Reference the code via :githublink:`path/to/your/example/code.py`
git_commit_id = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode().strip()

extlinks = {
    'githublink': ('https://github.com/microsoft/nni/blob/' + git_commit_id + '/%s', 'Github link: ')
}

# -- Extension configuration -------------------------------------------------
def setup(app):
    app.add_css_file('css/material_custom.css')
    app.add_css_file('css/index_page.css')
