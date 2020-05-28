.. raw:: html

   <div class="noprint infobox sidebox">

.. raw:: html

   <div class="center">

.. raw:: html

   </div>

{{#if: \|{{#if: \|

.. raw:: html

   <div class="infobox-multipleitem">

\*\ **[ }}}]\ \ '' \*\ [ }}}]**'' {{#if: \|\*\ **[ }}}]** }}

.. raw:: html

   </div>

\|

.. raw:: html

   <div class="infobox-singleitem">

**[ }}}]**

.. raw:: html

   </div>

}} }} {{#if: \|{{#if: \|

.. raw:: html

   <div class="infobox-multipleitem">

\*\ `}}} <{{{wikilink1}}}>`__\ **\ \ \ '' \*\ **\ `}}} <{{{wikilink2}}}>`__\ *{{#if: \|\*\ *\ `}}} <{{{wikilink3}}}>`__\ *\ *\ **\ \ \ '' {{#if: \|\*\ **\ *\ *\ `}}} <{{{wikilink4}}}>`__ }} }}

.. raw:: html

   </div>

\|

.. raw:: html

   <div class="infobox-singleitem">

`}}} <{{{wikilink1}}}>`__

.. raw:: html

   </div>

}} }}

.. raw:: html

   </div>

Usage
-----

\ ``{{Side box | text | link1 | label1 | link2 | label2 | link3 | label3 }}``\ 

or

\ ``{{Side box | text | wikilink1 | label1 | wikilink2 | label2 | wikilink3 | label3 | wikilink4 | label4 }}``\ 

This is a meta-template. There is no guarantee that usage will remain the same, but will be changed when needed. The only required parameter is ``text``. links and wikilinks are mutually exclusive. labels default to the link.

**Examples**

``{{side box|text=Example is [[free]] and [[open source]]!}}``

.. raw:: mediawiki

   {{side box|text=Example is [[free]] and [[open source]]!}}

.. raw:: mediawiki

   {{clear}}

``{{side box|text=[[wikipedia:Main_Page|Wikipedia]] has information on these entries:|wikilink1=wikipedia:MPEG-1|label1=MPEG 1|wikilink2=wikipedia:MPEG-2|label2=MPEG 2|wikilink3=wikipedia:MPEG-3|label3=MPEG 3}}``

.. raw:: mediawiki

   {{side box|text=[[wikipedia:Main_Page|Wikipedia]] has information on these entries:|wikilink1=wikipedia:MPEG-1|label1=MPEG 1|wikilink2=wikipedia:MPEG-2|label2=MPEG 2|wikilink3=wikipedia:MPEG-3|label3=MPEG 3|wikilink4=wikipedia:MPEG-4|label4=MPEG 4}}

`Category:Templates <Category:Templates>`__
