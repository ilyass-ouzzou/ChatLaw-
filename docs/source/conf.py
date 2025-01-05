import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

project = 'Chatbot des Codes Marocains'
copyright = '2024, [Votre nom]'
author = '[Votre nom]'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'recommonmark'
]

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
source_suffix = ['.rst', '.md']