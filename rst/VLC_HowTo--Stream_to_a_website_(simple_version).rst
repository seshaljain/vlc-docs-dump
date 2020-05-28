{{Howto|stream VLC to a website}} The following “How To” describes an
easy method of using VLC as a simple video streamer to enable a live
video stream (Eg web-cam) via VLC to be streamed from a web server
across a local LAN or the Internet. This method does also work for
streaming files and other media, CD, DVD Etc Using this method of
streaming from VLC allows the stream to be viewed from many media player
clients other than VLC, which is often the case The content and
description is aimed at those who only have an elementary knowledge of
VLC, Networking, and Web authoring / HTML. This method is not the most
sophisticated way to utilise VLC, but it does work well and has been
tested on both LAN and WAN using VLC versions 0.9.8a, 0.9.9, 1.0.x. and
1.1.x

== First checks ==

First, I have to make some assumptions and you will have to do some
checks.

-  You have a web site? If not see [[#Appendix]] at the bottom of this
   “HowTo”.
-  Your website works OK and is on your own web server on the same
   machine as VLC?
-  If your website is for external viewing (internet), you have a static
   IP and are not behind a proxy server?
-  Your ISP is not blocking any ports
-  Your firewall is not blocking any ports that you want to stream
   through. (Port 1234 for the example [[#The_method|below]])

I also assume you are using a NAT router with port forwarding for both
the website and port to be used by the video stream. You have sufficient
upstream bandwidth to support the size of video stream (See [[#Note 1]])

== Limitations ==

This HowTo was written with previous versions in mind, so the
descriptions of the VLC User Interface may differ slightly.

The following technique only works (tested so far) using the Windows
encapsulation method asf/wmv (and asf/div3 VLC 1.0.0) selected from the
Custom menu in the VLC Streaming Settings window. (other methods may
work, I have not tested them all)

== The method ==

The following method/technique uses a “metafile” or redirector. You
might want to check out the terms ”metafile”, “redirector” and “.asx”
for further information

Firstly create a text file (Eg in Notepad) and copy and paste the
following

<syntaxhighlight lang="XML">
   <ASX version ="3.0">
      <TITLE>Stream1234</TITLE> <ENTRY> <REF
      HREF="http://192.168.0.42:1234" /> </ENTRY>

   </ASX>

</syntaxhighlight>

Where the HREF value is your local LAN IP for a LAN ONLY website. Or The
HREF value is your external (Internet) [[IP]] for a WAN ONLY website The
port number (Eg :1234) is the [[port]] you will allocate in VLC
Streaming settings window.

The text file should then be saved as a .asx file. I suggest you create
two such files. One for LAN and one for WAN (See [[#Note 3]])& (See
[[#Note 5]]) \* Eg localstream1234.asx for the LAN version using your
internal LAN IP \* Eg extstream1234.asx for the WAN version using your
external WAN IP

Place these .asx files in your web server dir.

Create a links in a web page that point to the above .asx files. When
the link is activated, a pop out player will stream. Or Eg Embed the
stream on a page by the following in html

<syntaxhighlight lang="HTML5">
   <embed src="localstream1234.asx">

</syntaxhighlight>

Or Eg

<syntaxhighlight lang="HTML5">
   <embed src="localstream1234.asx” height=”370” width=”400">

</syntaxhighlight>

To resize the video on the web page.

=== Now for VLC ===

First check your video source (TV card, Video capture device, webcam
etc) is working OK and playing through VLC OK using the Play option
Select Streaming. Select Source, Capture device for this example (and
any necessary additional settings)

Check play locally box Check or select/add http box LEAVE the ADDRESS
FIELD BLANK!! Change the port number to 1234 (for this example) Select
“Windows asf/wmv” in the Custom dropdown selection box You may need to
alter the [[TTL]] value to allow more buffering, a value of 0 or 1
should be OK (no more than 12 should be necessary) as this increases
delay from live Then select Next and/or Stream VLC should open with a
local display stream, which should display the stream and an overlay
text displaying “streaming” for a few seconds.

''If this does not work… Obviously… Something is wrong! First check the,
Main Menu selection, Tools dropdown item “Messages” for suggestions as
to the cause of error and also re check all the above
instructions/settings.''

If all is well, then. Now check out your LAN website from another
machine on your LAN linking to (localstream1234.asx) The stream may take
up to 30 secs to display. OK? If not then go back and check it all out
again. Now get a friend/other to test out the WAN links from another
external location. (See [[#Note 4]])

== Results ==

I have found this method to work well on LAN and WAN It does not need
VLC to be at the client end. It also does not need or employ any Java on
the client or server machine. All it requires is the ability of a
browser and its associated media player to be able to display the now
universal ”.asf” stream which most can.

LAN tested with browsers: \* MS IE via MS Media Player \* Realplayer
pointing at URL/xxxxxx.asx \* Firefox via MPlayer and MS Media Player \*
Konquorer via Kaffeine \* Kaffeine pointing at URL/xxxxxxx.asx

WAN Tested with browsers: \* MS IE via MS Media Player \* Mozilla
Firefox via MS Media Player and Real Player

And. Of course VLC Player in all cases.

I have successfully used this method of serving from MS Windows XPpro
IIS 5.1 and Apache 2.2 and also Linux Ubuntu 8.04 LTS Apache 2.2

== Notes ==

=== Note 1 === How much '''bandwidth''' do I need for a given size of
video stream?

A very good question with no straight answer. It depends on how good the
encoding/compression is and other factors like the amount of dynamic
activity there is going on. It can vary quite a bit during the video
sequence. “Pixel noise” generated by the camera and capture hardware can
have an effect as well. An empirical method to determine this would be
to run a test video across a LAN using the hardware and software and
employing a network analyser to measure the bandwidth used.

=== Note 2 === Following on from Note 1, The overall '''system
capability''' will also determine how effectively the video stream can
be encoded, compressed and streamed.

The more system CPU power available the better! As a minimum The method
above will just about work with a video size of 384x288 streamed from
VLC using a totally dedicated server at 800MHz cpu + 512 MB RAM with
good hardware in good light. Employing wmv/asf encoding and an uplink
bandwidth sync of 832 (circa real700K) It is more than likely that you
will have to adjust the picture size to the bandwidth you have
available. Also note that USB video capture devices tend to use a great
deal of CPU/system resource, so do check out how much spare capacity you
have when everything is running, including your server when it is
“Serving” a stream?

=== Note 3 === If you are using classical routing (No NAT) then the
local and external IP will (probably) be the same unless you have an
unusual configuration.

=== Note 4 === It is ''not'' usually possible to view the streaming
output of a LAN from the WAN side. Also it is not usually possible to
view the streaming going out on the WAN from the LAN side.

This makes testing more difficult! (The exception to this being note 3,
that is the LAN and WAN having the same IP) I suggest that this
streaming method is first tested and proved on your LAN. Then test out
the WAN stream by calling someone to test it from a remote location on
the www.

=== Note 5 === The choice of '''port you use''' is up to you. [[Port]]
1234 is as good as any for LAN (over 1024 is better), but a port at or
above 8080 would be more appropriate for WAN (the Internet).

Do check that your chosen port is not being used by another application.
First place to look would be in your firewall and router settings when
you open that port for your stream.

Finally. If you have got all this working and want to try a slightly
more sophisticated stream to website, follow the White Rabbit (link
below)

[[Stream_VLC_to_Website_with_asf_and_Flash]]

== Appendix ==

What!!!? Web servers and streaming from website Not got a web site? Not
got a web server? No clue where to start? Find the whole idea rather
daunting? Well it is probably much easier than you thought. First you
will need a web server. The following link is to “Apache httpd”. The
Apache web server is as simple or as sophisticated as you want it to be.
It is well documented on the web and many books are available. And it is
free.

http://httpd.apache.org/

I would avoid use of MS IIS 5.1 as supplied with XP Pro on anything
other than a LAN as it poses many security issues on the www for a
novice.

Next you will need a web page creator/editor and some guidance on how to
use it. Take a look here:
[http://www.thesitewizard.com/gettingstarted/kompozer-tutorial-1.shtml
Kompozer Tutorial].

Again Kompozer is free and very simple to use. The only html that will
need to be added to make this work is the examples given previously.
