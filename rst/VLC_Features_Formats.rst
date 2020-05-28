.. raw:: mediawiki

   {{Back to|VLC Features}}

This is a new page that lists the audio/video codecs that VLC can or cannot read. It is still under development, don't hesitate to add a some `FourCC <FourCC>`__ and infos.

It should now be a bit more complete than the official features page on `VideoLAN website <https://www.videolan.org/vlc/features.html>`__.

If you have any question about those codecs, just consult our `Knowledge Base <Knowledge_Base>`__ or our friends on the `Multimedia Wiki <http://wiki.multimedia.cx>`__. If you don't find information, search with Wikipedia or Google.

Video Codecs
------------

Widely Used Video Codecs
~~~~~~~~~~~~~~~~~~~~~~~~

.. table:: **Most used Video Codecs**

   =========================================== ========================================================= ================== ================== ============================== ==================================================
   Name                                        FOURCC                                                    Playable           Encoder            library                        Comment
   =========================================== ========================================================= ================== ================== ============================== ==================================================
   MPEG-1 Part 2                               mpeg, mp1v, mpg1, PIM1                                    .. raw:: mediawiki .. raw:: mediawiki libmpeg2 , ffmpeg             
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{Yes}}                                       
   MPEG-2 Part 2                               mp2v, mpg2, vcr2, hdv1, hdv2, hdv3, mx*n, mx*p            .. raw:: mediawiki .. raw:: mediawiki libmpeg2 , ffmpeg             
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{Yes}}                                       
   MJPEG (A/B)                                                                                           .. raw:: mediawiki .. raw:: mediawiki ffmpeg                        
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{Yes}}                                       
   Divx (1, 2, 3)                              DIV1, DIV2, DIV3, mp41, mp42, MPG4, MPG3                  .. raw:: mediawiki .. raw:: mediawiki ffmpeg                        
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{Yes}}                                       
   DivX 4, 5, 6 , 3ivx D4, MPEG-4              DIV4, DIV5, DIV6, col1, col0, 3ivd                        .. raw:: mediawiki .. raw:: mediawiki ffmpeg                        
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{Yes}}                                       
   MPEG-4 Part 2 (AVP), Xvid                   DIVX, Xvid, mp4s, m4s2, xvid, mp4v, fmp4, 3iv2, smp4, ... .. raw:: mediawiki .. raw:: mediawiki ffmpeg                        
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{Yes}}                                       
   H.261                                       h261                                                      .. raw:: mediawiki .. raw:: mediawiki ffmpeg                        
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{Yes}}                                       
   H.262                                       h262                                                      .. raw:: mediawiki .. raw:: mediawiki ffmpeg                         Same as MPEG-2 Video
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{Yes}}                                       
   H.263 / H.263i                              h263                                                      .. raw:: mediawiki .. raw:: mediawiki ffmpeg                        
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{Yes}}                                       
   H.264 / X.264 (MPEG-4/AVC) (MPEG-4 Part.10) h264, s264, AVC1, DAVC, H264, X264, VSSH                  .. raw:: mediawiki .. raw:: mediawiki ffmpeg (decode), x264 (encode)
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{Yes}}                                       
   Sorenson 1 (Quicktime)                      SVQ 1                                                     .. raw:: mediawiki .. raw:: mediawiki ffmpeg                        
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{Yes}}                                       
   Sorenson 3 (Quicktime)                      SVQ 3                                                     .. raw:: mediawiki .. raw:: mediawiki ffmpeg                        
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{No}}                                        
   DV                                                                                                    .. raw:: mediawiki .. raw:: mediawiki ffmpeg                        
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{Yes}}                                       
   Cinepak                                     cvid                                                      .. raw:: mediawiki .. raw:: mediawiki internal, ffmpeg              
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{No}}                                        
   Theora                                      thra                                                      .. raw:: mediawiki .. raw:: mediawiki libtheora                     
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{Yes}}                                       
                                                                                                                                                                             
                                                                                                                            , violated                                       
   WMV 1/2 (7/8)                               wmv1, wmv2                                                .. raw:: mediawiki .. raw:: mediawiki ffmepg                        
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{Yes}}                                       
   WMV 3 / WMV-9 / VC-1                        wmv3, wvc1, wmva                                          .. raw:: mediawiki .. raw:: mediawiki ffmpeg                         Not all profiles are supported. See `DMO <DMO>`__.
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{No}}                                        
   On2 VP3,                                    VP31, VP30, VP3                                           .. raw:: mediawiki .. raw:: mediawiki ffmpeg                        
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{No}}                                        
   On2 VP5                                     VP50, VP5, VP51                                           .. raw:: mediawiki .. raw:: mediawiki ffmpeg                        
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{No}}                                        
   On2 VP6 (used by FLV)                       VP60, VP61, VP62, VP6F, VP6A                              .. raw:: mediawiki .. raw:: mediawiki ffmpeg                        
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{Yes}}                                       
   On2 VP7                                     VP7                                                       .. raw:: mediawiki .. raw:: mediawiki                               
                                                                                                                                                                             
                                                                                                            {{No}}             {{No}}                                        
   Flash Screen Video                          FSV1                                                      .. raw:: mediawiki .. raw:: mediawiki ffmpeg                        
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{Yes}}                                       
   Indeo Video 3                               IV31, IV32                                                .. raw:: mediawiki .. raw:: mediawiki ffmpeg                        
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{no}}                                        
   Indeo Video 4/5                             IV41, IV51                                                .. raw:: mediawiki .. raw:: mediawiki libavcodec                    
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{no}}                                        
   Real Video 1.0, 1.3, 2.0                    RV10, RV13, RV20                                          .. raw:: mediawiki .. raw:: mediawiki ffmpeg                        
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{Yes}}                                       
   Real Video 3.0, 4.0                         RV30, RV40                                                .. raw:: mediawiki .. raw:: mediawiki                               
                                                                                                                                                                             
                                                                                                            {{No}}             {{No}}                                        
   Dirac                                       BBCD                                                      .. raw:: mediawiki .. raw:: mediawiki dirac                         
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{Yes}}                                       
   Huffyuv / [STRIKEOUT:Lagarith]                                                                        .. raw:: mediawiki .. raw:: mediawiki ffmpeg                        
                                                                                                                                                                             
                                                                                                            {{Yes}}            {{Yes}}                                       
   \                                                                                                                                                                         
   =========================================== ========================================================= ================== ================== ============================== ==================================================

