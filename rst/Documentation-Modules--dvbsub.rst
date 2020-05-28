{{Moduletype=Subtitlesdescription=[[DVB subtitles]] decoder/encoder}}
{{Clear}}

There are notes in the source code: <syntaxhighlight lang="c">
/*************************************************************************\***\*
\* Preamble \* \* FIXME: \* DVB subtitles coded as strings of characters
are not handled correctly. \* The character codes in the string should
actually be indexes referring to a \* character table identified in the
subtitle descriptor. \* \* The spec is quite vague in this area, but
what is meant is perhaps that it \* refers to the character index in the
codepage belonging to the language \* specified in the subtitle
descriptor. Potentially it's designed for widechar \* (but not for
UTF-*)
codepages.**\ \***********************************************************************\*\ **\*/
</syntaxhighlight> and <syntaxhighlight lang="c">
/**\ \***********************************************************************\*\ **\*
\* Notes on DDS (Display Definition Segment) \*
----------------------------------------- \* DDS (Display Definition
Segment) tells the decoder how the subtitle image \* relates to the
video image. \* For SD, the subtitle image is always considered to be
for display at \* 720x576 (although it's assumed that for NTSC, this is
720x480, this \* is not documented well) Also, for SD, the subtitle
image is drawn 'on \* the glass' (i.e. after video scaling, letterbox,
etc.) \* For 'HD' (subs marked type 0x14/0x24 in PSI), a DDS must be
present, \* and the subs area is drawn onto the video area (scales if
necessary). \* The DDS tells the decoder what resolution the subtitle
images were \* intended for, and hence how to scale the subtitle images
for a \* particular video size \* i.e. if HD video is presented as
letterbox, the subs will be in the \* same place on the video as if the
video was presented on an HD set \* indeed, if the HD video was
pillarboxed by the decoder, the subs may \* be cut off as well as the
video. The intent here is that the subs can \* be placed accurately on
the video - something which was missed in the \* original spec. \* \* A
DDS may also specify a window - this is where the subs images are moved
so that the (0,0) \* origin of decode is
offset.**\ \******************************************************************************************/
</syntaxhighlight>

== Options == {{Option value=integer description=Subpicture
position<sup>('''[[#appendix_dvbsub-positionname=dvbsub-x default=-1
name=dvbsub-y default=-1 \|description=Y coordinate of the rendered
subtitle }}

=== Encoder === {{Option value=integer description=X coordinate of the
encoded subtitle }} {{Option value=integer description=Y coordinate of
the encoded subtitle }} {{Clear}}

== Appendix == <div class="plainlist"> \*^
[[#dvbsub-position|--dvbsub-position]]<span
id="appendix_dvbsub-position"></span> </div> {{Alignment mapping}}

== Source code == \* {{VLCSourceFile|modules/codec/dvbsub.c}}

{{Documentation footer}}
