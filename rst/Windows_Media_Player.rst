.. raw:: mediawiki

   {{wikipedia|Windows Media Player}}

Windows Media Player is the standard multimedia `player <player>`__ for Microsoft® `Windows <Windows>`__\ ® systems.

Supported formats
-----------------

According to Microsoft® `Knowledge Base Article 316992 <http://support.microsoft.com/kb/316992>`__, Windows Media Player supports the following formats "out of the box":

========================== ========================================================================
Type                       Supported formats
========================== ========================================================================
Microsoft® media formats   -  Advanced Systems Format (.`asf <asf>`__)
                           -  Audio Visual Interleave (.`avi <avi>`__)
                           -  Audio for Windows (.`wav <wav>`__)
                           -  Microsoft® Digital Video Recording (.dvr-ms)
                           -  Windows Media Audio (.`wma <wma>`__)
                           -  Windows Media Video (.wmv, .wm)
Microsoft® media metafiles -  Advanced Stream Redirector (.asx)
                           -  Windows Media Audio Redirector (.wax)
                           -  Windows Media Download Package (.wmd)
                           -  Windows Media Player Playlist (.wpl)
                           -  Windows Media Redirector (.wmx)
                           -  Windows Media Video Redirector (.wvx)
ISO/IEC (MPEG)             -  MPEG-1 (.mpeg, .mpg, .m1v)
                           -  MPEG Audio Layer III (.`mp3 <mp3>`__)
                           -  MPEG Audio Layer II (.mp2, .mpa)
                           -  Metafile Playlist (.`m3u <m3u>`__)
Industry standard          -  Audio Interchange File Format ( .aif, .aifc, .\ `aiff <aiff>`__)
                           -  CD Audio Track (.cda)
                           -  Musical Instrument Digital Interface (.mid, .\ `midi <midi>`__, .rmi)
                           -  Sun Microsystems and NeXT (.`au <au>`__, .snd)
========================== ========================================================================

Common Issues
-------------

MPEG-2 and MPEG-4 playback
~~~~~~~~~~~~~~~~~~~~~~~~~~

Microsoft® does not bundle `codecs <codec>`__ for `MPEG-2 <MPEG-2>`__ or `MPEG-4 <MPEG-4>`__ with Windows and recommends purchasing them as part of a "DVD decoder pack" from a third-party vendor.

The symptom associated with a missing codec is Windows Media Player displaying the cryptic "C00D11CD" error code immediately after opening an MPEG-2 or MPEG-4 coded file or stream. At that point, you must purchase the appropriate codec, perhaps from Microsoft's® `list of approved vendors <http://www.microsoft.com/windows/windowsmedia/player/plugins.aspx>`__.

Streaming from VLC
~~~~~~~~~~~~~~~~~~

To date, the only option for streaming from VLC to Windows Media Player is to:

-  `Transcode <Transcode>`__ the file or feed into `WMV <WMV>`__ format
-  Encapsulate the transcoded stream in the `ASF <ASF>`__ container format
-  Use `MMS <MMS>`__ or `MMSH <MMSH>`__ for the stream transport

.. raw:: mediawiki

   {{forum|255}}

.

Otherwise, Windows Media Player does not appear to support streaming for anything other than its proprietary formats.

   '' "Windows Media Player 9 Series can play files in a wide variety of digital media file formats, but Windows Media Services 9 Series **cannot stream all of those files**. In certain cases, you may need to convert digital media files into a compatible format before you can stream them." `1 <http://www.microsoft.com/windows/windowsmedia/forpros/server/faq.aspx#2_3>`__ ''

Streaming to Windows Media Player over `HTTP <HTTP>`__ is supported, but the multimedia stream must be converted to a Microsoft-proprietary format with `Windows Media Encoder <Windows_Media_Encoder>`__ beforehand.

Streaming is known to work with Windows Media Player 9 or higher. In particular, Windows Media Player 8 does not interoperate with VLC.

Compatibility
~~~~~~~~~~~~~

If you discover problems with your Windows Media Player please download the latest version:

-  `English <https://www.microsoft.com/EN-US/download/windows-media-player-details.aspx>`__
-  `Deutsch <https://www.microsoft.com/DE-DE/download/windows-media-player-details.aspx>`__
-  `Français <https://www.microsoft.com/FR-FR/download/windows-media-player-details.aspx>`__

.. raw:: mediawiki

   {{Outdated}}

`Category:Player <Category:Player>`__ `Category:Windows <Category:Windows>`__
