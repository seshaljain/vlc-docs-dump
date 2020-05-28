.. raw:: mediawiki

   {{Back to|Hacker Guide}}

VLC Interface
-------------

A typical VLC run course
~~~~~~~~~~~~~~~~~~~~~~~~

This section describes what happens when you launch the vlc program. After the ELF dynamic loader blah blah blah, the main thread becomes the interface thread. It passes through the following steps:

#. CPU detection: which CPU are we running on, what are its capabilities (MMX, MMXEXT, 3DNow, AltiVec...) ?
#. Message interface initialization
#. Command line options parsing
#. Playlist creation
#. Module bank initialization
#. Interface opening
#. Signal handler installation: ``SIGHUP``, ``SIGINT`` and ``SIGQUIT`` are caught to manage a clean quit (please note that the SDL library also catches ``SIGSEGV``)
#. Audio output thread spawning
#. Video output thread spawning
#. Main loop: events management

The following sections describe each of these steps in particular, and many more.

The message interface
~~~~~~~~~~~~~~~~~~~~~

It is a known fact that ``printf()`` functions are not necessarily thread-safe. As a result, one thread interrupted in a ``printf()`` call, followed by another call to it, will leave the program in an undetermined state. So an must be set up to print messages without crashing.

This API is implemented in two ways. If INTF_MSG_QUEUE is defined in ``config.h``, every printf-like (see below) call will queue the message into a chained list. This list will be printed and flushed by the interface thread once upon an event loop. If INTF_MSG_QUEUE is undefined, the calling thread will acquire the print lock (which prevents two print operations to occur at the same time) and print the message directly (default behaviour).

Functions available to print messages are:

``msg_Info ( p_this, ... )``
   Print a message to stdout, plain and stupid (for instance "it works!").
``msg_Err( p_this, ... )``
   Print an error message to stderr.
``msg_Warn( p_this, ... )``
   Print a message to stderr if the warning level (determined by ``-v``, ``-vv`` and ``-vvv``) is low enough. *Please note that the lower the level, the less important the message is.*
``msg_Dbg( p_this, ... )``
   This function is designed for optional checkpoint messages, such as "we are now entering function dvd_foo_thingy". It does nothing in non-trace mode. If VLC is compiled with ``--enable-trace`` (and TRACE_LOG is defined in ``config.h``), the message will be written to the file ``vlc-trace.log``; else the message will be printed on stderr.
``msg_Flush(p_this)``
   Flush the message queue, if it is in use.

Command line options
~~~~~~~~~~~~~~~~~~~~

VLC uses GNU getopt to parse command line options. getopt structures are defined in and command line parsing is done in .

Most configuration directives are exchanged via the environment array, using ``main_Put*Variable`` and ``main_Get*Variable``. As a result, ``./vlc --height 240`` is strictly equivalent to: ``vlc_height=240 ./vlc``. That way configuration variables are available everywhere, including plugins.

Warning
^^^^^^^

Please note that for thread-safety issues, you should not use ``main_Put*Variable`` once the second thread has been spawned.

Playlist management
~~~~~~~~~~~~~~~~~~~

The playlist is created on startup from files given on the command line. An appropriate interface plugin can then add or remove files from it. Functions to be used are described in .

How to write a plugin is described in the latter sections. Other threads can request a plugin descriptor with:

``module_Need ( module_bank_t * p_bank, int i_capabilities, void * p_data )``

| ``p_data`` is an optional parameter (reserved for future use) for the ``pf_probe()`` function. The returned ``module_t`` structure contains pointers to the functions of the plug-in.
| See for more information.

The interface main loop
~~~~~~~~~~~~~~~~~~~~~~~

The interface thread will first look for a suitable interface plugin. Then it enters the main interface loop, with the plugin's ``pf_run function``. This function will do what's appropriate, and every 100 ms will call (typically via a GUI timer callback) ``InteractionManage``.

InteractionManage cleans up the module bank by unloading unnecessary modules, manages the playlist, and flushes waiting messages (if the message queue is in use).

How to write an interface module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

API for the Module
^^^^^^^^^^^^^^^^^^

Have a look at the files in directories , , or . However the GUIs are not very easy to understand, since they are quite big. I suggest to start digging into a non-graphical interface modules first. For example .

An interface module is made of 3 entry functions and a module description:

The module description is made of macros that declares the capabilities of the module (interface, in this case) with their priority, the module description as it will appear in the preferences of GUI modules that implement them, some configuration variables specific to the module, shortcuts, sub-modules, etc.

``Open ( vlc_object_t* p_object )``
   This is called by VLC to initialize the module.
``Run ( vlc_object_t* p_object )``
   Really does the job of the interface module (waiting for user input and displaying info). It should check periodically that ``p_intf->b_die`` is not ``VLC_TRUE``.
``Close ( vcl_object_t * p_object )``
   This function is called by VLC to uninitialize the module (basically, this consists in destroying whatever have been allocated by Open)

The above functions take a ``vlc_object_t*`` as argument, but that may need to be cast into a ``intf_thread_t*`` depending on your needs. This structure is often needed as a parameter for exported VLC functions, such as ``msg_Err()``, ``msg_Warn()``, ...

Define ``intf_sys_t`` to contain any variable you need (don't use static variables, they suck in a multi-threaded application :-).

If additional capabilities (such as Open button, playlist, menus, etc.) are needed, consult one of the GUI modules. One of the simpler GUI modules to consult might be . It is a quite simple complete interface module with playlist interaction, and progress bar, among other things.

.. raw:: mediawiki

   {{Hacker Guide}}

`\* <Category:Interfaces>`__
