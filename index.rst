#############################
Guidelines for User Tutorials
#############################

.. abstract::

   Guidelines for anyone creating or updating user-facing tutorials for the Rubin Observatory, such
   as demonstrations of how to use the Rubin Science Platform (RSP) or how to analyze Legacy Survey 
   of Space and Time (LSST) data.
   Principles, conventions, templates, formats, and styles for code and text are provided.
   All Rubin staff and the broader science community should use these guidelines if contributing to
   the set of user-facing tutorials maintained by the Rubin Community Science team (CST).


.. Metadata such as the title, authors, and description are set in metadata.yaml

.. TODO: Delete the note below before merging new content to the main branch.

.. Make in-text citations with: :cite:`bibkey`.
.. Uncomment to use citations
.. .. rubric:: References
..
.. .. bibliography:: local.bib lsstbib/books.bib lsstbib/lsst.bib lsstbib/lsst-dm.bib lsstbib/refs.bib lsstbib/refs_ads.bib
..    :style: lsst_aa


.. _pedagogical-principles:

Principles
==========

All tutorials should be guided by the following principles,
and adhere to the `Rubin Developers Guide <https://developer.lsst.io/>`__.

**Inclusive:**
Follow the best practices described under :ref:`Accessibility considerations<accessibility-considerations>`.
Offensive or exclusionary language is never permitted (e.g., violent or ableist terms).
Ensure jargon and acronyms are defined, regardless of target audience.
See the `Rubin Observatory Communications Code of Conduct <https://docushare.lsstcorp.org/docushare/dsweb/Get/Document-24920/>`_ for additional guidance.

**Level-appropriate:**
Identify and teach to a target audience (e.g., beginner, intermediate, or advanced).

**Skill-focused:**
Teach one to a few skills, techniques, or RSP functionality, and/or
provide a demonstration of a scientific analysis with LSST data.

**Consumable:**
The tutorial should take about 30 minutes to complete
(not including any provided "Exercises for the learner").

**Well-referenced:**
Include citations, references, and external links (e.g., code package documentation).
Reference any precursor (or advanced) tutorials that users can consider as prerequisite (or as follow-up).

**Properly-credited:**
Appropriate acknowledgments should be provided to credit individuals whose work was used.
This sets a precedent of prioritizing credits in an openly collaborative environment.
Cite other scientists or papers within the text of the tutorial where appropriate.

**Clearly-written:**
Follow the best practices described under :ref:`Narrative text<narrative-text>`.
Write short, clear, instructional statements in the `imperative mood <https://en.wikipedia.org/wiki/Imperative_mood>`_.


.. _how-to-contribute:

How to contribute
=================

Anyone is welcome to create a tutorial and then work with the Rubin Community Science team (CST)
to have it ingested and made available alongside the rest of the tutorials.
CST members will help with the review process and GitHub workflows.
Contact any co-author of this document to get started.


.. _format-style-notebooks:

Jupyter Notebooks
=================

Template
--------

Use the `template <https://github.com/rubin-dp0/cst-dev/blob/main/template.ipynb>`_
Jupyter notebook in the ``cst-dev`` GitHub repository, which is part of the ``rubin-dp0`` GitHub Organization.
The template contains an example of the header and the mandatory first section, which are described
in `Section structure`_.


Use of PEP8 and flake8
----------------------

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


**Create the flake8 config file:**
These instructions use ``emacs``, but it doesn’t matter so long as the end result is a
correctly-named file with the right contents.
Start in the home directory and execute the following.

::

  touch .config/flake8
  emacs .config/flake8


Then copy-paste the following into the opened config file.

::

  [flake8]
  max-line-length = 99
  ignore = E133, E226, E228, E266, N802, N803, N806, N812, N813, N815, N816, W503

Use ``x-s`` then ``x-c`` to save and exit emacs.


**While developing a notebook** have the following "magic" commands as the first code cell:

::

  %load_ext pycodestyle_magic
  %flake8_on
  import logging
  logging.getLogger("flake8").setLevel(logging.FATAL)

Whenever a cell is executed, it will use ``flake8`` to check for adherence to the ``PEP8`` coding style guide, 
and report violations which can be fixed immediately.
When the notebook is ready to be merged, the cell with the magic commands must be removed.

**When the notebook is complete** execute the following from the command line in the notebook's directory:

::

  flake8-nb notebook_name.ipynb

This will do a final check of any violations with ``PEP8``.
This will catch things that can be missed line-by-line, such as packages that are imported but never used.


Markdown cells
--------------

**Monospace font:**
Any references to variables used in code cells or any code commands should be in ``monospaced font``.

**Warnings:**
Use of indented text should be limited to warnings, e.g., 
``> **Warning:** the following cell produces a warning which is ok to ignore because...``.


Section structure
^^^^^^^^^^^^^^^^^

