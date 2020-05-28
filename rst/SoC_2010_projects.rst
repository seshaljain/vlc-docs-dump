Here is a list of the accepted projects for Google Summer of Code 2010.

List of current VLC projects
============================

Shader support for video post-processing
----------------------------------------

-  **Project page:**\ `SoC 2010 Shader Support <SoC_2010_Shader_Support>`__
-  **Student**: `Sasha Koruga <User:Skoruga>`__
-  **Mentor**: Adrien Maglo
-  **Abstract**:

A lot of video post-processing such as RGB-YUV conversion can be accelerated by using the GPU. This can either be achieved through a fragment shader, where it is the last step before a pixel is displayed on the screen, or it can be done with DirectCompute/CUDA/OpenCL. The method will vary depending on the task and intent. I will implement support for shaders by using the DirectX and OpenGL API and write a few shaders such as RGB-YUV conversion.

Port VLC Player to Symbian Platform
-----------------------------------

-  **Project page:**\ `SoC 2010 Shader Support <SoC_2010_Shader_Support>`__
-  **Student**: `Pankaj Yadav <User:pk2010>`__
-  **Mentor**: Rémi Duraffort
-  **Abstract**:

To port VLC Player to Symbian S60 Platform.

ASF demuxer
-----------

-  **Project page:**\ `SoC 2010 ASF Demuxer <SoC_2010_ASF_Demuxer>`__
-  **Student**: `Juho Vähä-Herttua <User:Juhovh>`__
-  **Mentor**: Ilkka Ollakka
-  **Abstract**:

I was selected to do a project related to ASF and Matroska demuxers, but since there's some overlap related to Matroska, my main goal now is to improve the ASF demuxer as much as I can and then find another similar project to work on the rest of the time.

Implementing BD-J support in libbluray and VLC
----------------------------------------------

-  **Project page:**\ `SoC 2010/Implementing BD-J support in libbluray and VLC <SoC_2010/Implementing_BD-J_support_in_libbluray_and_VLC>`__
-  **Student**: `William Hahne <User:Will07c5>`__
-  **Mentor**: `Jean-Paul Saman <User:Jpsaman>`__
-  **Abstract**:

This project will focus primarily on getting BD-J (Blu-ray Disc Java) support into libbluray. BD-J support is important because many of the advanced features and extra content in Blu-ray movies uses BD-J. Currently people with Blu-ray drives are tied to Windows if they want to access this content, they are forced to use proprietary Blu-ray software which does not run on Linux or various other operating systems. This project will also integrate the BD-J support into VLC.

Interface for mobile phones (WinCE and others)
----------------------------------------------

-  '''Project page: '''`Interface for mobile phones
    <SoC_2010/Interface_for_mobile_phones>`__
-  **Student:** `Kumar Anik <User:Vnik>`__
-  **Mentor:** `Geoffroy Couprie <User:Geal>`__
-  '''Abstract: '''

To develop a GUI for Mobiles, especially WinCE ones.

Ogg demuxer
-----------

-  **Project page:**\ `SoC 2010 Ogg Demuxer <SoC_2010_Ogg_Demuxer>`__
-  **Student**: `salsaman <User:salsaman>`__
-  **Mentor**: Christophe Mutricy
-  **Abstract**:

I was selected to rewrite the ogg demuxer. I wrote an ogg/theora demuxer already for LiVES, but I am in the process of learning about other stream types within ogg (e.g. dirac, vorbis, kate, speex and flac).

DLNA UPnP Server/Client Modules
-------------------------------

-  **Project page:**\ `SoC 2010/DLNA UPnP Server Client Modules <SoC_2010/DLNA_UPnP_Server_Client_Modules>`__
-  **Student**: `Austin Burrow <User:Aust>`__
-  **Mentor**: Konstantin Pavlov
-  **Abstract**:

Implement Server/Client modules into VLC that are compatible with the DLNA specification for UPnP.

Media Library integration and LV2 Audio filters
-----------------------------------------------

-  **Project page:**\ `SoC 2010/Media Library and LV2 <SoC_2010/Media_Library_and_LV2>`__
-  **Student**: `Srikanth Raju <User:jetru>`__
-  **Mentor**: `Jean-Philippe André <User:J-Peg>`__
-  **Abstract**:

Complete integrating Media Library with the VLC UI and also implement LV2 filters module

[De]Muxer/Codec Layer fixes and improvements
--------------------------------------------

