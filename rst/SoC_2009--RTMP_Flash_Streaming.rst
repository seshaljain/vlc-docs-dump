.. raw:: mediawiki

   {{SoCProject|year=2009|student=[[User:zhigang|Zhigang Wang]]|mentor=[[User:Courmisch|Remi Denis-Courmont]]}}

RTMP Streaming
==============

Abstract
--------

This project is about to implement the RTMP Streaming function for VLC media player. It includes RTMP input and output functions (Fix bugs in RTMP input module and total rewrite the RTMP output module). when Adobe is about to publish the RTMP protocol spec in the first half of this year, It's the time to do this job.

Schedule
--------

**Before May 23:**

-  Read more RTMP protocal documents.

**May 23 - July 5:**

-  RTMP input works half of the time.

   -  Fix bug and improve AMF/RTMP message decoder and encoder (I already found it will segment fault in function rtmp_handler_invoke() of modules/access/rtmp/rtmp_amf_flv.c). The source code of gnash project can be referenced to.
   -  Fix other bugs in RTMP input.
   -  Pause/Seek/Resume support (Input).

-  VLC can stream FLV over HTTP.

   -  FLV Encapsulation over HTTP is not work.
   -  FIX: MPEG-TS Encapsulation over HTTP with FLV file, the Video can not streaming(Audio Only)

**July 6 - July 13:**

-  Mid-term evaluations, Review the function I had implement, and fix the bug which had found.

**July 14 - August 9:**

-  Possibly rewrite from scratch RTMP output (never worked).

   -  Totally rewrite the RTMP access output module work flow (Reference to the existed HTTP access output module implement), make the RTMP access output module can listen and handle concurrent requests.
   -  Make RTMP access output module successfully handshake with flashplayer.
   -  After flashplayer can successfully handshake and invoke connect -> createStream -> play with our RTMP access output module, make sure sending the right packed flv video to flashplayer (Base on the existed source code and this doc: http://osflash.org/flv)
   -  Pause/Seek/Resume support (output)

**August 10 - August 25:**

-  code review and testing. Fix bugs if necessary.

**September 3 - September 9:**

-  Submitting required code samples to Google

Detail
------

May 23 - May 29:

-  Check packet boundary to avoid "segment fault"
-  Improve AMF message decoding
-  Minor modification to RTMP connect action
-  Add seek function. (Not work yet)

May 30 - Jule 5 (TODO):

-  RTMP SEEK function
-  PAUSE/RESUME
-  Check other possible bug and fix

Source Code
-----------

You can git clone using http from repo.or.cz.

``$ git clone ``\ ```http://repo.or.cz/r/vlc/zhigang.git`` <http://repo.or.cz/r/vlc/zhigang.git>`__

More Information: `1 <http://repo.or.cz/w/vlc/zhigang.git>`__

Reference
---------

Reference projects:

-  `Gnash project <http://www.gnashdev.org/>`__ (AMF in gnash/libamf and RTMP in gnash/libnet)
-  `Red5 <http://www.red5.org/>`__

Reference documents:

-  `RTMP Protocol introduction on Gnash project wiki <http://wiki.gnashdev.org/RTMP>`__
-  `AMF Protocol introduction on Gnash project wiki <http://wiki.gnashdev.org/AMF>`__
-  `RTMP Protocol introduction on OSFlash <http://osflash.org/documentation/rtmp>`__
-  `AMF Protocol introduction on OSFlash <http://osflash.org/documentation/amf>`__
-  `Flash Video file format <http://osflash.org/flv>`__
-  `Adobe will publish RTMP spec here <http://www.adobe.com/devnet/rtmp/>`__