**First markdown cell:**
Set the title using heading level 1 (single ``#``).
Display the Rubin Observatory logo at upper left.
To the right of the logo list the contact author, date last verified, LSST Science Pipelines version,
container size, and targeted learning level, in that order.

**Second to seventh markdown cells:**
A very brief description, a list of core skills, a list of the LSST data products,
a list of the python packages used by the notebook, the credits and acknowledgements,
and information about where users should go to get support, in that order.
It is ok to limit the lists to include only the main data products and packages that the tutorial
is focused on teaching.
It is ok to omit basic support packages (e.g., ``os``, ``glob``, ``numpy``, ``matplotlib``).
The contents of cells two through five are used to generate the table of notebook metadata in the
README.md file for the repository.
It is a stretch goal to be able to auto-generate the table by scraping these notebook metadata.

**The first section** should be named "Introduction" using heading level 2: ``## 1. Introduction``.
Provide a brief narrative about this notebook, e.g., "This notebook will teach the user...".
Cite or link to any external information or documentation, and cross-reference to other notebooks.

The first subsection should always be ``### 1.1. Import packages``.
It should have a markdown cell that provides explanations and/or links to external package documentation, as appropriate.
All package imports must be done in the first code cell.

The second subsection should always be ``### 1.2. Define functions and parameters``.
Globally defined utility functions, classes, plotting defaults, or constants should be here.
Instantiations of the TAP or butler services should also be done here.

Single-use functions or classes can be defined immediately before they are used, for pedagogical purposes;
see the guidelines for functions and classes in the `Code cells`_ section below.
It is ok to have sub-subsections, such as ``#### 1.2.1. Define global cosmological parameter values``
or ``#### 1.2.2. Define a function to make an image cutout``.

**Additional sections** must be numbered to enable referencing in support requests,
e.g., "I'm having trouble with the second code cell in Section 2.3."
Use descriptive section titles, e.g., ``2.2 Create a color-magnitude diagram`` instead of ``2.2 Plot``,
so that the auto-generated table of contents is more useful.
Do not use title case for section headings; use sentence case.
(This Is Title Case. This is sentence case.)

**Exercises for the learner:**
It is very common, but not mandatory, to end all notebook tutorials with a section called
``Exercises for the learner`` with suggestions of how the user can make changes to the
tutorial test options and examples, or guide them on the next step forward on their own.


Code cells
----------

All python code in Jupyter Notebooks should adhere to the
`Code Style Guidelines <https://developer.lsst.io/coding/intro.html>`_
in the `Rubin Developer's Guide <https://developer.lsst.io/>`_.
Follow the guidelines above for the `Use of PEP8 and flake8`_.

**Comments:**
Avoid using comments within a code cell as documentation (i.e., with ``#``).
Markdown cells are the preferred way to provide descriptive text.


Functions and classes
^^^^^^^^^^^^^^^^^^^^^

Functions and classes should be named following the
`Naming Conventions <https://developer.lsst.io/python/style.html#naming-conventions>`_
defined in the `Rubin Developer's Guide <https://developer.lsst.io/>`_.

Globally defined functions or classes which are used more than once in a notebook should be
defined in Section 1.2, but single-use functions or classes can be defined immediately before they are used.

**Hiding long functions.**
Functions or classes that are particularly long blocks of code (e.g., >20 lines) can be hidden by going to
the "View" menu item and choosing "Collapse Selected Code", or by clicking on the blue bar that
appears to the left of a selected cell.
Hidden cells should be described in the preceding markdown cell with text like 
"the following hidden cell contains code that defines the ``make_cmd_plot`` function".
The first hidden cell in a notebook should include instructions for displaying the cell, such as
"to see the contents of the hidden cell, select View from the menu bar and then Expand Selected Code
or click on the vertical next to the cell or on the three dots that denote that the cell is hidden".

It is a stretch goal to create a package of commonly-used functions in order
to avoid users encountering long blocks of code, and help keep notebooks readable.


TAP queries
^^^^^^^^^^^

TAP queries should always be run as asynchronous as this is the best practice and a good habit for users.

As the execution of TAP queries can be time-variable, the notebook's narrative text should not include
any estimates for how long the query should take, to avoid confusing or concerning the user.
The ``html`` files of executed versions of the notebooks (see `Converted notebooks`_) will show the 
execution time, should the user require an estimate.


Clearing memory
^^^^^^^^^^^^^^^

To reduce the memory footprint of a notebook, remove figures once they're no longer needed.
See the ``remove_figure`` function defined in the DP0 notebook
`03_Image_Display_and_Manipulation.ipynb in the tutorial-notebooks repository <https://github.com/rubin-dp0/tutorial-notebooks/blob/main/03a_Image_Display_and_Manipulation.ipynb>`_.
This is only necessary in notebooks that demonstrate data visualization with large datasets.
Better ways to clear the memory are under consideration (see `Stretch goals`_). 


Assert statements
^^^^^^^^^^^^^^^^^

Where essential, or where a very specific value is expected, the ``assert`` command can be used to
demonstrate to users that a condition is true.
For example, ``assert`` statements can be used to confirm that service objects like TAP are not
``None`` or ``null`` before moving on and using that instance,
or to check that values meet expectations (e.g., total rows returned from a query).
Do not use ``assert`` statements when, e.g., querying dynamic (prompt) datasets, which could return
different results and cause the assert statement to fail.
Consider more pedagogical alternatives when possible (e.g., printing schema columns would also fail if
the TAP service was not instantiated).


Known warnings
^^^^^^^^^^^^^^

If a code cell produces a warning which is known and it should be ignored, the preferred method is to add a markdown cell
*before* the code cell which produces the warning, to tell the user it is acceptable to ignore.
It is not preferred to use, e.g., ``warnings.simplefilter("ignore", category=UserWarning)``, because
ignoring categories of warnings can allow real issues to go unnoticed.


Output
------

Tables
^^^^^^

Results from a Table Access Protocol (TAP) service search are best displayed as an
``astropy`` table using ``.to_table()``, or as a pandas dataframe using ``.to_table().to_pandas()``.

Do not use the ``.to_table().show_in_notebook()`` method.
This can cause issues in the RSP JupyterLab environment that cause the notebook to hang indefinitely.


Plots
^^^^^

**Size:**
Plots should be large enough such that the details in the data are easily discerned,
but small enough to fit within a small browser window (e.g., a laptop screen).
Typically, a statement such as ``fig = plt.figure(figsize=(6, 4))`` is sufficient (or ``(6, 6)`` for square plots).

**Labels:**
Axes labels with units are mandatory.
A legend must be included if multiple types of data are co-plotted.
A descriptive title is encouraged but not mandatory.

**Style:**
In general, the default ``matplotlib`` style is sufficient and should be adopted for plot attributes
such as line thickness, tick labels, fontsize, and so on.
However, the default ``matplotlib`` color palette is not sufficient, and the recommendations
under :ref:`Accessibility considerations<accessibility-considerations>` should be used to
create colorblind-friendly plots.

**Error bars:**
Error bars should be included wherever possible, and especially in cases where analyses such
as line fitting is being performed on the data in the plot, to help the user understand data quality.

**Captions:**
A markdown cell underneath the figure should provide a figure number and a caption that explains
the main attributes of the plot.
This caption should serve as alt-text (as described under :ref:`Accessibility considerations<accessibility-considerations>`)
and also as a way for the user to confirm the plot appears as expected.


Image display
^^^^^^^^^^^^^

**Image orientation:**
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



.. _format-style-docs:

Documentation-based tutorials
=============================

Tutorials for the Portal and API Aspects, or tutorials written as scripts that can be
copy-pasted into the command line interface in the Notebook Aspect,
are written in reStructuredText (RST) format and are kept within the data release documentation at
`DP0.2 Tutorials <https://dp0-2.lsst.io/tutorials-examples/index.html>`_ and
`DP0.3 Tutorials <https://dp0-3.lsst.io/tutorials-examples/index.html>`_.


Header and section structure
----------------------------

All tutorials should have a descriptive title.
At the top of the page, the tutorial should list the contact authors,
the date last verified to run, and the targeted learning level, before
providing a brief narrative introduction.

The rest of the tutorial should be divided into sequentially numbered steps.
Steps should be short (one to a few sentences) and provide a single action item for the user.

It is very common, but not mandatory, to end all tutorials with a section called 
"Exercises for the learner" with suggestions of
how the user can make changes to the tutorial test options and examples,
or guide them on the next step forward on their own.


Code blocks
-----------

Ensure that all code and any Astronomical Data Query Language (ADQL) statements are 
put into code boxes in RST so that users may copy-paste whenever possible.
In RST, this is done as in the following example.

::

     .. code-block:: SQL

       SELECT e, q, incl 
       FROM dp03_catalogs_10yr.MPCORB 
       WHERE ssObjectId > 9000000000000000000


Screenshots
-----------

Use screenshots to demonstrate the steps of the tutorial, to show the user what to do,
and to show the expected results for comparison.
Augment screenshots with indicators (e.g., arrows or circles) to guide the users attention as needed.

Data visualization should `Colorblind-friendly plots`_.

**Caption and alt-text:** 
All figures should have a caption and an `Alternative-text (alt-text)`_ statement.
The motivation and guidance for writing alt-text is provided under
:ref:`Accessibility considerations<accessibility-considerations>`.

To add a caption and alt-text to an image in rST, use the ``:alt:`` command
as in the following example.

::

     .. figure:: /_static/figure_filename.png
       :name: name_of_figure
       :alt: Descriptive text of image (use tab to indent second line of text)

       Figure 1: The caption goes here, indented the same way, but with an empty line between code and caption text.


.. _accessibility-considerations:

Accessibility considerations
============================

The following set of best practices to be implemented for Rubin tutorials is a work in progress.


Vision-impaired astronomers
---------------------------


Colorblind-friendly plots
^^^^^^^^^^^^^^^^^^^^^^^^^

The most common form of colorblindness is being unable to differentiate red and green.
Guidelines for colorblind-friendly plots includes the following.

* Do not use red and green together.
* Use color combinations that are high contrast.
* **Do not use color alone, but with different symbol and line styles.**

In Jupyter Notebooks, in order to be accessible to those with Color Vision Deficiency (CVD or colorblind), 
plots color tables with ``matplotlib`` should be either a greyscale,
a `preceptually uniform sequential colormap <https://matplotlib.org/stable/users/explain/colors/colormaps.html#sequential>`_
like viridis or cividis, or 
`tableau-colorblind10 <https://viscid-hub.github.io/Viscid-docs/docs/dev/styles/tableau-colorblind10.html>`_.

The ``tableau-colorblind10`` color table can be loaded with the following python code.

::

  import matplotlib.pyplot as plt
  plt.style.use('tableau-colorblind10')


For the LSST filter set ``ugrizy``, always use symbols and line styles to represent the filters in addition to color.

Use the following color cycles for each filter on both white and black backgrounds:

White background:

::

  plot_filter_colors_white_background = {'u': '#0c71ff', 'g': '#49be61', 'r': '#c61c00', 'i': '#ffc200', 'z': '#f341a2', 'y': '#5d0000'}

Black background:

::

  plot_filter_colors_black_background = {'u': '#3eb7ff', 'g': '#30c39f', 'r': '#ff73e00', 'i': '#2af5ff', 'z': '#a7f9c1', 'y': '#fdc900'}

Use the following symbols:

::

  plot_symbols = {'u': 'o', 'g': '^', 'r': 'v', 'i': 's', 'z': '*', 'y': 'p'}

Use the following line styles:

::

  plot_line_styles = {'u': '--', 'g': ':', 'r': '-', 'i': '-.', 'z': (0, (3, 5, 1, 5, 1, 5)), 'y': (0, (3, 1, 1, 1))}

Alternative-text (alt-text)
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


.. _narrative-text:

Narrative text
==============

Introductory text should be written in present, impersonal tense, similar to the introduction of a journal article.
Paragraphs may be used, but should be kept short.
Content should be limited to only background information that is relevant to the tutorial.

Instructional text should be written in the `imperative mood <https://en.wikipedia.org/wiki/Imperative_mood>`_, as is commonly adopted for technical writing.
Sentences should be kept short and unambiguous, only describing the actions the user needs to take to achieve the expected results.
When the user action is executing code, the instructional text should describe what the code does in simple terms.

To implement the imperative mood in tutorials, use the infinitive or second-person present tense (often this is the same).
Omit the "you" whenever possible, but it is OK to include "you" or "your", especially when it clarifies the instruction.
The passive voice should be avoided, as should use of "we", "our", and "let's" or "let us".

Below are a few examples to help with writing instructional statements in narrative text.

Best:
 * Run the query.

Also ok:
 * Run your query.

Do not use:
 * The query is run.
 * Now let's run the query.
 * Here we run our query.

Additional writing resources are found in Rubin's `User documentation style guide <https://developer.lsst.io/user-docs/index.html>`_.


.. _stretch-goals:

Stretch goals
=============

Work is on-going in these areas, and in time they will become part of the guidelines above.

**Notebook metadata:**
Embed notebook metadata (e.g., version, skills, packages) in a way that can be scraped and used to auto-generate the ``README.md`` file or a Table of Contents, to enable users to browse notebook contents.

**Accessibility:**
Continue to improve tutorials' accessibility to people with disabilities by finding and implementing, 
e.g., screen reader compatibility software, data sonification packages, 
customized use of `nbconvert <https://nbconvert.readthedocs.io/en/latest/>`_, 
additional policies for supporting neurodivergent users, and other jupyter notebook accessibility techniques.

**Translations:**
At minimum, translate any undergraduate-level tutorials into Spanish.
Additionally, improve tutorials' accessibility to non-English speakers by finding and implementing automatic translation and localization software.

**Clearing memory:**
Develop a best practice for how to keep notebook memory usage in check, in addition to deleting figures.
E.g., whether or not the ``del`` command is sufficient for this.

**Package of commonly-used functions:**
Create recipes for common user activities.
These could be, e.g., ADQL searches for the portal, code snippets for the command line,
or python modules that can be imported.
When these are used in the advanced notebooks, also demonstrate use of the ``inspect.getsource``
functionality for users to display function code.
