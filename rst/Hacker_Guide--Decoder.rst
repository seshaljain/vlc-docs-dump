{{Back to|Hacker Guide}} ==How to write a decoder==

===What is precisely a decoder in the VLC scheme ?===

The decoder does the mathematical part of the process of playing a
stream. It is separated from the demultiplexers (in the input module),
which manage packets to rebuild a continuous elementary stream, and from
the output thread, which takes samples reconstituted by the decoder and
plays them. Basically, a decoder has no interaction with devices, it is
purely algorithmic.

In the next section we will describe how the decoder retrieves the
stream from the input. The output API (how to say "this sample is
decoded and can be played at xx") will be talked about in the next
chapters.

===Decoder configuration===

The input thread spawns the appropriate decoder modules from
{{VLCSourceFile|src/input/decoder.c}}. The <code>CreateDecoder(
input_thread_t *p_input,es_format_t*\ fmt, int i_object_type )</code>
function creates a <code>p_dec</code> variable of type
<code>i_object_type</code>(in our case <code>VLC_OBJECT_DECODER</code>),
then calls <code>module_Need( vlc_object_t *p_this, const
char*\ psz_capability,const char *psz_name, bool b_strict )</code> with
<code>*\ psz_capability="decoder"</code> and
<code>*psz_name="$codec"</code>. <code>module_Need</code> builds a list
of the possible modules for this capability, using a score. As an
example, in the a52 module, we can read:

   set_capability( "decoder", 100 );

which means its score is 100 when we request a decoder. The same system is used in each part of VLC to chose which module will be used. Then, it verifies if the decoder needs [[packetize]]d data (in that case, it finds and loads a packetizer module). In the end, it starts the decoder thread by a call to:
   vlc_thread_create( p_dec, "decoder", DecoderThread, i_priority, false
   )

===Packet structures===

The input module provides an advanced API for delivering stream data to
the decoders. First let's have a look at the packet structures. They are
defined in {{VLCSourceFile|include/input_ext-dec.h}}.

data_packet_t contains a pointer to the physical location of data.
Decoders should only start to read them at <code>p_payload_start</code>
until <code>p_payload_end</code>. Thereafter, it will switch to the next
packet, <code>p_next</code> if it is not <code>NULL</code>. If the
<code>b_discard_payload</code> flag is up, the content of the packet is
messed up and it should be discarded.

data_packet_t are contained into <var>pes_packet_t</var>.
<var>pes_packet_t</var> features a chained list (<code>p_first</code>)
of <var>data_packet_t</var> representing (in the MPEG paradigm) a
complete PES packet. For PS streams, a <var>pes_packet_t</var> usually
only contains one <var>data_packet_t</var>. In TS streams though, one
PES can be split among dozens of TS packets. A PES packet has PTS dates
(see your MPEG specification for more information) and the current pace
of reading that should be applied for interpolating dates
(<code>i_rate</code>). <code>b_data_alignment</code> (if available in
the system layer) indicates if the packet is a random access point, and
<code>b_discontinuity</code> tells whether previous packets have been
dropped. A PES packet in a Program Stream

In a Program Stream, a PES packet features only one data packet, whose
buffer contains the PS header, the PES header, and the data payload.

A PES packet in a Transport Stream

In a Transport Stream, a PES packet can feature an unlimited number of
data packets (three on the figure) whose buffers contains the PS header,
the PES header, and the data payload.

The structure shared by both the input and the decoder is
<var>decoder_fifo_t</var>. It features a rotative FIFO of PES packets to
be decoded. The input provides macros to manipulate it :
<code>DECODER_FIFO_ISEMPTY</code>, <code>DECODER_FIFO_ISFULL</code>,
<code>DECODER_FIFO_START</code>, <code>DECODER_FIFO_INCSTART</code>,
<code>DECODER_FIFO_END</code>, <code>DECODER_FIFO_INCEND</code>. Please
remember to take <code>p_decoder_fifo->data_lock</code> before any
operation on the FIFO.

The next packet to be decoded is <code>DECODER_FIFO_START(
*p_decoder_fifo )</code>. When it is finished, you need to call
<code>p_decoder_fifo->pf_delete_pes( p_decoder_fifo->p_packets_mgt,
DECODER_FIFO_START(*\ p_decoder_fifo ) )</code> and then
<code>DECODER_FIFO_INCSTART( \*p_decoder_fifo )</code> to return the PES
to the buffer manager.

If the FIFO is empty (<code>DECODER_FIFO_ISEMPTY</code>), you can block
until a new packet is received with a cond signal : <code>vlc_cond_wait(
&p_fifo->data_wait, &p_fifo->data_lock )</code>. You have to hold the
lock before entering this function. If the file is over or the user
quits, <code>p_fifo->b_die</code> will be set to 1. It indicates that
you must free all your data structures and call
<code>vlc_thread_exit()</code> as soon as possible.

===The bit stream (input module)===

This classical way of reading packets is not convenient, though, since
the elementary stream can be split up arbitrarily. The input module
provides primitives which make reading a bit stream much easier. Whether
you use it or not is at your option, though if you use it you shouldn't
access the packet buffer any longer.

The bit stream allows you to just call <code>GetBits()</code>, and this
functions will transparently read the packet buffers, change data
packets and pes packets when necessary, without any intervention from
you. So it is much more convenient for you to read a continuous
Elementary Stream, you don't have to deal with packet boundaries and the
FIFO, the bit stream will do it for you.

The central idea is to introduce a buffer of 32 bits [normally
<code>WORD_TYPE</code>, but 64-bit version doesn't work yet],
<var>bit_fifo_t</var>. It contains the word buffer and the number of
significant bits (higher part). The input module provides five inline
functions to manage it :

{{FnReturns the next <code>i_bits</code> bits from the bit buffer. If
there are not enough bits, it fetches the following word from the
<var>decoder_fifo_t</var>. This function is only guaranteed to work with
up to 24 bits. For the moment it works until 31 bits, but it is a side
effect. We were obliged to write a different function, GetBits32, for
32-bit reading, because of the << operator.}} {{FnThe same as
<code>GetBits()</code>, except that the bits aren't returned (we spare a
few CPU cycles). It has the same limitations, and we also wrote
RemoveBits32.}} {{FnThe same as <code>GetBits()</code>, except that the
bits don't get flushed after reading, so that you need to call
<code>RemoveBits()</code> by hand afterwards. Beware, this function
won't work above 24 bits, except if you're aligned on a byte boundary
(see next function).}} {{FnDrops the n higher bits (n < 8), so that the
first bit of the buffer be aligned an a byte boundary. It is useful when
looking for an aligned startcode (MPEG for instance).}} {{FnIt is an
analog of <code>memcpy()</code>, but taking a bit stream as first
argument. <code>p_buffer</code> must be allocated and at least
<code>i_buf_len</code> long. It is useful to copy data you want to keep
track of. }}

All these functions recreate a continuous elementary stream paradigm.
When the bit buffer is empty, they take the following word in the
current packet. When the packet is empty, it switches to the next
<var>data_packet_t</var>, or if inapplicable to the next
<var>pes_packet_t</var> (see
<code>p_bit_stream->pf_next_data_packet</code>). All this is completely
transparent.

====Packet changes and alignment issues====

We have to study the conjunction of two problems. First, a
<var>data_packet_t</var> can have an even number of bytes, for instance
177, so the last word will be truncated. Second, many CPU (sparc,
alpha&hellip;) can only read words aligned on a word boundary (that is,
32 bits for a 32-bit word). So packet changes are a lot more complicated
than you can imagine, because we have to read truncated words and get
aligned.

For instance <code>GetBits()</code> will call
<code>UnalignedGetBits()</code> from
{{VLCSourceFile|src/input/input_ext-dec.c}}. Basically it will read byte
after byte until the stream gets realigned.
<code>UnalignedShowBits()</code> is a bit more complicated and may
require a temporary packet (<code>p_bit_stream->showbits_data</code>).

To use the bit stream, you have to call
<code>p_decoder_config->pf_init_bit_stream( bit_stream_t \*
p_bit_stream, decoder_fifo_t \* p_fifo )</code> to set up all variables.
You will probably need to regularly fetch specific information from the
packet, for instance the [[wikipedia:Presentation
timestampsrc/video_parser/video_parser.c}} for an example. The second
argument indicates whether it is just a new <var>data_packet_t</var> or
also a new <var>pes_packet_t</var>. You can store your own structure in
<code>p_bit_stream->p_callback_arg</code>.

====Warning====

When you call <code>pf_init_bit_stream</code>, the
<code>pf_bitstream_callback</code> is not defined yet, but it jumps to
the first packet, though. You will probably want to call your bitstream
callback by hand just after <code>pf_init_bit_stream</code>.

===Built-in decoders===

VLC already features an MPEG layer 1 and 2 audio decoder, an MPEG MP@ML
video decoder, an AC3 decoder (borrowed from LiViD), a DVD SPU decoder,
and an LPCM decoder. You can write your own decoder, just mimic the
video parser.

====Limitations in the current design====

To add a new decoder, you'll still have to add the stream type as
there's still a hard-wired piece of code in
{{VLCSourceFile|src/input/input_programs.c}} .

The MPEG audio decoder is native, but doesn't support layer 3 decoding
[too much trouble], the AC3 decoder is a port from Aaron Holtzman's
libac3 (the original libac3 isn't reentrant), and the SPU decoder is
native. You may want to have a look at BitstreamCallback in the AC3
decoder. In that case we have to jump the first 3 bytes of a PES packet,
which are not part of the elementary stream. The video decoder is a bit
special and will be described in the following section.

===The MPEG video decoder===

VLC media player provides an MPEG-1, and an MPEG-2 Main Profile @ Main
Level decoder. It has been natively written for VLC, and is quite
mature. Its status is a bit special, since it is split between two
logical entities : video parser and video decoder. The initial goal is
to separate bit stream parsing functions from highly parallelizable
mathematical algorithms. In theory, there can be one video parser thread
(and only one, otherwise we would have race conditions reading the bit
stream), along with a pool of video decoder threads, which do IDCT and
motion compensation on several blocks at once.

It doesn't (and won't) support MPEG-4 or DivX decoding. It is not an
encoder. It should support the whole MPEG-2 MP@ML specification, though
some features are still left untested, like Differential Motion Vectors.
Please bear in mind before complaining that the input elementary stream
must be valid (for instance this is not the case when you directly read
a DVD multi-angle .vob file).

The most interesting file is {{VLCSourceFile|src/vpar_synchro.c}}, it is
really worth the shot. It explains the whole frame dropping algorithm.
In a nutshell, if the machine is powerful enough, we decoder all IPBs,
otherwise we decode all IPs and Bs if we have enough time (this is based
on on-the-fly decoding time statistics). Another interesting file is
vpar_blocks.c, which describes all block (including coefficients and
motion vectors) parsing algorithms. Look at the bottom of the file, we
indeed generate one optimized function for every common picture type,
and one slow generic function. There are also several levels of
optimization (which makes compilation slower but certain types of files
faster decoded) called <code>VPAR_OPTIM_LEVEL</code>, level 0 means no
optimization, level 1 means optimizations for MPEG-1 and MPEG-2 frame
pictures, level 2 means optimizations for MPEG-1 and MPEG-2 field and
frame pictures. Motion compensation plug-ins

Motion compensation (i.e. copy of regions from a reference picture) is
very platform-dependent (for instance with MMX or AltiVec versions), so
we moved it to the plugins/motion directory. It is more convenient for
the video decoder, and resulting plug-ins may be used by other video
decoders (MPEG-4 ?). A motion plugin must define 6 functions, coming
straight from the specification : <code>vdec_MotionFieldField420</code>,
<code>vdec_MotionField16x8420</code>,
<code>vdec_MotionFieldDMV420</code>,
<code>vdec_MotionFrameFrame420</code>,
<code>vdec_MotionFrameField420</code>,
<code>vdec_MotionFrameDMV420</code>. The equivalent 4:2:2 and 4:4:4
functions are unused, since these formats are forbidden in MP@ML (it
would only take longer compilation time).

Look at the C version of the algorithms if you want more information.
Note also that the DMV algorithm is untested and is probably buggy.

===IDCT plug-ins===

Just like motion compensation, IDCT is platform-specific. So we moved it
to plugins/idct. This module does the IDCT calculation, and copies the
data to the final picture. You need to define seven methods :

{{FnDoes the complete 2-D IDCT. 64 coefficients are in
<code>p_block</code>.}} {{FnDoes an IDCT on a block with only one
non-<code>NULL</code> coefficient (designated by
<code>i_sparse_pos</code>). You can use the function defined in
plugins/idct/idct_common.c which precalculates these 64 matrices at
initialization time.}} {{FnDoes the initialization stuff needed by
<code>vdec_SparseIDCT</code>.}} {{FnNormally, this function does
nothing. For minor optimizations, some IDCT (MMX) need to invert certain
coefficients in the MPEG scan matrices (see ISO/IEC 13818-2).}}
{{FnInitializes the IDCT and optional crop tables.}} {{FnDecodes an
entire macroblock and copies its data to the final picture, including
chromatic information.}} {{FnDecodes an entire macroblock and copies its
data to the final picture, except chromatic information (used in
grayscale mode). }}

Currently we have implemented optimized versions for : MMX, MMXEXT, and
AltiVec [doesn't work]. We have two plain C versions, the normal
(supposedly optimized) Berkeley version (idct.c), and the simple 1-D
separation IDCT from the ISO reference decoder (idctclassic.c).

===Symmetrical Multiprocessing===

The MPEG video decoder of VLC can take advantage of several processors
if necessary. The idea is to launch a pool of decoders, which will do
IDCT/motion compensation on several macroblocks at once.

The functions managing the pool are in
{{VLCSourceFile|src/video_decoder/vpar_pool.c}}. Its use on non-SMP
machines is not recommended, since it is actually slower than the
monothread version. Even on SMP machines sometimes&hellip;

{{Hacker Guide}}

[[Category:Pages to check]]
