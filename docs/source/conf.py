# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'fwheel'
copyright = '2024, Opensource'
author = 'Ashish'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_click',
    # 'notfound.extension',
    # 'sphinx_docsearch',
    'sphinx_copybutton',
]

# docsearch_app_id = "UM5HRVXATR"
# docsearch_api_key = "21a390a684536b73f0aee9a20c708c4b"
# docsearch_index_name = "hckr"

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'shibuya'
html_static_path = ['_static']
# favicons
html_favicon = '_static/favicon.ico'

# TODO: enhance it https://shibuya.lepture.com/install/
html_theme_options = {
    "color_mode": "light",  # light or dark
    "github_url": "https://github.com/pateash/fwheel",
    "discussion_url": "https://github.com/pateash/fwheel/discussions",
    "globaltoc_expand_depth": 1,
    "nav_links": [
        {
            "title": "pypi",
            "url": "https://pypi.org/project/fwheel/",
            "external": "true"
        },
        # {
        #     "title": "Join our Slack",
        #     "url": "https://join.slack.com/t/hckr-cli/shared_invite/zt-2kpwz39dw-CIVDcv1nGhEnQNLumJxJDQ",
        #     "external": "true"
        # },
    ],
    # "light_logo": "_static/hckr-logo-black.png",
    # "dark_logo": "_static/hckr-logo-white.png",
    "accent_color": "bronze",
    "announcement": """<div style="text-align: center;">
        <div style="display: inline-block;">
         Please support the project by starring it on <a href='https://github.com/pateash/fwheel/' target="_blank">Github</a>
        </div>
    </div>""",
}

html_context = {
    "source_type": "github",
    "source_user": "pateash",
    "source_repo": "fwheel",
    "source_version": "main",  # Optional
    "source_docs_path": "/docs/source/",  # Optional
}
