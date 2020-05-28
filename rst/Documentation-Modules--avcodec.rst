.. raw:: mediawiki

   {{See also|Documentation:Modules/avformat}}

.. raw:: mediawiki

   {{Module|name=avcodec|type=codec library|description=Various audio and video decoders/encoders delivered by the FFmpeg library. This includes (MS)[[MPEG4]], [[DivX]], [[SVQ1]], [[H261]], [[H263]], [[H264]], [[WMV]], [[WMA]], [[AAC]], [[AMR]], [[DV]], [[MJPEG]] and other codecs}}

libavcodec provided by the `FFmpeg <FFmpeg>`__ project. A full list of `supported <supported>`__ codecs may be found with

Options prefixed with *ffmpeg-* or *sout-ffmpeg-* were deprecated in 2.1.0 to reflect the new module name *avcodec*. The only option that seems not to have been replaced later is ``--avcodec-vismv``, removed in 3.0.0.

The variable ENC_PROFILE_LONGTEXT `defined in modules/codec/avcodec/avcodec.h <https://git.videolan.org/?p=vlc.git;a=blob;f=modules/codec/avcodec/avcodec.h;h=5e526a3b1cd61d9eb90d79223994c115c1ac35e1;hb=HEAD#l230>`__ does not mention `that it checks <https://git.videolan.org/?p=vlc.git;a=blob;f=modules/codec/avcodec/encoder.c;h=2f8e2d8a145c2558f57c97787eba2af407ec6af3;hb=HEAD#l477>`__ for ``ld`` (Low Delay) and ``eld`` (Extended Low Delay). FIXME: Unclear whether they are actually supported.

Options as of 3.0.6:

Decoding
--------

.. raw:: mediawiki

   {{Option|name=avcodec-dr|value=boolean|default=enabled|description=Direct rendering}}

.. raw:: mediawiki

   {{Option|name=avcodec-corrupted|value=boolean|default=enabled|description=Prefer visual artifacts instead of missing frames}}

.. raw:: mediawiki

   {{Option|name=avcodec-error-resilience|value=integer|min=0|max=4|default=1|description=libavcodec can do error resilience. However, with a buggy encoder (such as the ISO MPEG-4 encoder from M$) this can produce a lot of errors. Valid values range from 0 to 4 (0 disables all errors resilience)}}

.. raw:: mediawiki

   {{Option|name=avcodec-workaround-bugs|value=integer|default=1|description=Try to fix some bugs: 1  autodetect, 2  old msmpeg4, 4  xvid interlaced, 8  ump4, 16 no padding, 32 ac vlc, 64 Qpel chroma. This must be the sum of the values. For example, to fix "ac vlc" and "ump4", enter 40.)}}

