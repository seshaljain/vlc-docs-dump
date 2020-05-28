{{Back tomodules}} directory in the [[{{#rel2abs:../VLC source
tree}}|source tree of VLC]], aimed at giving new beginners an overview
of the code.

The directories are listed in alphabetical order, with an overview of
their contents on the right. Any first level subdirectories are shown as
well.

For detailed documentation on VLC modules, please see
'''[[Documentation:Modules]]'''.

'''''Note:''''' This table is by no means exhaustive. Note that only
plugins with their own subdirectories are listed; plugins inside the
parent directories are not emphasized unless they are too important. For
a comprehensive list of the plugins VLC makes use of, consult
{{VLCSourceFile|modules/MODULES_LIST}} in your source code checkout.

{\| class="wikitable" - -\| input module to read audio CDs DirectShow
access plugin for encoding cards under Windows input module for
DVB-S/C/T streaming using v4l2 API mms]] -\| screen]] -\| input module
for accessing Video CDs. input module for accessing Video CDs with
navigation & stills \| \| access-filter \| timeshift]],
[[Documentation:Modules/recorddump]], which are used for ????? \| \|
access-output \| \| \| \| audio-filter \| \|Various audio filters like
decoders, equalizers, converters.

Various mixers and decoders like Dolby decoder Fixed and floating-point
audio format conversions such as AC/3 or MPEG I-II Audio Layer 1, 2, 3
decoding Various audio resampler \| \| audio-mixer \| -\| \| \|
audio-output \| -\| \| \| codec \| -\| Continuous Media Markup Language
annotations/hyperlinks decoder a DirectMediaObject decoder that uses
DirectMedia to decode video (WMV3) Video decoder using the ffmpeg
library RLE DVD subtitles decoder XVMC video output and decoder \| \|
control \| -\| http]] -\| \| \| demux \| -\| ASF demuxer AVI File stream
demuxer MP4 file input module playlist import module??? \| \| gui \|
ncurses ]] interface beos]] -\| \|macosx]] -\| interface for iPaq using
the Gtk2+ widget set. QNX RTOS plugin \|qt4]] -\| \|skins2]] -\| Pocket
PC interface interface module using the cross-platform wxWindows
library: Multi-platform. The default interface as of VLC 0.86a. \| \|
meta-engine \| \| \| \| misc \| \| Dummy (no GUI) audio output, video
output, interface and input modules. memory chunk copying module.
notifications using libnotify LibXML and xtag xml parsers \| \| mux
packetizer \| -\| \| \| services-discovery \| \| \| \| stream-out \| \|
\| video-chroma \| -\| \| \| video-filter \| Deinterlace]],
[[Documentation:Modules/transformWall]],
[[Documentation:Modules/cropPanoramix]] etc. \| \| video-output \| Video
output module using the [[Documentation:Modules/direct3dDirect X]] API's
; [[Documentation:Modules/glwin32-\| video output module for Qt
Embedded. x11]] -\| \| \| visualization \| goom]] a visualization module
that outputs OpenGL visualisation system \|}

See Also: [http://www.videolan.org/doc/vlc-user-guide/en/ch02.html VLC
User Guide - Chapter 2. Modules and options for VLC ]

[[Category:Building]] {{Hacker_Guide}}
