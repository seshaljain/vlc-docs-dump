.. raw:: mediawiki

   {{Historical|Use [[Python bindings]]}}

Python binding documentation
----------------------------

**NOTE: this version of python bindings (compiled C-module) is deprecated in favor of the new**\ `PythonBinding <PythonBinding>`__\ **.**

The old version of python bindings, which can be found in ``bindings/python``, is a python C-based module. Sources are browsable from `python binding <http://trac.videolan.org/vlc/browser/bindings/python>`__ and a code sample can be found in the sources (file `vlcwidget.py <http://trac.videolan.org/vlc/browser/bindings/python/vlcwidget.py>`__).

It has been compiled, and is being used, on Linux, Windows and Mac OS X.

Compile HOWTO
-------------

Only for < 0.9.0 versions: If you want to include the python bindings in your build, you must pass --enable-python-bindings (svn version) or --enable-mediacontrol-python-bindings (0.8.6\* versions) to ./configure as it is disabled by default.

For >= 0.9.0 versions, python bindings cannot be compiled at the same time as the main VLC tree. They can (and event must) be compiled from a compiled VLC, provided that appropriate headers and libraries (libvlc.so/.dll) are available.

Linux/Debian
~~~~~~~~~~~~

On Debian:

-  install the libvlc2-dev package
-  Get the python bindings sources from the Git repository :
-  in the python directory, launch

`` python setup.py build``

The module will be built in build/lib.linux-i686-2.5

-  install the module through (as root)

`` python setup.py install``

or simply copy the vlc.so file to some appropriate directory.

Windows
~~~~~~~

-  Get and install a nighty-built package from http://nightlies.videolan.org/build/windows/
-  Get and extract the corresponding sources from http://nightlies.videolan.org/build/source/
-  Create a .libs subdirectory in vlc/src
-  Copy the libvlc.dll file from c:\Program Files\VideoLAN\VLC into src/.libs
-  Go into the vlc/bindings/python directory and run

`` python setup.py build --compiler=mingw32``

You should get a vlc.pyd (or vlc.dll) file in the build/ subdirectory.

Basics
------

The vlc python module provides 4 main classes : MediaControl, Instance, MediaPlayer and Media.

**vlc.MediaControl** implements the `MediaControlAPI <MediaControlAPI>`__. Methods taking positions as parameters expect a **vlc.Position** object, that provides a very flexible way to address absolute or relative positions, in a number of units (milliseconds, frames or bytes). For convenience, the python binding automatically converts integer positions into milliseconds **vlc.Position** objects.

**vlc.Instance**, **vlc.MediaPlayer** and **vlc.Media** match the new `LibVLC <LibVLC>`__ API. Refer (for now) to the docstrings provided by the python objects to get their usage.

Tips and tricks
---------------

Building notes
~~~~~~~~~~~~~~

-  on 0.8.6(a), the --enable-mediacontrol-python-bindings option is not compatible with --enable-libtool. If you need libtool support, please use the svn version.

Python specificities
~~~~~~~~~~~~~~~~~~~~

The python bindings provide a binding for the `MediaControlAPI <MediaControlAPI>`__, with some variations :

-  the methods taking a *vlc.Position* parameter also accept an integer, which will then be converted to a relative position in milliseconds (vlc.MediaTime)
-  the start, stop, pause and resume method position parameter is optional. If omitted, it will default to a 0-relative position.
-  RGBPicture (returned by snapshot) and StreamInformation (returned by get_stream_information) are not objects with attributes, but instead dictionaries.

Snapshot support
~~~~~~~~~~~~~~~~

In the current svn revision, we use the core snapshot functionality of vlc, which is simpler to setup (no additional module, see below) and directly returns PNG, but less precise.

Prior to revision 13881, in order to get snapshot support, you had to activate the snapshot vout module through a clone video filter. The following code gives a way to achieve this :

`` mc=vlc.MediaControl("--vout-filter clone --clone-vout-list default,snapshot --snapshot-width 320 --snapshot-height 200".split())``

Advantages of the old (filter-based) approach:

-  the snapshot vout module holds a cache of reduced-size snapshots, that allow to take into account the reaction time of the user (around 200ms) and also to precisely select the more appropriate snapshot from the cache.

Win32 initialization
~~~~~~~~~~~~~~~~~~~~

If the vlc module was not compiled with the exact same prefix as the VLC installation (e.g. c:\\Program Files\\Videolan), then it cannot find itself the installation directory (stored in the registry Software\VideoLAN\VLC\InstallDir), and the MediaControl instanciation will fail with a message like "Cannot find interface plugins".

The workaround consists in changing directory to the VLC installation directory before instanciating the MediaControl object, since VLC will look for its plugins in the current directory. Another way is to pass the correct --plugin-path option.

.. code:: python

       def get_registry_value (self, subkey, name):
           import _winreg
           value = None
           for hkey in _winreg.HKEY_LOCAL_MACHINE, _winreg.HKEY_CURRENT_USER:
               try:
                   reg = _winreg.OpenKey(hkey, subkey)
                   value, type_id = _winreg.QueryValueEx(reg, name)
                   _winreg.CloseKey(reg)
               except _winreg.error:
                   pass
           return value
       
       vlcpath=get_registry_value('Software\\VideoLAN\\VLC','InstallDir')
       if vlcpath is None:
           print "Cannot locate VLC installation directory"
       else:
           os.chdir(vlcpath)
           mc=vlc.MediaControl()

Source code
-----------

Formerly located at bindings/python/

`Category:Bindings <Category:Bindings>`__
