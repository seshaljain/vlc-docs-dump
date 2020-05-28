.. raw:: mediawiki

   {{Back to|Hacker Guide}}

How to write a decoder
----------------------

What is precisely a decoder in the VLC scheme ?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The decoder does the mathematical part of the process of playing a stream. It is separated from the demultiplexers (in the input module), which manage packets to rebuild a continuous elementary stream, and from the output thread, which takes samples reconstituted by the decoder and plays them. Basically, a decoder has no interaction with devices, it is purely algorithmic.

In the next section we will describe how the decoder retrieves the stream from the input. The output API (how to say "this sample is decoded and can be played at xx") will be talked about in the next chapters.

Decoder configuration
~~~~~~~~~~~~~~~~~~~~~

The input thread spawns the appropriate decoder modules from . The ``CreateDecoder( input_thread_t *p_input,es_format_t *fmt, int i_object_type )`` function creates a ``p_dec`` variable of type ``i_object_type``\ (in our case ``VLC_OBJECT_DECODER``), then calls ``module_Need( vlc_object_t *p_this, const char *psz_capability,const char *psz_name, bool b_strict )`` with ``*psz_capability="decoder"`` and ``*psz_name="$codec"``. ``module_Need`` builds a list of the possible modules for this capability, using a score. As an example, in the a52 module, we can read:

``   set_capability( "decoder", 100 );``

which means its score is 100 when we request a decoder. The same system is used in each part of VLC to chose which module will be used. Then, it verifies if the decoder needs `packetized <packetize>`__ data (in that case, it finds and loads a packetizer module). In the end, it starts the decoder thread by a call to:

``   vlc_thread_create( p_dec, "decoder", DecoderThread, i_priority, false )``

Packet structures
~~~~~~~~~~~~~~~~~

The input module provides an advanced API for delivering stream data to the decoders. First let's have a look at the packet structures. They are defined in .

data_packet_t contains a pointer to the physical location of data. Decoders should only start to read them at ``p_payload_start`` until ``p_payload_end``. Thereafter, it will switch to the next packet, ``p_next`` if it is not ``NULL``. If the ``b_discard_payload`` flag is up, the content of the packet is messed up and it should be discarded.

data_packet_t are contained into pes_packet_t. pes_packet_t features a chained list (``p_first``) of data_packet_t representing (in the MPEG paradigm) a complete PES packet. For PS streams, a pes_packet_t usually only contains one data_packet_t. In TS streams though, one PES can be split among dozens of TS packets. A PES packet has PTS dates (see your MPEG specification for more information) and the current pace of reading that should be applied for interpolating dates (``i_rate``). ``b_data_alignment`` (if available in the system layer) indicates if the packet is a random access point, and ``b_discontinuity`` tells whether previous packets have been dropped. A PES packet in a Program Stream

In a Program Stream, a PES packet features only one data packet, whose buffer contains the PS header, the PES header, and the data payload.

A PES packet in a Transport Stream

In a Transport Stream, a PES packet can feature an unlimited number of data packets (three on the figure) whose buffers contains the PS header, the PES header, and the data payload.

The structure shared by both the input and the decoder is decoder_fifo_t. It features a rotative FIFO of PES packets to be decoded. The input provides macros to manipulate it : ``DECODER_FIFO_ISEMPTY``, ``DECODER_FIFO_ISFULL``, ``DECODER_FIFO_START``, ``DECODER_FIFO_INCSTART``, ``DECODER_FIFO_END``, ``DECODER_FIFO_INCEND``. Please remember to take ``p_decoder_fifo->data_lock`` before any operation on the FIFO.

The next packet to be decoded is ``DECODER_FIFO_START( *p_decoder_fifo )``. When it is finished, you need to call ``p_decoder_fifo->pf_delete_pes( p_decoder_fifo->p_packets_mgt, DECODER_FIFO_START( *p_decoder_fifo ) )`` and then ``DECODER_FIFO_INCSTART( *p_decoder_fifo )`` to return the PES to the buffer manager.

If the FIFO is empty (``DECODER_FIFO_ISEMPTY``), you can block until a new packet is received with a cond signal : ``vlc_cond_wait( &p_fifo->data_wait, &p_fifo->data_lock )``. You have to hold the lock before entering this function. If the file is over or the user quits, ``p_fifo->b_die`` will be set to 1. It indicates that you must free all your data structures and call ``vlc_thread_exit()`` as soon as possible.

The bit stream (input module)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This classical way of reading packets is not convenient, though, since the elementary stream can be split up arbitrarily. The input module provides primitives which make reading a bit stream much easier. Whether you use it or not is at your option, though if you use it you shouldn't access the packet buffer any longer.

The bit stream allows you to just call ``GetBits()``, and this functions will transparently read the packet buffers, change data packets and pes packets when necessary, without any intervention from you. So it is much more convenient for you to read a continuous Elementary Stream, you don't have to deal with packet boundaries and the FIFO, the bit stream will do it for you.

