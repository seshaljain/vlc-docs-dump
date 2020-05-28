.. raw:: mediawiki

   {{See also|Debug}}

The point of this page is to show you how to get VLC related crash info with a tool called **gdb**.

This crash info is **VERY** useful when tracking down the reason for the crash, so if you can provide us with this info, the likelihood of getting your bug fixed is much higher.

What you need
-------------

-  Windows computer
-  32-bit VLC build (this tutorial isn't for 64-bit VLC builds, but it will work for 64-bit Windows versions that run 32-bit VLC).
-  A way to crash VLC (freezes aren't useful unfortunately)

What you have to do
-------------------

1. Download latest nightly debug build of VLC from http://nightlies.videolan.org/build/win32/?C=M;O=D

-  **Trunk** folders are current development (unstable) version, **Branch** folders are current/next stable versions (usually you want latest branch folder)
-  Make sure you take the debug version. It is usually named as vlc-x.y.z-something-date-randomnumber-win32-\ **debug**.7z or vlc-x.y.z-something-date-randomnumber-win32-\ **debug**.zip

.. figure:: Vlc_gdb_nightly.png‎
   :alt: Vlc_gdb_nightly.png‎

   Vlc_gdb_nightly.png‎

2. Extract the .zip/.7z to somewhere (like in your desktop)

-  Tool called 7-Zip can be used to extract .7z packages
-  Folder doesn't really matter. So you **don't** have to uninstall your current VLC version. And you can have multiple VLC versions in your computer.

.. figure:: Vlc_gdb_nofolder.png‎‎
   :alt: Vlc_gdb_nofolder.png‎‎

   Vlc_gdb_nofolder.png‎‎

3. Run vlc.exe from that folder and see if you can replicate the issue that is causing your current VLC to crash.

-  Some issues might be already fixed, so it might not be possible to replicate the crash

4. If you can replicate the issue, next step is to download gdb debugger from ftp://ftp.equation.com/gdb/32/gdb.exe

5. Copy the gdb.exe to the same directory where you extracted the VLC debug build

.. figure:: Vlc_gdb_folder.png‎‎
   :alt: Vlc_gdb_folder.png‎‎

   Vlc_gdb_folder.png‎‎

6. Launch gdb.exe by double clicking it

-  You can also launch it via .bat or by other method

7. Type in *target exec vlc* and press enter

-  gdb takes commands via this terminal

.. figure:: Vlc_gdb_target_exec.png‎‎‎‎
   :alt: Vlc_gdb_target_exec.png‎‎‎‎

   Vlc_gdb_target_exec.png‎‎‎‎

8. Type in *run* and VLC should start after few moments

-  first vlc.exe startup might take some time, so please wait

.. figure:: Vlc_gdb_run.png‎
   :alt: Vlc_gdb_run.png‎

   Vlc_gdb_run.png‎

9. After vlc.exe is launched, repeat the actions that crash VLC

-  certain crashes might not happen when vlc.exe is run via gdb.exe, so crash might not happen
-  crashes can be noticed from gdb console, which shows "Program received signal..." message

.. figure:: Vlc_gdb_signal.png‎
   :alt: Vlc_gdb_signal.png‎

   Vlc_gdb_signal.png‎

10. Once vlc.exe has crashed, type in *bt* to the gdb console

-  bt is short for backtrace

.. figure:: Vlc_gdb_bt.png‎‎‎
   :alt: Vlc_gdb_bt.png‎‎‎

   Vlc_gdb_bt.png‎‎‎

11. Share us the info that bt command gave

-  right click the gdb window and select Edit -> Mark to mark the text you want to copy, and then left click to select area, then right click to copy it to clipboard
-  you can share us info via trac, via IRC, via forums etc.

.. figure:: Vlc_gdb_marked.png‎‎‎‎
   :alt: Vlc_gdb_marked.png‎‎‎‎

   Vlc_gdb_marked.png‎‎‎‎

12. You can close the gdb by typing *quit*

-  you can answer *y* to the question

.. figure:: Vlc_gdb_quit.png‎‎‎‎‎
   :alt: Vlc_gdb_quit.png‎‎‎‎‎

   Vlc_gdb_quit.png‎‎‎‎‎

`Category:Building <Category:Building>`__ `Category:Coding <Category:Coding>`__ `Category:Windows <Category:Windows>`__
