:tocdepth: 2

.. sectnum::

.. Metadata such as the title, authors, and description are set in metadata.yaml

.. TODO: Delete the note below before merging new content to the main branch.

.. Make in-text citations with: :cite:`bibkey`.
.. Uncomment to use citations
.. .. rubric:: References
..
.. .. bibliography:: local.bib lsstbib/books.bib lsstbib/lsst.bib lsstbib/lsst-dm.bib lsstbib/refs.bib lsstbib/refs_ads.bib
..    :style: lsst_aa


.. _abstract:

Abstract
========

This document provides guidelines for anyone creating or updating the tutorials produced and maintained by the Vera C. Rubin Observatory Community Science Team (CST).
This includes all community-facing demonstrations made by CST members of how to use the Rubin Science Platform (RSP) or how to analyze Legacy Survey of Space and Time (LSST) data.
Formatting, editorial standards, workflow, and review policies are provided.

The CST uses these guidelines in the `Documentation for Data Preview 0.2 (DP0.2) <https://dp0-2.lsst.io>`_,
the `Documentation for Data Preview 0.3 (DP0.3) <https://dp0-3.lsst.io>`_,
and GitHub `tutorial-notebooks repository <https://github.com/rubin-dp0/tutorial-notebooks>`_.
Members of the Rubin Observatory staff, as well as the broad community, are encouraged to contribute to the tutorial documentation.


.. _pedagogical-principles:

Pedagogical principles
======================

All tutorials should have the following attributes.


Inclusive
---------

Follow the best practices described under :ref:`Accessibility considerations<accessibility-considerations>`.

Offensive or exclusionary language is never permitted (e.g., violent or ableist terms).
Ensure jargon and acronyms are defined, regardless of target audience.

See the `Rubin Observatory Communications Code of Conduct <https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-24920/>`_ for additional guidance.


Level-appropriate
-----------------

Tutorials should clearly identify and teach to their target audience:  beginner, intermediate, or advanced.


Skill-focused
-------------

Tutorials should focus on teaching one or a few new skills or techniques, or providing one scientific demonstration.


Consumable
----------

The user should be able to work through the core contents of a tutorial within about 30 minutes
(i.e., not including any additional suggested "Exercises for the learner").


Well-documented
---------------

High-quality documentation should be provided with the tutorial, including narrative descriptions, citations, references,
and external links to, e.g., package documentation.


Clearly-written
---------------

Tutorials should write in short, clear statements describing the actions a user should take
and the expected results.
Aside from introductory or background information, 
instructional text should be written in the `imperative mood <https://en.wikipedia.org/wiki/Imperative_mood>`_,
as is commonly adopted for technical writing.


Cross-referenced
----------------

Tutorials should reference any precursor or advanced tutorials that users should consider as prerequisites or follow-up resources.


Proper credits
--------------

Appropriate acknowledgments should be provided to credit individuals whose notebooks were used as examples,
and to set a precedent of prioritizing credits in an openly collaborative environment.
Authors should cite other scientists or papers within the text of the tutorial where appropriate.


.. _format-style-notebooks:

Jupyter notebook format, style, and code standards
==================================================


Template
--------

As a starting point, use the `template Jupyter notebook in the cet-dev repository <https://github.com/rubin-dp0/cet-dev/blob/main/template.ipynb>`_, which is part of the ``rubin-dp0`` GitHub Organization.
The template contains an example of the header and the mandatory first section described below.


Header
^^^^^^

The structure of the header is mandatory, and all of the following is already set up in the template.

In the first markdown cell, display the Rubin Observatory logo at upper left.
To the right of the logo list the contact author, date last verified, version, container size, and targeted learning level.

The second, third, fourth, and fifth markdown cells should contain a very brief description,
a list of core skills, a list of the LSST data products, and a list of the python packages used by the notebook.
List the packages being taught first (e.g., ``afwDisplay`` for a notebook about displaying images), and then supporting packages
(e.g., ``lsst.daf.butler`` for a notebook about displaying images).
It is acceptable to omit basic support packages (e.g., ``os``, ``glob``, ``numpy``, ``matplotlib``).
The contents of cells two through five are used to automatically generate a table of notebook metadata in the README.md file for the repository.

