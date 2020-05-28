.. raw:: mediawiki

   {{Back to|Hacker Guide}}

LibVLC is based on many independent modules, like most competing multimedia frameworks. Each module provides specific functionality.

This article focuses on adding a new module (a.k.a. plug-in) to VLC (or any other LibVLC application). You **will need to read** `VLC Core and Modules <{{#rel2abs:../Core#VLC_Pipeline_and_Modularity}}>`__ and `How VLC loads modules <Documentation:VLC_Modules_Loading>`__ first, otherwise you will not be able to flesh out the content of your new module.

In-tree and out-of-tree modules
-------------------------------

Most existing VLC modules are provided as source code in the directory `modules <{{#rel2abs:../Modules_source_tree}}>`__ within the main VLC source code repository (and also the source tarballs). They are compiled at the same time as the VLC core, and usually provided distributed together with VLC binary packages and installers. These modules are called in-tree modules.

However, it is also possible to write and compile VLC modules outside of VLC. That has some pros and cons over developing modules in-tree:

Pros
~~~~

-  Compilation is a lot faster (VLC and other modules are not included in the process).
-  You can use your own version control system, or even none at all.
-  The copyright license does not need to abide by the requirements of the `VideoLAN <VideoLAN>`__ association for inclusion in VLC.
-  The source code does not need to be provided, reviewed and accepted by the VLC developers.
-  The release schedule is independent of VLC releases. New versions of the module can be published at any time regardless of VLC release planning.
-  Different programming languages can be used at least in theory. (The main VLC code base only uses C, C++ and Lua, and on MacOS Objective C.)
-  The module can use software libraries that would be inadequate for VLC to depend on.

Cons
~~~~

-  The VLC developers will not review the code, which would be a good opportunity to improve the code quality.
-  VLC translators will not take care of localization for the module(s) where applicable. VLC is translated in many tens of languages.
-  The module(s) cannot be distributed through the `videolan.org <http://www.videolan.org/>`__ website and use the VideoLAN infrastructure such as the bug tracker and the build bots.
-  The module(s) will only work with the particular VLC (major) version that it has been compiled for. For instance, a module compiled for VLC 1.1.x will not work with VLC 1.0.x or VLC 2.0.x.
-  The module(s) will only work on the particular operating systems and architecture that it has been compiled for. For instance, a Windows 32-bit module will only work with Windows 32-bit versions of VLC. VLC supports many different combinations of operating systems and architectures.

Example stub module
-------------------

Let's start with a small example module in the C language:

.. code:: c

   /**
    * @file hello.c
    * @brief Hello world interface VLC module example
    */
   #ifdef HAVE_CONFIG_H
   # include "config.h"
   #endif

   #include <stdlib.h>
   /* VLC core API headers */
   #include <vlc_common.h>
   #include <vlc_plugin.h>
   #include <vlc_interface.h>

   /* Internal state for an instance of the module */
   struct intf_sys_t
   {
       char *who;
   };

   /**
    * Starts our example interface.
    */
   static int Open(vlc_object_t *obj)
   {
       intf_thread_t *intf = (intf_thread_t *)obj;

       /* Allocate internal state */
       intf_sys_t *sys = malloc(sizeof (*sys));
       if (unlikely(sys == NULL))
           return VLC_ENOMEM;
       intf->p_sys = sys;

       /* Read settings */
       char *who = var_InheritString(intf, "hello-who");
       if (who == NULL)
       {
           msg_Err(intf, "Nobody to say hello to!");
           goto error;
       }
       sys->who = who;

       msg_Info(intf, "Hello %s!", who);
       return VLC_SUCCESS;

   error:
       free(sys);
       return VLC_EGENERIC;    
   }

   /**
    * Stops the interface. 
    */
   static void Close(vlc_object_t *obj)
   {
       intf_thread_t *intf = (intf_thread_t *)obj;
       intf_sys_t *sys = intf->p_sys;

       msg_Info(intf, "Good bye %s!", sys->who);

       /* Free internal state */
       free(sys->who);
       free(sys);
   }

   /* Module descriptor */
   vlc_module_begin()
       set_shortname(N_("Hello"))
       set_description(N_("Hello interface"))
       set_capability("interface", 0)
       set_callbacks(Open, Close)
       set_category(CAT_INTERFACE)
       add_string("hello-who", "world", "Target", "Whom to say hello to.", false)
   vlc_module_end ()

And now some explanations about the code...

Module Descriptor
~~~~~~~~~~~~~~~~~

A module **must** include a *description* of itself, and the *parameters* it accepts.

The module descriptor begins with:

.. code:: c

   vlc_module_begin()

You should set some basic information about your module. This is for the dvdread module:

