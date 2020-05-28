{{Back to|Hacker Guide}} ==VLC Interface==

===A typical VLC run course===

This section describes what happens when you launch the vlc program.
After the ELF dynamic loader blah blah blah, the main thread becomes the
interface thread. It passes through the following steps:

# CPU detection: which CPU are we running on, what are its capabilities
(MMX, MMXEXT, 3DNow, AltiVec...) ? # Message interface initialization #
Command line options parsing # Playlist creation # Module bank
initialization # Interface opening # Signal handler installation:
<code>SIGHUP</code>, <code>SIGINT</code> and <code>SIGQUIT</code> are
caught to manage a clean quit (please note that the SDL library also
catches <code>SIGSEGV</code>) # Audio output thread spawning # Video
output thread spawning # Main loop: events management

The following sections describe each of these steps in particular, and
many more.

===The message interface===

It is a known fact that <code>printf()</code> functions are not
necessarily thread-safe. As a result, one thread interrupted in a
<code>printf()</code> call, followed by another call to it, will leave
the program in an undetermined state. So an {{API}} must be set up to
print messages without crashing.

This API is implemented in two ways. If <var>INTF_MSG_QUEUE</var> is
defined in <code>config.h</code>, every printf-like (see below) call
will queue the message into a chained list. This list will be printed
and flushed by the interface thread once upon an event loop. If
<var>INTF_MSG_QUEUE</var> is undefined, the calling thread will acquire
the print lock (which prevents two print operations to occur at the same
time) and print the message directly (default behaviour).

Functions available to print messages are:

; <code>msg_Info ( p_this, ... )</code> : Print a message to stdout,
plain and stupid (for instance "it works!"). ; <code>msg_Err( p_this,
... )</code> : Print an error message to stderr. ; <code>msg_Warn(
p_this, ... )</code> : Print a message to stderr if the warning level
(determined by <code>-v</code>, <code>-vv</code> and <code>-vvv</code>)
is low enough. ''Please note that the lower the level, the less
important the message is.'' ; <code>msg_Dbg( p_this, ... )</code> : This
function is designed for optional checkpoint messages, such as "we are
now entering function dvd_foo_thingy". It does nothing in non-trace
mode. If VLC is compiled with <code>--enable-trace</code> (and
<var>TRACE_LOG</var> is defined in <code>config.h</code>), the message
will be written to the file <code>vlc-trace.log</code>; else the message
will be printed on stderr. ; <code>msg_Flush(p_this)</code> : Flush the
message queue, if it is in use.

===Command line options===

VLC uses GNU getopt to parse command line options. getopt structures are
defined in {{VLCSourceFilesrc/config/cmdline.c}}.

Most configuration directives are exchanged via the environment array,
using <code>main_Put*Variable</code> and <code>main_Get*Variable</code>.
As a result, <code>./vlc --height 240</code> is strictly equivalent to:
<code>vlc_height=240 ./vlc</code>. That way configuration variables are
available everywhere, including plugins.

====Warning==== Please note that for thread-safety issues, you should
not use <code>main_Put*Variable</code> once the second thread has been
spawned.

===Playlist management=== The playlist is created on startup from files
given on the command line. An appropriate interface plugin can then add
or remove files from it. Functions to be used are described in
{{VLCSourceFile|src/playlist/control.c}}.

How to write a plugin is described in the latter sections. Other threads can request a plugin descriptor with:
   module_Need ( module_bank_t \* p_bank, int i_capabilities, void \*
   p_data )

<code>p_data</code> is an optional parameter (reserved for future use)
for the <code>pf_probe()</code> function. The returned
<code>module_t</code> structure contains pointers to the functions of
the plug-in.<br /> See {{VLCSourceFile|include/vlc_modules.h}} for more
information.

===The interface main loop===

The interface thread will first look for a suitable interface plugin.
Then it enters the main interface loop, with the plugin's <code>pf_run
function</code>. This function will do what's appropriate, and every 100
ms will call (typically via a GUI timer callback)
<code>InteractionManage</code>.

InteractionManage cleans up the module bank by unloading unnecessary
modules, manages the playlist, and flushes waiting messages (if the
message queue is in use).

===How to write an interface module=== ====API for the Module==== Have a
look at the files in directories {{VLCSourceFoldermodules/access}}, or
{{VLCSourceFoldermodules/control/hotkeys.c}}.

An interface module is made of 3 entry functions and a module
description:

The module description is made of macros that declares the capabilities
of the module (interface, in this case) with their priority, the module
description as it will appear in the preferences of GUI modules that
implement them, some configuration variables specific to the module,
shortcuts, sub-modules, etc.

; <code>Open ( vlc_object_t\* p_object )</code> : This is called by VLC
to initialize the module. ; <code>Run ( vlc_object_t\* p_object )</code>
: Really does the job of the interface module (waiting for user input
and displaying info). It should check periodically that
<code>p_intf->b_die</code> is not <code>VLC_TRUE</code>. ; <code>Close (
vcl_object_t \* p_object )</code> : This function is called by VLC to
uninitialize the module (basically, this consists in destroying whatever
have been allocated by Open)

The above functions take a <code>vlc_object_t*</code> as argument, but
that may need to be cast into a <code>intf_thread_t*</code> depending on
your needs. This structure is often needed as a parameter for exported
VLC functions, such as <code>msg_Err()</code>, <code>msg_Warn()</code>,
...

Define <code>intf_sys_t</code> to contain any variable you need (don't
use static variables, they suck in a multi-threaded application <span
title="smile">:-)</span>.

If additional capabilities (such as Open button, playlist, menus, etc.)
are needed, consult one of the GUI modules. One of the simpler GUI
modules to consult might be {{VLCSourceFile|modules/gui/ncurses.c}}. It
is a quite simple complete interface module with playlist interaction,
and progress bar, among other things.

{{Hacker Guide}}

[[Category:Interfaces|*]]
