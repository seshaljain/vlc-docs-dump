{{Back to|Hacker Guide}} == Description ==

The modules of ''''access'''' capability are designed to be the first
and last elements of a modules chain.

They take an [[MRL]] in, and output a bitstream, that can be fed to a
[[Demuxer]].

Access input and [[{{#rel2abs:../Access Output}}|output]] handles most
of the basic '''I/O''' for VLC. They are usually '''protocols'''
implementations (http, ftp,...) or '''devices''' access (Webcams,
Capture cards).

We will discuss about ''''input access'''' in this page.

== Write an access module ==

To write an access module, read first the [[{{#rel2abs:../How To Write a
Module}}|introduction to module writing]].

Then, you should specify your module of being of access type:
<syntaxhighlight lang="c"> set_capability( "access", 60 ) set_category(
CAT_INPUT ) set_subcategory( SUBCAT_INPUT_ACCESS ) </syntaxhighlight>

=== Type === Your module can be of either a ''''Block'''' or a
''''Read'''' type, depending on your medium:

-  if the underlying protocol '''returns data blocks of unknown or
   unpredictable size''', '''Block''' is a better type,
-  if you '''can control the size of the data requested''' to the
   underlying protocol, '''Read''' is a better type.

== Functions to implement ==

After implementing <code>Open()</code> and <code>Close()</code>
functions, you will need to implement a few major features that will be
implemented by your functions.

As you can see in
[https://www.videolan.org/developers/vlc/doc/doxygen/html/vlc__access_8h_source.html
include/vlc_access.h], you should define:

-  Seek, as in <code>pf_seek</code>,
-  Control, as in <code>pf_control</code>,
-  Read or Block, depending on your module [[#Type|type]].

After implementing those functions, you should assign them to the
corresponding <code>`pf <>`__\ </code> function.

=== Seek ===

''Prototype'': <syntaxhighlight lang="c"> int (*pf_seek) ( access_t*,
uint64_t ); </syntaxhighlight>

The seeking function will be called whenever a seek is requested.

The arguments are a ''pointer'' to the module structure, and the
requested '''position'''.

{{Note-nb|Seeking function can be <code>NULL</code>, if it isn't
possible to seek in the protocol or device.}}

You shall set <code>p_access->info.b_eof</code> to <code>false</code> if
seek worked.

''Return:''<br>

If the seek has succeeded, it should return <code>VLC_SUCCESS</code>,
else it should return <code>VLC_EGENERIC</code>. <br>

=== Control ===

''Prototype'': <syntaxhighlight lang="c"> int (*pf_control)( access_t*,
int i_query, va_list args); </syntaxhighlight>

Control function is quite easy, the input core will query the module
using this function with:

*A pointer to the module structure.*\ An '''i_query''' parameter that
can be of several type. We will cover afterward the most important on.
\*A list of arguments, that depends on the '''i_query''' type.

''Return'':

If the query has succeeded, it should return <code>VLC_SUCCESS</code>.
Else it should return <code>VLC_EGENERIC</code> (''fail'').

==== Control Query types ====

The first ones are request to know what the module supports. They are
all of '''[[boolean]]''' type and should always succeed.
<syntaxhighlight lang="c"> ACCESS_CAN_SEEK, ACCESS_CAN_FASTSEEK,
ACCESS_CAN_PAUSE, ACCESS_CAN_CONTROL_PACE, </syntaxhighlight>

<br> The following one is a request for the '''PTS delay'''. It must
always succeed. <syntaxhighlight lang="c"> ACCESS_GET_PTS_DELAY,
</syntaxhighlight>

<br> The following ones are for '''requesting''' various '''info'''
about the input, like Metadata, Titles and Chapters or device signal
strength. All of them can fail. <syntaxhighlight lang="c">
ACCESS_GET_TITLE_INFO, ACCESS_GET_META, ACCESS_GET_CONTENT_TYPE,
ACCESS_GET_SIGNAL, </syntaxhighlight>

<br> Depending to the answer of the <code>`CAN <>`__\ </code> requests,
the core can '''set''' a few things, like pausing or changing
'''title''' or '''chapter''' <syntaxhighlight lang="c">
ACCESS_SET_PAUSE_STATE, ACCESS_SET_TITLE, ACCESS_SET_SEEKPOINT,
</syntaxhighlight>

You can find the list of arguments corresponding to query types in the
comments of <code>access_query_e</code> definition in vlc_access.h

=== Read ===

''Prototype'': <syntaxhighlight lang="c"> ssize_t (*pf_read) (
access_t*, uint8_t \*, size_t ); </syntaxhighlight>

''Return'':

Return <code>-1</code> if no data yet, <code>0</code> if no more data,
else actual data read on the medium.

=== Block ===

''Prototype'': <syntaxhighlight lang="c"> block_t *(*\ pf_block)(
access_t \* ); </syntaxhighlight>

''Return:''

Returns a block of data in its 'natural' size. It will return
<code>NULL</code> if there is not yet data or end-of-file (eof) has been
reached.

To differentiate between ''no data'' and ''eof'', you shall set
<code>p_access->info.b_eof</code> to <code>true</code> in case of eof.

{{Hacker_Guide}}
