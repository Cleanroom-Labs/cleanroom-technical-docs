# Configuration file for the Sphinx documentation builder.
#
# Cleanroom Labs Technical Documentation
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
import os

# Add common submodule to path
sys.path.insert(0, os.path.abspath('../common'))
from theme_config import *

# Override default paths from theme_config.py for this project's layout
html_static_path = ['../common/sphinx/_static']
templates_path = ['../common/sphinx/_templates']
html_favicon = '../common/sphinx/_static/favicon.ico'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Project information -----------------------------------------------------

project = 'Technical Documentation'
copyright = '2026, Cleanroom Labs'
author = 'Cleanroom Labs'
version = get_docs_version()
release = get_docs_version()

# -- Extensions configuration ------------------------------------------------

# Extend shared extensions with project-specific ones (if needed)
# extensions is imported from theme_config

# -- Templates path ----------------------------------------------------------

# templates_path = ['_templates']  # Use theme's templates from theme_config.py

# -- sphinx-needs configuration (project-specific types) --------------------

needs_types = make_needs_types()

# -- Sidebar configuration ---------------------------------------------------

html_sidebars = {
    '**': [
        'globaltoc.html',
        'relations.html',
        'sourcelink.html',
        'searchbox.html',
    ]
}

# -- HTML output options -----------------------------------------------------

html_title = 'Technical Documentation'
html_short_title = 'Tech Docs'

# Additional HTML context
html_context = {
    'display_github': True,
    'github_user': 'cleanroom-labs',
    'github_repo': 'airgap',
    'github_version': 'main',
    'conf_py_path': '/sphinx-docs/source/',
}
setup_project_icon(project, html_context)
setup_version_context(html_context)

# Favicon and logo (placeholders - can be added later)
# html_favicon = '_static/favicon.ico'
# html_logo = '_static/airgap-logo.png'

# HTML last updated format
html_last_updated_fmt = '%Y-%m-%d'

# HTML permalinks
html_permalinks = True
html_permalinks_icon = '¶'

# HTML search options
html_search_language = 'en'
html_search_options = {
    'type': 'default',
    'minlength': 3,
}

# Additional CSS classes for specific pages
html_additional_pages = {}

# Output file base name for HTML help builder
htmlhelp_basename = 'AirGapSuitedoc'

# -- Intersphinx mapping (for cross-project references) ---------------------

# Extend the base intersphinx_mapping from theme_config
intersphinx_mapping.update({
    'cleanroom-whisper': ('/docs/whisper/', '../whisper/build/html/objects.inv'),
    'airgap-deploy': ('/docs/deploy/', '../deploy/build/html/objects.inv'),
    'airgap-transfer': ('/docs/transfer/', '../transfer/build/html/objects.inv'),
})

# -- Sphinx-needs external needs (cross-project need links) -----------------

needs_external_needs = [
    {
        'base_url': '/docs/whisper/',
        'json_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'whisper', 'build', 'html', 'needs.json'),
    },
    {
        'base_url': '/docs/deploy/',
        'json_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'deploy', 'build', 'html', 'needs.json'),
    },
    {
        'base_url': '/docs/transfer/',
        'json_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'transfer', 'build', 'html', 'needs.json'),
    },
]

# -- LaTeX/PDF output (optional - for printable docs) -----------------------

latex_documents = [
    (master_doc, 'AirGapSuite.tex', 'AirGap Suite Documentation',
     'Cleanroom Labs', 'manual'),
]
