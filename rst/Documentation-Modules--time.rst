{{Historicalmarq]] filter in version 0.9.0.}} {{Moduletype=Video
sub-filterlast_version=0.8.6sc=time}} Allows overlaying date and time
information on the video.

== Options == The option for the time picture subfilter in version 0.8.6
are the following:
{{Optionvalue=stringdescription=[[Special:PermanentLink/5790#Timename=time-xdefault=-1name=time-ydefault=0name=time-position<span
id="time-position"></span>default=9{ 0, 1, 2, 4, 8, 5, 6, 9, 10
}]]name=time-opacitymin=0default=255name=time-color<span
id="time-color"></span>default=16777215description=Colour<sup>('''[[#appendix_time-colorname=time-sizedefault=-1|description=Font
size, pixels}}

== Usage == There are two ways to use the time module: over screen
output or display; and over transcoded output.

=== Screen output or display === To overlay the current time over vlc
screen output or display, use the --time-? options (where ? means
"format," "x", "y" etc; i.e. --time-format).

In this example, the time will be displayed in white on the lower right
hand corner of the viewable output of a transcoded stream and sent to a
multicast IP address with the associated SAP announce.

   % '''vlc input_stream --sub-filter=time --time-format
   %Y-%m-%d,%H:%M:%S --time-position 9 --time-color 16777215 --time-size
   12 --sout
   "#transcode{venc=ffmpeg,vcodec=mp4v}:duplicate{dst=display,dst=rtp{mux=ts,dst=239.255.12.42,sdp=sap,name="TestStream"}}"'''

In this example, the time will be displayed as 2007-6-19,10:09:33. In
addition, the time will only be displayed on the visual display of the
input_stream. It will not be part of the transcoded output.

=== Transcoded output === To overlay the current time over the
transcoded output, enable the transcode module subpicture filter or
sfilter option.

In this example, the time will be displayed in white on the lower right
only in the transcoded output.

   % '''vlc input_stream --time-format %Y-%m-%d,%H:%M:%S --time-position
   9 --time-color 16777215 --time-size 12 --sout
   "#transcode{venc=ffmpeg,vcodec=mp4v,sfilter=time}:duplicate{dst=display,dst=rtp{mux=ts,dst=239.255.12.42,sdp=sap,name="TestStream"}}"'''

Note that this is accomplished by removing the --sub-filter=time command
line option and adding the sfilter transcode module option. If the
--sub-filter=time is included vlc will overlay the time over the overlay
transcode time, essentially overlapping it.

Also note that the --time-? command line options are "global;" i.e.,
they affect the way the time overlays both the display and the
transcoded output.

== Source code == \* {{VLCSourceFilemodules/video_filter/time.c}}

== Appendix == <div class="plainlist"> *^
--[[#time-position|time-position]]<span
id="appendix_time-position"></span>*\ ^ --[[#time-color
class="mw-datatable sortable" Sample !! scope="col" \| Integer code !!
scope="col" \| Colour \|\| <code>-268435456</code> \|\| Default
style="background-color:black;"\| \|\| <code>0</code> \|\| Black
style="background-color:gray;"\| \|\| <code>8421504</code> \|\| Gray
style="background-color:silver;"\| \|\| <code>12632256</code> \|\|
Silver style="background-color:white;"\| \|\| <code>16777215</code> \|\|
White style="background-color:maroon;"\| \|\| <code>8388608</code> \|\|
Maroon style="background-color:red;"\| \|\| <code>16711680</code> \|\|
Red style="background-color:fuchsia;"\| \|\| <code>16711935</code> \|\|
Fuchsia style="background-color:yellow;"\| \|\| <code>16776960</code>
\|\| Yellow style="background-color:olive;"\| \|\| <code>8421376</code>
\|\| Olive style="background-color:green;"\| \|\| <code>32768</code>
\|\| Green style="background-color:teal;"\| \|\| <code>32896</code> \|\|
Teal style="background-color:lime;"\| \|\| <code>65280</code> \|\| Lime
style="background-color:purple;"\| \|\| <code>8388736</code> \|\| Purple
style="background-color:navy;"\| \|\| <code>128</code> \|\| Navy
style="background-color:blue;"\| \|\| <code>255</code> \|\| Blue
style="background-color:aqua;"\| \|\| <code>65535</code> \|\| Aqua \|}

{{Documentation}}
