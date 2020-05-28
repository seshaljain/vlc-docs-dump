{{Back to|Hacker Guide}} LibVLC is based on many independent modules,
like most competing multimedia frameworks. Each module provides specific
functionality.

This article focuses on adding a new module (a.k.a. plug-in) to VLC (or
any other LibVLC application). You '''will need to read'''
[[{{#rel2abs:../Core#VLC_Pipeline_and_Modularity}}How VLC loads
modules]] first, otherwise you will not be able to flesh out the content
of your new module.

== In-tree and out-of-tree modules ==

Most existing VLC modules are provided as source code in the directory
[[{{#rel2abs:../Modules source tree}}|modules]] within the main VLC
source code repository (and also the source tarballs). They are compiled
at the same time as the VLC core, and usually provided distributed
together with VLC binary packages and installers. These modules are
called in-tree modules.

However, it is also possible to write and compile VLC modules outside of
VLC. That has some pros and cons over developing modules in-tree:
===Pros=== \* Compilation is a lot faster (VLC and other modules are not
included in the process). \* You can use your own version control
system, or even none at all. \* The copyright license does not need to
abide by the requirements of the [[VideoLAN]] association for inclusion
in VLC. \* The source code does not need to be provided, reviewed and
accepted by the VLC developers. \* The release schedule is independent
of VLC releases. New versions of the module can be published at any time
regardless of VLC release planning. \* Different programming languages
can be used at least in theory. (The main VLC code base only uses C, C++
and Lua, and on MacOS Objective C.) \* The module can use software
libraries that would be inadequate for VLC to depend on.

===Cons=== \* The VLC developers will not review the code, which would
be a good opportunity to improve the code quality. \* VLC translators
will not take care of localization for the module(s) where applicable.
VLC is translated in many tens of languages. \* The module(s) cannot be
distributed through the [http://www.videolan.org/ videolan.org] website
and use the VideoLAN infrastructure such as the bug tracker and the
build bots. \* The module(s) will only work with the particular VLC
(major) version that it has been compiled for. For instance, a module
compiled for VLC 1.1.x will not work with VLC 1.0.x or VLC 2.0.x. \* The
module(s) will only work on the particular operating systems and
architecture that it has been compiled for. For instance, a Windows
32-bit module will only work with Windows 32-bit versions of VLC. VLC
supports many different combinations of operating systems and
architectures.

== Example stub module ==

Let's start with a small example module in the C language:
<syntaxhighlight lang="c">/*\* \* @file hello.c \* @brief Hello world
interface VLC module example \*/ #ifdef HAVE_CONFIG_H # include
"config.h" #endif

#include <stdlib.h> /\* VLC core API headers \*/ #include <vlc_common.h>
#include <vlc_plugin.h> #include <vlc_interface.h>

/\* Internal state for an instance of the module */ struct intf_sys_t {
char*\ who; };

/*\*
   \* Starts our example interface. \*/

static int Open(vlc_object_t *obj) { intf_thread_t*\ intf =
(intf_thread_t \*)obj;

   /\* Allocate internal state */ intf_sys_t*\ sys = malloc(sizeof
   (*sys)); if (unlikely(sys == NULL)) return VLC_ENOMEM; intf->p_sys =
   sys;

   /\* Read settings */ char*\ who = var_InheritString(intf,
   "hello-who"); if (who == NULL) { msg_Err(intf, "Nobody to say hello
   to!"); goto error; } sys->who = who;

   msg_Info(intf, "Hello %s!", who); return VLC_SUCCESS;

error:
   free(sys); return VLC_EGENERIC;

}

/*\*
   \* Stops the interface. \*/

static void Close(vlc_object_t *obj) { intf_thread_t*\ intf =
(intf_thread_t *)obj; intf_sys_t*\ sys = intf->p_sys;

   msg_Info(intf, "Good bye %s!", sys->who);

   /\* Free internal state \*/ free(sys->who); free(sys);

}

/\* Module descriptor \*/ vlc_module_begin()
set_shortname(\ `N <>`__\ ("Hello")) set_description(\ `N <>`__\ ("Hello
interface")) set_capability("interface", 0) set_callbacks(Open, Close)
set_category(CAT_INTERFACE) add_string("hello-who", "world", "Target",
"Whom to say hello to.", false) vlc_module_end () </syntaxhighlight>

And now some explanations about the code...

=== Module Descriptor ===

A {{VLC}} module '''must''' include a ''description'' of itself, and the
''parameters'' it accepts.

The module descriptor begins with: <syntaxhighlight
lang="c">vlc_module_begin() </syntaxhighlight> You should set some basic
information about your module. This is for the dvdread module:
<syntaxhighlight lang="c"> set_shortname(\ `N <>`__\ ("DVD without
menus")) set_description(\ `N <>`__\ ("DVDRead Input"))
set_category(CAT_INPUT) set_subcategory(SUBCAT_INPUT_ACCESS)
</syntaxhighlight> ''Note'' the use of `N <>`__\ ("") to create a string
that needs to be translated by gettext.

==== Capability and score ====

Definition '''Example''': <syntaxhighlight lang="c">
set_capability("interface", 0) </syntaxhighlight> This defines a module
of "interface" capability and a score of 0.

The capability determines the type of module we are dealing with. It
could be an access, a demux, a decoder, an interface, etc. Now is the
time to '''re-read [[Documentation:VLC Modules Loading#How|how VLC loads
modules]]'''.

*If VLC needs to load a specific name, it will load it by its name and
VLC directly opens this module*\ If VLC needs a type of module ("I need
a decoder"), VLC will load all modules matching this capability in a
decreasing score order until one modules's Open() function (see later)
returns VLC_SUCCESS.

See the major types of [[Documentation:VLC Modules
Loading#Capabilities|capabilities of VLC]].

'''Score''' should be an integer, and related to other scores in the
same category. Score 0 is a [[Documentation:VLC Modules
Loading#Score_of_0|special case]].

==== Configuration categories and sub-categories ====

You should use '''one''' of the '''predefined categories''' for
configuration. The configuration categories and sub-categories specify
'''where''' the module will appear in the '''preferences''' UI dialog.

The configuration categories include: *CAT_INTERFACE*\ CAT_AUDIO
*CAT_VIDEO*\ CAT_INPUT *CAT_SOUT*\ CAT_ADVANCED \*CAT_PLAYLIST

You should use one of '''predefined sub-categories''' as well. See
{{VLCSourceFile|include/vlc_configuration.h}} for definition of all
configuration categories and sub-categories.

==== Configuration parameters ====

You may need options to configure the run-time behavior of your module.
Defining new options is easy.

All option definitions take the following argument list:
<syntaxhighlight lang="c"> add_integer(name, value, text, longtext,
advanced) </syntaxhighlight> *'''name''' is the string that identifies
this parameter in the configuration. This name is used at the command
prompt to set the configuration value.*'''value''' is the default value
for this parameter, *'''text''' A short description of the parameter,
use \_("") to create a string that needs to be
translated,*'''longtext''' A complete description of the parameter, use
\_("") to create a string that needs to be translated, \*'''advanced'''
Boolean, ADVanced Configuration. If TRUE, this parameter will only be
displayed when using the --advanced flag.

<br> You may add the following options/parameter types to your module:
*add_integer,*\ add_string, *add_float,*\ add_bool,
*add_key,*\ add_file, \*add_directory,

For complete definitions, see {{VLCSourceFile|include/vlc_plugin.h}}

==== Callback ====

The activation and deactivation functions, detailed afterwards, must be
defined in the descriptor. This is so that the VLC core knows how to
instantiate and run the module.

The set_callbacks() macro allows you to define 2 parameters: the first
parameter is the pf_activate callback, and the second one,
pf_deactivate. The functions are most often called "Open" and "Close"
respectively, though. VLC invokes the pf_activate callback if/when it
needs a plugin instance providing the correct interface, as declared
with the set_capability() macro.

Conversely, VLC invokes the pf_deactivate callback when the plugin is no
longer needed - but only if the pf_activate callback returned
VLC_SUCCESS (0) earlier.

=== Open(vlc_object_t \*) ===

The most important function of a module is the opening: the
usually-named Open() function. <syntaxhighlight lang="c">static int Open
( vlc_object_t \* );</syntaxhighlight> The Open() function is called
when the VLC core tries to open the module, and wants to load it.

During Open(), setup of structures, devices or I/O, checks should be
done. A successful open should return VLC_SUCCESS. If the module cannot
complete its initialization, it can return any other value, usually
VLC_EGENERIC or VLC_ENOMEM.

The '''Open()''' function is expected to allocate private data (if any),
and set up the private structure.

If the Opening fails, you may need to free any already allocated
resources before returning. Otherwise, leaks will occur.

=== Close(vlc_object_t *) === The second most important function of a
module is the closing: the usually-named Close() function.
<syntaxhighlight lang="c">static int Close ( vlc_object_t*
);</syntaxhighlight>

The Close() function is called when the VLC core tries to close or
unload an '''already-loaded''' module.

'''NB:''' If the Open() function failed, Close() will not get called.

During Close(), closing devices or I/O, and cleaning of structures
should be done. Do not leak memory here!

The '''Close()''' function should deallocate private data.

== In-tree module integration ==

=== Git === If you plan to submit your work to VLC upstream, be sure to
look at [[Git send patches part]].

=== Compiling your module ===

==== Modules.am ==== First, find the right subdirectory under
[[{{#rel2abs:../Modules_source_tree}}\| modules/]] to add your new code.

# If the module has only one source code file module, simply add it in
the subdirectory (e.g. modules/control/hello.c). # Larger modules should
get a sub-subdirectory of their own (e.g. modules/control/hello/*).

Then you need to declare the module in the build system. For example,
the file {{VLCSourceFile|modules/control/Modules.am}} tells the build
system which source files are needed for each control module. For the
example above, we could add these lines:

<syntaxhighlight lang="c"> libhello_plugin_la_SOURCES = hello.c
libhello_plugin_la_CFLAGS = $(AM_CFLAGS) libhello_plugin_la_LIBADD =
$(AM_LIBADD) libhello_plugin_la_DEPENDENCIES = # Always compile the
hello module: libvlc_LTLIBRARIES += libhello_plugin.la
</syntaxhighlight>

Note that indentation in Modules.am (if needed) uses tabulations (ASCII
0x09), not white spaces.

==== configure.ac ====

If the module depends on some new library, some architecture or some
operating system characteristics, you may need to extend configure.ac to
detect when and how to build the module. Refer to the configure.ac file
and the [http://www.gnu.org/software/autoconf/manual/index.html GNU
autoconf documentation] for details.

Once this is done, you should only need to rebuild VLC: <syntaxhighlight
lang="bash"> make </syntaxhighlight> (This will probably trigger a
re-run of autoconf and automake, so it might take a while.)

=== Loading your module ===

VLC keeps a cache of available modules for performance reasons. It
should be updated automatically. But you can use ''./vlc
--reset-plugins-cache'' to force a reset.

Then use <syntaxhighlight lang="bash"> ./vlc -vv --color --list
</syntaxhighlight> to check that your plugin is seen by {{VLC}}.

You should also see it in the plugins dialog of the [[Qt interface]]
(Linux and Windows).

== Out-of-tree module ==

There is a dedicated article. Please read [[OutOfTreeCompile|out of tree
compilation]].

== Sub-modules ==

Sub-modules, declared in some module descriptors with

<syntaxhighlight lang="c">
   add_submodule()

</syntaxhighlight>

work exactly the same way as modules. They are useful when different
modules (usually but not necessarily of different capability) share
common code. All sub-modules will be included in the same run-time
library as the main module.

== Module types ==

Depending on the module capability, you will need more information,
about the necessary functions to implement.

We will detail those here: \* [[{{#rel2abs:../Access}}Demux]] \*
[[{{#rel2abs:../Access_Demux}}Decoder]] \*
[[{{#rel2abs:../Interfaces}}Video filter]] \*
[[{{#rel2abs:../Video_Output}}Audio filter]] \*
[[{{#rel2abs:../Audio_Output}}|Audio output]]

== Module load troubleshooting ==

Sometimes when building an in-tree module, stuff doesn't work due to
build system problems and other inconsistencies.

You probably need to go to the root of your VLC source tree, and do
something akin to the following. The examples here assume the ''bash''
shell.

==='''Mild version'''===

In some cases, automake dependencies break (for instance after some
filenames have changed). This might then work:

<syntaxhighlight lang="bash">
   find . -name .deps -exec rm -rf {} ; ./config.status make

</syntaxhighlight>

...but not always, so it may save some headaches to always use the
"medium version" below.

==='''Medium version''' (try this first)===

This is a more radical but still safe rebuild procedure:

<syntaxhighlight lang="bash">
   find . -name .deps -exec rm -rf {} ; ./bootstrap ./configure make

</syntaxhighlight>

==='''Extreme version'''===

If the none of the above helped, you can clean the source tree as a
measure of last resort. Before you proceed, it is highly recommended
that you check which files are going to be erased: <syntaxhighlight
lang="bash"> git clean -nxd </syntaxhighlight> And then check what
source code changes you would lose (if any): <syntaxhighlight
lang="bash"> git diff </syntaxhighlight> You can extremely easily lose
entire days of hard work with the following commands. The first command
will permanently remove any files not tracked in [[git]], including
files that you might have created yourself. The second command will
remove any uncommitted modification to existing files. Consider yourself
warned.

'''!!!BEWARE: THIS MAY CAUSE UNRECOVERABLE DATA LOSS!!!'''

<syntaxhighlight lang="bash">
   git clean -fxd git reset --hard HEAD ./bootstrap ./configure make

</syntaxhighlight>

{{Documentation}} [[Category:Coding]] [[Category:Hacker Guide]]
