{{#ifeq:\|y \|{{#switch: \|windows = {{#ifeq:\|n|%PROGRAMFILES%\VideoLAN\VLC|"%PROGRAMFILES%\VideoLAN\VLC"}} \|mac = /Applications/VLC.app/Contents/MacOS \|linux = }} \|{{#switch: \|windows = "%PROGRAMFILES%\VideoLAN\VLC\vlc.exe" \|mac = /Applications/VLC.app/Contents/MacOS/VLC \|linux = vlc }} }}

Usage
-----

A template for default locations on desktop computers by `operating system <operating_system>`__.

Parameters:

-  (unnamed) required. One of ``windows``, ``mac`` or ``linux``. No default
-  **``|dir=``** optional (short for *directory*). Only checks for value ``y`` (*yes*). Default disabled
-  **``|q=``** optional (short for *quotes*). Only checks for value ``n`` (*no*). Default enabled

Showcase of various modes:

-  ``{{``\ \ ``|windows}}``

      {{\|windows}}

-  ``{{``\ \ ``|windows|dir=y}}``

      {{\|windows|dir=y}}

-  ``{{``\ \ ``|windows|dir=y|q=n}}``

      {{\|windows|dir=y|q=n}}

-  ``{{``\ \ ``|mac}}``

      {{\|mac}}

-  ``{{``\ \ ``|mac|dir=y}}``

      {{\|mac|dir=y}}

-  ``{{``\ \ ``|linux}}``

      {{\|linux}}

-  ``{{``\ \ ``|linux|dir=y}}``

      {{\|linux|dir=y}}

See also
--------

-  

   .. raw:: mediawiki

      {{tl|Path to VLC}}

-  

   .. raw:: mediawiki

      {{tl|VLC folder}}

   - simple wrapper template for directory paths only (no quotes)

`Category:Templates <Category:Templates>`__
