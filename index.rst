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