The sixth and seventh markdown cells should contain the credits and acknowledgments, and information about where users should go to get support.


First section
^^^^^^^^^^^^^

The structure of the first section is mandatory, and all of the following is already set up in the template.

Provide a brief narrative about this notebook, e.g., "This notebook will teach the user...".
Cite or link to any external information or documentation, and cross-reference to other notebooks.

The first subsection should always be ``1.1 Import packages``.
It should have a markdown cell that provides explanations and/or links to external package documentation, as appropriate.
All package imports must be done in the first code cell.

The second subsection should always be ``1.2 Define functions and parameters``.
Globally defined utility functions, classes, plotting defaults, or constants should be here.
(Single-use functions or classes can be defined immediately before they are used; see the section on functions and classes below).

If a notebook has no functions or parameters to define, it is preferred to leave this subsection header in the document
and state that no additional functions and parameters are used.

If a notebook has many such things to define, it is acceptable to rename the subsection to be more specific to the notebook,
and/or to use sub-subsections like ``1.2.1 Define global cosmological parameter values`` or ``1.2.2 Define a function to make an image cutout``.


Section structure
^^^^^^^^^^^^^^^^^

For all sections after the first, use numbers for sections, subsections, and sub-subsections to enable referencing in support requests,
e.g., "I'm having trouble with the second code cell in Section 2.3."

Use section titles that actively describe what is being done, e.g., ``2.2 Create a color-magnitude diagram`` instead of ``2.2 Plot``, so that the auto-generated table of contents is easy to navigate.

Do not use title case for section headings; use sentence case.

It is very common, but not mandatory, to end all notebook tutorials with a section called ``Exercises for the learner`` with suggestions of
how the user can make changes to the tutorial test options and examples, or guide them on the next step forward on their own.


Tables and plots
----------------


Table data format
^^^^^^^^^^^^^^^^^

Results from a Table Access Protocol (TAP) service search are best displayed as an ``astropy`` table using ``.to_table()``,
or as a pandas dataframe using ``.to_table().to_pandas()``.

Do not use the ``.to_table().show_in_notebook()`` method.
This can cause issues in the RSP JupyterLab environment that cause the notebook to hang indefinitely.


Plot format and style
^^^^^^^^^^^^^^^^^^^^^

Plots should be large enough such that the details in the data are easily discerned,
but small enough to fit within a small browser window (e.g., a laptop screen).
Typically, a statement such as ``fig = plt.figure(figsize=(6, 4))`` is sufficient (or ``(6, 6)`` for square plots).

Axes labels with units are mandatory.
A legend must be included if multiple types of data are co-plotted.
A descriptive title is encouraged but not mandatory.

In general, the default ``matplotlib`` style is sufficient and should be adopted for plot attributes
such as line thickness, tick labels, fontsize, and so on.
However, the default ``matplotlib`` color palette is not sufficient, and the recommendations
under :ref:`Accessibility considerations<accessibility-considerations>` should be adopted to create colorblind-friendly plots.

Error bars should be included wherever possible, and especially in cases where analyses such
as line fitting is being performed on the data in the plot, to help the user understand data quality.

A markdown cell underneath the figure should provide a caption that adequately explains what the main
attributes of the plot.
This caption should serve as alt-text (as described under :ref:`Accessibility considerations<accessibility-considerations>`)
and also as a way for the user to confirm the plot appears as expected.


Image orientation
^^^^^^^^^^^^^^^^^

When using a World Coordinate System (WCS), display East left, North up.
If only using pixels, ``(0,0)`` should be the lower-left, which is the default for ``awfDisplay``.

When using other plotting packages, transformations might be needed in order to match the afwDisplay default.
See the LSST Science Pipelines documentation about `Image Indexing <https://pipelines.lsst.io/modules/lsst.afw.image/indexing-conventions.html>`_.

Since use of "extent" is necessary for displaying a WCS overlay for ``deepCoadds``, use it all the time:

