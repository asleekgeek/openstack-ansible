#!/usr/bin/env python3

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import subprocess
import sys

import openstackdocstheme
import yaml

# -- OpenStack-Ansible configuration --------------------------------------
# Variables to override
target_name = 'openstack-ansible'
description = 'OpenStack-Ansible deploys OpenStack environments using Ansible.'
previous_series_name = '2024.2'
previous_slurp_name = '2024.1'
current_series_name = '2025.1'

# General information about the project.
author = 'OpenStack-Ansible Contributors'
category = 'Miscellaneous'
copyright = '2014-2018, OpenStack-Ansible Contributors'
title = 'OpenStack-Ansible Documentation'

# Smart variable replacements with what we can. The openstackdocstheme has
# no stable interface though. This works with 1.20.
current_series = openstackdocstheme.ext._get_series_name()

if current_series == "latest":
    latest_tag = "master"
    branch = "master"
    upgrade_warning = ("Upgrading to master is not recommended. "
                       "Master is under heavy development, and is not stable.")
else:
    series_names = current_series.capitalize()
    latest_tag = subprocess.check_output(["git", "describe", "--abbrev=0",
                                          "--tag"]).strip().decode()
    branch = "stable/{}".format(current_series)
    upgrade_warning = "The upgrade is always under active development."

CONF_PATH = os.path.dirname(os.path.realpath(__file__))
GNOCCHI_DETAILS = '../../inventory/group_vars/gnocchi_all/source_git.yml'
with open(os.path.join(CONF_PATH, GNOCCHI_DETAILS), 'r') as fdesc:
    gnocchi_file_content = yaml.safe_load(fdesc)
    gnocchi_branch = gnocchi_file_content['gnocchi_git_track_branch']

# References variable for substitutions
deploy_guide_prefix = ("https://docs.openstack.org/"
                       "project-deploy-guide/openstack-ansible/"
                       "{}/%s".format(current_series))
dev_docs_prefix = ("https://docs.openstack.org/openstack-ansible/"
                   "{}/%s".format(current_series))

if previous_slurp_name:
    slurp_epilog = f"replace:: or {previous_slurp_name.capitalize()}"
else:
    slurp_epilog = "unicode:: U+200B"

# Substitutions loader
rst_epilog = """
.. |current_release_git_branch_name| replace:: {current_release_git_branch_name}
.. |current_release_gnocchi_git_branch_name| replace:: {current_release_gnocchi_git_branch_name}
.. |previous_series_name| replace:: {previous_series_name}
.. |previous_release_formal_name| replace:: {previous_release_formal_name}
.. |current_release_formal_name| replace:: {current_release_formal_name}
.. |latest_tag| replace:: {latest_tag}
.. |upgrade_warning| replace:: {upgrade_warning}
.. |previous_slurp_name| {slurp_epilog}
""".format(  # noqa: E501
    current_release_git_branch_name=branch,
    current_release_gnocchi_git_branch_name=gnocchi_branch,
    previous_series_name=previous_series_name,
    previous_release_formal_name=previous_series_name.capitalize(),
    current_release_formal_name=current_series_name.capitalize(),
    slurp_epilog=slurp_epilog,
    latest_tag=latest_tag,
    upgrade_warning=upgrade_warning,
)

# Format: Reference name: (string containing %s for substitution, linkname)
extlinks = {'deploy_guide': (deploy_guide_prefix, ''),
            'dev_docs': (dev_docs_prefix, '')
}

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('../../inventory/'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'openstackdocstheme',
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks',
    'sphinxcontrib.rsvgconverter'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# openstackdocstheme options
openstackdocs_repo_name = 'openstack/' + target_name
openstackdocs_pdf_link = True
# The bug project is always the same for all our repos
openstackdocs_bug_project = 'openstack-ansible'
openstackdocs_bug_tag = ''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['admin/maintenance-tasks/galera.rst']

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'native'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'openstackdocs'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = target_name + '-docs'

# If true, publish source files
html_copy_source = False

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': r'''
        \let\cleardoublepage=\clearpage
    ''',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'doc-' + target_name + '.tex',
     title, author, 'manual'),
]

latex_use_xindy = False

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, target_name,
     title, [author], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, target_name,
     title, author, openstackdocs_bug_project,
     description, category),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False

# -- Options for PDF output --------------------------------------------------

pdf_documents = [
    (master_doc, target_name,
     title, author)
]

locale_dirs = ['locale/']
