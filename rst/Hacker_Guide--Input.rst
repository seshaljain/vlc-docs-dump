.. raw:: mediawiki

   {{Back to|Hacker Guide}}

The complex multi-layer input
-----------------------------

The idea behind the input module is to treat packets, without knowing at all what is in it. It only takes a packet, reads its ID, and delivers it to the decoder at the right time indicated in the packet header (SCR and PCR fields in MPEG). All the basic browsing operations are implemented without peeking at the content of the elementary stream.

Thus it remains very generic. This also means you can't do stuff like "play 3 frames now" or "move forward 10 frames" or "play as fast as you can but play all frames". It doesn't even know what a "frame" is. There is no privileged elementary stream, like the video one could be (for the simple reason that, according to MPEG, a stream may contain several video ).

What happens to a file
~~~~~~~~~~~~~~~~~~~~~~

An input thread is spawned for every file read. Indeed, input structures and decoders need to be reinitialized because the specificities of the stream may be different. ``input_CreateThread`` is called by the interface thread (playlist module).

At first, vlc looks for an access or ``access_demux`` module to open the stream, by calling the function ``module->pf_activate``. If it succeeds, the module thread is started, and vlc can start looking for a demux module to demultiplex the output of the access module.

Stream Management
~~~~~~~~~~~~~~~~~

The function which has opened the input socket must specify two properties about it:

p_input->stream.b_pace_control: Whether or not the stream can be read at our own pace (determined by the stream's frequency and the host computer's system clock). For instance a file or a pipe (including TCP/IP connections) can be read at our pace, if we don't read fast enough, the other end of the pipe will just block on a ``write()`` operation. On the contrary, UDP streaming (such as the one used by VideoLAN Server) is done at the server's pace, and if we don't read fast enough, packets will simply be lost when the kernel's buffer is full. So the drift introduced by the server's clock must be regularly compensated. This property controls the clock management, and whether or not fast forward and slow motion can be done.

Subtleties in the clock management: With a UDP socket and a distant server, the drift is not negligible because on a whole movie it can account for seconds if one of the clocks is slightly borked. That means that presentation dates given by the input thread may be out of sync, to some extent, with the frequencies given in every Elementary Stream. Output threads (and, anecdotally, decoder threads) must deal with it.

The same kind of problems may happen when reading from a device (like video4linux's ``/dev/video`` ) connected for instance to a video encoding board. There is no way we could differentiate it from a simple ``cat foo.mpg | vlc -``, which doesn't imply any clock problem. So the Right Thing™ would be to ask the user about the value of b_pace_control , but nobody would understand what it means (you are not the dumbest person on Earth, and obviously you have read this paragraph several times to understand it :-). Anyway, the drift should be negligible since the board would share the same clock as the CPU, so we chose to neglect it.

p_input->stream.b_seekable: Whether we can do ``lseek()`` calls on the file descriptor or not. Basically whether we can jump anywhere in the stream (and thus display a scrollbar) or if we can only read one byte after the other. This has less impact on the stream management than the previous item, but it is not redundant, because for instance ``cat foo.mpg | vlc -`` is \ ``b_pace_control``\ \ ``= 1`` but \ ``b_seekable``\ \ ``= 0``. On the contrary, you cannot have \ ``b_pace_control``\ \ ``= 0`` along with \ ``b_seekable``\ \ ``= 1``. If a stream is seekable, p_input->stream.p_selected_area->i_size must be set (in an arbitrary unit, for instance bytes, but it must be the same as p_input->i_tell which indicates the byte we are currently reading from the stream).

Offset to time conversions
^^^^^^^^^^^^^^^^^^^^^^^^^^

Functions managing clocks are located in . All we know about a file is its start offset and its end offset (p_input->stream.p_selected_area->i_size), currently in bytes, but it could be plugin-dependent. So how the hell can we display in the interface a time in seconds? Well, we cheat. `PS <PS>`__ streams have a mux_rate property which indicates how many bytes we should read in a second. This is subject to change at any time, but practically it is a constant for all streams we know. So we use it to determine time offsets.

Structures exported to the interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's focus on the communication between the input module and the interface. The most important files are , which defines the ``input_thread_t`` structure, for the stream descriptor structure (between access and demux) ``stream__t``, and for the ES descriptors (you can view it as a tree).

First, note that the ``input_thread_t`` structure features two ``void *`` pointers, ``p_method_data`` and ``p_plugin_data``, which you can respectively use for buffer management data and plugin data.

Second, a stream description is stored in a tree featuring program descriptors, which themselves contain several elementary stream descriptors. For those of you who don't know all MPEG concepts, an elementary stream (ES), is a continuous stream of video or (exclusive) audio data, directly readable by a decoder, without decapsulation.

This tree structure is illustrated by the following figure, where one stream holds two programs. In most cases there will only be one program (to my knowledge only streams can carry several programs, for instance a movie and a football game at the same time—this is adequate for satellite and cable broadcasting).

.. raw:: mediawiki

   {{Warning|
   For all modifications and accesses to the <code>p_input->stream structure</code>, you must hold the <code>p_input->stream.stream_lock</code>.

   ES are described by an ID (the ID the appropriate demultiplexer will look for), a <var>stream_id</var> (the real MPEG stream ID), a type (defined in ISO/IEC 13818-1 table 2-29) and a literal description. It also contains context information for the demultiplexer, and decoder information <code>p_decoder_fifo</code> we will talk about in the next chapter. If the stream you want to read is not an MPEG system layer (for instance AVI or RTP), a specific demultiplexer will have to be written. In that case, if you need to carry additional information, you can use <code>void * p_demux_data</code> at your convenience. It will be automatically freed on shutdown.
   }}

Why ID and not use the plain MPEG stream_id ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When a packet (be it a packet, `PS <PS>`__ packet, or whatever) is read, the appropriate demultiplexer will look for an ID in the packet, find the relevant elementary stream, and demultiplex it if the user selected it. In case of TS packets, the only information we have is the , so the reference ID we keep is the PID. PID don't exist in PS streams, so we have to invent one. It is of course based on the stream_id found in all PS packets, but it is not enough, since private streams (i.e., AC3, SPU and LPCM) all share the same stream_id (0xBD). In that case the first byte of the PES payload is a stream private ID, so we combine this with the stream_id to get our ID (if you did not understand everything, it isn't very important—just remember we used our brains before writing the code :-).

