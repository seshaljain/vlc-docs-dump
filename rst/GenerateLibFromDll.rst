.. raw:: mediawiki

   {{Example code|for=libVLC}}

from: http://www.coderetard.com/2009/01/21/generate-a-lib-from-a-dll-with-visual-studio/

Introduction
------------

To avoid installing and fighting against MSYS and Cygwin, you can just extract exported symbols from libvlc.dll to generate a .lib (libvlc.lib) and link your program against it. And all of this using only with Microsoft Visual Studio Tools!

In case you don't have Visual Studio you can download the free version here `Visual Studio Express <http://www.microsoft.com/express/download>`__.

Open a Command Prompt
---------------------

It can be found within the Visual Studio Tools menu entry: Start / Program Files / Microsoft Visual Studio / Visual Studio Tools / Visual Studio Command Prompt.

Extract Symbols
---------------

Within the command prompt type:

\ `` dumpbin /exports "``\ \ ``\libvlc.dll" > "``\ \ ``\libvlc.def"``

Edit the libvlc.def file and modify it to get something like this:

| ``EXPORTS``
| ``libvlc_add_intf``
| ``libvlc_audio_get_channel``
| ``libvlc_audio_get_mute``
| ``libvlc_audio_get_track``
| ``libvlc_audio_get_track_count``
| ``libvlc_audio_get_track_description``
| ``libvlc_audio_get_volume``
| ``...``

Alternatively, the following command will automatically generate the DEF file:

| \ `` echo EXPORTS > libvlc.def``
| \ :literal:` for /f "usebackq tokens=4,* delims=_ " %i in (`dumpbin /exports "`\ \ :literal:`\\libvlc.dll"`) do if %i==libvlc echo %i_%j >> libvlc.def`

Generate the .lib
-----------------

Still within the command prompt type:

\ `` lib /def:"``\ \ ``\libvlc.def" /out:"``\ \ ``\libvlc.lib" /machine:x86``

Of course, you'll need to adapt the path according to your configuration.

Voilà! You have it, now you can link against libvlc.lib in your program :-)

`Category:libVLC <Category:libVLC>`__
