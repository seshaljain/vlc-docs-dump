.. raw:: mediawiki

   {{Lowercase}}

.. raw:: mediawiki

   {{Example code}}

libVLC C Tutorial
-----------------

Installing the SDK
~~~~~~~~~~~~~~~~~~

This code is written for `libVLC <libVLC>`__ version 1.1.0 or later. It **cannot** be compiled with older versions.

Older versions are found at `libVLC Tutorial 0.9 <libVLC_Tutorial_0.9>`__ and `libVLC Tutorial 086c <libVLC_Tutorial_086c>`__ respectively for historical interest only.

Windows
^^^^^^^

VLC binary installers for Windows do not include the libVLC . It would be a waste of bandwidth and space for most users.

You can find the SDK files, i.e. development headers and import libraries, from the plain 7-ZIP packages in the ``sdk`` directory. Alternatively, you can build VLC from source.

See `libVLC Tutorial 086c <libVLC_Tutorial_086c>`__ for some more instructions on getting the build working.

Linux
^^^^^

You should find the necessary files (libvlc.so, libvlc.pc, header files...) in a binary package called libvlc-dev (Debian, Ubuntu...), libvlc-devel (RPM distros) or similar. Make sure that the version is recent enough before going forward.

Linking against libVLC
~~~~~~~~~~~~~~~~~~~~~~

::

   cc example.c -lvlc -o example

On Linux/BSD, you may prefer to use pkg-config:

.. code:: bash

   pkg-config --print-errors 'libvlc >= 1.1.0'
   cc -c example.c -o example.o $(pkg-config --cflags libvlc)
   cc example.o -o example $(pkg-config --libs libvlc)

Sample libVLC code
~~~~~~~~~~~~~~~~~~

This sample code will (try to) play back an URL. There is also an `example using SDL for video output <libVLC_SampleCode_SDL>`__.

.. code:: c

    #include <stdio.h>
    #include <stdlib.h>
    #include <vlc/vlc.h>
    
    int main(int argc, char* argv[])
    {
        libvlc_instance_t * inst;
        libvlc_media_player_t *mp;
        libvlc_media_t *m;
        
        /* Load the VLC engine */
        inst = libvlc_new (0, NULL);
     
        /* Create a new item */
        m = libvlc_media_new_location (inst, "http://mycool.movie.com/test.mov");
        //m = libvlc_media_new_path (inst, "/path/to/test.mov");
           
        /* Create a media player playing environement */
        mp = libvlc_media_player_new_from_media (m);
        
        /* No need to keep the media now */
        libvlc_media_release (m);
    
    #if 0
        /* This is a non working code that show how to hooks into a window,
         * if we have a window around */
         libvlc_media_player_set_xwindow (mp, xid);
        /* or on windows */
         libvlc_media_player_set_hwnd (mp, hwnd);
        /* or on mac os */
         libvlc_media_player_set_nsobject (mp, view);
     #endif
    
        /* play the media_player */
        libvlc_media_player_play (mp);
       
        sleep (10); /* Let it play a bit */
       
        /* Stop playing */
        libvlc_media_player_stop (mp);
    
        /* Free the media_player */
        libvlc_media_player_release (mp);
    
        libvlc_release (inst);
    
        return 0;
    }

`Category:libVLC <Category:libVLC>`__
