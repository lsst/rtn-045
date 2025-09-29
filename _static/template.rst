.. Review the README on instructions to contribute.
.. Review the style guide to keep a consistent approach to the documentation.
.. Static objects, such as figures, should be stored in the _static directory. Review the _static/README on instructions to contribute.
.. Do not remove the comments that describe each section. They are included to provide guidance to contributors.
.. Do not remove other content provided in the templates, such as a section. Instead, comment out the content and include comments to explain the situation. For example:
	- If a section within the template is not needed, comment out the section title and label reference. Do not delete the expected section title, reference or related comments provided from the template.
    - If a file cannot include a title (surrounded by ampersands (#)), comment out the title from the template and include a comment explaining why this is implemented (in addition to applying the ``title`` directive).

.. This is the label that can be used for cross referencing this file.
.. Recommended title label format is "Directory Name"-"Title Name" -- Spaces should be replaced by hyphens.
.. _Tutorials-Examples-DPX-Aspect-Y:
.. Each section should include a label for cross referencing to a given area.
.. Recommended format for all labels is "Title Name"-"Section Name" -- Spaces should be replaced by hyphens.
.. To reference a label that isn't associated with an reST object such as a title or figure, you must include the link and explicit title using the syntax :ref:`link text <label-name>`.
.. A warning will alert you of identical labels during the linkcheck process.


##############################################
101.1. A template documentation-based tutorial
##############################################

For the Portal Aspect of the Rubin Science Platform at data.lsst.cloud.

**Data Release:** *DPX* or *DRX*

**Last verified to run:** *yyyy-mm-dd*

**Learning objective:** *Very brief description of tutorial's learning objective.*

**LSST data products:** *List the catalogs and images used.*

**Credit:** *E.g., "Originally developed by" or "Based on tutorials developed by" and then people's names, including journal article or software release citations if appropriate.* Please consider acknowledging them if this tutorial is used for the preparation of journal articles, software releases, or other tutorials.

**DOI:** `10.11578/rubin/dc.20250909.20 <https://doi.org/10.11578/rubin/dc.20250909.20>`_

**Get Support:** Everyone is encouraged to ask questions or raise issues in the `Support Category <https://community.lsst.org/c/support/6>`_ of the Rubin Community Forum. Rubin staff will respond to all questions posted there.

*How-to tutorials should NOT need sections, and have a minimal number of very concise steps. How-tos should NOT have an introduction as this is covered by the learning objective above.*

*Like the notebook template, italicized text should be removed or replaced.*


.. _DPX-Aspect-Y-Intro:

Introduction
============

*Provide a light narrative about this tutorial, e.g., "This tutorial will demonstrate how to...".*

*Cite or link to any external information, documentation, or papers.*

*Describe key scientific concepts.*

**Related tutorials:**
*If applicable, mention other relevant tutorials by name but do not link to them.*
*Tutorials evolve continuously, there is no linkchecker for the notebook repo, and tutorial hotlinks will go stale quickly.*
*It is not necessary to mention the preceeding/subsequent tutorials in the same series as this one - those are trivial for the user to find.*
*But do use this section to mention related tutorials in other series.*



.. _DPX-Aspect-Y-1:

1. The first section
====================

**1.1. Log in to the Portal Aspect of the Rubin Science Platform.**
In a browser, go to the URL `data.lsst.cloud <https://data.lsst.cloud>`_ and select the Portal Aspect.
Follow the process to log in.

**1.2. Select the X tab in the Portal.** 
*Explanation of the setup, reference to Figure 1.*

.. figure:: /_static/aspect_y_1_fig1.png
    :name: aspect_y_1_fig1
    :alt: Alt-text goes here.

    Figure 1: Figure caption goes here.


**1.3. Execute the ADQL query.**
*Explanation of the query, reference to the code block below.*

.. code-block:: SQL 
    
    SELECT g_H, r_H, i_H, z_H 
    FROM dp03_catalogs_10yr.SSObject 
    WHERE ssObjectId > 8660000000000000000



.. _DPX-Aspect-Y-2:

2. The second section
=====================

**2.1.** *And so on.*



.. _DPX-Aspect-Y-exercises:

X. Exercises for the learner 
============================

**X.1. A clear, achievable task.**

**X.2. Another clear, achievable task.**
