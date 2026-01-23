"""
Shared Sphinx theme configuration for all AirGap project documentation.

This module provides common theme settings that are imported by individual
project conf.py files to ensure consistent branding and styling.
"""

# Theme settings
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'style_nav_header_background': '#2980B9',
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# Shared extensions - projects can extend this list
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx_needs',
    'myst_parser',
]

# Common intersphinx mapping (can be extended by projects)
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# Shared static files path
html_static_path = ['_static']

# Custom CSS
html_css_files = [
    'custom.css',
]

# Default language
language = 'en'

# Exclude patterns
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv']

# Source suffix
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Master document
master_doc = 'index'

# HTML output options
html_show_sourcelink = False
html_show_sphinx = False
html_show_copyright = True