::

  deepCoadd = butler.get('deepCoadd', dataId=dataId)
  deepCoadd_bbox = butler.get('deepCoadd_calexp.bbox', dataId=dataId)
  deepCoadd_wcs = butler.get('deepCoadd_calexp.wcs', dataId=dataId)
  deepCoadd_WCSfMd = WCS(deepCoadd_wcs.getFitsMetadata())
  deepCoadd_extent = (deepCoadd_bbox.beginX, deepCoadd_bbox.endX, deepCoadd_bbox.beginY, deepCoadd_bbox.endY)
  plt.subplot(projection=deepCoadd_WCSfMd)
  plt.imshow(deepCoadd.image.array, cmap='gray', vmin=0, vmax=2, extent=deepCoadd_extent, origin='lower')


Functions and classes
---------------------

While globally defined functions or classes which are used more than once in a notebook should be
defined in section ``1.2 Define Functions and Parameters``, single-use functions or classes 
can be defined immediately before they are used.

Functions or classes that are particularly long blocks of code (e.g., >20 lines) can be hidden by going to
the "View" menu item and choosing "Collapse Selected Code", or by clicking on the blue bar that
appears to the left of a selected cell.
Hidden cells should be described in the preceding markdown cell with text like 
"the following hidden cell contains code that defines the ``make_cmd_plot`` function".
The first hidden cell in a notebook should include instructions for displaying the cell, such as
"to see the contents of the hidden cell, select View from the menu bar and then Expand Selected Code
or click on the vertical next to the cell or on the three dots that denote that the cell is hidden".


Clearing memory
---------------

These are optional methods for keeping memory use manageable in notebooks which may be computationally restrictive,
e.g., demonstrating data visualization techniques with big datasets.

To reduce the memory footprint of a notebook, remove figures once they're no longer needed.
See the ``remove_figure`` function defined in the DP0 notebook `03_Image_Display_and_Manipulation.ipynb in the tutorial-notebooks repository <https://github.com/rubin-dp0/tutorial-notebooks/blob/main/03a_Image_Display_and_Manipulation.ipynb>`_.

Better ways to clear the memory of, for example, large arrays that are not going to be used further on in the notebook
is in development as mentioned under :ref:`Stretch goals<stretch-goals>`.


Assert statements
-----------------

It is not mandatory nor expected for assert statements to be included in python scripts or notebooks, but tutorial developers should consider the following guidance.

Where essential, or where a very specific value is expected, the ``assert`` command can be used to demonstrate to users that a condition is true.
For example, ``assert`` statements can be used to confirm that service objects like TAP are not ``None`` or ``null`` before moving on and using that instance,
or to check that values meet expectations (e.g., total rows returned from a query).

However, take care not to use ``assert`` statements when, e.g., querying dynamic (prompt) datasets, which could return different results and cause the assert statement to fail.
Consider more pedagogical alternatives when possible (e.g., printing schema columns would also fail if the TAP service was not instantiated).


Known warnings
--------------

If a code cell produces a warning which is known and it should be ignored, the preferred method is to add a markdown cell
*before* the code cell which produces the warning, to tell the user it is acceptable to ignore.

Guidelines about the options to ignore categories of warnings are under consideration, and will be added here in the future.
Until then, use of, e.g., ``warnings.simplefilter("ignore", category=UserWarning)`` is not preferred because ignoring categories
of warnings can allow real issues to go unnoticed.


Markdown style
--------------

Any references to variables used in code cells or any code commands should be in ``monospaced font``.

Use of indented text should be limited to warnings and notices, e.g., ``> **Warning:** the following cell...``.


Code cell comments
------------------

Markdown cells are the preferred way to provide descriptive text.
Avoid using comments within a code cell as documentation.


Code cell style standard PEP8
-----------------------------

``PEP8`` is the style guide for Python code that comprises the standard library of the distribution,
and ``flake8`` is a tool to ensure compliance with these standards.

Use ``flake8`` to ensure notebook code conforms to  `PEP 8 -- Style Guide for Python Code <https://www.python.org/dev/peps/pep-0008/>`_, with a few exceptions.

Notebook tutorial developers must install the following packages locally in their home directory:

::

  pip install --user flake8-nb
  pip install --user pycodestyle_magic

