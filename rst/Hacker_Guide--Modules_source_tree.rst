.. raw:: mediawiki

   {{Back to|Hacker Guide}}

This page lists the content of the directory in the `source tree of VLC <{{#rel2abs:../VLC_source_tree}}>`__, aimed at giving new beginners an overview of the code.

The directories are listed in alphabetical order, with an overview of their contents on the right. Any first level subdirectories are shown as well.

For detailed documentation on VLC modules, please see `Documentation:Modules <Documentation:Modules>`__.

**Note:** This table is by no means exhaustive. Note that only plugins with their own subdirectories are listed; plugins inside the parent directories are not emphasized unless they are too important. For a comprehensive list of the plugins VLC makes use of, consult in your source code checkout.

================== ============================================= ===================================================================================================================================================================================================================================================================
Directory Name     Subdirectory Name                             Directory Explanation
================== ============================================= ===================================================================================================================================================================================================================================================================
access                                                           protocols to access streams through network (http,ftp,fake,tcp,udp etc.), access to physical media like cd's and dvd's
\                  cdda                                          input module to read audio CDs
\                  dshow                                         DirectShow access plugin for encoding cards under Windows
\                  dvb                                           input module for DVB-S/C/T streaming using v4l2 API
\                  `mms <Documentation:Modules/mms>`__           MMS over TCP, UDP and HTTP access module
\                  rtsp                                         
\                  `screen <Documentation:Modules/screen>`__     an input module that takes screenshots of the primary monitor
\                  vcd                                           input module for accessing Video CDs.
\                  vcdx                                          input module for accessing Video CDs with navigation & stills
\                                                               
access-filter                                                    Includes the following filters: `timeshift <Documentation:Modules/timeshift>`__, `record <Documentation:Modules/record>`__, `dump <Documentation:Modules/dump>`__, which are used for ?????
\                                                               
access-output                                                   
\                                                               
audio-filter                                                     Various audio filters like decoders, equalizers, converters.
\                  channel-mixer                                 Various mixers and decoders like Dolby decoder
\                  converter                                     Fixed and floating-point audio format conversions such as AC/3 or MPEG I-II Audio Layer 1, 2, 3 decoding
\                  resampler                                     Various audio resampler
\                                                               
audio-mixer                                                      Mixer plugins.
\                                                               
audio-output                                                     Audio output plugins like ALSA, OSS and DirectX audio.
\                                                               
codec                                                            This directory includes various codecs, notably *ffmpeg* which is used for encoding and decoding various formats.
\                  cmml                                          Continuous Media Markup Language annotations/hyperlinks decoder
\                  dmo                                           a DirectMediaObject decoder that uses DirectMedia to decode video (WMV3)
\                  ffmpeg                                        Video decoder using the ffmpeg library
\                  spudec                                        RLE DVD subtitles decoder
\                  xvmc                                          XVMC video output and decoder
\                                                               
control                                                          Various interfaces to control the player: gestures, hotkeys, lirc, remote control (rc) and telnet
\                  `http <Documentation:Modules/http_intf>`__    HTTP remote control webinterface
\                                                               
demux                                                            Various demuxers
\                  asf                                           ASF demuxer
\                  avi                                           AVI File stream demuxer
\                  mp4                                           MP4 file input module
\                  mpeg                                         
\                  playlist                                      playlist import module???
\                                                               
gui                                                              GUI's for different platforms and the `ncurses <Documentation:Modules/ncurses>`__ interface
\                  `beos <Documentation:Modules/beos>`__         Audio output, video output and interface module for BeOS.
\                  `macosx <Documentation:Modules/macosx_gui>`__ Video output, and interface module for Mac OS X.
\                  pda                                           interface for iPaq using the Gtk2+ widget set.
\                  qnx                                           QNX RTOS plugin
\                  `qt4 <Documentation:Modules/Qt4>`__           interface module using the cross-platform Qt4 library: Multi-platform. This interface will be the default one upon subsequent releases.
\                  `skins2 <Documentation:Modules/skins2>`__     Skinnable interface, new generation
\                  wince                                         Pocket PC interface
\                  wxwidgets                                     interface module using the cross-platform wxWindows library: Multi-platform. The default interface as of VLC 0.86a.
\                                                               
meta-engine                                                     
\                                                               
misc                                                            
\                  dummy                                         Dummy (no GUI) audio output, video output, interface and input modules.
\                  memcpy                                        memory chunk copying module.
\                  notify                                        notifications using libnotify
\                  playlist                                     
\                  probe                                        
\                  testsuite                                    
\                  xml                                           LibXML and xtag xml parsers
\                                                               
mux                Various Muxers                               
\                  mpeg                                         
\                  rtp                                          
packetizer                                                       Packetizers for H264/AVC and MPEG 4 audio and video streams.
\                                                               
services-discovery                                              
\                                                               
stream-out                                                      
\                  transrate                                    
\                                                               
video-chroma                                                     Image conversions such as YUV to RGB
\                                                               
video-filter                                                     Various video filters like `Deinterlace <Documentation:Modules/deinterlace>`__, `Transform <Documentation:Modules/transform>`__, `Wall <Documentation:Modules/wall>`__, `Crop <Documentation:Modules/crop>`__, `Panoramix <Documentation:Modules/panoramix>`__ etc.
\                                                               
video-output                                                    
\                  directx                                       Video output module using the `Direct3D <Documentation:Modules/direct3d>`__ and `Direct X <Documentation:Modules/directx_vout>`__ API's ; `OpenGL <Documentation:Modules/glwin32>`__ for Windows.
\                  qte                                           video output module for Qt Embedded.
\                  `x11 <Documentation:Modules/x11>`__           video output module using the X11 API.
\                                                               
visualization                                                    Several visualizations, including `goom <Documentation:Modules/goom>`__
\                  galaktos                                      a visualization module that outputs OpenGL
\                  visual                                        visualisation system
================== ============================================= ===================================================================================================================================================================================================================================================================

See Also: `VLC User Guide - Chapter 2. Modules and options for VLC <http://www.videolan.org/doc/vlc-user-guide/en/ch02.html>`__

`Category:Building <Category:Building>`__
