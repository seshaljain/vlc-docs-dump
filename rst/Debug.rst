When compiling , you can compile a debug binary using ``--enable-debug`` on the ./configure script.

Those debug facts are common to every programs, not only VLC.

What it is used for
-------------------

Of course, the binary compiled in debug mode will or should behave like the release one (more or less). Differences are

-  developers can cause VLC to crash when it reached a suspicious state for development purpose, while release version will not in the same suspicious state
-  binary backtraces are meaningful in this mode since symbols are embedded in it.

So its main usage is for developers to use debug-friendly binaries and to reproduce a crash and get its backtrace.

How to enable it
----------------

As said above, you basically just have to add ``CFLAGS="-g" CXXFLAGS="-g" --enable-debug`` parameters at the `./configure <configure>`__ stage.

For stepping into code, better is to do ``CFLAGS="-g -Og" CXXFLAGS="-g -Og"`` also add ``--disable-optimizations`` and not use ``--enable-release``. Replace ``-Og`` with ``-O0`` to prevent compiler from optimizing out variables. For more information see `VLC configure help <VLC_configure_help>`__.

Backtraces
----------

A backtrace is a snapshot of a process at the time it is about to crash.

What does it look like?
~~~~~~~~~~~~~~~~~~~~~~~

Here is a debug-friendly backtrace:

| *``Program``\ ````\ ``received``\ ````\ ``signal``\ ````\ ``SIGSEGV,``\ ````\ ``Segmentation``\ ````\ ``fault.``*
| *``[Switching``\ ````\ ``to``\ ````\ ``Thread``\ ````\ ``0xb22e9b90``\ ````\ ``(LWP``\ ````\ ``17982)]``*
| *``0xb7a965e8``\ ````\ ``in``\ ````\ ``CDDAFormatTitle``\ ````\ ``(p_access=0x842afe0,``\ ````\ ``i_track=99``\ ````\ ``'c')``\ ````\ ``at``\ ````\ ``info.c:630``*
| *``630``\ ````\ ``info.c:``\ ````\ ``No``\ ````\ ``such``\ ````\ ``file``\ ````\ ``or``\ ````\ ``directory.``*
| ``''        in info.c''``
| *``(gdb)``\ ````\ ``bt``\ ````\ ``full``*
| ``#0  0xb7a965e8 in CDDAFormatTitle (p_access=0x842afe0, i_track=99 'c') at``
| ``info.c:630``
| ``        psz_name = ``\ 
| ``        config_varname = ``\ 
| ``        p_cdda = ``\ 
| ``        psz_mrl = 0x8277238 "cddax:///dev/sr0@T99"``
| ``#1  0xb7a94b0f in CDDAReadBlocks (p_access=0x842afe0) at access.c:264``
| ``        psz_title = ``\ 
| ``        go_on = ``\ 
| ``        p_block = ``\ 
| ``        p_cdda = (cdda_data_t *) 0x84323c0``
| ``        i_blocks = 20``
| ``        __func__ = "CDDAReadBlocks"``
| ``[...]``
| ``#6  0xb6acfe9c in Demux (p_demux=0x833dcb0) at ../../include/vlc_stream.h:189``
| ``        p_sys = (demux_sys_t *) 0x842eca8``
| ``        i_pos = ``\ 
| ``        p_block = (block_t *) 0x859f380``
| ``#7  0xb7f34bae in MainLoop (p_input=0x8429c08) at input/input.c:538``
| ``        b_force_update = 0``
| ``        i_ret = ``\ 
| ``        i_type = 138588128``
| ``        val = {i_int = 1064861644, b_b..........= 0 '\0', h = 0 '\0'}}``
| ``        i_intf_update = 1214500117823853``
| ``#8  0xb7f362b2 in Run (p_input=0x8429c08) at input/input.c:444``
| ``No locals.``
| ``#9  0xb7e7917b in start_thread () from /lib/libpthread.so.0``
| ``No symbol table info available.``
| ``#10 0xb7ddb09e in clone () from /lib/libc.so.6``
| ``No symbol table info available.``

And here is a not debug-friendly backtrace, unuseful in fact.

| *``Program``\ ````\ ``received``\ ````\ ``signal``\ ````\ ``SIGSEGV,``\ ````\ ``Segmentation``\ ````\ ``fault.``*
| *``[Switching``\ ````\ ``to``\ ````\ ``Thread``\ ````\ ``-1342661712``\ ````\ ``(LWP``\ ````\ ``8792)]``*
| *``0xb7db65ab``\ ````\ ``in``\ ````\ ``__module_Need``\ ````\ ``()``\ ````\ ``from``\ ````\ ``/usr/lib/libvlc.so.0``*
| *``(gdb)``\ ````\ ``bt``*
| ``#0  0xb7db65ab in __module_Need () from /usr/lib/libvlc.so.0``
| ``#1  0xb7ec5c34 in ?? () from /usr/lib/libvlc.so.0``
| ``#2  0xb5487553 in ?? ()``
| ``   from /usr/lib/vlc/stream_out/libstream_out_transcode_plugin.so``
| ``#3  0x00000009 in ?? ()``
| ``#4  0xb7ec3c74 in ?? () from /usr/lib/libvlc.so.0``
| ``#5  0x0854bef8 in ?? ()``
| ``#6  0x08525a00 in ?? ()``
| ``#7  0xb7efaf04 in ?? () from /usr/lib/libvlc.so.0``
| ``#8  0xb7dce493 in __vlc_object_release () from /usr/lib/libvlc.so.0``
| ``#9  0x0000006f in ?? ()``
| ``#10 0x00000003 in ?? ()``
| ``#11 0x00000000 in ?? ()``

As you can see, developers can't cope with last backtrace.

Is a backtrace enough to debug?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It is not enough for someone else than you to fix a bug. At least, you really should describe what you were doing, how to reproduce the bug if you can, etc.

If you try to fix a bug with someone else or if you are asking help on your backtrace, better is really to use an up-to-date VLC source-code. Otherwise, say so and maybe give the commit ID/VLC tag you are working on.

See also
--------

-  `Report Bugs <Report_Bugs>`__
-  `Tutorial for GDB with Win32 <Tutorial_for_gdb_debug_under_Win32>`__

`Category:Building <Category:Building>`__ `Category:Coding <Category:Coding>`__