The stream, program and ES structures are filled in by the plugin's ``pf_init()`` using functions in , but are subject to change at any time. The DVD plugin parses .ifo files to know which ES are in the stream; the TS plugin reads the PAT and PMT structures in the stream; the PS plugin can either parse the PSM structure (but it is rarely present), or build the tree "on the fly" by pre-parsing the first megabyte of data.

.. raw:: mediawiki

   {{Warning|
   In most cases we need to pre-parse (that is, read the first MB of data, and go back to the beginning) a PS stream, because the PSM (Program Stream Map) structure is almost never present. This is not appropriate, though, but we don't have the choice. A few problems will arise. First, non-seekable streams cannot be pre-parsed, so the {{ES}} tree will be built on the fly. Second, if a new elementary stream starts after the first MB of data (for instance a subtitle track won't show up during the credits), it won't appear in the menu before we encounter the first packet. We cannot pre-parse the entire stream because it would take hours (even without decoding it).

   It is currently the responsibility of the input plugin to spawn the necessary decoder threads. It must call <code>input_SelectES ( input_thread_t * p_input, es_descriptor_t * p_es )</code> on the selected ES.

   The stream descriptor also contains a list of areas. Areas are logical discontinuities in the stream, for instance chapters and titles in a DVD. There is only one area in {{TS}} and [[PS]] streams, though we could use them when the PSM (or PAT/PMT) version changes. The goal is that when you seek to another area, the input plugin loads the new stream descriptor tree (otherwise the selected ID may be wrong).
   }}

Methods used by the interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Besides, ``input_ext-intf.c`` provides a few functions to control the reading of the stream:

.. raw:: mediawiki

   {{Note|
   Internally, the pace of reading is determined by the variable <var>p_input->stream.control.i_rate</var>. The default value is <code>DEFAULT_RATE</code>. The lower the value, the faster the pace is. Rate changes are taken into account in <code>input_ClockManageRef</code>. Pause is accomplished by simply stopping the input thread (it is then awakened by a pthread signal). In that case, decoders will be stopped too. Please remember this if you do statistics on decoding times (like [https://git.videolan.org/?p{{=}}

vlc.git;a{{=}}blob;f{{=}}src/video_parser/vpar_synchro.c src/video_parser/vpar_synchro.c] does). Don't call this function if \ ``p_input->b_pace_control``\ \ ``{{=}}{{=}} 0``. }}

.. raw:: mediawiki

   {{Note|
   Multimedia files can be very large, especially when we read a device like <code>/dev/dvd</code>, so offsets must be 64 bits large. Under a lot of systems, like FreeBSD, <var>off_t</var> are 64 bits by default, but it is not the case under GNU libc 2.x. That is why we need to compile VLC with <code>-D_FILE_OFFSET_BITS{{=}}

64 -D__USE_UNIX98. }}

Escaping stream discontinuities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Changing the reading position at random can result in a messed up stream, and the decoder which reads it may segfault. To avoid this, we send several ``NULL`` packets (i.e., packets containing nothing but zeros) before changing the reading position. Indeed, under most video and audio formats, a long enough stream of zeros is an escape sequence and the decoder can exit cleanly.

Buffers management
~~~~~~~~~~~~~~~~~~

Input plugins must implement a way to allocate and deallocate packets (whose structures will be described in the next chapter). We basically need four functions:

All functions are given ``p_input->p_method_data`` as first parameter, so that you can keep records of allocated and freed packets.

Buffers management strategies
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Buffers management can be done in three ways:

#. Traditional libc allocation: For a long time we have used in the `PS <PS>`__ plugin ``malloc()`` and ``free()`` every time we needed to allocate or deallocate a packet. Contrary to a popular belief, it is not that slow.
#. Netlist: In this method we allocate a very big buffer at the beginning of the problem, and then manage a list of pointers to free packets (the "netlist"). This only works well if all packets have the same size. It is used for ``long`` for the input. The DVD plugin also uses it, but adds a refcount flag because buffers (2048 bytes) can be shared among several packets. It is now deprecated and won't be documented.
#. Buffer cache: We are currently developing a new method. It is already in use in the PS plugin. The idea is to call ``malloc()`` and ``free()`` to absorb stream irregularities, but re-use all allocated buffers via a cache system. We are extending it so that it can be used in any plugin without performance hit, but it is currently left undocumented.

Demultiplexing the stream
~~~~~~~~~~~~~~~~~~~~~~~~~

After being read by ``pf_read``, your plugin must give a function pointer to the demultiplexer function. The demultiplexer is responsible for parsing the packet, gathering PES, and feeding decoders.

Demultiplexers for standard MPEG structures (`PS <PS>`__ and ) have already been written. You just need to indicate ``input_DemuxPS`` and ``input_DemuxTS`` for pf_demux. You can also write your own demultiplexer.

It is not the purpose of this document to describe the different levels of encapsulation in an MPEG stream. Please refer to your MPEG specification for that.

.. raw:: mediawiki

   {{Hacker Guide}}
