{{Back to|Hacker Guide}} == Description ==

The modules of ''''demux'''' capability are designed to handle the
different "file" formats, like [[AVI]] or [[MKV]]. They usually come
after the [[{{#rel2abs:../Access}}|Access]] module in the modules chain,
and create the different tracks, that are sent to the decoders.

The '''demuxer''' modules are working on the ''input stream'' that is
provided by the core input to them. It splits the input stream into the
different tracks (called ''elementary streams'').

Technically, the demuxers are '''pulling data''' from the stream; data
is not pushed by the access to the demux.

Examples of demuxers are [[ASF|WMV/ASF]], [[Ogg]] or [[Mkv]].

== Write an demuxer module ==

To write an demuxer module, start by reading the [[{{#rel2abs:../How To
Write a Module}}|introduction to module writing]].

Then, you should specify your module of being of demux type:

   set_capability( "demux", 60 ) set_category( CAT_INPUT )
   set_subcategory( SUBCAT_INPUT_DEMUX )

== Functions to implement ==

After implementing Open() and Close() functions, you will need to
implement a few majors features that will be implemented by your
functions.

As you can see {{VLCSourceFile|include/vlc_demux.h}}, you should define:

*Demux, as in pf_demux*\ Control, as in pf_control

After implementing those functions, you should assign them to the
corresponding `pf <>`__ function.<br>

=== Demux ===

''Prototype'':

   int (*pf_demux) ( demux_t* );

Demux function is quite easy, it pulls data from '''s*''' the pointer to
the stream_t.

''Return'':

It should return 0 for EOF, something positive when success and
something negative when fail to demux.

=== Control ===

''Prototype'':

   int (*pf_control)( access_t*, int i_query, va_list args);

Control function is quite easy, the input core will query the module
using this function with:

*A pointer to the module structure.*\ An '''i_query''' parameter that
can be of several type. We will cover afterward the most important on.
\*A list of arguments, that depends on the '''i_query''' type.

''Return'':

If the query has succeeded, it should return VLC_SUCCESS. Else it should
return VLC_EGENERIC (''fail'').

==== Control Query types ====

See {{VLCSourceFile|include/vlc_demux.h}}<br>

== Useful primitives and types ==

When implementing a demux, you will need to work on a '''stream'''
(''stream_t''), but also to create and control '''tracks''' (ES)
(''es_out_id_t'').

''stream_t *'' is the input (multiplexed) byte stream.<br />
''es_out_id_t*'' are the elementary streams, to hand to the decoder.

=== Tracks / ES manipulation ===

Tracks in VLC are named '''ES''', as ''Elementary Streams''

You will probably need

*es_out_Add*\ es_out_Send \*es_out_Control

See {{VLCSourceFileinclude/vlc_es.h}}

=== Stream manipulation ===

Stream manipulation can be done with a few functions
*stream_Read*\ stream_Peek *stream_Control*\ stream_ReadLine
\*stream_Block

See {{VLCSourceFile|include/vlc_stream.h}} for more information

{{Hacker_Guide}}
