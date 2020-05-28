{{Back to|Hacker Guide}} This page lists the directories in the
[https://git.videolan.org/?p=vlc.git;a=tree source tree of VLC] to give
an overview of the code. Because VLC has evolved with not so much
accumulation in mind, when a new coder looks at the code, s/he is
terrified by the abundance of directories. This page was prepared to
remedy that situation.

The directories are listed in alphabetical order, with an overview of
their contents on the right. {\| class="wikitable"

-Java, CIL and Python bindings {{VLCSourceFolder for required libraries
(contains Makefiles to automatically download and compile (or
cross-compile) and patch those). Please first attempt to get the
development headers precompiled for your distribution.
{{VLCSourceFolderDocumentation (not up-to-date) {{VLCSourceFolder
''[[#Contents_of_extras-include}} -lib}} -m4}} - modules}} -po}} -
Projects based on libvlc, Mozilla plugin, ActiveX plugin and [[Mac OS X
Framework]] {{VLCSourceFoldericons, scripts to make VLC the default
player etc. {{VLCSourceFolderThe most important directory besides
modules/. ''See [[{{#rel2abs:/src}}-test}} \|scripts to see if
everything is OK

\|}

== Contents of extras == {\| class="wikitable" \| {{VLCSourceFolder
contains some code style editor (vim, emacs) macro and some valgrind
suppressions {{VLCSourceFolder contains alternative buildsystems
extras/deprecated \| contains deprecated files {{VLCSourceFolder
contains files that don't fit into any other category {{VLCSourceFolder
contains distribution specific files such as ipkg, different rpm spec
files, win32 and Mac OS X installation files. }

{{Hacker Guide}} [[Category:Building]]
