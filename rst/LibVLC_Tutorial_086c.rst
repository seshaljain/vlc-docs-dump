.. raw:: mediawiki

   {{Lowercase}}

.. raw:: mediawiki

   {{Historical}}

Tutorial for libVLC for version 0.8.6c
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tested on cygwin with gcc 3.4, windows xp; instructions also for linux with small code change. You will want to change the plugin path to where you actually have vlc installed. And you will want to change the video filename to one which actually exists on your system. This will initialize vlc and play the video for ten seconds. After you get this to work, then you will want to look up the external API documentation to see how to use the other interfaces. Note there are two interfaces documented in the external API page; the first one is the "old" legacy one using calls such as ``VLC_Init``. The second one is the "current" one using calls such as ``libvlc_new``, which is used in the following code.

Code
~~~~

.. code:: c

    #include <stdio.h>
    #include <windows.h>
    #include <vlc/libvlc.h>
    
    static void quit_on_exception (libvlc_exception_t *excp) {
       if (libvlc_exception_raised (excp)) {
          fprintf(stderr, "error: %s\n", libvlc_exception_get_message(excp));
          exit(-1);
       }
    }
    
    int main(int argc, char **argv) {
       libvlc_exception_t excp;
       libvlc_instance_t *inst;
       int item;
       char *myarg0 = "-I";  char *myarg1 = "dummy";
       char *myarg2 = "--plugin-path=c:\\program files\\videolan\\plugins";
       char *myargs[4] = {myarg0, myarg1, myarg2, NULL};
       char *filename = "c:\\video\\main\\Everybody_Hates_Chris_Feb_26.mpg";
    
       libvlc_exception_init (&excp);
       inst = libvlc_new (3, myargs, &excp);
       quit_on_exception (&excp);
       item = libvlc_playlist_add (inst, filename, NULL, &excp); 
       quit_on_exception (&excp);
       libvlc_playlist_play (inst, item, 0, NULL, &excp); 
       quit_on_exception (&excp);
       Sleep (10000);
       libvlc_destroy (inst);
       return 0;
    }

Compile/link
~~~~~~~~~~~~

You can use `libVLC <libVLC>`__ without compiling your own copy of the VLC source code. You can use the libvlc.dll which comes in the standard end user installation. But, to access the include files, you will need to download and extract the source code. You only need to untar it; you do not even need to run the configure script. Set your ``%PATH%`` to include the directory which contains libvlc.dll and the plugins directory. For example, add ``"C:\Program files\VideoLAN\VLC"`` in a relatively standard installation. This way the compiler can find libvlc.dll. Otherwise you have to copy the dll to your current directory. Use the following Makefile:

.. code:: winbatch

    VLC_INST = "C:\Program files\VideoLAN\VLC"
    VLC_SRC = "C:\tools\vlc-0.8.6c\"
    demo: demo.c
       gcc -o demo demo.c -I$(VLC_SRC)/include \
       -L$(VLC_INST) -llibvlc

Code for Linux
~~~~~~~~~~~~~~

.. code:: c

    #include <stdio.h>
    #include <stdlib.h>
    #include <vlc/libvlc.h>
    
    static void quit_on_exception (libvlc_exception_t *excp) {
       if (libvlc_exception_raised (excp)) {
          fprintf(stderr, "error: %s\n", libvlc_exception_get_message(excp));
          exit(-1);
       }
    }
    
    int main(int argc, char **argv) {
       libvlc_exception_t excp;
       libvlc_instance_t *inst;
       int item;
       char *filename = "/tmp/WorldOfPadman_Intro.avi";
    
       libvlc_exception_init (&excp);
       inst = libvlc_new (argc, argv, &excp);
       quit_on_exception (&excp);
       item = libvlc_playlist_add (inst, filename, NULL, &excp); 
       quit_on_exception (&excp);
       libvlc_playlist_play (inst, item, 0, NULL, &excp); 
       quit_on_exception (&excp);
       usleep (10000000);
       libvlc_destroy (inst);
       return 0;
    }

See `1 <http://files.filefront.com/WorldOfPadman+Introavi/;6089800;/fileinfo.html>`__ for *WorldOfPadman_Intro.avi*. (You can, of course, substitute any video you like.)

Compile/Link/Run for Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ export VLC_SRC=/tmp/vlc-0.8.6c
    $ gcc -I ${VLC_SRC}/include/ -lvlc -L ${VLC_SRC}/src/.libs/ demo.c -o demo
    $ export LD_LIBRARY_PATH=${VLC_SRC}/src/.libs/ 
    $ ./demo --plugin-path ${VLC_SRC}

`Category:libVLC <Category:libVLC>`__
