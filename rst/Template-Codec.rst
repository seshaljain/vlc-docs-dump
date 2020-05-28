.. raw:: mediawiki

   {{top box
   |id={{#if:{{{id|}}}|{{{id}}}|??[[Category:Codecs missing ids]]}}

| \|text= This is {{#switch: \|audio = an `audio codec <Codec#Audio>`__ \|video = a `video codec <Codec#Video>`__ \|#default = a `codec <codec>`__ }}. The name to use at the `command line <command_line>`__ is {{#if:\|\ ****\ \|unknown}}{{#if:\|, but you can also use ****\ {{#if:\|, or ****}}}}. {{#switch: \|y =
| VLC can **encode** using this codec. \|n = \| =
| VLC can **encode** using this codec through the ` <Documentation:Modules/{{{encoder}}}>`__ module. }} {{#if:\|
| This codec can be used inside the containers.}} {{#if:\|
| This codec is from the ` <Documentation:Modules/{{{mod}}}>`__ module.}} \|bgcol={{#switch: \| audio = #f0fcfc \| video = #fcf0fc \| #default = White }} \|brcol={{#switch: \| audio = #a0c0c0 \| video = #c0a0c0 \| #default = #aaa }} }} {{#switch: \| audio = \| video = \| #default = }} A meta-template for codecs.

Usage:

``{{codec |type= | id= | altid= | altid2= | encoder= | for= | mod= }}``

You should supply type and id, the rest are optional.

-  type: the type of codec, currently audio or video
-  id: the module name for the codec. If other shortcuts to the same module exist, also list them with altid, or altid and altid2
-  for: a list of containers this codec is compatible with. Put the names in [[ ]] so they link properly
-  mod: module name from `Documentation:Modules <Documentation:Modules>`__
-  encoder:

   -  If equal to y, display a message, currently "VLC can **encode** using this codec."
   -  If equal to n (default), do nothing
   -  All other values attempt to link to a module of that name (even if it doesn't exist!). Useful for e.g. H.264 and H.265, which decode and encode through separate modules

See also
--------

-  

   .. raw:: mediawiki

      {{tl|Codec}}

-  

   .. raw:: mediawiki

      {{tl|Codec audio}}

-  

   .. raw:: mediawiki

      {{tl|Codec video}}

-  

   .. raw:: mediawiki

      {{tl|Mux}}

`Category:Audio codecs <Category:Audio_codecs>`__ `Category:Codecs <Category:Codecs>`__ `Category:Video codecs <Category:Video_codecs>`__ `Category:Codecs <Category:Codecs>`__ `Category:Codecs <Category:Codecs>`__ `Category:Templates <Category:Templates>`__
