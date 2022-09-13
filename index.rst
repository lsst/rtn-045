:tocdepth: 1

.. sectnum::

.. Metadata such as the title, authors, and description are set in metadata.yaml

.. TODO: Delete the note below before merging new content to the main branch.

.. note::

   **This technote is a work-in-progress.**

Abstract
========

Principles, guidelines, conventions, formatting style, and workflow for tutorials developed by the Community Engagement Team (CET).

Add content here.
See the `reStructuredText Style Guide <https://developer.lsst.io/restructuredtext/style.html>`__ to learn how to create sections, links, images, tables, equations, and more.

.. Make in-text citations with: :cite:`bibkey`.
.. Uncomment to use citations
.. .. rubric:: References
.. 
.. .. bibliography:: local.bib lsstbib/books.bib lsstbib/lsst.bib lsstbib/lsst-dm.bib lsstbib/refs.bib lsstbib/refs_ads.bib
..    :style: lsst_aa

Adhere to our pedagogical principles
====================================

CET Jupyter Notebooks should be all of the following:

Inclusive. 
----------

All notebook developers should keep research inclusion in mind as our primary goal: providing equitable access to the LSST data products for a diverse community.

Level-Appropriate.
------------------
Notebooks should be clearly identify and teach to their target audience (beginner, intermediate, or advanced).

Skill-Focused.
--------------
Notebooks should be focused on teaching one or a few new skills or techniques, or providing one scientific demonstration.

Consumable.
-----------
The user should be able to work through the core contents of the notebooks within 30 minutes.  Additional examples could be included, but should be clearly labeled as such.

Well-Documented.
----------------
High quality documentation should be provided in the notebook, including narrative descriptions, citations, references, and external links to, e.g., package documentation.

Cross-Referenced.
-----------------
Intermediate and advanced notebooks should attempt to provide the names of precursory notebooks that teach any basic skills required. Beginner and intermediate notebooks should attempt to provide the names of more advanced notebooks developed in a series on the same topic.

Properly Credited.
------------------
Appropriate acknowledgements should be provided, in order to (1) give credit to individuals whose notebooks were used as examples and (2) set a precident of prioritizing credits in an openly collaborative environment.


Follow our format, style and code standards
===========================================

Template Notebook. 
------------------
Use this `template notebook <https://github.com/rubin-dp0/cet-dev/blob/main/template.ipynb>`_ in the rubin-dp0 GitHub Organization's cet-dev repository as a starting point.  The template contains an example of the header and the mandatory first section, as described below.

Header.
^^^^^^^
Logo.
"""""
In the first markdown cell, display the Rubin Observatory logo at upper left, and to the right list the contact author, date last verified, version, container size, and targeted learning level.

Second-Fifth Markdown Cells.
""""""""""""""""""""""""""""
The second, third, fourth, and fifth markdown cells should contain a very brief description, a list of core skills, a list of the LSST data products, and a list of the python packages used by the notebook.  The contents of these four cells will be used to generate a table of notebook metadata in the README.md file for the repository.

Note regarding listing package imports - List the packages being taught first (e.g., afwDisplay for a notebook about diaplaying images), and then supporting packages (e.g., lsst.daf.butler for a notebook about displaying images). OK to leave out of this list basic support packages like os, glob, numpy, matplotlib.

Sixth and Seventh Markdown Cells.
"""""""""""""""""""""""""""""""""
The sixth and seventh markdown cells should contain the credits and acknowledgements, and inforamtion about where users got to get support.  

Use of Template Notebook.
"""""""""""""""""""""""""
Use the template notebook to ensure the same format (and wording, where possible) is used for all notebooks, as this might help us to implement the metadata stetch goal.

Section Structure.
^^^^^^^^^^^^^^^^^^

Use of Numbers.
"""""""""""""""
Use numbers for sections, sub-sections, and sub-sub-sections to enable referencing, e.g., "I'm having trouble with the second code cell in Section 2.3."

Section Titles.
"""""""""""""""
Use section titles that actively describe what is being done, e.g., "2.2 Create a color-magnitude diagram" instead of "2.2 Plot", so that the auto-generated table of contents is easy to navigate.

Mandatory first section: "1. Introduction".
"""""""""""""""""""""""""""""""""""""""""""
It should provide a brief narrative about this notebook, e.g., "This notebook will teach the user...". It should also cite or link to any external information or documentation, and cross-reference to other notebooks.
- In the first section, the first sub-section should always be "1.1 Package Imports". It should have a markdown cell that provides explanations and/or links to external package documentation, as appropriate.  All package imports should be done in the first code cell.
- In the first section, the sub-section should be "1.2 Define Functions and Parameters", if applicable.  Globally defined utility functions, plotting defaults, or constants should be here.  It is OK to rename the subsection to be more specific to the notebook, and/or to use sub-sub-sections like "1.2.1 Define global cosmological parameter values" or "1.2.2 Define a function to make an image cutout". It is OK to remove this sub-section if it is not being used.

Table Data Format.
^^^^^^^^^^^^^^^^^^
Results from a TAP service search are best displayed as an astropy table using .to_table(), or as a pandas dataframe using .to_table().to_pandas().  However, do not use the .to_table().show_in_notebook() method.  This can cause issues in the RSP JupyterLab environment that make the notebook hang indefinitely.

Plotting.
^^^^^^^^^
Color Palette.
""""""""""""""
To be colorblind-friendly, plots should use the matplotlib color tables viridis or `cividis <https://matplotlib.org/stable/users/prev_whats_new/whats_new_2.2.html#cividis-colormap>`_ (or a greyscale), or the new `tableau-colorblind10 <https://viscid-hub.github.io/Viscid-docs/docs/dev/styles/tableau-colorblind10.html>`_ (see important statement below). 