Rarer Video Codecs
~~~~~~~~~~~~~~~~~~

.. table:: **Less Used Video Codecs**

   =========================================== =========================== ================== ================== ======= =========================================
   Rare codecs                                 FOURCC                      Decoder            Encoder            library Comment
   =========================================== =========================== ================== ================== ======= =========================================
   Apple Animation, Graphics, Video, QuickDraw 'rle','smc ','rpza', 'qdrw' .. raw:: mediawiki .. raw:: mediawiki ffmpeg 
                                                                                                                        
                                                                              {{Yes}}            {{No}}                 
   SheerVideo                                                              .. raw:: mediawiki .. raw:: mediawiki         Professional use, no open source decoders
                                                                                                                        
                                                                              {{No}}             {{No}}                 
   CorePNG                                                                 ??                 ??                        
   MSU Lossless                                                            ??                 ??                        
   Snow                                                                    .. raw:: mediawiki .. raw:: mediawiki        
                                                                                                                        
                                                                              {{Yes}}            {{Yes}}                
   Pixlet                                                                  ??                 ??                        
   Rare codecs (Asus V1, Asus V2)              ASV1, ASV2                  .. raw:: mediawiki .. raw:: mediawiki ffmpeg 
                                                                                                                        
                                                                              {{Yes}}            {{Yes}}                
   Game Codecs (Some)                                                      .. raw:: mediawiki .. raw:: mediawiki ffmpeg 
                                                                                                                        
                                                                              {{Yes}}            {{no}}                 
   Tarkin                                                                  .. raw:: mediawiki .. raw:: mediawiki        
                                                                                                                        
                                                                              {{No}}             {{No}}                 
   QPEG                                        QPEG                        .. raw:: mediawiki .. raw:: mediawiki ffmpeg 
                                                                                                                        
                                                                              {{Yes}}            {{Untested}}           
   =========================================== =========================== ================== ================== ======= =========================================

Audio Codecs
------------