It is known that the most up-to-date version of ``flake8`` has some issues.
If errors are encountered such as ``AttributeError: '_io.StringIO' object has no attribute 'buffer'``,
force-downgrade ``flake8`` from version ``4.0.1`` to ``3.9.2`` with ``pip install flake8==3.9.2``.


The flake8 config file
^^^^^^^^^^^^^^^^^^^^^^

Create a configuration file for ``flake8``.
For example, from the command line in the home directory, execute the following.
These instructions use ``emacs``, but it doesn’t matter so long as the end result is a correctly-named file with the right contents.

::

  touch .config/flake8
  emacs .config/flake8


Then copy-paste the following into the opened config file.

::

  [flake8]
  max-line-length = 99
  ignore = E133, E226, E228, E266, N802, N803, N806, N812, N813, N815, N816, W503

Use ``x-s`` then ``x-c`` to save and exit emacs.


While developing a notebook
^^^^^^^^^^^^^^^^^^^^^^^^^^^

While developing a notebook, have the following "magic" commands as the first code cell:

::

  %load_ext pycodestyle_magic
  %flake8_on
  import logging
  logging.getLogger("flake8").setLevel(logging.FATAL)

Whenever a cell is executed, it will use ``flake8`` to check for adherence to the ``PEP8`` coding style guide, 
and report violations which can be fixed immediately.
When the notebook is ready to be merged, the cell with the magic commands must be removed.


When the notebook is complete
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When the notebook is complete, execute the following from the command line in the notebook's directory:

::

  flake8-nb notebook_name.ipynb

This will do a final check of any violations with ``PEP8``.
This will catch things that can be missed line-by-line, such as packages that are imported but never used.


.. _git-policy-notebooks:

Git branch, merge, and review policy for the tutorial-notebooks repository
==========================================================================

The following applies when creating or updating notebooks in the 
`tutorial-notebooks repository <https://github.com/rubin-dp0/tutorial-notebooks>`_,
which is part of the ``rubin-dp0`` GitHub Organization.
The ``main`` branch is where changes are collected before pushing ``prod`` branch.
The ``prod`` branch is the version available in the RSP.


Branch
------

Develop new notebooks, or update existing ones, in a new branch.
This branch should be named for the corresponding Jira ticket (e.g., "tickets/PREOPS-12345").
The new branch should be created from ``main``, *not* from ``prod``.