.. raw:: mediawiki

   {{Option|name=avcodec-hurry-up|value=boolean|default=enabled|description=The decoder can partially decode or skip frame(s) when there is not enough time. It's useful with low CPU power but it can produce distorted pictures}}

.. raw:: mediawiki

   {{Option|name=avcodec-skip-frame|value=integer|select={-1,0,1,2,3,4}|default=0|description=Force skipping of [[frame]]s to speed up decoding (-1=None, 0=Default, 1=[[B-frame]]s, 2=[[P-frame]]s, 3=B+P frames, 4=all frames)}}

.. raw:: mediawiki

   {{Option|name=avcodec-skip-idct|value=integer|select={-1,0,1,2,3,4}|default=0|description=Force skipping of [[wikipedia:IDCT#DCT-III|IDCT]] to speed up decoding for frame types (-1=None, 0=Default, 1=B-frames, 2=P-frames, 3=B+P frames, 4=all frames)}}

.. raw:: mediawiki

   {{Option|name=avcodec-fast|value=boolean|default=disabled|description=Allow non specification compliant speedup tricks. Faster but error-prone}}

.. raw:: mediawiki

   {{Option|name=avcodec-skiploopfilter|value=integer|select={0 (None), 1 (Non-ref), 2 (Bidir), 3 (Non-key), 4 (All)}|default=0|description=Skipping the loop filter (aka deblocking) usually has a detrimental effect on quality. However it provides a big speedup for high definition streams}}

.. raw:: mediawiki

   {{Option|name=avcodec-debug|value=integer|default=0|description=Set FFmpeg debug mask}}

.. raw:: mediawiki

   {{Option|name=avcodec-codec|value=string|default=NULL|description=Internal libavcodec codec name}}

.. raw:: mediawiki

   {{Option|name=avcodec-hw|value=integer|select={any,vdpau_avcodec,vaapi,vaapi_drm,none}|default=any|description=This allows hardware decoding when available}}

.. raw:: mediawiki

   {{Option|name=avcodec-threads|value=integer|default=0|description=Number of threads used for decoding, 0 meaning auto}}

.. raw:: mediawiki

   {{Option|name=avcodec-options|value=string|default=NULL|description=Advanced options, in the form <code>{opt=val,opt2=val2}</code>}}

Encoding
--------

.. raw:: mediawiki

   {{Option|name=sout-avcodec-codec|value=string|default=NULL|description=Internal libavcodec [[codec]] name}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-hq|value=string|select={rd,bits,simple}|default=rd|description=Quality level for the encoding of motions vectors (this can slow down the encoding very much)}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-keyint|value=integer|default=0|description=Number of frames that will be coded for one [[key frame]]}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-bframes|value=integer|default=0|description=Number of [[B-frame]]s that will be coded between two reference frames}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-hurry-up|value=boolean|default=disabled|description=The encoder can make on-the-fly quality tradeoffs if your CPU can't keep up with the encoding rate. It will disable trellis quantization, then the rate distortion of motion vectors (hq), and raise the noise reduction threshold to ease the encoder's task}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-interlace|value=boolean|default=disabled|description=Enable dedicated 
   algorithms for [[interlaced]] frames}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-interlace-me|value=boolean|default=enabled|description=Enable interlaced motion estimation algorithms. This requires more CPU}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-vt|value=integer|default=0|description=Video [[bitrate]] tolerance in kbit/s}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-pre-me|value=boolean|default=disabled|description=Enable the pre-motion estimation algorithm}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-rc-buffer-size|value=integer|default=0|description=Rate control buffer size (in kbytes). A bigger buffer will allow for better rate control, but will cause a delay in the stream}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-rc-buffer-aggressivity|value=float|default=1.0|description=Rate control buffer aggressiveness}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-i-quant-factor|value=float|default=0|description=Quantization factor of [[I-frame]]s, compared with [[P-frame]]s (for instance 1.0 => same qscale for I and P frames)}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-noise-reduction|value=integer|default=0|description=Enable a simple noise reduction algorithm to lower the encoding length and bitrate, at the expense of lower quality frames}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-mpeg4-matrix|value=boolean|default=disabled|description=Use the [[MPEG-4]] quantization matrix for [[MPEG-2]] encoding. This generally yields a better looking picture, while still retaining the compatibility with standard MPEG-2 decoders}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-qmin|value=integer|default=0|description=Minimum video quantizer scale}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-qmax|value=integer|default=0|description=Maximum video quantizer scale}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-trellis|value=boolean|default=disabled|description=Enable trellis quantization (rate distortion for block coefficients)}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-qscale|value=float|min=0.01|max=255.0|default=3|description=A fixed video quantizer scale for [[VBR]] encoding (accepted values: 0.01 to 255.0)}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-strict|value=integer|min=-2|max=2|default=0|description=Force a strict standard  compliance when encoding (accepted values: -2 to 2)}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-lumi-masking|value=float|default=0.0|description=Raise the quantizer for very bright macroblocks}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-dark-masking|value=float|default=0.0|description=Raise the quantizer for very dark macroblocks}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-p-masking|value=float|default=0.0|description=Raise the quantizer for macroblocks with a high temporal complexity}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-border-masking|value=float|default=0.0|description=Raise the quantizer for macroblocks at the border of the frame}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-luma-elim-threshold|value=integer|default=0|description=Eliminates luminance blocks when the PSNR isn't much changed. The [[H.264]] specification recommends -4}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-chroma-elim-threshold|value=integer|default=0|description=Eliminates chrominance blocks when the PSNR isn't much changed. The [[H.264]] specification recommends 7}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-aac-profile|value=string|default=low|description=Specify the [[AAC]] audio profile to use for encoding the audio bitstream. It takes the following options: main, low, ssr (not supported), ltp, hev1, hev2. hev1 and hev2 are currently supported only with libfdk-aac enabled libavcodec}}

.. raw:: mediawiki

   {{Option|name=sout-avcodec-options|value=string|default=NULL|description=Advanced options, in the form <code>{opt=val,opt2=val2}</code>}}

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFolder|modules/codec/avcodec}}

   (folder)

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/codec/avcodec/avcodec.c}}

   (main file)

.. raw:: mediawiki

   {{Documentation footer}}
