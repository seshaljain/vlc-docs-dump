{{Back to|Hacker Guide}} == Description ==

The modules of ''''access_demux'''' capability are designed to handle
the [[{{#rel2abs:../Access}}demux]] stage in the same module.

Therefore, you are '''required''' to read
[[{{#rel2abs:../Access}}demux]] pages before going on.

An access-demuxer could be seen as a demuxer that handles the access at
the same time.

In an access-demuxer, the stream s is null.

Examples of access-demuxer are DVD, Bluray, v4l2 modules.

== Write an access-demux module ==

To write an access_demuxer module, start by reading the
[[{{#rel2abs:../How To Write a Module}}|introduction to module
writing]].

Then, you should specify your module of being of access_demux type:

   set_capability( "access_demux", 60 ) set_category( CAT_INPUT )
   set_subcategory( SUBCAT_INPUT_ACCESS )

== Functions to implement ==

After implementing Open() and Close() functions, you will need to
implement a few majors features that will be implemented by your
functions.

As you can see in [[{{#rel2abs:../Demux}}|demux]], you should define:

*Demux, as in pf_demux*\ Control, as in pf_control ''' NB:''' please
refer to [[{{#rel2abs:../Demux#Control}}|demux Control documentation]]

After implementing those functions, you should assign them to the
corresponding `pf <>`__ function.

See {{VLCSourceFileinclude/vlc_access.h}}

== Demux ==

Demux in access_demux is a bit different than in a demux module, because
all the seeking and access of the stream is internal to the module.

''Prototype'':

   int (*pf_demux) ( demux_t* );

''Return'':

It should return 0 for EOF, something positive when success and
something negative when fail to demux.

{{Hacker_Guide}}
