.. raw:: mediawiki

   {{see also|Documentation:Modules}}

.. raw:: mediawiki

   {{wikipedia|List of codecs}}

.. raw:: mediawiki

   {{mmwiki|label1=Video codecs|Category:Video_Codecs|label2=Audio codecs|Category:Audio_Codecs|label3=Containers|Category:Container_Formats}}

A part of the program which understands a type of video or audio (short for **Co**\ der/\ **Dec**\ oder or **Co**\ mpression/\ **Dec**\ ompression). DivX and Theora are examples of video codecs; MP3 and Vorbis are audio codecs. The output stream produced when a codec to audio or video is generally "muxed" into a container format, such as AVI or Ogg. As certain codecs are often associated with certain container formats, the name of the container is often used to imply the codec, such as "Ogg", which usually refers to a Vorbis stream in an Ogg container.

To know what codecs are readable with , *see*\ `VLC Features Formats <VLC_Features_Formats>`__.

For `portability to almost all decoders <http://discerning.com/topics/audiovideo/video_encoding.html>`__, we recommend using the `MPEG-1 <MPEG-1>`__ standard of **``vcodec``**\ ``=``\ **``mp1v``**, **``acodec``**\ ``=``\ **``mpga``**, and **``mux``**\ ``=``\ **``mpeg1``**. See the `MPEG <MPEG>`__ Wiki page for more details on the other MPEG standards.

To save a file in a different codec, you can use the `streaming wizard <Documentation:Streaming_HowTo_New#Streaming_using_the_GUI>`__ or `transcode <transcode>`__ from the `command prompt <command_prompt>`__ with a command like this:

``vlc file --sout='#transcode{``\ **``vcodec``**\ ``=``\ **``mp1v``**\ ``,``\ **``vb``**\ ``=``\ **``1024``**\ ``,``\ **``acodec``**\ ``=``\ **``mpga``**\ ``,``\ **``ab``**\ ``=``\ **``128``**\ ``}:std{access=file,``\ **``mux``**\ ``=``\ **``mpeg1``**\ ``,``\ **``dst``**\ ``=``\ **``C:\file_name.mpg``**\ ``}'``

 Video Codecs
------------

.. raw:: mediawiki

   {{See also|Category:Video codecs}}

Use the "name" part in your ``vcodec=...`` commands

======== ======================================================================================
**name** *description*
**mp1v** `MPEG-1 <MPEG-1>`__ Video - recommended for portability
**mp2v** `MPEG-2 <MPEG-2>`__ Video - used in DVDs
**mp4v** `MPEG-4 <MPEG-4>`__ Video
**SVQ1** `Sorenson Video <Sorenson_Video>`__ v1
**SVQ3** Sorenson Video v3
**DVDv** `VOB <MPEG-2>`__ Video - used in DVDs
**WMV1** `Windows Media Video <Windows_Media_Video>`__ v1
**WMV2** Windows Media Video v2
WMV3     Windows Media Video v3, also called Windows Media 9 (`unsupported <VSG:Format:WMV>`__)
**DVSD** `Digital Video <Digital_Video>`__
**MJPG** `MJPEG <MJPEG>`__
**H263** `H263 <H263>`__
**h264** `H264 <H264>`__
**theo** `Theora <Theora>`__
**IV20** `Indeo Video <Indeo_Video>`__
IV40     Indeo Video version 4 or later
**RV10** `Real Media Video <Real_Media_Video>`__
**cvid** `Cinepak <Cinepak>`__
**VP31** On2 `VP3 <VP3>`__
**FLV1** `Flash Video <Flash_Video>`__
**CYUV** `Creative YUV <Creative_YUV>`__
**HFYU** `Huffman YUV <Huffman_YUV>`__
**MSVC** Microsoft Video v1
**MRLE** Microsoft `RLE <RLE>`__ Video
**AASC** `Autodesk Animator Studio Codec <Autodesk_Animator_Studio_Codec>`__ RLE Video
**FLIC** `FLIC <FLIC>`__ video
**QPEG** `QPEG <QPEG>`__ Video
**VP8**  `VP8 <VP8>`__ Video
======== ======================================================================================

 Audio Codecs