.. table:: **Audio Codecs Status**

   ========================== ==================================================== ================== ================== ============================================= ============================================================================================================================
   Name                       FOURCC                                               Decoder            Encoder            library                                       Comment
   ========================== ==================================================== ================== ================== ============================================= ============================================================================================================================
   MPEG-Audio 1 Layer-1/2     mpga                                                 .. raw:: mediawiki .. raw:: mediawiki libmad (decoding), twolame (encoding)         ISO/IEC MPEG
                                                                                                                                                                      
                                                                                      {{Yes}}            {{Yes}}                                                      
   MP3                        mp3, .mp3, LAME                                      .. raw:: mediawiki .. raw:: mediawiki libmad (decoding), ffmpeg-mp3lame             ISO/IEC MPEG - **(recompile needed for encoding)**
                                                                                                                                                                      
                                                                                      {{Yes}}            {{Yes}}                                                      
   AAC                        mp4a                                                 .. raw:: mediawiki .. raw:: mediawiki faad (decode), faac (encoding)                ISO/IEC MPEG
                                                                                                                                                                      
                                                                                      {{Yes}}            {{Yes}}                                                      
   HE-AAC                                                                          .. raw:: mediawiki .. raw:: mediawiki faad (decode), libaacplus + ffmpeg (encoding) ISO/IEC MPEG, AAC+ encoding through libaacplus + ffmpeg (patched) - untested **RECOMPILE VLC & ffmpeg for this** Audio codec
                                                                                                                                                                      
                                                                                      {{Yes}}            {{Untested}}                                                 
   AC-3                       a52, a52b                                            .. raw:: mediawiki .. raw:: mediawiki liba52 (decode), ffmpeg (encode)             
                                                                                                                                                                      
                                                                                      {{Yes}}            {{Yes}}                                                      
   ATRAC                      atrc                                                 .. raw:: mediawiki .. raw:: mediawiki                                              
                                                                                                                                                                      
                                                                                      {{Yes}}            {{No}}                                                       
   iLBC                       ILBC, ilbc                                           .. raw:: mediawiki .. raw:: mediawiki QuickTime (decode)                            (check for encoder and free decoder)
                                                                                                                                                                      
                                                                                      {{Untested}}       {{Untested}}                                                 
   Mu-Law                                                                          .. raw:: mediawiki .. raw:: mediawiki ffmpeg                                        (check for encoder)
                                                                                                                                                                      
                                                                                      {{Yes}}            {{No}}                                                       
   NellyMoser                                                                      .. raw:: mediawiki .. raw:: mediawiki ffmpeg                                       
                                                                                                                                                                      
                                                                                      {{Yes}}            {{No}}                                                       
   QCELP (PureVoice)          Qclp                                                 .. raw:: mediawiki .. raw:: mediawiki ffmpeg                                        Usually in QCP container. `buggy? <https://trac.videolan.org/vlc/ticket/5347>`__
                                                                                                                                                                      
                                                                                      {{Yes}}            {{No}}                                                       
                                                                                                                                                                      
                                                                                                      ?                                                               
   Real Audio                 lpcJ, 28_8, dnet, sipr, cook, atrc, raac, racp, ralf .. raw:: mediawiki .. raw:: mediawiki                                               Some work. Half don't
                                                                                                                                                                      
                                                                                      {{Yes}}            {{No}}                                                       
   Shorten                    shrn                                                 .. raw:: mediawiki .. raw:: mediawiki                                               ffmpeg and ffplay do it. VLC doesn't. (It is in the FOURCC list in VLC's --`Dionoea <User:Dionoea>`__)
                                                                                                                                                                      
                                                                                      {{No}}             {{No}}                                                       
   Speex                      spex                                                 .. raw:: mediawiki .. raw:: mediawiki libspeex                                     
                                                                                                                                                                      
                                                                                      {{Yes}}            {{Yes}}                                                      
   Vorbis                     vorb                                                 .. raw:: mediawiki .. raw:: mediawiki libvorbis                                    
                                                                                                                                                                      
                                                                                      {{Yes}}            {{Yes}}                                                      
   DTS                        dts                                                  .. raw:: mediawiki .. raw:: mediawiki libdca                                        DTS-HD unsupported
                                                                                                                                                                      
                                                                                      {{Yes}}            {{No}}                                                       
   MPC                                                                             .. raw:: mediawiki .. raw:: mediawiki libmpcdec                                    
                                                                                                                                                                      
                                                                                      {{Yes}}            {{No}}                                                       
   WMA 1/2                    wma1, wma2                                           .. raw:: mediawiki .. raw:: mediawiki ffmpeg                                        WMA9 is not supported
                                                                                                                                                                      
                                                                                      {{Yes}}            {{Yes}}                                                      
                                                                                                                                                                      
                                                                                                      , violated                                                      
   Flac                       flac                                                 .. raw:: mediawiki .. raw:: mediawiki libflac                                       lossless
                                                                                                                                                                      
                                                                                      {{Yes}}            {{Yes}}                                                      
   Apple Lossless Audio Codec alac                                                 .. raw:: mediawiki .. raw:: mediawiki ffmpeg                                        lossless
                                                                                                                                                                      
                                                                                      {{Yes}}            {{No}}                                                       
   Monkey's Audio                                                                  .. raw:: mediawiki .. raw:: mediawiki                                               lossless
                                                                                                                                                                      
                                                                                      {{Yes}}            {{No}}                                                       
   Musepack                                                                        .. raw:: mediawiki .. raw:: mediawiki libmpcdec                                    
                                                                                                                                                                      
                                                                                      {{Yes}}            {{No}}                                                       
   ADMPCM (various)                                                                .. raw:: mediawiki .. raw:: mediawiki ffmpeg and internal                          
                                                                                                                                                                      
                                                                                      {{Yes}}            {{Yes}}                                                      
   AMR                        samr                                                 .. raw:: mediawiki .. raw:: mediawiki ffmpeg + libamrnb + libamrwb                  **RECOMPILE VLC for this** Speech codec
                                                                                                                                                                      
                                                                                      {{Yes}}            {{Yes}}                                                      
   Sonic                      SONC                                                 .. raw:: mediawiki .. raw:: mediawiki ffmpeg                                       
                                                                                                                                                                      
                                                                                      {{Yes}}            {{Yes}}                                                      
   \                                                                                                                                                                  
   ========================== ==================================================== ================== ================== ============================================= ============================================================================================================================

