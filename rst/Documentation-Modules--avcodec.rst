{{See alsoname=avcodecdescription=Various audio and video
decoders/encoders delivered by the FFmpeg library. This includes
(MS)[[MPEG4]], [[DivX]], [[SVQ1]], [[H261]], [[H263]], [[H264]],
[[WMV]], [[WMA]], [[AAC]], [[AMR]], [[DV]], [[MJPEG]] and other codecs}}

libavcodec provided by the [[FFmpeg]] project. A full list of
[[supported]] codecs may be found with
{{VLCSourceFile|modules/codec/avcodec/fourcc.c}}

Options prefixed with ''ffmpeg-'' or ''sout-ffmpeg-'' were deprecated in
2.1.0 to reflect the new module name ''avcodec''. The only option that
seems not to have been replaced later is <code>--avcodec-vismv</code>,
removed in 3.0.0.

The variable <var>ENC_PROFILE_LONGTEXT</var>
[https://git.videolan.org/?p=vlc.git;a=blob;f=modules/codec/avcodec/avcodec.h;h=5e526a3b1cd61d9eb90d79223994c115c1ac35e1;hb=HEAD#l230
defined in modules/codec/avcodec/avcodec.h] does not mention
[https://git.videolan.org/?p=vlc.git;a=blob;f=modules/codec/avcodec/encoder.c;h=2f8e2d8a145c2558f57c97787eba2af407ec6af3;hb=HEAD#l477
that it checks] for <code>ld</code> (Low Delay) and <code>eld</code>
(Extended Low Delay). FIXME: Unclear whether they are actually
supported.

Options as of 3.0.6:

== Decoding == {{Optionvalue=booleandescription=Direct rendering}}
{{Optionvalue=booleandescription=Prefer visual artifacts instead of
missing frames}} {{Optionvalue=integermax=4description=libavcodec can do
error resilience. However, with a buggy encoder (such as the ISO MPEG-4
encoder from M$) this can produce a lot of errors. Valid values range
from 0 to 4 (0 disables all errors resilience)}}
{{Optionvalue=integerdescription=Try to fix some bugs: 1 autodetect, 2
old msmpeg4, 4 xvid interlaced, 8 ump4, 16 no padding, 32 ac vlc, 64
Qpel chroma. This must be the sum of the values. For example, to fix "ac
vlc" and "ump4", enter 40.)}} {{Optionvalue=booleandescription=The
decoder can partially decode or skip frame(s) when there is not enough
time. It's useful with low CPU power but it can produce distorted
pictures}}
{{Optionvalue=integerdefault=0name=avcodec-skip-idctselect={-1,0,1,2,3,4}description=Force
skipping of
[[wikipedia:IDCT#DCT-IIIname=avcodec-fastdefault=disabledname=avcodec-skiploopfilterselect={0
(None), 1 (Non-ref), 2 (Bidir), 3 (Non-key), 4
(All)}description=Skipping the loop filter (aka deblocking) usually has
a detrimental effect on quality. However it provides a big speedup for
high definition streams}} {{Optionvalue=integerdescription=Set FFmpeg
debug mask}} {{Optionvalue=stringdescription=Internal libavcodec codec
name}}
{{Optionvalue=integerdefault=anyname=avcodec-threadsdefault=0name=avcodec-optionsdefault=NULL|description=Advanced
options, in the form <code>{opt=val,opt2=val2}</code>}}

== Encoding == {{Optionvalue=stringdescription=Internal libavcodec
[[codec]] name}}
{{Optionvalue=stringdefault=rdname=sout-avcodec-keyintdefault=0name=sout-avcodec-bframesdefault=0name=sout-avcodec-hurry-updefault=disabledname=sout-avcodec-interlacedefault=disabledname=sout-avcodec-interlace-medefault=enabledname=sout-avcodec-vtdefault=0name=sout-avcodec-pre-medefault=disabledname=sout-avcodec-rc-buffer-sizedefault=0name=sout-avcodec-rc-buffer-aggressivitydefault=1.0name=sout-avcodec-i-quant-factordefault=0name=sout-avcodec-noise-reductiondefault=0name=sout-avcodec-mpeg4-matrixdefault=disabledname=sout-avcodec-qmindefault=0name=sout-avcodec-qmaxdefault=0name=sout-avcodec-trellisdefault=disabledname=sout-avcodec-qscalemin=0.01default=3name=sout-avcodec-strictmin=-2default=0name=sout-avcodec-lumi-maskingdefault=0.0name=sout-avcodec-dark-maskingdefault=0.0name=sout-avcodec-p-maskingdefault=0.0name=sout-avcodec-border-maskingdefault=0.0name=sout-avcodec-luma-elim-thresholddefault=0name=sout-avcodec-chroma-elim-thresholddefault=0name=sout-avcodec-aac-profiledefault=lowname=sout-avcodec-optionsdefault=NULL|description=Advanced
options, in the form <code>{opt=val,opt2=val2}</code>}}

== Source code == \* {{VLCSourceFoldermodules/codec/avcodec/avcodec.c}}
(main file)

{{Documentation footer}}