Only update one notebook per ticket branch, unless the ticket is to make similar updates to all notebooks
(e.g., when bumping the RSP's recommended image).

Update the repository's ``README.md`` file in the branch when appropriate.


Commit and push
---------------

Always restart the Jupyter Notebook kernel and clear all outputs before saving, committing, and pushing changes to the branch.


Pull request
------------

When the notebook is complete open a pull request (PR) to merge the ticket branch into the ``main`` branch (again, *not* to ``prod``).


Review
------

Contact one or more Rubin Observatory staff members with the appropriate expertise and ask them to review the tutorial.
Reviewers do not need to be members of the CST.
If they agree, assign them as a reviewer on the pull request.
If there is uncertainty about whom to assign as a reviewer, ask the Lead Community Scientist to help identify someone.

If the reviewer requests changes, ensure that all of the reviewers' comments are addressed.
Make changes and new commits to the branch, and respond to all of their comments with either a confirmation a change was made,
or an explanation of why the request was not implemented.
Contact the reviewers to let them know the pull request now awaits their approval.


Merge
-----

After the reviewers have approved the pull request, ``rebase and merge`` the ticket branch into the ``main`` branch (again, *not* to ``prod``).
Resolve all conflicts, if there are any.
After the successful merge, delete the ticket branch.


Release to prod branch
----------------------

To "release" the new version of ``main`` to ``prod`` branch (i.e., to update all RSP users' tutorial notebooks),
delete the current ``prod-prior-to-rebranch`` branch, rename ``prod`` as ``prod-prior-to-rebranch``, then create a new ``prod`` branch from ``main``.
Doing this way avoids weird history-based git issues that cause conflicts in ``main`` to ``prod`` merges.
There is no need to track the history between ``main`` and ``prod``.

The number of pushes to the ``prod`` branch should be minimized.
For example, if there are a few tickets being completed within a week, coordinate with other notebook developers to collect all changes in
the ``main`` branch, and then do a single "release" to ``prod``.


Jira tickets
------------

Remember to make comments in the associated Jira tickets about the major updates as work progresses.

After the PR is merged, request a review on the ticket (usually from the CST team lead).
After the ticket has been reviewed, the ticket status can be set as done.


Updates to the RSP's recommended version
----------------------------------------

Decisions on whether to update (or, "bump") the recommended image for the RSP are made jointly between the CST and the RSP teams.
Once the decision has been made, a PREOPS Jira ticket will be created and assigned to a CST member.

Bumping the recommended image always occurs during the regularly scheduled maintenance periods, "Patch Thursday."
The notebook updates should be merged to the ``main`` branch by the day before.

The workflow is to create a new branch of the ``tutorial-notebooks`` repository from the ``main`` branch,
test all of the notebooks with the new version, and make updates as needed.

Do not suppress warnings while testing.
It is not necessary to use the ``flake8`` "magic" commands while testing, unless significant changes to the code are required.

At minimum, the header will have to be updated with a new date and verified version.
Ensure that all notebooks are cleared before committing new versions.

When the updates are complete, use a new pull request to merge the branch into ``main``.
A review is not typically needed at this stage.

Create a version tag using the new ``main`` branch of the ``tutorial_notebooks`` repo. 
For example, for the update to ``Weekly 2023_27``, it would be ``git tag -a w.2023.27 -m "Weekly 2023_37"``
followed by ``git push --tags``.

During the Patch Thursday window, after the recommended image has been bumped, release to ``prod`` following the instructions of `Release to prod branch`_.

Remember to make comments in the associated Jira tickets about the major updates and mark the ticket as done.


Major updates log
-----------------

All new tutorials or significant changes should be documented for users in the logs of
major tutorial updates for `DP0.2 <https://dp0-2.lsst.io/tutorials-examples/major-updates-log.html>`_
and `DP0.3 <https://dp0-3.lsst.io/tutorials-examples/major-updates-log.html>`_.


.. _format-style-portal:

Portal tutorial format and style
================================

The portal tutorials are written in reStructuredText (RST) format and are kept within the data release documentation at
`DP0.2 Tutorials <https://dp0-2.lsst.io/tutorials-examples/index.html#portal-tutorials>`_ and
`DP0.3 Tutorials <https://dp0-3.lsst.io/tutorials-examples/index.html#portal-tutorials>`_.

All portal tutorials should have a descriptive title, list the contact authors, 
the date last verified to run, and the targeted learning level.
A brief narrative introduction to the tutorial should be provided at the top of the page.

The rest of the portal tutorial should be divided into sequentially numbered steps and substeps.

It is very common, but not mandatory, to end all portal tutorials with a section called 
``Exercises for the learner`` with suggestions of
how the user can make changes to the tutorial test options and examples, or guide them on the next step forward on their own.


Code blocks
-----------

Ensure that any Astronomical Data Query Language (ADQL) is put into code boxes in RST so that users may copy-paste whenever possible.
In RST, this is done as in the following example.

::

     .. code-block:: SQL

       SELECT e, q, incl 
       FROM dp03_catalogs_10yr.MPCORB 
       WHERE ssObjectId > 9000000000000000000


Figures
-------

Use descriptive text and screenshots to demonstrate the steps of the tutorial, to show the user what to do,
and to show the expected results for comparison.

Augment screenshots with indicators (e.g., arrows or circles) to guide the users attention as needed.

Include a caption that describes the figure (see example below, with alt-text and a caption).

For plots made in the Portal results view, the recommendations
under :ref:`Accessibility considerations<accessibility-considerations>` should be adopted to create colorblind-friendly plots.


Alternate-Text (alt-text)
^^^^^^^^^^^^^^^^^^^^^^^^^

All figures in Portal tutorials should have an alt-text statement.
The motivation and guidance for writing alt-text is provided under :ref:`Accessibility considerations<accessibility-considerations>`.

To add alt-text to an image in the reStructured text environment, use the ``:alt:`` command.
In RST, this is done as in the following example.

::

     .. figure:: /_static/figure_filename.png
       :name: name_of_figure
       :alt: Descriptive text of image (use tab to indent second line of text)

       The caption goes here, indented the same way, but with an empty line between code and caption text.


.. _git-policy-portal:

Git branch, merge, and review policy for portal tutorials
=========================================================

The following applies when creating or updating tutorials in the `dp0-2_lsst_io repository <https://github.com/lsst/dp0-2_lsst_io>`_, which is part of the ``lsst`` GitHub Organization.

Develop new tutorials, or update existing ones, in a new branch.
This branch should be named for the corresponding Jira ticket (e.g., "tickets/PREOPS-12345").
The new branch should be created from ``main``.
Typically, only one tutorial is updated per ticket branch.

Make commits and push changes to the branch in the ``dp0-2_lsst_io`` (or ``dp0-3_lsst_io``) repository until work is complete, then open a pull request to ``main``.

Contact one or more Rubin Observatory staff members with the appropriate expertise and ask them to review the tutorial.
At least one reviewer should be a member of the CST.
If they agree, assign them as a reviewer on the pull request.

If the reviewer requests changes, ensure that all of the reviewers' comments are addressed.
Make changes and new commits to the branch, and respond to all of their comments with either a confirmation a change was made,
or an explanation of why the request was not implemented.
Contact the reviewers to let them know the pull request now awaits their approval.

After the reviewers have approved the pull request, ``rebase and merge`` the ticket branch into the ``main`` branch.
Do not click the "Update branch" button as that does a merge from main.
Resolve all conflicts, if there are any.
After the successful merge, delete the ticket branch.

Remember to make comments in the associated Jira tickets about the major updates as work progresses.

After the PR is merged, request a review on the ticket (usually from the CST team lead).
After the ticket has been reviewed, the ticket status can be set as done.

All new tutorials or significant changes should be documented for users in the logs of
major tutorial updates for `DP0.2 <https://dp0-2.lsst.io/tutorials-examples/major-updates-log.html>`_
and `DP0.3 <https://dp0-3.lsst.io/tutorials-examples/major-updates-log.html>`_.


.. _accessibility-considerations:

Accessibility considerations
============================

The following set of best practices to be implemented for Rubin tutorials is a work in progress.
Individual components have been incorporated into the sections above, but are collected here for reference.


Vision-impaired astronomers
---------------------------


Colorblind-friendly plots
^^^^^^^^^^^^^^^^^^^^^^^^^

The most common form of colorblindness is being unable to differentiate red and green.
Guidelines for colorblind-friendly plots includes the following.

* Do not use red and green together.
* Use color combinations that are high contrast.
* Do not use color alone, but with different symbol and line styles.

In Jupyter Notebooks, in order to be accessible to those with Color Vision Deficiency (CVD or colorblind), 
plots color tables with ``matplotlib`` should be either a greyscale,
a `preceptually uniform sequential colormap <https://matplotlib.org/stable/users/explain/colors/colormaps.html#sequential>`_
like viridis or cividis, or 
`tableau-colorblind10 <https://viscid-hub.github.io/Viscid-docs/docs/dev/styles/tableau-colorblind10.html>`_.

The ``tableau-colorblind10`` color table can be loaded with the following python code.

::

  import matplotlib.pyplot as plt
  plt.style.use('tableau-colorblind10')


For the LSST filter set ``ugrizy``, adopt the same colors as Dark Energy Survey (DES), 
which were chosen to be colorblind-friendly.
The following python code can be used to create a dictionary that assigns colors by filter name.

::

  plot_filter_colors = {'u': '#56b4e9', 'g': '#008060', 'r': '#ff4000', 'i': '#850000', 'z': '#6600cc', 'y': '#000000'}


Alternative-Text (alt-text)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Alt-text is added to figures, images, and graphics in the documentation and documentation-based tutorials
(but not notebooks, where figures are typically dynamically generated) to ensure that visually impaired 
individuals, who use screen readers, are given sufficient information to understand what is displayed. 

In general, alt-text descriptions can be written as either a literal description of the figure or image, 
or a more creative description.
In CST tutorials, most figures display screen shots of the RSP portal interface and should 
describe the information in a practical way versus a creative way.

Guidelines for writing alt-text:

* Be brief, if possible. Write in short, succinct sentences.
* Spell out acronyms (e.g. Right Ascension versus RA).
* Avoid jargon or undefined terms.
* Symbols and equations should be expressed in words (e.g. use "equals" rather than "=").
* Write for the text to be read aloud. Written visual cues (e.g. quotation marks or dashes) are not necessary.
* Pictures should be described in terms of what the listener needs to know (e.g., a large galaxy in the center).
* For RSP screenshots, state which interface is being shown and describe the actions the user should take and the expected results, or the main functionality of the interface (as appropriate).
* Where possible, use consistent terms such as the `JupyterLab User Interface Naming Conventions <https://jupyterlab.readthedocs.io/en/stable/developer/contributing.html#user-interface-naming-conventions>`_.
* Limit the use of visual cues, such as colors or shapes, or visual-centric language (e.g., "as you can see").
* If color is a useful attribute to distinguish items in a figure, then describe the attribute rather than the color (e.g. a blue star versus a red star could be described as a hotter star and a cooler star).
* For plots, include type of plot (e.g., bar, scatter), titles and labels, and a general explanation of the data and what it means.


Converted notebooks
^^^^^^^^^^^^^^^^^^^

For offline viewing, create ``html`` versions of executed notebooks and not ``pdf`` versions, as
the latter are typically less compatible with screen readers.

At this time it is not necessary to use, e.g., `nbconvert <https://nbconvert.readthedocs.io/en/latest/>`_,
but a customized application might be considered in the future (and is included under :ref:`Stretch goals<stretch-goals>`).


Neurodivergent astronomers
--------------------------

Use fonts that work well for people with dyslexia, such as sans serif, monospaced, and roman font types such as 
Helvetica, Courier, Arial, Verdana and CMU (Computer Modern Unicode), OpenDyslexic. 

*Italic fonts* decrease readability and should be used sparingly. 

Avoid text crowding and long paragraphs.
Use short sentences and, where possible, arrange text in shorter paragraphs.


Resources
---------

A few useful resources for accessibility include:

 * The document on `Improving Accessibility of Astronomical Publications <https://aas.org/sites/default/files/2019-09/Recommendations_WGAD_2016.pdf>`_ by the `AAS Working Group on Accessibility and and Disability <https://aas.org/comms/wgad>`_.
 * The `Web Content Accessibility Guidelines (WCAG) <https://www.w3.org/WAI/standards-guidelines/wcag/>`_.
 * The `Notebooks for All <https://iota-school.github.io/notebooks-for-all/>`_ initiative by STScI.


.. _stretch-goals:

Stretch goals
=============

Work is on-going in these areas, and in time they will become part of the guidelines above.


Notebook metadata
-----------------

Embed notebook metadata (e.g., version, skills, packages) in a way that can be scraped and used to auto-generate the ``README.md`` file or a Table of Contents, to enable users to browse notebook contents.


Accessibility
-------------

Continue to improve tutorials' accessibility to people with disabilities by finding and implementing, 
e.g., screen reader compatibility software, data sonification packages, 
customized use of `nbconvert <https://nbconvert.readthedocs.io/en/latest/>`_, 
additional policies for supporting neurodivergent users,
and other jupyter notebook accessibility techniques.


Translations
------------

At minimum, translate any undergraduate-level tutorials into Spanish.

Additionally, improve tutorials' accessibility to non-English speakers by finding and implementing automatic translation and localization software.


Purge extraneous items in notebooks
-----------------------------------

Develop a best practice for how to keep notebook memory usage in check, in addition to deleting figures.
E.g., whether or not the ``del`` command is sufficient for this.


Recipe functions
----------------

Create recipes for common user activities.
These could be, e.g., ADQL searches for the portal, code snippets for the command line, or python modules that can be imported.

When these are used in the advanced notebooks, also demonstrate use of the ``inspect.getsource`` functionality for users to display function code.