Subtitles Codecs
----------------

.. raw:: mediawiki

   {{Transcluded|Subtitles codecs}}

.. raw:: mediawiki

   {{:Subtitles codecs}}

Format/Container/Muxers
-----------------------

.. table:: **Muxer**

   ==================================== ================================== ================== ================== =========================================
   Name                                 extensions                         Playable           Savable            Comment
   ==================================== ================================== ================== ================== =========================================
   3GP                                  .3gp                               .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                
                                                                              {{Yes}}            {{Untested}}   
   AIFF                                 .asf, .wmv                         .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                
                                                                              {{Yes}}            {{No}}         
   ASF                                  .asf, .wmv                         .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                
                                                                              {{Yes}}            {{Yes}}        
   AU                                   .au                                .. raw:: mediawiki                   
                                                                                                                
                                                                              {{Yes}}                           
   AVI                                  .avi                               .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                
                                                                              {{Yes}}            {{Yes}}        
                                                                                                                
                                                                                              , violated        
   DMF                                                                     .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                
                                                                              {{Untested}}       {{Untested}}   
   FLV                                  .flv                               .. raw:: mediawiki .. raw:: mediawiki through ffmpeg
                                                                                                                
                                                                              {{Yes}}            {{Yes}}        
   MOV                                  .mov                               .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                
                                                                              {{Yes}}            {{Yes}}        
   MP4                                  .mp4                               .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                
                                                                              {{Yes}}            {{Yes}}        
   OGG                                  .ogm, .ogg                         .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                
                                                                              {{Yes}}            {{Yes}}        
   MKV                                  .mkv, .mka                         .. raw:: mediawiki .. raw:: mediawiki Summer of Code 2007 Project
                                                                                                                
                                                                              {{Yes}}            {{No}}         
                                                                                                                
                                                                                              , WIP             
   MPEG-2 / TS                          .ts, .mpg                          .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                
                                                                              {{Yes}}            {{Yes}}        
   MPEG-2 / ES, PS, PVA, MP3            .mpg, .mp3, .mp2                   .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                
                                                                              {{Yes}}            {{Yes}}        
   NSC                                  .nsc                               .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                
                                                                              {{Yes}}            {{No}}         
   NSV                                  .nsv                               .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                
                                                                              {{Yes}}            {{No}}         
   Nut                                  .nut                               .. raw:: mediawiki .. raw:: mediawiki Muxable through libavformat
                                                                                                                
                                                                              {{Yes}}            {{Yes}}        
   Real                                 .ra, .ram, .rm, .rv , .rmbv        .. raw:: mediawiki .. raw:: mediawiki version 4 and 5, no support for version 3
                                                                                                                
                                                                              {{Partial}}        {{No }}        
   Raw (a52, dts, aac, flac, .dv, .vid) .a52, .dts, .aac, .flac, .dv, .vid .. raw:: mediawiki ??                
                                                                                                                
                                                                              {{Yes}}                           
   True Audio Codec                     .tta, .tac                         .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                
                                                                              {{Yes}}            {{No}}         
   Ty Tivo                              .ty                                .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                
                                                                              {{Yes}}            {{No}}         
   Wav                                  .wav, .dts                         .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                
                                                                              {{Yes}}            {{Yes}}        
   Xa                                   .xa                                .. raw:: mediawiki .. raw:: mediawiki
                                                                                                                
                                                                              {{Yes}}            {{No}}         
   \                                                                                                            
   ==================================== ================================== ================== ================== =========================================

HD-Discs codecs
---------------

.. raw:: mediawiki

   {{Transcluded|HD-Discs codecs}}

.. raw:: mediawiki

   {{:HD-Discs codecs}}

.. raw:: mediawiki

   {{DEFAULTSORT:*}}

`Category:Codecs <Category:Codecs>`__ `Category:Knowledge Base <Category:Knowledge_Base>`__
