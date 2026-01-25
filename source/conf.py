# Configuration file for the Sphinx documentation builder.
#
# Cleanroom Labs Technical Documentation
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
import os

# Add cleanroom-design-system submodule to path (local to this repo)
sys.path.insert(0, os.path.abspath('cleanroom-design-system'))
from theme_config import *

# -- Project information -----------------------------------------------------

project = 'Technical Documentation'
copyright = '2026, Cleanroom Labs'
author = 'Cleanroom Labs'
version = '1.0.0'
release = '1.0.0'

# -- Extensions configuration ------------------------------------------------

# Extend shared extensions with project-specific ones (if needed)
# extensions is imported from theme_config

# -- Templates path ----------------------------------------------------------

templates_path = ['_templates']

# -- sphinx-needs configuration (project-specific types) --------------------

needs_types = [
    {
        'directive': 'usecase',
        'title': 'Use Case',
        'prefix': 'UC-',
        'color': '#BFD8D2',
        'style': 'node'
    },
    {
        'directive': 'req',
        'title': 'Requirement',
        'prefix': 'FR-',
        'color': '#FEDCD2',
        'style': 'node'
    },
    {
        'directive': 'nfreq',
        'title': 'Non-Functional Requirement',
        'prefix': 'NFR-',
        'color': '#DF744A',
        'style': 'node'
    },
    {
        'directive': 'spec',
        'title': 'Design Specification',
        'prefix': 'DS-',
        'color': '#DCB239',
        'style': 'node'
    },
    {
        'directive': 'test',
        'title': 'Test Case',
        'prefix': 'TC-',
        'color': '#84B39D',
        'style': 'node'
    },
    {
        'directive': 'impl',
        'title': 'Implementation',
        'prefix': 'IMPL-',
        'color': '#00A8B5',
        'style': 'node'
    }
]

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
    'cleanroom-whisper': ('../cleanroom-whisper-docs/build/html/', None),
    'airgap-deploy': ('../airgap-deploy-docs/build/html/', None),
    'airgap-transfer': ('../airgap-transfer-docs/build/html/', None),
})

# -- LaTeX/PDF output (optional - for printable docs) -----------------------

latex_documents = [
    (master_doc, 'AirGapSuite.tex', 'AirGap Suite Documentation',
     'Cleanroom Labs', 'manual'),
]
