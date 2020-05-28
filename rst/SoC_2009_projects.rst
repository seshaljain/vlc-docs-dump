Here is a list of the accepted projects for Google Summer of Code 2OO9.

List of current VLC projects
============================

QuickTimeVR Playback
--------------------

-  **Project page:**\ `SoC 2009/QuickTimeVR Playback <SoC_2009/QuickTimeVR_Playback>`__
-  **Student**: `León Moctezuma <User:Leonox>`__
-  **Mentor**: `Antoine Cellerier <User:Dionoea>`__
-  **Comentor**: Yuval Levy
-  **Abstract**:

   VLC is a cross platform media player widely used and FreePV is a panoramic viewer that was initially developed due to the lack of an implementation of QuickTime and Shockwave for Linux, both work with QuickTime files and the problem arise from that, since video and vr share the mime type, to solve this, the main goal is to integrate the FreePV library into VLC to enable it to play QuickTimeVR contents, the second goal is to explore the use of wiimote as an advance interaction method.

Media Library
-------------

-  **Project page:**\ `SoC 2009/Media Library <SoC_2009/Media_Library>`__
-  **Student**: `Srikanth Raju <User:jetru>`__
-  **Mentor**: `Jean-Philippe Andre <User:J-Peg>`__
-  **Abstract**:

   The project is about extending the Media Library(ML) for VLC Player. The media library will allow users to manage all their local and network media. The project will use the basic structure that already exists for the ML and will focus on extending the features. New features include Search, Smart playlists, Annotations and "Just play music".

Lua Services Discovery
----------------------

-  **Project page:**\ `SoC 2009/Lua Services Discovery <SoC_2009/Lua_Services_Discovery>`__
-  **Student**: `Fabio Ritrovato <User:Sephiroth87>`__
-  **Mentor**: `Jean-Philippe Andre <User:J-Peg>`__
-  **Abstract**:

   The main goal of this project will be giving VideoLAN a Lua framework to load scriptable services discovery, to make them easier to write, if they don't require C complexity.
   Second goal will be giving VideoLAN access to a great number of online music and video services, like Jamendo, Magnatune, youtube, Dailymotion, etc..., using the new Lua modules.

A Media Center Interface for VLC
--------------------------------

-  **Project page:**\ `SoC 2009/Media Center Interface for VLC <SoC_2009/Media_Center_Interface_for_VLC>`__
-  **Student**: `Barry Wardell <User:barrywardell>`__
-  **Mentor**: `Ilkka Ollakka <User:ILEoo>`__
-  **Abstract**:

   While it is easy to use and functional, the existing default, Qt based GUI for VLC is quite minimal and basic. I propose to develop a new "Media Center" style GUI. This GUI will be based on Qt/OpenGL and will aim to be aesthetically pleasing, while remaining easy to use and functional. It will draw on many nice features of other popular media center software such as Front Row, Windows Media Center and XBMC.

Qt Interface Improvements
-------------------------

-  **Project page:**\ `SoC 2009/Qt Interface Improvements <SoC_2009/Qt_Interface_Improvements>`__
-  **Student**: `Cyril Nikolaev <User:cyril7>`__
-  **Mentor**: `Jean-Baptiste Kempf <User:J-b>`__
-  **Abstract**:

   Though existing Qt interface offers the user extensive control over VLC functionality, there is much to do from a usability point of view. The project aims to streamline the interface, deliver it from pointless elements and integrate neatly the uncoordinated dilog boxes (like Adjustments or Playlist) into main interface. Reorganization of the interface would reduce user efforts (and mouse click) needed to access desired feature.

DXVA integration
----------------

-  **Project page:**\ `SoC 2009/DXVA integration <SoC_2009/DXVA_integration>`__
-  **Student**: `Geoffroy Couprie <User:Geal>`__
-  **Mentor**: Jérôme Decoodt
-  **Abstract**:

   The Windows DXVA API gives access to video decoding and processing in the graphic card. Decoding with the GPU will reduce the load on the CPU and (hopefully) speed up the decoding. This project aims at creating a MPEG2 and H.264 decoder for VLC using this API.

RTMP Flash Streaming
--------------------

