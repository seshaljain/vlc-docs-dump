{{Back to|Hacker Guide}} ==Introduction== VideoLAN Manager is a small
media manager designed to control multiple streams with only one
instance of VLC. It allows multiple streaming and video on demand (VoD).
VLM can be controlled through the telnet and http interfaces of VLC as
described in [[Documentation:Streaming_HowTo/VLM]].

This document will describe the internals of VLM including data
structures and functions, as well the the libvlc bindings for control of
vlm.

==vlm_t==

In a running instance of VLC or libvlc only 1 instance of VLM can be
running. This instance of VLM is represented by <code>'''struct
vlm_t'''</code> as defined in <tt>src/input/vlm_internal.h</tt>.
<code>vlm_t</code> contains a list of Medias, Schedules and vod servers,
as well as a lock for the data structure, and a unique id. In essence,
the <code>vlm_t</code> data structure is the global container for all
VLM related data.

==Medias and Instances==

A ''Media'' is composed with a list of inputs (the video and audio
streams you want to stream), an output (how and where you want to stream
them) and some options.

There are two types of medias: ; vod : A vod media is commonly used for
Video on Demand. It will be launched only if a vod client asks for it. ;
broadcast : A broadcast media is very close to a TV program or channel.
It is launched, stopped or paused by the administrator and may be
repeated several times. The client has no control over this media.

A media is represented by the structure
<code>'''vlm_media_sys_t'''</code> defined in
<tt>src/input/vlm_internal.h</tt>. Each <code>vlm_media_sys_t</code>
contains a configuration structure, a list of instances of the media, as
well as a structure representing a vod server which is initialized only
if the media is of type vod.

The configuration structure is of type <code>'''vlm_media_t'''</code> (a
misnomer due to historical reasons) and contains the name of the media,
as well as its type and a host of other details. It is defined in
<tt>src/input/vlm_internal.h</tt> also.

A media instance is represented by the structure
<code>'''vlm_media_instance_sys_t'''</code> defined in
<tt>src/input/vlm_internal.h</tt> also. This structure contains a
playlist index as well as the current input thread and output stream
instance. Mulitple media instances can exist for each media.

Each VOD server is represented by the struct <code>'''vod_t'''</code>.
This structure contains a pointer to the module that will be loaded to
help the vod server, as well as a pointer to an RTSP server. It also
contains several function pointers to help create and delete vod medias
of type <code>vod_media_t</code>. Each <code>vod_media_t</code> is
actually referenced by a <code>vlm_media_sys_t</code> if that media is
of vod type. <code>vod_t</code> is defined in <tt>include/vlc_vod.h</tt>
and <code>vod_media_t</code> is defined in <tt>modules/misc/rtsp.c</tt>.

The layout of the main vlm structures hierarchically looks like this:
<pre> vlm_t vlm_media_sys_t vlm_media_t vlm_media_instance_sys_t
vod_media_t vod_t </pre>

==Schedules==

==Initializing VLM and Adding Medias==

Since VLM is a part of libvlc, I will describe initialization of VLM
with respect to libvlc. If we want to use VLM we are probably going to
have at least one media. Therefore we can use the libvlc functions
<code>'''libvlc_vlm_add_broadcast()'''</code> or
<code>'''libvlc_vlm_add_vod()'''</code> to instantiate and initialize
VLM. Each one of these functions checks to see if a VLM instance exists.
If it does not, the function creates a <code>'''vlm_t'''</code> instance
and creates and adds either a broadcast or vod media to the
<code>'''vlm_t'''</code> instance. If the media is of type vod, then a
separate <code>'''vod_media_t'''</code> is created and linked to the
media of type <code>'''vlm_media_sys_t'''</code> and a vod server of
type <code>'''vod_t'''</code> is created and linked to the
<code>'''vlm_t'''</code> instance.

Note also, that the VLM instance is attached to the libvlc instance as a
singleton, therefore allowing only one VLM instance per libvlc instance.
Both <code>'''libvlc_vlm_add_broadcast()'''</code> and
<code>'''libvlc_vlm_add_vod()'''</code> wrap around the
<code>'''VLM()'''</code> macro which wraps around
<code>'''__vlm_New()'''</code> which actually does the instantiation,
initialization, and binding of the VLM instance to the libvlc instance.
These functions are found in the <tt>src/control/vlm.c</tt>.
<code>__vlm_New()</code> is found in <tt>src/input/vlm.c</tt>.

==Control==

Once VLM is initialized, there needs to be some way to control it, such
as adding medias, starting and stopping a media instance, etc... The
<code>'''vlm_Control()'''</code> function is used for this purpose. This
allows all VLM commands to be issued through one common interface, and
it takes care of locking issues. By executing
<code>'''vlm_Control()'''</code> with the proper command code, such as
<code>'''VLM_ADD_MEDIA'''</code>, and a variable argument list, any VLM
command can be executed without the need to understand the lower level
details. This allows for easily wrapping the VLM code to be used by many
interfaces. <code>'''vlm_Control()'''</code> can be found in
<tt>src/input/vlm.c</tt>. The list of VLM command codes can be found in
the enumerated type <code>'''vlm_query_e'''</code> in the file
<tt>include/vlc_vlm.h</tt>.

==Thread Creation==

VLM is a complex subsystem within VLC. When VLM is initialized, when a
media is created etc…, threads are created to handle these tasks. This
section will describe the thread model used by VLM.

When new instance of VLM is created by the <code>__vlm_New()</code>
function, a management thread is created which has as its start function
<code>Manage()</code> residing in <tt>src/input/vlm.c</tt>. This takes
care of scheduling, as well as destruction of dead input objects.

when a new vod media is added to VLM, an input thread is created with
<code>Run()</code> as its start function. This thread takes care of all
streaming for that media.

If a broadcast media is added, it needs to be played. When The libvlc
function <code>libvlc_vlm_play_media()</code> is called, an instance of
the broadcast media is created as well as an input thread with
<code>Run()</code> as its start function. This thread takes care of all
streaming for the broadcast instance by calling appropriate demux,
codec, and sout modules.

{{Hacker_Guide}}
