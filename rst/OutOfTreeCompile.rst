This page outlines setting up a module for building outside of the main VLC source tree. See also `how to write a module <Hacker_Guide/How_To_Write_a_Module>`__.

Source code
-----------

There are a few differences that need to be taken into account when writing a module out-of-tree:

-  **MODULE_STRING must be defined** manually. In-tree, the VLC build system would take care of it.
-  The static import compatibility library (compat/libcompat.la) is not available. Thus some standard functions might be unavailable on old or sub-standard platforms.
-  **<config.h> is not available**. Thus the usual HAVE_\* and CAN_\* macros are not defined.
-  The gettext functional macros N_(), \_(), vlc_pgettext() and gettext_noop() are not defined automatically.
-  Some (few) parts of the VLC core API are unavailable: some <vlc_*.h> files cannot be used out-of-tree.

Internationalization
~~~~~~~~~~~~~~~~~~~~

The VLC build system cannot scan out-of-tree source code for text to be translated. If you want gettext translations, you need to setup gettext in the build system and maintain the PO files.

However, the VLC core is able to load your module text domain into the process automatically. This is required for the plugins cache to operate correctly. You simply need to add one "set_text_domain" line in the module descriptor, e.g.:

.. code:: c

   #define DOMAIN  "vlc-myplugin"
   #define _(str)  dgettext(DOMAIN, str)
   #define N_(str) (str)

   /* ... */

   vlc_module_begin()
      set_text_domain (DOMAIN)
      set_description (N_("My plugin"))
      /* ... */
   vlc_module_end()

You might find it hard to maintain this, and choose to ignore internationalization altogether.

Symbols
~~~~~~~

External VLC modules are run-time libraries. They need to expose some predefined symbols (functions). They all start with the prefix "vlc_entry_". In principles, the vlc_module_begin() macro ensures that those function are exported, so you should not worry about this. But then again, that depends on how your build system and build-time linker are set up.

Installing the development files
--------------------------------

The VLC header files, the pkg-config files, and the import libraries for the target platform are required.

For native builds on Debian/Ubuntu and derivatives, you can simply install them:

``{{$}} sudo apt-get install libvlc-dev gcc make``

On Windows, you can find those files within the vlc-*-win*.7z file, inside the sdk/ directory.

Building
--------

Note that the following examples assume that the VLC development package is installed and configured correctly. In particular, these commands should work (results may vary though):

| ``{{$}} pkg-config --modversion vlc-plugin``
| ``1.1.13``

| ``{{$}} pkg-config --cflags vlc-plugin``
| ``-D__PLUGIN__ -D_FILE_OFFSET_BITS=64 -D__USE_UNIX98 -D_REENTRANT -D_THREAD_SAFE -I/usr/include/vlc/plugins  ``

| ``{{$}} pkg-config --libs vlc-plugin``
| ``-lvlccore  ``

If cross-compiling, you will most certainly need to adjust the pkg-config-related environment variables. By default pkg-config assumes native build, and will use the native VLC development files (if present) or fail (if not present). Please refer to the pkg-config manual page for details.

Makefile
~~~~~~~~

This is an example plain makefile (using GNU/make syntax) for Linux/BSD/Solaris:

.. code:: make

   PREFIX = /usr/local
   LD = ld
   CC = cc
   PKG_CONFIG = pkg-config
   INSTALL = install
   CFLAGS = -g -O2 -Wall -Wextra
   LDFLAGS =
   LIBS =
   VLC_PLUGIN_CFLAGS := $(shell $(PKG_CONFIG) --cflags vlc-plugin)
   VLC_PLUGIN_LIBS := $(shell $(PKG_CONFIG) --libs vlc-plugin)

   libdir = $(PREFIX)/lib
   plugindir = $(libdir)/vlc/plugins

   override CC += -std=gnu99
   override CPPFLAGS += -DPIC -I. -Isrc
   override CFLAGS += -fPIC
   override LDFLAGS += -Wl,-no-undefined,-z,defs

   override CPPFLAGS += -DMODULE_STRING=\"foo\"
   override CFLAGS += $(VLC_PLUGIN_CFLAGS)
   override LIBS += $(VLC_PLUGIN_LIBS)

   TARGETS = libfoo_plugin.so

   all: libfoo_plugin.so

   install: all
           mkdir -p -- $(DESTDIR)$(plugindir)/misc
           $(INSTALL) --mode 0755 libfoo_plugin.so $(DESTDIR)$(plugindir)/misc

   install-strip:
           $(MAKE) install INSTALL="$(INSTALL) -s"

   uninstall:
           rm -f $(plugindir)/misc/libfoo_plugin.so

   clean:
           rm -f -- libfoo_plugin.so src/*.o

   mostlyclean: clean

   SOURCES = foo.c bar.c

   $(SOURCES:%.c=src/%.o): %: src/foo.h

   libfoo_plugin.so: $(SOURCES:%.c=src/%.o)
           $(CC) $(LDFLAGS) -shared -o $@ $^ $(LIBS)

   .PHONY: all install install-strip uninstall clean mostlyclean

To cross-compile, you will need to override the CC, LD and possibly PKG_CONFIG, and other variables at the top to point to the adequate cross-toolchain. For the sake of simplicity, the Makefile above uses filenames for ELF-based operating systems; you may need to tweak it in other cases.

with GNU/autotools
~~~~~~~~~~~~~~~~~~

If using GNU/automake and GNU/libtool, you can follow this instead:

configure.ac
^^^^^^^^^^^^

.. code:: autoconf

   # ...

   AC_PROG_CC_C99
   AM_PROG_CC_C_O
   AM_PROG_LIBTOOL
   PKG_PROG_PKG_CONFIG()

   # ...

   PKG_CHECK_MODULES(VLC_PLUGIN, [vlc-plugin >= 1.1.0])

Makefile.am
^^^^^^^^^^^

.. code:: make

   vlclibdir = $(libdir)/vlc

   vlclib_libfoo_plugin_la_SOURCES = src/foo.c src/foo.h src/bar.c
   vlclib_libfoo_plugin_la_CFLAGS = $(VLC_PLUGIN_CFLAGS) \
         -DMODULE_STRING=\"foo\"
   vlclib_libfoo_plugin_la_LIBADD = $(VLC_PLUGIN_LIBS)
   vlclib_libfoo_plugin_la_LDFLAGS = \
         -avoid-version -module -export-symbol-regex ^vlc_entry

`Category:Building <Category:Building>`__
