.. raw:: mediawiki

   {{top box
   |id={{{1|??}}}
   |text=<!--
   Line 1:               -->VLC uses this [[protocol]] (or [[access module]]) to read data from a device or network.{{#if:{{{info|}}}|&#32;Additional information: '''{{{info}}}'''}}

| {{#if:}}}}}\|
| This protocol is handled by the **}}}}}** `module <module>`__.}} \|bgcol=#ffe0e0 \|brcol=#e0c0c0 }}{{#ifeq:\|y\| \|}}

Usage
-----

``{{protocol |<protocol> |info= |mod= }}``

| The purpose of the template is to visually inform readers that VLC supports the protocol and through which module.
| The page will be added automatically to `:Category:Protocols <:Category:Protocols>`__.

Parameters:

-  (unnamed) (required): the text in the small box, defaults to \ **??**\ 
-  **``|info=``** (optional) extra text
-  **``|mod=``** (optional) link to a particular module while displaying the given

Enter the protocol name as-is. If the name differs other than casing supply the module name with **``|mod=``**

Examples
--------

For `HTTP <HTTP>`__ the casing difference between `HTTP <HTTP>`__ and ** is not a problem:

``{{``\ \ ``|HTTP}}``

{{\|HTTP|nocat=y}} For `RTSP <RTSP>`__, the protocol is handled by the module:

``{{``\ \ ``|RTSP|mod=live}}``

{{\|RTSP|mod=live|nocat=y}} To say something for `Dummy <Dummy>`__:

``{{``\ \ ``|Dummy|info=Fakes codec input, but is no longer used.}}``

{{\|Dummy|info=Fakes codec input, but is no longer used.|nocat=y}}

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

`Category:Protocols <Category:Protocols>`__ `Category:Templates <Category:Templates>`__