The central idea is to introduce a buffer of 32 bits [normally ``WORD_TYPE``, but 64-bit version doesn't work yet], bit_fifo_t. It contains the word buffer and the number of significant bits (higher part). The input module provides five inline functions to manage it :

.. raw:: mediawiki

   {{Fn|u32 GetBits ( bit_stream_t * p_bit_stream, unsigned int i_bits ) |Returns the next <code>i_bits</code> bits from the bit buffer. If there are not enough bits, it fetches the following word from the <var>decoder_fifo_t</var>. This function is only guaranteed to work with up to 24 bits. For the moment it works until 31 bits, but it is a side effect. We were obliged to write a different function, GetBits32, for 32-bit reading, because of the << operator.}}

.. raw:: mediawiki

   {{Fn|RemoveBits ( bit_stream_t * p_bit_stream, unsigned int i_bits ) |The same as <code>GetBits()</code>, except that the bits aren't returned (we spare a few CPU cycles). It has the same limitations, and we also wrote RemoveBits32.}}

.. raw:: mediawiki

   {{Fn|u32 ShowBits ( bit_stream_t * p_bit_stream, unsigned int i_bits ) |The same as <code>GetBits()</code>, except that the bits don't get flushed after reading, so that you need to call <code>RemoveBits()</code> by hand afterwards. Beware, this function won't work above 24 bits, except if you're aligned on a byte boundary (see next function).}}

.. raw:: mediawiki

   {{Fn|RealignBits ( bit_stream_t * p_bit_stream ) |Drops the n higher bits (n < 8), so that the first bit of the buffer be aligned an a byte boundary. It is useful when looking for an aligned startcode (MPEG for instance).}}

.. raw:: mediawiki

   {{Fn|GetChunk ( bit_stream_t * p_bit_stream, byte_t * p_buffer, size_t i_buf_len ) |It is an analog of <code>memcpy()</code>, but taking a bit stream as first argument. <code>p_buffer</code> must be allocated and at least <code>i_buf_len</code> long. It is useful to copy data you want to keep track of. }}

All these functions recreate a continuous elementary stream paradigm. When the bit buffer is empty, they take the following word in the current packet. When the packet is empty, it switches to the next data_packet_t, or if inapplicable to the next pes_packet_t (see ``p_bit_stream->pf_next_data_packet``). All this is completely transparent.

Packet changes and alignment issues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We have to study the conjunction of two problems. First, a data_packet_t can have an even number of bytes, for instance 177, so the last word will be truncated. Second, many CPU (sparc, alpha…) can only read words aligned on a word boundary (that is, 32 bits for a 32-bit word). So packet changes are a lot more complicated than you can imagine, because we have to read truncated words and get aligned.

For instance ``GetBits()`` will call ``UnalignedGetBits()`` from . Basically it will read byte after byte until the stream gets realigned. ``UnalignedShowBits()`` is a bit more complicated and may require a temporary packet (``p_bit_stream->showbits_data``).

To use the bit stream, you have to call ``p_decoder_config->pf_init_bit_stream( bit_stream_t * p_bit_stream, decoder_fifo_t * p_fifo )`` to set up all variables. You will probably need to regularly fetch specific information from the packet, for instance the `PTS <wikipedia:Presentation_timestamp>`__. If ``p_bit_stream->pf_bit_stream_callback`` is not ``NULL``, it will be called on a packet change. See for an example. The second argument indicates whether it is just a new data_packet_t or also a new pes_packet_t. You can store your own structure in ``p_bit_stream->p_callback_arg``.

Warning
^^^^^^^

When you call ``pf_init_bit_stream``, the ``pf_bitstream_callback`` is not defined yet, but it jumps to the first packet, though. You will probably want to call your bitstream callback by hand just after ``pf_init_bit_stream``.

Built-in decoders
~~~~~~~~~~~~~~~~~

VLC already features an MPEG layer 1 and 2 audio decoder, an MPEG MP@ML video decoder, an AC3 decoder (borrowed from LiViD), a DVD SPU decoder, and an LPCM decoder. You can write your own decoder, just mimic the video parser.

Limitations in the current design
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To add a new decoder, you'll still have to add the stream type as there's still a hard-wired piece of code in .

The MPEG audio decoder is native, but doesn't support layer 3 decoding [too much trouble], the AC3 decoder is a port from Aaron Holtzman's libac3 (the original libac3 isn't reentrant), and the SPU decoder is native. You may want to have a look at BitstreamCallback in the AC3 decoder. In that case we have to jump the first 3 bytes of a PES packet, which are not part of the elementary stream. The video decoder is a bit special and will be described in the following section.

The MPEG video decoder
~~~~~~~~~~~~~~~~~~~~~~

VLC media player provides an MPEG-1, and an MPEG-2 Main Profile @ Main Level decoder. It has been natively written for VLC, and is quite mature. Its status is a bit special, since it is split between two logical entities : video parser and video decoder. The initial goal is to separate bit stream parsing functions from highly parallelizable mathematical algorithms. In theory, there can be one video parser thread (and only one, otherwise we would have race conditions reading the bit stream), along with a pool of video decoder threads, which do IDCT and motion compensation on several blocks at once.

It doesn't (and won't) support MPEG-4 or DivX decoding. It is not an encoder. It should support the whole MPEG-2 MP@ML specification, though some features are still left untested, like Differential Motion Vectors. Please bear in mind before complaining that the input elementary stream must be valid (for instance this is not the case when you directly read a DVD multi-angle .vob file).

The most interesting file is , it is really worth the shot. It explains the whole frame dropping algorithm. In a nutshell, if the machine is powerful enough, we decoder all IPBs, otherwise we decode all IPs and Bs if we have enough time (this is based on on-the-fly decoding time statistics). Another interesting file is vpar_blocks.c, which describes all block (including coefficients and motion vectors) parsing algorithms. Look at the bottom of the file, we indeed generate one optimized function for every common picture type, and one slow generic function. There are also several levels of optimization (which makes compilation slower but certain types of files faster decoded) called ``VPAR_OPTIM_LEVEL``, level 0 means no optimization, level 1 means optimizations for MPEG-1 and MPEG-2 frame pictures, level 2 means optimizations for MPEG-1 and MPEG-2 field and frame pictures. Motion compensation plug-ins

Motion compensation (i.e. copy of regions from a reference picture) is very platform-dependent (for instance with MMX or AltiVec versions), so we moved it to the plugins/motion directory. It is more convenient for the video decoder, and resulting plug-ins may be used by other video decoders (MPEG-4 ?). A motion plugin must define 6 functions, coming straight from the specification : ``vdec_MotionFieldField420``, ``vdec_MotionField16x8420``, ``vdec_MotionFieldDMV420``, ``vdec_MotionFrameFrame420``, ``vdec_MotionFrameField420``, ``vdec_MotionFrameDMV420``. The equivalent 4:2:2 and 4:4:4 functions are unused, since these formats are forbidden in MP@ML (it would only take longer compilation time).

Look at the C version of the algorithms if you want more information. Note also that the DMV algorithm is untested and is probably buggy.

IDCT plug-ins
~~~~~~~~~~~~~

Just like motion compensation, IDCT is platform-specific. So we moved it to plugins/idct. This module does the IDCT calculation, and copies the data to the final picture. You need to define seven methods :

.. raw:: mediawiki

   {{Fn|vdec_IDCT ( decoder_config_t * p_config, dctelem_t * p_block, int ) |Does the complete 2-D IDCT. 64 coefficients are in <code>p_block</code>.}}

.. raw:: mediawiki

   {{Fn|vdec_SparseIDCT ( vdec_thread_t * p_vdec, dctelem_t * p_block, int i_sparse_pos ) |Does an IDCT on a block with only one non-<code>NULL</code> coefficient (designated by <code>i_sparse_pos</code>). You can use the function defined in plugins/idct/idct_common.c which precalculates these 64 matrices at initialization time.}}

.. raw:: mediawiki

   {{Fn|vdec_InitIDCT ( vdec_thread_t * p_vdec ) |Does the initialization stuff needed by <code>vdec_SparseIDCT</code>.}}

.. raw:: mediawiki

   {{Fn|vdec_NormScan ( u8 ppi_scan[2][64] ) |Normally, this function does nothing. For minor optimizations, some IDCT (MMX) need to invert certain coefficients in the MPEG scan matrices (see ISO/IEC 13818-2).}}

.. raw:: mediawiki

   {{Fn|vdec_InitDecode ( struct vdec_thread_s * p_vdec ) |Initializes the IDCT and optional crop tables.}}

.. raw:: mediawiki

   {{Fn|vdec_DecodeMacroblockC ( struct vdec_thread_s *p_vdec, struct macroblock_s * p_mb )|Decodes an entire macroblock and copies its data to the final picture, including chromatic information.}}

.. raw:: mediawiki

   {{Fn|vdec_DecodeMacroblockBW ( struct vdec_thread_s *p_vdec, struct macroblock_s * p_mb )|Decodes an entire macroblock and copies its data to the final picture, except chromatic information (used in grayscale mode). }}

Currently we have implemented optimized versions for : MMX, MMXEXT, and AltiVec [doesn't work]. We have two plain C versions, the normal (supposedly optimized) Berkeley version (idct.c), and the simple 1-D separation IDCT from the ISO reference decoder (idctclassic.c).

Symmetrical Multiprocessing
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The MPEG video decoder of VLC can take advantage of several processors if necessary. The idea is to launch a pool of decoders, which will do IDCT/motion compensation on several macroblocks at once.

The functions managing the pool are in . Its use on non-SMP machines is not recommended, since it is actually slower than the monothread version. Even on SMP machines sometimes…

.. raw:: mediawiki

   {{Hacker Guide}}

`Category:Pages to check <Category:Pages_to_check>`__
