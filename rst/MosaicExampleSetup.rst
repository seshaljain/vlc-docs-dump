.. raw:: mediawiki

   {{Example code|for=mosaic}}

Example set-up for a conference: Plans
--------------------------------------

Problem description
~~~~~~~~~~~~~~~~~~~

For a conference we needed a web stream for participants who were not able to come. The set-up needed to be flexible as well transportable, since the conference took place at two venues which were several hundred meters apart. VLC was chosen because there was already a somehow working set-up available which was modified for this conference.

Hardware
~~~~~~~~

We were using a dual-core AMD box (Athlon X2 4600+) with 1 GB of memory and only two PCI slots (Fujitsu Siemens PC). So nothing out of the ordinary. We had two PolyCom remote controllable cameras which can output SVIDEO signals which we feed into to BT878 based grabber cards.

Software
~~~~~~~~

We used the vlc version coming with Ubuntu Gutsy 0.8.6c along with xawtv for direct control of the cameras (the encoding process and buffering of the clients usually introduce a lag of a few seconds which makes it hard to steer the camera efficiently.

Network distribution
~~~~~~~~~~~~~~~~~~~~

One of our problems was that at one of the conference venues the network bandwidth was somehow limited and we feared to overload that network. We thus decided to stream only to a single dedicated box which is connected to a network with a much larger bandwidth. This box was restreaming the content to anyone interested.

Details
-------

Needed devices
~~~~~~~~~~~~~~

Video
^^^^^

Grabber cards registered their devices where the camera output can be viewed from:

| ``/dev/video0``
| ``/dev/video1``

The very first step is to check, if these are working. For this, start

``xawtv -c /dev/video0``

and we saw a blue window, because xawtv sets the input mode to composite not SVIDEO. To change this, right-click on the blue window, and change the input to SVIDEO. I have not found a possibility to change this via the command line.

If *video0* is working, try the same with *video1* it should work as well.

Audio
^^^^^

The grabber cards I used, do have audio input but I only got very bad quality. With the on-board audio I got a much better quality so this was used. If you are a fan of a graphical interface try to record input from */dev/dsp* (need the OSS kernel modules) with *audacity*. Don't simply connect the output of the sound card to loudspeakers and the input of your microphone to the microphone input of your computer. The sound card may directly connect those two channels without the software having the possibility to record anything. If you find the input of the grabber cards are good enough, they are usually labeled */dev/dsp0* or something like this.

Setup
~~~~~

For a simple set-up with two equally sized images next to each other I use the following config file for vlc:

| ``# first camera uses /dev/video0 and the on-board sound /dev/audio or /dev/dsp``
| ``new cam1 broadcast enabled``
| ``setup cam1 input v4l:/dev/video0:norm=PAL:channel=1:adev=/dev/audio``
| ``setup cam1 option rtsp-tcp``
| ``setup cam1 output #transcode{vcodec=mp4v,vb=512,scale=1}:duplicate{dst=mosaic-bridge{id=1,height=400,width=300},``
| ``select=video,dst={transcode{acodec=mp3,ab=64,channels=1}:bridge-out{id=0}},select=audio}``
| ``# second camera. Important: adev=/dev/null otherwise I couldn't get it to run``
| ``new cam2 broadcast enabled``
| ``setup cam2 input v4l:/dev/video1:norm=PAL:channel=1:adev=/dev/null``
| ``setup cam2 output #transcode{vcodec=mp4v,vb=512,scale=1}:duplicate{dst=mosaic-bridge{id=2,height=400,width=300}}``
| ``# set up for the background``
| ``new background broadcast enabled``
| ``setup background input fake:``
| ``setup background option mosaic-width=800``
| ``setup background option mosaic-height=300``
| ``setup background option mosaic-rows=1``
| ``setup background option mosaic-cols=2``
| ``setup background option mosaic-position=1``
| ``setup background option mosaic-order="1,2"``
| ``setup background option fake-file="back.gif"``
| ``setup background option fake-width=800``
| ``setup background option fake-height=300``
| ``setup background option fake-fps="8"``
| ``setup background output #transcode{sfilter=mosaic,soverlay,vcodec=mp4v,acodec=mp3,ab=64,channels=1,scale=1}:bridge-in{id-offset=100}:std{access=http{mime=video/x-asf-stream},mux=asf,dst=/}``
| ``# put it all together``
| ``control background play``
| ``control cam1 play``
| ``control cam2 play``