-  **Project page:**\ `SoC 2010/Demux and codec layer improvements <SoC_2010/Demux_and_codec_layer_improvements>`__
-  **Student**: `Jai Menon <User:jai>`__
-  **Mentor**: `Jean-Baptiste Kempf <User:J-b>`__
-  **Abstract**:

This project aims at improving the current [de]mux and codec layer in VLC with a specific focus on matroska and the avformat/avcodec wrappers. Details on what is being worked on would be tracked on the project page.

| 

List of current x264 projects
=============================

Support for high bit depth encoding
-----------------------------------

-  **Project page**: `SoC 2010/High Bit Depth Encoding <SoC_2010/High_Bit_Depth_Encoding>`__
-  **Student**: `Oskar Arvidsson <User:Irock>`__
-  **Mentor**: `Holger Lubitz <User:Holger>`__
-  **Abstract**:

The primary goal for this project is to prepare the code base of x264 for encoding H.264 video with user defined sample depths. This will involve templating the encoder and migrating existing C code for use with higher sample depths.

Audio support
-------------

-  **Project page**: `SoC 2010/Audio on x264 <SoC_2010/Audio_on_x264>`__
-  **Student**: `Diogo Franco <User:Kovensky>`__
-  **Mentor**: `Jason Garret-Glaser <User:Dark_Shikari>`__
-  **Abstract**:

Implement an audio filtering system that allows transcoding of audio with resampling, sample format conversion and channel remixing. This is meant to be used for using with the soon-to-be-merged video filtering system for doing transcoding using only x264. Is also a prerequisite for the planned --device option that will automatically downscale the video if needed, set the appropriate H.264 level options and transcode to the appropriate audio codec.

Macroblock adaptive frame-field interlacing
-------------------------------------------

-  **Project page**: `SoC 2010/Macroblock adaptive frame field interlacing <SoC_2010/Macroblock_adaptive_frame_field_interlacing>`__
-  **Student**: `Simon Horlick-Loach <User:Simonhorlick>`__
-  **Mentor**: `Jason Garret-Glaser <User:Dark_Shikari>`__
-  **Abstract**:

Currently x264 supports interlaced encoding with MBAFF frame structure where each macroblock is encoded as interlaced. This project will implement full adaptive interlacing support where macroblocks are encoded as progressive or interlaced depending on their content.

List of current VLMC projects
=============================

VLMC Youtube Integration+
-------------------------

-  **Project page:**\ `SoC 2010/Youtube Integration in VLMC <SoC_2010/Youtube_Integration_VLMC>`__
-  **Student**: `Rohit Yadav <User:Rohityadav>`__
-  **Mentor**: Ludovic 'etix' Fauvet
-  **Abstract**:

Youtube is the most popular video sharing website, right now. VLMC is a video editing software and having features in VLMC to search-retrieve videos, directly upload/update/delete videos on Youtube, within the application itself, would be awesome. The aim of this project is to write a small C++/Qt based Youtube client library for VLMC that provides her all the APIs to perform all those things.

List of current Phonon projects
===============================

PCM I/O API
-----------

-  **Project page**: `SoC 2010/PCM IO API (Phonon) <SoC_2010/PCM_IO_API_(Phonon)>`__
-  **Student**: `Michael Forney <User:Mforney>`__
-  **Mentor**: Jean-Baptiste Kempf
-  **Abstract**:

Design a fully featured PCM I/O API for Phonon, and provide an implementation for the Phonon-VLC backend and one other (either MPlayer or Xine). This API will allow developers to capture PCM data from devices like a sound card, or to play back raw audio from memory, or elsewhere. This will provide some important missing features in Phonon, and open the door for many applications waiting to make use of an API like this.

Capture API
-----------

-  **Project page:**\ `SoC 2010 Phonon Capture API <SoC_2010_Phonon_Capture_API>`__
-  **Student**: `Casian Andrei <User:Skelet>`__
-  **Mentor**: Hugo Beauzee-Luyssen
-  **Abstract**:

The goal of this project is to enable Phonon applications to access and display input devices, like webcams. The Phonon code-base is well designed and flexible, and apparently no major modifications are needed to the current API. The ease of use for the Phonon application developer is a priority. Features implemented in Phonon will be implemented in the Phonon-VLC back-end in parallel. Various device classes should be supported.

`\* <Category:SoC_2010_Project>`__
