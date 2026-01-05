# Configuration file for the Sphinx documentation builder.
#
# AirGap Project Suite Documentation
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = 'AirGap Project Suite'
copyright = '2026, Cleanroom Labs'
author = 'Cleanroom Labs'
version = '1.0.0'
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',        # For future Python code docs
    'sphinx.ext.intersphinx',    # Cross-project references
    'sphinx.ext.todo',           # TODO directives
    'sphinx.ext.viewcode',       # Source code links
    'sphinx.ext.graphviz',       # Diagrams from dot files
    'sphinx_needs',              # CRITICAL - Traceability
    # 'sphinxcontrib.rust',      # FUTURE - Rust API docs (commented out - import issue)
    'myst_parser',               # Optional: Keep some markdown support
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
language = 'en'

# -- sphinx-needs configuration (CRITICAL for traceability) ------------------

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

# Needs extra options for links
needs_extra_links = [
    {
        'option': 'tests',
        'incoming': 'is tested by',
        'outgoing': 'tests',
        'copy': False,
        'color': '#84B39D'
    },
    {
        'option': 'implements',
        'incoming': 'is implemented by',
        'outgoing': 'implements',
        'copy': False,
        'color': '#00A8B5'
    },
    {
        'option': 'satisfies',
        'incoming': 'is satisfied by',
        'outgoing': 'satisfies',
        'copy': False,
        'color': '#FEDCD2'
    },
    {
        'option': 'derives',
        'incoming': 'is derived from',
        'outgoing': 'derives from',
        'copy': False,
        'color': '#BFD8D2'
    }
]

# Enable needs filtering and flow diagrams
needs_build_needflow = True
needs_flow_show_links = True
needs_flow_link_types = ['links', 'tests', 'implements', 'satisfies']

# Use Graphviz instead of PlantUML for diagrams (PlantUML requires Java)
needs_flow_engine = 'graphviz'

# Allow hyphens in need IDs (default only allows underscores)
needs_id_regex = '^[A-Z0-9_-]{3,}'

# Add custom options for needs
needs_extra_options = ['priority']

# -- sphinxcontrib-rust configuration ----------------------------------------

# Placeholder for future Rust API documentation
# Will be populated when Rust code is implemented

# -- Theme configuration -----------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False,
    'logo_only': False,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
}

# Sidebar configuration for multi-project navigation
html_sidebars = {
    '**': [
        'globaltoc.html',
        'relations.html',
        'sourcelink.html',
        'searchbox.html',
    ]
}

# -- Static files and CSS ----------------------------------------------------

html_static_path = ['_static']
html_css_files = ['custom.css']

# -- Source file configuration -----------------------------------------------

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',  # Optional: phase out during conversion
}

master_doc = 'index'

# -- HTML output options -----------------------------------------------------

html_title = 'AirGap Suite Documentation'
html_short_title = 'AirGap Docs'
html_show_sourcelink = True
html_show_sphinx = False
html_show_copyright = True

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

# If true, links to the source are added to the sidebar
html_show_sourcelink = True

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

# -- Intersphinx mapping (for future code docs) -----------------------------

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

# -- LaTeX/PDF output (optional - for printable docs) -----------------------

latex_documents = [
    (master_doc, 'AirGapSuite.tex', 'AirGap Suite Documentation',
     'Cleanroom Labs', 'manual'),
]