For us it was not so important to have both images the same. The first camera just showed the audience while the second one looked at the projections made which needed to be of higher quality. We used therefore a special background image with a logo in the bottom left corner and this configuration:

| ``new cam1 broadcast enabled``
| ``setup cam1 input v4l:/dev/video0:norm=PAL:channel=1:adev=/dev/audio``
| ``setup cam1 option rtsp-tcp``
| ``setup cam1 output #transcode{vcodec=mp4v,vb=384,scale=1}:duplicate{dst=mosaic-bridge{id=1,height=300,width=400},select=video,dst={transcode{acodec=mp3,ab=64,channels=1}:bridge-out{id=0}},select=audio}``
| ``new cam2 broadcast enabled``
| ``setup cam2 input v4l:/dev/video1:norm=PAL:channel=1:adev=/dev/null``
| ``setup cam2 output #transcode{vcodec=mp4v,vb=1500,scale=1}:duplicate{dst=mosaic-bridge{id=2,height=600,width=800},select=video}``
| ``new background broadcast enabled``
| ``setup background input fake:``
| ``setup background option mosaic-width=1200``
| ``setup background option mosaic-height=600``
| ``setup background option mosaic-rows=2``
| ``setup background option mosaic-cols=3``
| ``setup background option mosaic-position=1``
| ``setup background option mosaic-order="1,2,0,0,0,0"``
| ``setup background option fake-file="aei3.gif"``
| ``setup background option fake-width=1200``
| ``setup background option fake-height=600``
| ``setup background option fake-fps="8"``
| ``setup background option mosaic-keep-picture=1``
| ``setup background option mosaic-keep-aspect-ratio=1``
| ``setup background output #transcode{sfilter=mosaic,soverlay,vcodec=mp4v,vb=2000,acodec=mp3,ab=64,channels=1,scale=1}:bridge-in{id-offset=100}:std{access=http{mime=video/x-asf-stream},mux=asf,dst=/}``
| ``control background play``
| ``control cam1 play``
| ``control cam2 play``

Either of these set-ups will start a streaming server listening on port 8080 for incoming http connections.

Out next problem was, how shall we prevent our small internet connection from the conference venue from being saturated?

Internet setup
~~~~~~~~~~~~~~

We used a very simple but effective way. For this we not only needed our streaming server (from now on named **origin**), but also another server on a much faster network (named **broadcast**). We started the server on **origin** with

``vlc -vvv --color -I telnet --vlm-conf conference.conf --ttl 10 --upd-caching 2000``

Then we start a ssh tunnel from **origin** to **broadcast** (best placed into a screen environment):

``ssh -N -c blowfish -R8000:localhost:8080 account@broadcast``

This will forward the local port 8080 (on **origin**) to port 8000 on **broadcast**.

Finally, we start another vlc instance on **broadcast** to restream the original stream:

``vlc -vvv ``\ ```http://localhost:8000/`` <http://localhost:8000/>`__\ `` --udp-caching 1500 --sout '#standard{access=http{mime=video/x-ms-asf},mux=asf,dst=/}' --http-port=7070``

Final tips
~~~~~~~~~~

Port multiplication
^^^^^^^^^^^^^^^^^^^

If you need to "multiply" a port easily, you can use iptables on Linux:

| ``#possibly not all of these modules are strictly needed:``
| ``modprobe xt_tcpup``
| ``modprobe ip_tables``
| ``modprobe iptable_filter``
| ``modprobe ip_conntraqck``
| ``modprobe iptable_nat``
| ``modprobe ipt_state``
| ``modprobe ipt_MASQUERADE``
| ``modprobe ipt_REDIRECT``
| ``echo "1" > /proc/sys/net/ipv4/ip_forward``
| ``# I'm flushing everything here, this may not be good for you``
| ``iptables -F``
| ``iptables -F -t nat``
| ``iptables -A INPUT -i lo -j ACCEPT``
| ``iptables -t nat -A PREROUTING -i eth0 -p tcp --dport 8080 -j REDIRECT --to-ports 7070``

This will forward all requests to port 8080 transparently to port 7070 (where our broadcast server listens). Note: Port 8080 might be better because some firewalls allow only http related ports out and 8080 is a typical proxy port.

Credits
-------

Thanks a lot for the folks on #videolan, especially ILEoo for helping me a lot when need was great! Without your help I don't think I would have finished this set-up in time!