------------

.. raw:: mediawiki

   {{See also|Category:Audio codecs}}

Use the "name" part in your ``acodec=...`` commands

======== ==================================================================
**name** *description*
**mpga** `MPEG audio <MPEG_audio>`__ (recommended for portability)
**mp3**  `MPEG Layer 3 audio <MP3_audio>`__
**mp4a** `MP4 audio <MP4_audio>`__
**a52**  `Dolby Digital <Dolby_Digital>`__ (`A52 <A52>`__ or `AC3 <AC3>`__)
**vorb** `Vorbis <Vorbis>`__
**opus** `Opus <Opus>`__
**spx**  `Speex <Speex>`__
**flac** `FLAC <FLAC>`__
======== ==================================================================

No-"name" Codecs
~~~~~~~~~~~~~~~~

-  `DTS <DTS>`__
-  `AAC (Advanced Audio Coding) <AAC_(Advanced_Audio_Coding)>`__
-  `Windows Media Audio <Windows_Media_Audio>`__
-  `DV Audio <DV_Audio>`__
-  `LPCM <LPCM>`__
-  `ADPCM <ADPCM>`__
-  `AMR <AMR>`__
-  `QuickTime Audio <QuickTime_Audio>`__
-  `RealAudio <RealAudio>`__
-  `MACE <MACE>`__
-  `MusePack <MusePack>`__

Subtitle Codecs
---------------

See `Subtitles codecs <Subtitles_codecs>`__ for more information.

=========================== ================================================================================================================
**CVD**                     `CVD <CVD>`__
**SVCD (Overlay Graphics)** `SVCD Subtitle (OGT) Information <http://www.vcdimager.org/pub/vcdimager/manuals/0.7/svcd-ogt-subtitles.html>`__
**SRT**                     `SubRip <SubRip>`__
**SSA/ASS**                 `SubStation Alpha <SubStation_Alpha>`__
**SubViewer**               `SubViewer <SubViewer>`__
**VobSub**                  `VobSub <VobSub>`__
**DVD subtitles**           `DVD subtitles <DVD_subtitles>`__
**DVB subtitles**           `DVB subtitles <DVB_subtitles>`__
**VPlayer**                 `Vplayer <Vplayer>`__
**MicroDVD**                `MicroDVD <MicroDVD>`__
**SAMI**                    `SAMI <SAMI>`__
=========================== ================================================================================================================

Muxers
------

Use the "name" part in your ``mux=...`` commands

========= =========================================================================================================================================
**name**  *description*
**mpeg1** `MPEG-1 <MPEG-1>`__ multiplexing - recommended for portability. Only works with mp1v video and mpga audio, but works on all known players
**ts**    `MPEG Transport Stream <MPEG-TS>`__, primarily used for streaming MPEG. Also used in DVDs
**ps**    `MPEG Program Stream <MPEG-PS>`__, primarily used for saving MPEG data to disk.
**mp4**   `MPEG-4 mux format <MPEG-4>`__, used only for MPEG-4 video and MPEG audio.
**avi**   `AVI <AVI>`__
**asf**   `ASF <ASF>`__
**dummy** `dummy <dummy>`__ output, can be used in creation of `MP3 <MP3>`__ files.
**ogg**   `Xiph.org <Xiph.org>`__'s `ogg <ogg>`__ container format. Can contain audio, video, and metadata.
========= =========================================================================================================================================

See Also
--------

-  `FourCC <FourCC>`__ and http://www.fourcc.org/
-  http://discerning.com/topics/audiovideo/video_encoding.html

.. raw:: mediawiki

   {{stub}}

`\* <Category:Codecs>`__ `Category:Glossary <Category:Glossary>`__
