{{See alsoWin8 Dictionary}} {{Historical}} \__NOTOC_\_ Some terms used
in the area of Audio/Video and their meaning.

=== [[Aspect Ratio]] ===

The ratio of width to height of a video.

=== [[Bitrate]] ===

The number of bits of data to be played per second.

=== [[Chroma]] ===

Greek for color, the part of a video file or signal that encodes the
color portion.

=== [[Codec]] ===

A part of the program which understands a type of video or audio (short
for '''Co'''mpression/'''Dec'''ompression). DivX and Theora are examples
of video codecs; MP3 and Vorbis are audio codecs. The output stream
produced when a codec to audio or video is generally "muxed" into a
container format, such as AVI or Ogg. As certain codecs are often
associated with certain container formats, the name of the container is
often used to imply the codec, such as "Ogg", which usually refers to a
Vorbis stream in an Ogg container.

=== [[Decode]] ===

To understand and play a file, VideoLAN needs to decode it. It does this
with a decoder. See codec.

=== [[Deinterlacing]] ===

Deinterlacing is the process of converting interlaced video (a sequence
of fields) into a non-interlaced form (a sequence of frames). This is a
fundamentally impossible process that must always produce some image
degradation, since it ideally requires "temporal interpolation" which
involves guessing the movement of every object in the image and applying
motion correction to every object.

=== [[Demuxing]] === Process that reads the container format and
separates audio, video, and subtitles, if any. Demuxing files doesn't
weaken the video nor audio quality, it doesn't do anything for these
data streams, it just simply saves them into separate files, each
containing one element of the original file.

=== [[Encode]] ===

=== [[ES]] ===

An '''E'''lementry '''S'''tream, a single channel of audio, video or
subtitles (without a container).

=== [[FourCC]] ===

=== [[Framerate]] ===

The number of frames of video displayed (or encoded to be displayed) per
unit time, usually expressed in frames per second (fps) or Hertz (Hz).
One Hertz is equivilant to one frame per second.

{{wikipedialabel1=Video compression picture typeslabel2=Inter
frame#Frame_types}}

=== [[Frame types]] === <!--([[I-frameP-]] & [[B-frame|B-]frames])-->

[[I-frame]]
   A full ''''I'''ntra-coded picture'

[[P-frame]]
   ''''P'''redicted' from previous frame(s)'s picture

[[B-frame]]
   ''''B'''i-predictive' or ''''B'''idirectional' calculated from
   surrounding frames's pictures. Can painlessly be skipped.

=== IDCT === {{wikipedialabel1=IDCT}}

'''I'''nverse '''D'''iscrete '''c'''osine '''t'''ransform

=== [[Keyframe]] ===

A [[Frame]] of video which is stored as a complete image, not just as
the changes from the previous image.

=== [[Lossless and Lossy|Lossless]] ===

Compression by means of an algorithm that does not change the data once
decompressed. Programs and most types of exact data are examples of
types of information that suffer greatly from being changed. If
information is lost then the compression method is considered to be
lossy.

=== [[Lossless and Lossy|Lossy]] ===

Compression that causes some data to be changed in the process. Some
data will not suffer from this, such as a photo that looks very much
like the original despite some degradation. Photos, videos and audio are
good examples of such compression.

=== [[Motion Compensation]] ===

Part of the video compression process. New frames normally store changes
in the image since the previous frame. If the scene is moving as a whole
(such as panning), motion compensation moves the reference frame to line
up with the new frame. This means that there are less changes to be
stored since the previous frame, and so less data needs to be stored.

=== [[Muxing]] ===

The process of encapsulating an encoded stream (see codec) into a
container format, such as AVI, Ogg, or Matroska.

=== [[Overlay]] ===

Displaying an image on top of the video

=== [[Packetizing]] ===

=== [[Post Processing]] ===

Post processing attempts to increase the quality of a decoded stream. In
VLC media player, it will reduce blockiness for low-bitrate video
streams, at the expense of smoothing out some detail. This feature is
not available for all codecs that VLC supports.

=== [[PCR]] (Program Clock Reference) ===

=== [[PS]] ===

Abbreviation for '''P'''rogram '''S'''tream.

{{wikipedialabel1=PTS}}

=== [[PTS]] === '''P'''resentation '''t'''ime-stamp

=== [[Sample rate]] ===

Usually used with audio, the frequency at which a signal is digitally
sampled, usually expressed in Hertz (Hz) or kiloHertz (kHz). One Hertz
is equivilant to one sample per second, One kiloHertz is a thousand
(1000) Hertz.

=== [[Transcode]] ===

Transcoding is changing the format of a file. This can be for the
purpose of changing the audio or video's bitrate, codec, or other
attributes, to reduce disk usage or for compatibility with a certain
program/device.

It is important to note that transcoding can be highly detrimental to
quality when dealing with lossy codecs, particularly for video. This is
because the second time a stream is encoded lossily the codec has less
information to work with, causing it to produce a cruder approximation
of the original. As with many other quality issues, this problem can be
worked around by increasing the bitrate, though some quality loss (as
well as possible re-encoding of the previous codec's artifacts) will
inevitably occur.

Also note that, provided both container formats support the codec,
transcoding is not necessary to switch container formats. For example,
an XviD video stream in an AVI file can be losslessly remuxed into an
Ogg file.

=== [[TS]] ===

Abbreviation for '''T'''ransport '''S'''tream, as in [[MPEG-TS]].

=== [[Transport Stream]] ===

See [[MPEG-TS]]

[[Category:Proposed deletion]] [[Category:Glossary]] {{DEFAULTSORT:*}}