-  **Project page:**\ `SoC 2009/RTMP Flash Streaming <SoC_2009/RTMP_Flash_Streaming>`__
-  **Student**: `Zhigang Wang <User:zhigang>`__
-  **Mentor**: `Remi Denis-Courmont <User:Courmisch>`__
-  **Abstract**:

   This project is about to implement the RTMP Streaming function for VLC media player. It includes RTMP input and output parts(Fix bugs in RTMP input module and total rewrite the RTMP output module). while Adobe is about to publish the RTMP protocol spec in the first half of this year, It's the time to do this job.

Audio Filters in lua
--------------------

-  **Project page:**\ `SoC_2009/Audio_Filter_Improvement <SoC_2009/Audio_Filter_Improvement>`__
-  **Student**: Xiang Wang
-  **Mentor**: `Antoine Cellerier <User:Dionoea>`__
-  **Abstract**:

   Lua script language has been used successfully to VLC.First I'll try to create scriptable new audio filters in lua and enable users to create whatever audio filtering function they want in a Lua script. The second task is to implement new algorithm for 3D effects of VLC filters.

GPU Decoding
------------

-  **Project page:**\ `SoC_2009/GPU_Decoding_Support <SoC_2009/GPU_Decoding_Support>`__
-  **Student**: `Etienne Membrives <User:Sterops>`__
-  **Mentor**: `Jean-Paul Saman <User:jpsaman>`__
-  **Abstract**:

   The Video Acceleration API is an API designed to provide hardware acceleration for graphic application using the processing power of graphic cards. Drivers exists for Intel graphic cards. This project aims to implement a decoder and the corresponding video output for VLC, using the power of VA API to reduce CPU consumption while reading h.264, VC-1 and MPEG-4 videos.

libprojectM and p2p access
--------------------------

-  **Project page:**\ `SoC_2009/p2p_projectM <SoC_2009/p2p_projectM>`__
-  **Student**: `Rémi Duraffort <User:ivoire>`__
-  **Mentor**: `Pavlov Konstantin <User:thresh>`__
-  **Abstract**:

   The first goal of this project is to integrate libprojectM, an audio visualization library, into VLC. The second goal is to make VLC able to directly access to p2p content. This approach is a first step for the intagration of on-demand p2p streaming into VLC media player.

List of current x264 projects
=============================

ARM NEON Optimization
---------------------

-  **Project page:**\ `SoC 2009/ARM NEON Optimization <SoC_2009/ARM_NEON_Optimization>`__
-  **Student**: `David Conrad <User:conrad>`__
-  **Mentor**: Holger Lubitz
-  **Abstract**:

   Formerly used primarily in PDAs and cellphones, ARM is starting to target netbooks and laptops with its new Cortex-A series of processors. One key feature of these new processors is the NEON SIMD unit, the use of which will massively boost the performance of many multimedia applications. This project will consist of writing NEON/ARMv6 SIMD assembly for all of the major DSP functions in x264, ideally speeding x264 up by over 4-5 times.

Weighted P-frame Prediction
---------------------------

-  **Project page:**\ `SoC 2009/Weighted P-frame Prediction <SoC_2009/Weighted_P-frame_Prediction>`__
-  **Student**: `Dylan Yudaken <User:Dylan>`__
-  **Mentor**: Jason Garrett-Glaser
-  **Abstract**:

   x264 is a highly popular h264 encoder. It currently does not implement the entire spec of h264. Currently weighted P-frames are not used to assist in prediction. If implemented this would give huge benefits in cases where the scene fades or where there are flashes. I am proposing to implement an implementation of this that is good enough and fast enough to warrant inclusion in most video encodings.

444 422
-------

-  **Project page:**\ `SoC_2009/4:4:4_and_4:2:2_Colorspaces <SoC_2009/4:4:4_and_4:2:2_Colorspaces>`__

List of current VLMC projects
=============================

Enhancing VLMC
--------------

-  **Project page:**\ `SoC 2009/Enhancing VLMC <SoC_2009/Enhancing_VLMC>`__
-  **Student**: `Hugo Beauzee-Luyssen <User:chouquette>`__
-  **Mentor**: Ludovic 'etix' Fauvet
-  **Abstract**:

   The aim of this student project is to provide a functionnal video generation workflow for the video editing tool 'VLMC'. It includes an effect and a transition API, in order to allow developpers to create new modules for this application. This project will be developped closely with VLMC team, so they can add required features, such as the timeline, a previsualisation widget, and many others...

`\* <Category:SoC_2009_Project>`__