.. code:: c

       set_shortname(N_("DVD without menus"))
       set_description(N_("DVDRead Input"))
       set_category(CAT_INPUT)
       set_subcategory(SUBCAT_INPUT_ACCESS)

*Note* the use of N_("") to create a string that needs to be translated by gettext.

Capability and score
^^^^^^^^^^^^^^^^^^^^

Definition **Example**:

.. code:: c

      set_capability("interface", 0)

This defines a module of "interface" capability and a score of 0.

The capability determines the type of module we are dealing with. It could be an access, a demux, a decoder, an interface, etc. Now is the time to **re-read**\ `how VLC loads modules <Documentation:VLC_Modules_Loading#How>`__.

-  If VLC needs to load a specific name, it will load it by its name and VLC directly opens this module
-  If VLC needs a type of module ("I need a decoder"), VLC will load all modules matching this capability in a decreasing score order until one modules's Open() function (see later) returns VLC_SUCCESS.

See the major types of `capabilities of VLC <Documentation:VLC_Modules_Loading#Capabilities>`__.

**Score** should be an integer, and related to other scores in the same category. Score 0 is a `special case <Documentation:VLC_Modules_Loading#Score_of_0>`__.

Configuration categories and sub-categories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You should use **one** of the **predefined categories** for configuration. The configuration categories and sub-categories specify **where** the module will appear in the **preferences** UI dialog.

The configuration categories include:

-  CAT_INTERFACE
-  CAT_AUDIO
-  CAT_VIDEO
-  CAT_INPUT
-  CAT_SOUT
-  CAT_ADVANCED
-  CAT_PLAYLIST

You should use one of **predefined sub-categories** as well. See for definition of all configuration categories and sub-categories.

Configuration parameters
^^^^^^^^^^^^^^^^^^^^^^^^

You may need options to configure the run-time behavior of your module. Defining new options is easy.

All option definitions take the following argument list:

.. code:: c

    add_integer(name, value, text, longtext, advanced) 

-  **name** is the string that identifies this parameter in the configuration. This name is used at the command prompt to set the configuration value.
-  **value** is the default value for this parameter,
-  **text** A short description of the parameter, use \_("") to create a string that needs to be translated,
-  **longtext** A complete description of the parameter, use \_("") to create a string that needs to be translated,
-  **advanced** Boolean, ADVanced Configuration. If TRUE, this parameter will only be displayed when using the --advanced flag.

| 
| You may add the following options/parameter types to your module:

-  add_integer,
-  add_string,
-  add_float,
-  add_bool,
-  add_key,
-  add_file,
-  add_directory,

For complete definitions, see

Callback
^^^^^^^^

The activation and deactivation functions, detailed afterwards, must be defined in the descriptor. This is so that the VLC core knows how to instantiate and run the module.

The set_callbacks() macro allows you to define 2 parameters: the first parameter is the pf_activate callback, and the second one, pf_deactivate. The functions are most often called "Open" and "Close" respectively, though. VLC invokes the pf_activate callback if/when it needs a plugin instance providing the correct interface, as declared with the set_capability() macro.

Conversely, VLC invokes the pf_deactivate callback when the plugin is no longer needed - but only if the pf_activate callback returned VLC_SUCCESS (0) earlier.

Open(vlc_object_t \*)
~~~~~~~~~~~~~~~~~~~~~

The most important function of a module is the opening: the usually-named Open() function.

.. code:: c

   static int  Open ( vlc_object_t * );

The Open() function is called when the VLC core tries to open the module, and wants to load it.

During Open(), setup of structures, devices or I/O, checks should be done. A successful open should return VLC_SUCCESS. If the module cannot complete its initialization, it can return any other value, usually VLC_EGENERIC or VLC_ENOMEM.

The **Open()** function is expected to allocate private data (if any), and set up the private structure.

If the Opening fails, you may need to free any already allocated resources before returning. Otherwise, leaks will occur.

Close(vlc_object_t \*)
~~~~~~~~~~~~~~~~~~~~~~

The second most important function of a module is the closing: the usually-named Close() function.

.. code:: c

   static int  Close ( vlc_object_t * );

The Close() function is called when the VLC core tries to close or unload an **already-loaded** module.

**NB:** If the Open() function failed, Close() will not get called.

During Close(), closing devices or I/O, and cleaning of structures should be done. Do not leak memory here!

The **Close()** function should deallocate private data.

In-tree module integration
--------------------------

Git
~~~

If you plan to submit your work to VLC upstream, be sure to look at `the git introduction <Git>`__ and check the `send patches part <Git#Submitting_patches>`__.

Compiling your module
~~~~~~~~~~~~~~~~~~~~~

