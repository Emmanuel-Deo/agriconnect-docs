# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'agriconnect-docs'
copyright = '2025, Emmanuel Kipngetich'
author = 'Emmanuel Kipngetich'
release = '28 March 2025'

# -- General configuration ---------------------------------------------------
extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # Switch to Read the Docs theme for better sidebar handling
html_static_path = ['_static']
html_css_files = ['custom.css']  # Load custom CSS for sticky sidebar
