{{Back to|Hacker Guide}} ==Libvlc Startup==

===Introduction=== [[Libvlc]] represents the underlying {{API}} of
{{VLC}}. VLC itself is just a wrapper around libvlc. By utilizing libvlc
developers can take advantage of all the complex functionalities of vlc.
Libvlc is generated as a shared library and can be wrapped up with
numerous interfaces, including both Python and Java bindings. This
allows the end user to build applications around the vlc code base and
take advantage of all the plugins available to vlc instead of writing
everything from scratch.

This document will explain how to get started using libvlc. It will step
through the instantiation of a libvlc instance and explain the typical
startup procedure of libvlc.

===Libvlc Instantiation===

Libvlc is a singleton. For each application wrapped around libvlc, only
one libvlc instance should be running. In order to create an instance of
libvlc, you must call <code>libvlc_new()</code>. This function
initializes the thread system and allocates a libvlc instance.
<code>libvlc_new()</code> resides in
{{VLCSourceFile|src/config/core.c}}.

<code>libvlc_new()</code> calls <code>libvlc_InternalInit()</code> which
handles command line parsing, loads the module bank, and spawns a number
of threads to handle various vlc subsystems. The threads are spawned
from inside the function <code>playlist_ThreadCreate()</code>. Below is
a list of thread start functions that are run for playlist processing.
The threads corresponding to these functions are spawned in the order
listed.

-  <code>RunPreparse()</code> - Perform initial parsing of the playlist
-  <code>RunFetcher()</code> - load artwork associated with playlist
   item
-  <code>RunControlThread()</code> - perform playlist scheduling and
   playing

See [[{{#rel2abs:../Playlist}}|Playlist]] for more details.

{{Hacker_Guide}}

[[Category:libVLC|*]]
