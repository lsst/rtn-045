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
The user should be able to work through the core contents of the notebooks within 30 minutes.  Additional examples could be included, 
but should be clearly labeled as such.

Well-Documented.
----------------
High quality documentation should be provided in the notebook, including narrative descriptions, citations, references, 
and external links to, e.g., package documentation.

Cross-Referenced.
-----------------
Intermediate and advanced notebooks should attempt to provide the names of precursory notebooks that teach any basic skills required. 
Beginner and intermediate notebooks should attempt to provide the names of more advanced notebooks developed in a series on the same topic.

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

  import matplotlib.pyplot as plt
  
  plt.style.use('tableau-colorblind10')
  
  For the LSST filter set ugrizy, adopt the same colors as DES, which were chosen to be colorblind-friendly:
  
  plot_filter_colors = {'u' : '#56b4e9', 'g' : '#008060', 'r' : '#ff4000', 'i' : '#850000', 'z' : '#660cc', 'y' : '#000000'}
  
Image Orientation.
""""""""""""""""""
If using a WCS: east left, north up.  If only using pixels, (0,0) should be lower left, which is the default for awfDisplay.  When using other plotting packages, transofrmations might be needed in order to match the afwDisplay default.  See the LSST Science Pipelines documentation about `Image Indexing. <https://pipelines.lsst.io/modules/lsst.afw.image/indexing-conventions.html>`_. Since use of "extent" is necessry for displaying a WCS overlay for deepCoaads, let's use it all the time:

  deepCoadd = butler.get('deepCoadd', dataId=dataId)
  deepCoadd_bbox = butler.get('deepCoadd_calexp.bbox', dataId=dataId)
  deepCoadd_wcs = butler.get('deepCoadd_calexp.wcs', dataId=dataId)
  deepCoadd_WCSfMd = WCS(deepCoadd_wcs.getFitsMetadata())
  deepCoadd_extent = (deepCoadd_bbox.beginX, deepCoadd_bbox.endX, deepCoadd_bbox.beginY, deepCoadd_bbox.endY)
  
  plt.subplot(projection=deepCoadd_WCSfMd
  plt.imshow(deepCoadd.image.array, cmap='gray', vmin=0, vmax=2, extent=deepCoadd_extent, origin='lower')
  
Remove Figures.
"""""""""""""""
To reduce the memory footprint of a notebook, remove figures once they're no longer needed.  See the DP0.1 Notebook 03_Image_Display_and_Manipulation.ipynb.

"Assert" Statements.
^^^^^^^^^^^^^^^^^^^^
Where essential, or where a very specific value is expected, use "assert" statements. E.g., check that service objects like TAB are not `None` or `null` before moving on and using that instance, or check that values meet expectations (e.g., total rows returned from a query).  However, take care not to use when, e.g., querying dynamic (prompt) datasets. Consider more pedagogical alternatives when possible (e.g., printing schema columns would also fail if the TAP service was not instantiated).

Warnings.
^^^^^^^^^
If a code cell consistently produces a warning which is known and not a cause for worry, consider adding a warning exception in Section 1.1 (see below) or including a markdown text to let the user know that the warning is known and to not report it.

  warnings.simplefilter("ignore", category=UserWarning)
  
Code Cell Comments.
^^^^^^^^^^^^^^^^^^^
Keep comments within a code cell brief and on a separate single line.  Use of code-cell comments should be limited, and markdown cells are the preferred way to provide descriptive text.

Code Standards.
---------------
Use flake8 to ensure notebook code conforms to codebase style `PEP8 <https://www.python.org/dev/peps/pep-0008/>`_ , with a few exceptions. 

Install the required packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Install the required packages locally in your RSP@IDF home directory:

  pip install --user flake8-nb
  pip install --user pycodestyle_magic
  
Create a configureation file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Create a configuration file for flake8. These instructions use emacs but it doesn't matter so long as the end result is correctly-named file with the right contents. From the command line in your home directory, execute:

  touch .config/flake8
  emacs .config/flake8
  
Then copy-paste the following into the opened config file:
  
  [flake8]
  max-line-length = 99
  ignore = E133, E226, E228, N802, N803, N806, N812, N813, N815, N816, W503
  
Use x-s x-c to save and exit emacs.

While developing a notebook.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
While developing a notebook, have the following 'magic' commands as the first code cell:

  %load_ext pycodestyle_magic
  %flake8_on
  import logging
  logging.getLogger("flake8").setLevel(logging.FATAL)
  
Whenever you execute a cell, it will use flake8 to check for adherence to the PEP8 coding style guide, and report violations. Fix them as you go. Once you're done with the entire notebook you can remove that cell with the magic commands. 

When the notebook is complete.
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
When the notebook is complete, from the command line in the notebook's directory execute:

  flake8-nb notebook_name.ipynb
  
This will give you a final check of any violations with PEP8. This will catch things that can be missed line-by-line, such as packages that are imported but never used.  

Comply with out GitHub branch, merge, and review policy.
========================================================

The following applies when creating or updating notebooks in the `tutorial-notebooks` repository of the `rubin-dp0` GitHub Org.

Branch.
-------
Develop new notebooks, or update existin ones, in a new branch (from main, not from prod) named for the associated Jira ticket (e.g., tickets/PREOPS-12345) or with the username/task convention (e.g., u/melissag/makeNB10). Only update one notebook per ticket branch, unless the ticket is to make similar updates to all notebooks (e.g., when bumping the RSP's recommended image). Update the README file when appropriate.

Commit and Push.
----------------
Always restart the kernel and clear all outputs before saving, committing, and pushing changes.

Pull Request.
-------------
When the notebook is complete, and at least two weeks before the planned deployment data wherever possible, open a pull request to merge the ticket branch into the main branch (*not* to prod). 

Review.
-------
Contact one or more Rubin staff members (it need not be a Community Engagement team member) with the appropriate expertise and ask them to review the notebook.  If they agree, assign them as a reviewer on your pull request.

Update.
-------
After the reviewers have provided comments or requested changes, make new commits to the branch, incorporate as many of their requests as possible. In GitHub, respond to all comments with either a confirmation or an explanation of why the request was not implemented. Contact the reviewers to let them know the pull request now awaits their approval.

Merge.
------
After the reviewers have approved the pull request, rebase and merge your ticket branch into the main branch (*not* to prod). Resolve all conlicts, if there are any. After the successful merge, delete your branch.

Release.
--------
To "release" the new version of main to prod branch (i.e., to update all RSP users' tutorial notebooks), open a new pull request from the main to the prod (production) branch, and rebase and merge. Do not squash commits, in order to keep prod and main with the same commit history. This stage does not need another review. Usually Melissa or Matthew handle this. The very last step is to do a final PR of prod->main, rebase and merge, to ensure main is now 'up to date' with prod, and avoid future conflics. 

Coordinate.
-----------
The number of pushes to the prod branch should be minimized. E.g., if there are a few tickets being completed within a week, coordinate with other notebook developers to collect all changes in the main branch, and then do a single pull request from main to prod.

Jira Tickets.
-------------
Remember to make comments in the associated Jira tickets about the major updates and mark the ticket as Done once the brainch has been merged into main.

Update Notebooks when the RSP's recommended version is bumped.
==============================================================

DM Instigates.
--------------
When the Data Management team is ready to bump the recommended, they will make a DM ticket and confirm that the tutorial-notebooks run to completion with the new version.

PREOPS Ticket.
--------------
*(Open, describe, link to DM ticket, assign, etc.)*

Branch.
-------
*(From main, NOT from prod. Name it for the PREOPS ticket.)*

Update NBs.
-----------
*(Login to RSP selecting the weekly that will become the recommended. Update notebook headers etc. Execute all notebooks and check for any warnings. Address warnings in text of NB (or remove text that addresses warnings which no longer appear). Make sure all NBs are cleared (unexecuted) in commit. Discuss with CET or the NB's contact author if any big changes are needed (DM will have verified that all notebooks run, and they generally do not want big changes to occur in these version bumps).)*

PR to main.
-----------
*(Use rebase and merge (do not squash), as in 3.6 above. No need for a review, as it should only be small changes to the header & text. Delete the PREOPS-named ticket branch.)*

Confirm with DM. 
----------------
Close the loop with DM and report on their original ticket that CET is ready to PR main -> prod during Patch Thursday after the recommended is updated.

PR to prod.
-----------
*(Use rebase and merge (do not squash), as in 3.7 above. Do the merge during Patch Thursday. Then immediately do a PR prod->main to avoid future issues.)*

Close PREOPS Ticket.
--------------------
You're done!

Work towards our stretch goals.
===============================

Notebook Metadata.
------------------
Embed notebook metadata (e.g., version, skills, packages) in a way that can be scraped and used to auto-generate the `README.md <http://readme.md/>`_ file or a Table of Contents, to emable users to browse notebook contents. 

Accessibility for Visual Disabilities.
--------------------------------------
Improve notebooks' accessibility to people with visual disabilities by finding and implementing, e.g., screen reader compatibility software, data sonification packages.

Translations.
-------------
Improve notebooks' accessibility to non-English speakers by finding and implementing automatic translation software.

Garbage Collection.
-------------------
Develop a best practice for how to keep notebook memory usage in check, in addition to deleting figures. Do not rely on the 'del' command for this.

Functions.
----------
Create a set of functions for common user activities, like cutouts or image display with a particular scaling (or anything else we find ourselves repeating). Use these in the advanced notebooks, and use the "inspect.getsource' functionality (pass it a function and it will print the source code that defined it) for users to see function code in-NB.

Support users with updates and git issues.
==========================================

Troubleshooting.
----------------
The notebooks/tutorial-notebooks directory is not read-only, and when users change and save files in that directory, it can lead to issues when the prod branch is updated. Troubleshooting those issues is documented at `https://dp0-2.lsst.io/data-access-analysis-tools/nb-intro.html#troubleshooting-tips <https://dp0-2.lsst.io/data-access-analysis-tools/nb-intro.html#troubleshooting-tips>`_ , but doing this is still confusing and tiime-consuming for users, especially those new to git.

Making the tutorial-notebooks directory read-only.
--------------------------------------------------
As discussed in LSSTC Slack space #ops-data-previews: `https://lsstc.slack.com/archives/C015B006ZAB/p1661200755846119 <https://lsstc.slack.com/archives/C015B006ZAB/p1661200755846119>`_ .

After identify migration at the IDF (planned for fall 2022), the notebooks/tutorial-notebooks directory will be read-only as a default, but since the directory is owned by the user, they can change the permissions to be writeable. The README.md file and relevant documentation will be updated by the CET at that time, and messaging sent to delegates, about the change in this directory, with a recommendation to leave it as read-only. The RSP team will adjust the system such that, if the user's "notebooks/tutorial-notebooks/" directory is deleted to be not in a clean state (or maybe just if the directory permission have bene changed, if that's and easier test), then the following file is added.

00_WARNING_README.md

The presence of this file indicates the user has changed the permissions on this directory from read-only, and that the directory's contents might no longer be in sync with the prod ('production') branch of the tutorial-notebooks repository in the rubin-dp0 GitHub organization [link].

The recommended recovery method is to move this directory to a new location with a new name (or simply delete the directory if you do not need to save your changes), stop your current JupyterLab instance, and then start a new one (i.e., log back into the RSP's Notebook Aspect). An up-to-date read-only version of the tutorial-notebooks directory will appear.  It is recommended to leave that directory as read-only.

Find more detailed options for recovery and use of git here in the documentation [link].

The first link will go to `https://github.com/rubin-dp0/tutorial-notebooks <https://github.com/rubin-dp0/tutorial-notebooks>`_ , and the second link to an updated version of `https://dp0-2.lsst.io/data-access-analysis-tools/nb-intro.html#troubleshooting-tips <https://dp0-2.lsst.io/data-access-analysis-tools/nb-intro.html#troubleshooting-tips>`_ .

