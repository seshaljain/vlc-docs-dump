.. raw:: mediawiki

   {{top box
   |id={{{id|??}}}
   |text=<!--
   Line 1: -->VLC can {{ #ifeq: {{{encoder|n}}} | y | '''encode''' and }}

| **decode** this `container <container>`__. 
| {{#if: \|The `module <module>`__ name to use at the `command line <command_line>`__ is {{#switch: \| page = **}}}** \| none = }}} \| #default = [ }}}] }} {{#if: \|, but you can also use **** {{#if: \|, or **** }} }}. \|The `module <module>`__ name to use at the `command line <command_line>`__ is unknown. }} }} {{ #ifeq: \| y \| }} 

Usage
-----

``{{mux|id= |encoder= |info= |module link= { page, none, <value> } |altid= |altid2= |mod= }}``

id is supposed to be what you'd put in the command line, like

``--sout='#std{mux=``\ **``id``**\ ``,url=....}'``

If there is more than one shortcut, use altid for the others.

Parameter **``|module``\ ````\ ``link=``** defaults to ``page``:

-  page

   -  ``mod`` will link to a particular module while displaying the ``id`` given. Use this when ``altid`` would not make sense. For example, on the page `MOV <MOV>`__ the code ``{{Mux|id=mov|mod=mp4}}`` will link to the *mp4* module while prominently displaying the shortcut *mov* in the box.

-  none - ID only, no links
-  

   .. raw:: mediawiki

      {{tag|value}}

   - URL to the Git file

It will add it to `:Category:Container <:Category:Container>`__ (all containers) and `:Category:Container_Decoder <:Category:Container_Decoder>`__ (containers which can be decoded... which is all containers ;-) If you think that's stupid, change it!

If encoder is "y" then it also adds it to `:Category:Container_Encoder <:Category:Container_Encoder>`__ and changes the text a bit.

Info is for extra text in the box.

Examples
--------

Example, `avi <avi>`__

``{{mux|id=avi|encoder=y}}``

becomes

Example, `asf <asf>`__

``{{mux|id=asf|encoder=y|info=This works with mp2v, blah blah}}``

becomes

Example, `mp4 <mp4>`__

``{{mux|id=mp4|encoder=y|altid=mov|altid2=3gp}}``

becomes

See also
--------

-  

   .. raw:: mediawiki

      {{tl|Codec audio}}

-  

   .. raw:: mediawiki

      {{tl|Codec video}}

-  

   .. raw:: mediawiki

      {{tl|Mux}}

-  

   .. raw:: mediawiki

      {{tl|Protocol}}

`Category:Container <Category:Container>`__ `Category:Container_Encoder <Category:Container_Encoder>`__ `Category:Container_Decoder <Category:Container_Decoder>`__ `Category:Templates <Category:Templates>`__