Modules.am
^^^^^^^^^^

First, find the right subdirectory under `modules/ <{{#rel2abs:../Modules_source_tree}}>`__ to add your new code.

#. If the module has only one source code file module, simply add it in the subdirectory (e.g. modules/control/hello.c).
#. Larger modules should get a sub-subdirectory of their own (e.g. modules/control/hello/*).

Then you need to declare the module in the build system. For example, the file tells the build system which source files are needed for each control module. For the example above, we could add these lines:

.. code:: c

   libhello_plugin_la_SOURCES = hello.c
   libhello_plugin_la_CFLAGS = $(AM_CFLAGS)
   libhello_plugin_la_LIBADD = $(AM_LIBADD)
   libhello_plugin_la_DEPENDENCIES =
   # Always compile the hello module:
   libvlc_LTLIBRARIES += libhello_plugin.la

Note that indentation in Modules.am (if needed) uses tabulations (ASCII 0x09), not white spaces.

configure.ac
^^^^^^^^^^^^

If the module depends on some new library, some architecture or some operating system characteristics, you may need to extend configure.ac to detect when and how to build the module. Refer to the configure.ac file and the `GNU autoconf documentation <http://www.gnu.org/software/autoconf/manual/index.html>`__ for details.

Once this is done, you should only need to rebuild VLC:

.. code:: bash

    make

(This will probably trigger a re-run of autoconf and automake, so it might take a while.)

Loading your module
~~~~~~~~~~~~~~~~~~~

VLC keeps a cache of available modules for performance reasons. It should be updated automatically. But you can use *./vlc --reset-plugins-cache* to force a reset.

Then use

.. code:: bash

    ./vlc -vv --color --list

to check that your plugin is seen by .

You should also see it in the plugins dialog of the `Qt interface <Qt_interface>`__ (Linux and Windows).

Out-of-tree module
------------------

There is a dedicated article. Please read `out of tree compilation <OutOfTreeCompile>`__.

Sub-modules
-----------

Sub-modules, declared in some module descriptors with

.. code:: c

    add_submodule()

work exactly the same way as modules. They are useful when different modules (usually but not necessarily of different capability) share common code. All sub-modules will be included in the same run-time library as the main module.

Module types
------------

Depending on the module capability, you will need more information, about the necessary functions to implement.

We will detail those here:

-  `Access <{{#rel2abs:../Access}}>`__
-  `Demux <{{#rel2abs:../Demux}}>`__
-  `Access_Demux <{{#rel2abs:../Access_Demux}}>`__
-  `Decoder <{{#rel2abs:../Decoder}}>`__
-  `Interface <{{#rel2abs:../Interfaces}}>`__
-  `Video filter <{{#rel2abs:../Video_Filters}}>`__
-  `Video output <{{#rel2abs:../Video_Output}}>`__
-  `Audio filter <{{#rel2abs:../Audio_Filters}}>`__
-  `Audio output <{{#rel2abs:../Audio_Output}}>`__

Module load troubleshooting
---------------------------

Sometimes when building an in-tree module, stuff doesn't work due to build system problems and other inconsistencies.

You probably need to go to the root of your VLC source tree, and do something akin to the following. The examples here assume the *bash* shell.

**Mild version**
~~~~~~~~~~~~~~~~

In some cases, automake dependencies break (for instance after some filenames have changed). This might then work:

.. code:: bash

    find . -name .deps -exec rm -rf \{\} \;
    ./config.status
    make

...but not always, so it may save some headaches to always use the "medium version" below.

**Medium version** (try this first)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a more radical but still safe rebuild procedure:

.. code:: bash

    find . -name .deps -exec rm -rf \{\} \;
    ./bootstrap
    ./configure
    make

**Extreme version**
~~~~~~~~~~~~~~~~~~~

If the none of the above helped, you can clean the source tree as a measure of last resort. Before you proceed, it is highly recommended that you check which files are going to be erased:

.. code:: bash

    git clean -nxd

And then check what source code changes you would lose (if any):

.. code:: bash

    git diff

You can extremely easily lose entire days of hard work with the following commands. The first command will permanently remove any files not tracked in `git <git>`__, including files that you might have created yourself. The second command will remove any uncommitted modification to existing files. Consider yourself warned.

**!!!BEWARE: THIS MAY CAUSE UNRECOVERABLE DATA LOSS!!!**

.. code:: bash

    git clean -fxd
    git reset --hard HEAD
    ./bootstrap
    ./configure
    make

.. raw:: mediawiki

   {{Documentation}}

`Category:Coding <Category:Coding>`__ `Category:Hacker Guide <Category:Hacker_Guide>`__
