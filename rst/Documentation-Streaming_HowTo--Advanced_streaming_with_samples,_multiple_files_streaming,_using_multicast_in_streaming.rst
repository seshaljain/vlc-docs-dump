.. raw:: mediawiki

   {{RightMenu|Documentation TOC}}

**This document explains how to stream a file, stream multiple files, use multicast, etc., using the VideoLAN solution. With examples.**

UDP streaming examples
----------------------

Standard UDP streaming:

``{{%}} '''vlc -vvv ``\ ```file:////home/vlc/2007.avi`` <file:////home/vlc/2007.avi>`__\ `` --sout '#std{access=udp,mux=ts,dst=:1234}' '''``

Nothing impossible yet. Streaming a file 2007.avi from /home/vlc/ to udp port 1234.

Multicast RTP streaming examples
--------------------------------

``{{%}} ``\ **``vlc``\ ````\ ``-vvv``\ ````\ **\ ```file:////home/vlc/Jumper.avi`` <file:////home/vlc/Jumper.avi>`__\ **\ ````\ ``--sout``\ ````\ ``'#rtp{access=udp,mux=ts,dst=224.255.1.1,port=1234,sap,group="Video",name=Jumper``\ ````\ ``Movie"}'``\ ````\ ``:sout-all``**

| Hard? No!
| This is known key **file**. The key **--sout** starts output as in the UDP sample. Then we set **#rtp** with access type **udp**, muxer **ts**. Then point to multicast IP address **224.255.1.1** with port **1234**. And some keys. We point VLC to do announcements of this stream using **SAP** (see `service advertisements protocol <SAP>`__), set description of the streaming group to **Video**, and name this stream ''' 'Jumper Movie' '''.

Multicast RTP streaming with multiple source files (with examples)
------------------------------------------------------------------

| *When you start this, you can't stop.*
| I spent several hours trying to find this solution. Here it is:

``{{%}} ``\ **``vlc``\ ````\ ``-vvv``\ ````\ ``--color``\ ````\ ``-I``\ ````\ ``telnet``\ ````\ ``--telnet-password``\ ````\ ``"i_dont_know_this_password"``\ ````\ ``--vlm-conf=/home/vlc/vlc.streaming.conf``**

We told that VLC must colorize its output using key **--color**. Then we told VLC to open the telnet server. We must control it, really?! This is the **-I telnet** key. And we the set the password **"i_dont_know_this_password"** to get access to the console. We use the standard VLC telnet port 4212. If you need to change it, use **--telnet-port xxx**. Use **--vlm-conf=/home/vlc/vlc.streaming.conf** to point VLC to open - at start - a special file with multiple files description.

Special multiple files description configuration file
-----------------------------------------------------

-  **vlc.streaming.conf**

Using this config file we try to cast 2 video files: **2007.avi** and **Jumper.avi**. To do this, we must describe 2 channels: *channel1* and *channel2*, set the input, and set the output format (we try to multicast this):

| ``  new channel1 broadcast enabled ``
| ``  setup channel1 input ``\ ```file:////home/vlc/2007.avi`` <file:////home/vlc/2007.avi>`__\ `` loop``
| ``  setup channel1 output #rtp{access=udp,mux=ts,dst=224.255.1.1,port=1234,sdp=sap,sap,group="Video",name="2007 Movie"}``

| ``  new channel2 broadcast enabled ``
| ``  setup channel2 input ``\ ```file:////home/vlc/Jumper.avi`` <file:////home/vlc/Jumper.avi>`__\ `` loop``
| ``  setup channel2 output #rtp{access=udp,mux=ts,dst=224.255.1.2,port=1234,sdp=sap,sap,group="Video",name="Jumper Movie"}``

| ``  control channel1 play``
| ``  control channel2 play``
