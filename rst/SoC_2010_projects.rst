Here is a list of the accepted projects for Google Summer of Code 2010.

= List of current VLC projects =

== Shader support for video post-processing ==

*'''Project page: [[SoC 2010 Shader Support]]'''*'''Student''':
[[User:Skoruga|Sasha Koruga]] *'''Mentor''': Adrien
Maglo*'''Abstract''':

A lot of video post-processing such as RGB-YUV conversion can be
accelerated by using the GPU. This can either be achieved through a
fragment shader, where it is the last step before a pixel is displayed
on the screen, or it can be done with DirectCompute/CUDA/OpenCL. The
method will vary depending on the task and intent. I will implement
support for shaders by using the DirectX and OpenGL API and write a few
shaders such as RGB-YUV conversion.

== Port VLC Player to Symbian Platform ==

*'''Project page: [[SoC 2010 Shader Support]]'''*'''Student''':
[[User:pk2010|Pankaj Yadav]] *'''Mentor''': Rémi
Duraffort*'''Abstract''':

To port VLC Player to Symbian S60 Platform.

== ASF demuxer ==

*'''Project page: [[SoC 2010 ASF Demuxer]]'''*'''Student''':
[[User:Juhovh|Juho Vähä-Herttua]] *'''Mentor''': Ilkka
Ollakka*'''Abstract''':

I was selected to do a project related to ASF and Matroska demuxers, but
since there's some overlap related to Matroska, my main goal now is to
improve the ASF demuxer as much as I can and then find another similar
project to work on the rest of the time.

== Implementing BD-J support in libbluray and VLC ==

*'''Project page: [[SoC 2010/Implementing BD-J support in libbluray and
VLC]]'''*'''Student''': [[User:Will07c5|William Hahne]] *'''Mentor''':
[[User:Jpsaman|Jean-Paul Saman]]*'''Abstract''':

This project will focus primarily on getting BD-J (Blu-ray Disc Java)
support into libbluray. BD-J support is important because many of the
advanced features and extra content in Blu-ray movies uses BD-J.
Currently people with Blu-ray drives are tied to Windows if they want to
access this content, they are forced to use proprietary Blu-ray software
which does not run on Linux or various other operating systems. This
project will also integrate the BD-J support into VLC.

== Interface for mobile phones (WinCE and others) ==

*'''Project page: '''[[SoC 2010/Interface for mobile phones|'''Interface
for mobile phones<br>''']]*'''Student:''' [[User:Vnik|Kumar Anik]]<br>
*'''<u></u>Mentor:''' [[User:Geal|Geoffroy Couprie]]<br>*'''Abstract:
'''

To develop a GUI for Mobiles, especially WinCE ones.

== Ogg demuxer ==

*'''Project page: [[SoC 2010 Ogg Demuxer]]'''*'''Student''':
[[User:salsaman|salsaman]] *'''Mentor''': Christophe
Mutricy*'''Abstract''':

I was selected to rewrite the ogg demuxer. I wrote an ogg/theora demuxer
already for LiVES, but I am in the process of learning about other
stream types within ogg (e.g. dirac, vorbis, kate, speex and flac).

== DLNA UPnP Server/Client Modules ==

*'''Project page: [[SoC 2010/DLNA UPnP Server Client
Modules]]'''*'''Student''': [[User:Aust|Austin Burrow]] *'''Mentor''':
Konstantin Pavlov*'''Abstract''':

Implement Server/Client modules into VLC that are compatible with the
DLNA specification for UPnP.

== Media Library integration and LV2 Audio filters ==

*'''Project page: [[SoC 2010/Media Library and LV2]]'''*'''Student''':
[[User:jetru|Srikanth Raju]] *'''Mentor''': [[User:J-Peg|Jean-Philippe
André]]*'''Abstract''':

Complete integrating Media Library with the VLC UI and also implement
LV2 filters module

== [De]Muxer/Codec Layer fixes and improvements ==

*'''Project page: [[SoC 2010/Demux and codec layer
improvements]]'''*'''Student''': [[User:jai|Jai Menon]] *'''Mentor''':
[[User:J-b|Jean-Baptiste Kempf]]*'''Abstract''':

This project aims at improving the current [de]mux and codec layer in
VLC with a specific focus on matroska and the avformat/avcodec wrappers.
Details on what is being worked on would be tracked on the project page.

<br>

= List of current x264 projects = ==Support for high bit depth
encoding== \* '''Project page''': [[SoC 2010/High Bit Depth Encoding]]
\* '''Student''': [[User:IrockHolger Lubitz]] \* '''Abstract''':

The primary goal for this project is to prepare the code base of x264
for encoding H.264 video with user defined sample depths. This will
involve templating the encoder and migrating existing C code for use
with higher sample depths.

==Audio support== \* '''Project page''': [[SoC 2010/Audio on x264]] \*
'''Student''': [[User:KovenskyJason Garret-Glaser]] \* '''Abstract''':

Implement an audio filtering system that allows transcoding of audio
with resampling, sample format conversion and channel remixing. This is
meant to be used for using with the soon-to-be-merged video filtering
system for doing transcoding using only x264. Is also a prerequisite for
the planned --device option that will automatically downscale the video
if needed, set the appropriate H.264 level options and transcode to the
appropriate audio codec.

==Macroblock adaptive frame-field interlacing== \* '''Project page''':
[[SoC 2010/Macroblock adaptive frame field interlacing]] \*
'''Student''': [[User:SimonhorlickJason Garret-Glaser]] \*
'''Abstract''':

Currently x264 supports interlaced encoding with MBAFF frame structure
where each macroblock is encoded as interlaced. This project will
implement full adaptive interlacing support where macroblocks are
encoded as progressive or interlaced depending on their content.

= List of current VLMC projects = ==VLMC Youtube Integration+==

-  '''Project page: [[SoC 2010/Youtube Integration VLMC|SoC 2010/Youtube
   Integration in VLMC]]'''
-  '''Student''': [[User:Rohityadav|Rohit Yadav]]
-  '''Mentor''': Ludovic 'etix' Fauvet
-  '''Abstract''':

Youtube is the most popular video sharing website, right now. VLMC is a
video editing software and having features in VLMC to search-retrieve
videos, directly upload/update/delete videos on Youtube, within the
application itself, would be awesome. The aim of this project is to
write a small C++/Qt based Youtube client library for VLMC that provides
her all the APIs to perform all those things.

= List of current Phonon projects = == PCM I/O API ==

-  '''Project page''': [[SoC 2010/PCM IO API (Phonon)]]
-  '''Student''': [[User:Mforney|Michael Forney]]
-  '''Mentor''': Jean-Baptiste Kempf
-  '''Abstract''':

Design a fully featured PCM I/O API for Phonon, and provide an
implementation for the Phonon-VLC backend and one other (either MPlayer
or Xine). This API will allow developers to capture PCM data from
devices like a sound card, or to play back raw audio from memory, or
elsewhere. This will provide some important missing features in Phonon,
and open the door for many applications waiting to make use of an API
like this.

== Capture API ==

-  '''Project page: [[SoC 2010 Phonon Capture API]]'''
-  '''Student''': [[User:Skelet|Casian Andrei]]
-  '''Mentor''': Hugo Beauzee-Luyssen
-  '''Abstract''':

The goal of this project is to enable Phonon applications to access and
display input devices, like webcams. The Phonon code-base is well
designed and flexible, and apparently no major modifications are needed
to the current API. The ease of use for the Phonon application developer
is a priority. Features implemented in Phonon will be implemented in the
Phonon-VLC back-end in parallel. Various device classes should be
supported.

[[Category:SoC 2010 Project|*]]
