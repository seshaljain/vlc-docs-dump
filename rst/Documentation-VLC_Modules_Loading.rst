{{Back to|Hacker Guide}} '''VLC modules loading'''

== <span id="How"></span> How does VLC load modules? ==

=== <span id="Introduction"></span> Introduction about Modules ===

VLC has a core and a lot of modules (between 200 and 400 depending on
the build).

VLC cannot do much without modules, since modules are providing most of
the functionalities we expect. See the [[#Capabilities|Major
Capabilities]] sections.

A VLC module has 2 ''major'' ''properties'':

*the capability, VLC_MODULE_CAPABILITY, that describes the category of
the module*\ the score, VLC_MODULE_SCORE, that holds the priority of the
module

=== <span id="Process"></span> How does the loading of modules happen
===

The first time you load VLC, it will scan the default '''plugins'''
directories that should contain VLC modules and generate a cache (named
the '''plugins cache''') so that the modules can be loaded quickly the
next time VLC launches. Modules can be organized into directories (up to
5 layers deep) beneath the '''plugins''' directory.

Recent versions of VLC require that the modules follow a specific naming
convention or they will not be loaded. Modules must be named in the
following format: '''lib''module_name''_plugin.''ext''''' where
''module_name'' should be the name of your module in lower case, and
''ext'' is the system's shared library extension. For example, the
'''http''' access module is named '''libaccess_http_plugin.dll''' on a
Windows machine.

When VLC needs a module, it tries to open the module with the highest
score that has the required capability and accepts the request.

Let's do an '''example'''.

When VLC needs a "decoder" ("decoder" is one category/capability), it
opens all "decoder" modules, until one matches.

It opens them in decreasing score order (biggest score first, smaller
ones at the end), and runs the Open() function of the modules. When one
module returns OK, VLC uses this module.

=== <span id="Advanced"></span> Advanced info about modules loading ===

==== Score of 0 ====

If a module has a score of 0, it needs to be explicitly requested by the
user or vlc (like forcing --codec, --vout or
<code>module_need("foo")</code>) to be loaded.<br>

==== all, none and other special tweaks ====

\*The '''"all"''' mode means all modules will be tested in decreasing
order of score.

\*The '''"none"''' mode means no modules will be tested.

\*Any module can be requested by using its direct shortname. This is
useful for 0-scored modules.

==== Examples ====

Modules requests can be chained, as the '''examples''' show:

   --codec avcodec,all ''try the avcodec module than all modules as a
   "decoder"''

   --demux avformat,none '' try the avformat module and no other
   module''

By default, modules requests are in the '''"all"''' mode, and "all" can
be omitted.

=== How to list Modules ===

\*Using Console

   vlc --list

\*Using the Qt GUI

   Menu → Tools → Plugins and extensions

== <span id="Capabilities"></span> Major Capabilities of Modules ==

; <code>audio filter</code> : An audio filter, like an equalizer ;
<code>audio mixer</code> : An audio channel mixer, like a downmixer ;
<code>audio output</code> : An audio output, like Windows DirectX audio
output ; <code>decoder</code> : A codec decoder, like theora ;
<code>demux</code> : A demuxer, to open a file format, like mkv ;
<code>encoder</code> : A codec encoder, like x264 ;
<code>interface</code> : An interface, like the Qt interface ;
<code>meta reader</code> : A meta reader, to read metadata ;
<code>packetizer</code> : A packetizer ; <code>playlist export</code> :
A module to write playlist, like .m3u ; <code>services_discovery</code>
: A module to get extra content from your computer or the network, like
Upnp, DLNA ; <code>sout access</code> : An access for the streaming ;
<code>sout mux</code> : A muxer when streaming and encoding ;
<code>stream_filter</code> : A stream filter ; <code>text
renderer</code> : A way to display subtitles and other text on top of
the video ; <code>video filter</code> : A video filter, like contrast
adjusting ; <code>visualization2</code> : A visualizer, to create videos
from the music ; <code>vout display</code> : A video output, to display
videos like Direct3D or Xv

{{Documentation}}
