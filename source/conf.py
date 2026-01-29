# Configuration file for the Sphinx documentation builder.
#
# Cleanroom Labs Technical Documentation
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
import os

# Add cleanroom-theme submodule to path (local to this repo)
sys.path.insert(0, os.path.abspath('cleanroom-theme'))
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
    'cleanroom-whisper': ('/docs/cleanroom-whisper/', '../cleanroom-whisper-docs/build/html/objects.inv'),
    'airgap-deploy': ('/docs/airgap-deploy/', '../airgap-deploy-docs/build/html/objects.inv'),
    'airgap-transfer': ('/docs/airgap-transfer/', '../airgap-transfer-docs/build/html/objects.inv'),
})

# -- Sphinx-needs external needs (cross-project need links) -----------------

needs_external_needs = [
    {
        'base_url': '/docs/cleanroom-whisper/',
        'json_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'cleanroom-whisper-docs', 'build', 'html', 'needs.json'),
    },
    {
        'base_url': '/docs/airgap-deploy/',
        'json_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'airgap-deploy-docs', 'build', 'html', 'needs.json'),
    },
    {
        'base_url': '/docs/airgap-transfer/',
        'json_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'airgap-transfer-docs', 'build', 'html', 'needs.json'),
    },
]

# -- LaTeX/PDF output (optional - for printable docs) -----------------------

latex_documents = [
    (master_doc, 'AirGapSuite.tex', 'AirGap Suite Documentation',
     'Cleanroom Labs', 'manual'),
]
