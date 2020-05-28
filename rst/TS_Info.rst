In the Open Source multimedia field there are various choices for multimedia streaming and playback. However analysing and checking validity of `MPEG-TS <MPEG-TS>`__ streams is not really possible. DVBsnoop (http://dvbsnoop.sourceforge.net/) is the only application that is only one that comes near this goal, but it is a commandline utility. This doesn't make it easy to be used.

The goal of TS Info is to be an easy to use MPEG-TS (MPTS/SPTS) analyser with all the information, analysis and validation right under you finger tips.

It should also be possible to insert the TS Analyser/TS Monitor in between the client and the server and monitor the stream for the boundaries configured. If the boundaries (or rules) are crossed, then a trigger will be sent to indicate a deviation from the required settings.

Features
--------

-  Input from TS/RTP/UDP or TS/UDP
-  Possible extension to use linux-dvb device (maybe use `dvblast <dvblast>`__ as input)
-  PID list and bandwidths / %age - bargraph
-  `Bitrates <Bitrate>`__ (also audio and video separate)
-  Mux distance of audio and video packets
-  SI table parsing (NIT, PMT, PAT, EIT, CAT, etc.) / descriptor parsing
-  Detect scrambled content (check scrambling bits 11, 10, optional 01/00)
-  `I-frame <I-frame>`__ gap
-  Determine `GOP <GOP>`__ length
-  Detect Open/Closed GOP
-  Teletext/closed captioning detection
-  CRC errors
-  I-frame decoding
-  Discontinuity indication
-  Subtitle decoding
-  EPG grid
-  PID selection and forwarding to VLC (via UDP stream?)
-  Triggers on deviation from set boundaries (mux distance < 500ms, if not then sent trigger eg: sms/e-mail)
-  Mention conformance to which standard and link to it if online source is available

Architecture
------------

proposal:

-  TS Analyser GUI - user interface to browse the MPEG-TS stream content (information gathered is similar to DVBsnoop)
-  TS Analyser - real-time MPEG-TS analyser that informs the GUI/TS Monitor of features discovered and various measurements
-  TS Monitor - real-time MPEG-TS monitor that triggers on deviations of preferred features in the MPEG-TS stream

::

                                        TS Analyser GUI
                                              |

   MPEG-TS --------> RTP/UDP input ---> TS Analyser --> RTP/UDP output
   (MPTS/SPTS)                                |
                                        TS Monitor --> send trigger if deviation detected

License
-------

-  TS Analyser GUI : GPLv2
-  TS Analyser library : LGPLv2.1
-  TS Monitor daemon : GPLv2

`Category:Dev Discussions <Category:Dev_Discussions>`__
