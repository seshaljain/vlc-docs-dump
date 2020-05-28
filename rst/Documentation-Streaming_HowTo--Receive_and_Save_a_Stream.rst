.. raw:: mediawiki

   {{RightMenu|documentation streaming howto toc}}

Receive a stream with VLC
-------------------------

Receive an unicast stream
~~~~~~~~~~~~~~~~~~~~~~~~~

``{{%}} ``\ **``vlc``\ ````\ ``-vvv``\ ````\ ``rtp://``**

Receive a multicast stream
~~~~~~~~~~~~~~~~~~~~~~~~~~

``{{%}} ``\ **``vlc``\ ````\ ``-vvv``\ ````\ ``rtp://@239.255.12.42``**

where **239.255.12.42** is the multicast IP address you want to join.

Receive an HTTP/FTP/MMS stream
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use one of the following command lines:

``{{%}} ``\ **``vlc``\ ````\ ``-vvv``\ ````\ **\ ```http://example/stream.xyz`` <http://example/stream.xyz>`__

where http://example/stream.xyz is the HTTP address of the stream;

``{{%}} ``\ **``vlc``\ ````\ ``-vvv``\ ````\ **\ ```ftp://example/stream.xyz`` <ftp://example/stream.xyz>`__

where ftp://example/stream.xyz is the FTP address of the stream;

``{{%}} ``\ **``vlc``\ ````\ ``-vvv``\ ````\ **\ ```mms://viptvr.yacast.fr/encoderfranceinfo`` <mms://viptvr.yacast.fr/encoderfranceinfo>`__

where mms://viptvr.yacast.fr/encoderfranceinfo is the MMS address of the stream.

Receive a RTP stream available through RTSP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``{{%}} ``\ **``vlc``\ ````\ ``-vvv``\ ````\ **\ ```rtsp://www.hardradio.com/tonbeme.mov`` <rtsp://www.hardradio.com/tonbeme.mov>`__

where rtsp://www.hardradio.com/tonbeme.mov is the address of the stream.

Receive a stream described by an SDP file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``{{%}} ``\ **``vlc``\ ````\ ``-vvv``\ ````\ **\ ```http://server.example.org/stream.sdp`` <http://server.example.org/stream.sdp>`__

Save a stream with VLC
----------------------

VLC can save the stream to the disk. In order to do this, use the Stream Output of VLC: you can do it via the graphical interface (Media [menu] → streaming) or use the `record button <http://www.howtogeek.com/howto/2686/how-to-copy-a-dvd-with-vlc-1.0/>`__, or you can add to the command line the following argument:

**``--sout``\ ````\ ``file/muxer:stream.xyz``**

where:

-  **muxer** is one of the formats supported by VLC's stream output, i.e. :

   -  **ogg** for OGG format,
   -  **ps** MPEG2-PS format,
   -  **ts** for MPEG2-TS format.

-  and **stream.xyz** is the name of the file you want to save the stream to, with the right extension.

For example:

``'''vlc your_input_file_or_stream_here --sout=file/ps:go.mpg '''``

This is short hand for the more verbose

``'''vlc your_input_file_or_stream_here --sout="#std{access=file,mux=ps,dst=go.mpg}" ``

NB that you must choose a muxer that supports your stream type. See `Transcode#Compatibility_issues <Transcode#Compatibility_issues>`__

It can also be quite helpful to look at the settings VLC uses when it records using its record button. For example, in the logs you might see something like this:

...: Using record output \`std{access=file,mux='ps',dst='C:\vlc-record-2010__E-.mpg'}'

Which gives you a hint/clue as to how to record your current stream. In this case this would translate into --sout "#std{access=file... on the command line.

Receive a stream with a set-top-box
-----------------------------------

Some set-top-boxes with Ethernet cards can receive MPEG2-TS streams over UDP and support multicast.

Set-top-boxes known to work with VLC are:

-  `Pace <http://www.pace.co.uk>`__ set top boxes. (Pace Micro DSL 4000)
-  `Aminocom <http://www.aminocom.com>`__ set top boxes. (all the models with mpeg2)
-  tuxia / gct-allwell (mpeg4 and mpeg2) sigma designs8174 chipset
-  i3micro mood200 (mpeg4 and mpeg2 in transport streams)
-  ps3 media server streams using VLC (or mencoder) to the PS3

.. raw:: mediawiki

   {{Documentation}}
