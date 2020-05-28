{{howto|Set up Video on Demand on a Dreambox}} {{Example code}} I have
spent some time now to figure out how to get Video on Demand to work on
my dreambox. I have a DreamBox DM500S running the Gemini Image (Gemini
Project), and this howto is based on that, however I believe the
procedure will be similar on other DB's running the Gemini image as
well…

Sources I have used:
   http://digsat.net/wbb2/thread.php?threadid=36965&hilight=vlc
   http://forum.videolan.org

First we need to get a plugin called VLC FrontEnd installed on the
dreambox, it might already be there; check under blue panel → plugins.
If it is not there, install it using the instructions in the
[[#Install|next section]].

== Install == To install VLCf (VLC Frontend): \* Press Blue button \*
Choose Addons(2) \* Confirm option Gemini-server \* Search for Plugins
\* Install VLCF (currently is VLC-Final RC15 23.09.2k7)

Now, the front end is installed and almost ready to use. We still have
nothing that can feed the frontend, so first we must create an xml file
for the frontend to use:

<syntaxhighlight lang="xml" line> <?xml version="1.0"
encoding="iso-8859-1"?> <?xml-stylesheet type="text/xsl"
href="/XSLMPSettings.xsl"?> <vlc> <server ip="192.168.1.10"
webif-port="8080" stream-port="9090" user="admin" pass="admin" />
<config startdir="c:/movies" cddrive="d:" /> <codec mpeg1="mpgv"
mpeg2="mp2v" audio="mpga" /> <setup name="SVCD" ext="NONE"
Videorate="1000" fps="25" Videotranscode="0" Videocodec="mpeg2"
Videosize="352x576" Audiorate="192" Audiotranscode="0" /> <setup
name="VCD" ext="NONE" Videorate="1000" fps="25" Videotranscode="0"
Videocodec="mpeg1" Videosize="352x576" Audiorate="192"
Audiotranscode="0" /> <setup name="DVD" ext="NONE" Videorate="1000"
fps="25" Videotranscode="0" Videocodec="mp2v" Videosize="704x576"
Audiorate="192" Audiotranscode="1" /> <setup name="File" ext="MPG"
Videorate="1000" fps="25" Videotranscode="1" Videocodec="mp2v"
Videosize="704x576" Audiorate="192" Audiotranscode="1" /> <setup
name="File" ext="MPEG" Videorate="1000" fps="25" Videotranscode="1"
Videocodec="mp2v" Videosize="704x576" Audiorate="192" Audiotranscode="1"
/> <setup name="File" ext="M2P" Videorate="1000" fps="25"
Videotranscode="0" Videocodec="mpgv" Videosize="704x576" Audiorate="192"
Audiotranscode="0" /> <setup name="File" ext="MPV" Videorate="1000"
fps="25" Videotranscode="0" Videocodec="mpgv" Videosize="704x576"
Audiorate="192" Audiotranscode="0" /> <setup name="File" ext="DAT"
Videorate="1000" fps="25" Videotranscode="0" Videocodec="mpgv"
Videosize="704x576" Audiorate="192" Audiotranscode="0" /> <setup
name="File" ext="AVI" Videorate="2048" fps="25" Videotranscode="1"
Videocodec="mp2v" Videosize="704x576" Audiorate="192" Audiotranscode="1"
/> <setup name="File" ext="ASF" Videorate="1000" fps="25"
Videotranscode="1" Videocodec="mpgv" Videosize="704x576" Audiorate="192"
Audiotranscode="1" /> <setup name="File" ext="TS" Videorate="1000"
fps="25" Videotranscode="0" Videocodec="mp2v" Videosize="704x576"
Audiorate="192" Audiotranscode="0" /> </vlc> </syntaxhighlight>

Use a unix compatible editor, like UltraEdit, edit lines 4 and 5. The
server ip to fit the IP-address of the backend PC. Startdir and cddrive
to fit correspondingly the movie folder and the cddrive on the backend
pc.<br> Save it to a file called '''''movieplayer_My_Server.xml''''' to
your dreambox's '''''/var/etc''''' folder. (save the file locally and
FTP it to your dreambox, log in to your dreambox with default username
root and password dreambox, or set up UltraEdit to save directly using
FTP; your choice).

== Update == Update VLCf for the latest version of VLC Frontend:
VLCF-Final. This new VLC Frontend works slightly different. It is
downloaded and installed in the same way as the earlier versions, but
configuring it is a bit more easy: \* There is now a file called
'''''vlcf_original.xml''''' in '''''/var/tuxbox/config/'''''. It opens
the possibility to configure more than one streaming server (up to 4)
using only this one config file as opposed to changing config-files on
earlier versions of VLCF \* Now, open the file through a Unix compatible
editor like UltraEdit or similar editor (Notepad is no good)

I modified the following lines: \* '''Line 4:''' Inserting the correct
IP of my streaming server \* '''Line 8:''' Setting the correct Startdir
and cddrive

Once editing has been done, save the file to your dreambox'
'''''/var/tuxbox/config''''' as '''''vlcf.xml'''''.

As you can see, the config file is put together by 4 config sets. set1,
set2, set3 and set4. These will be reflected in the VLCF application on
the dreambox as you can configure the frontend to use either of these 4
sets.

<syntaxhighlight lang="xml" line> <?xml version="1.0"
encoding="iso-8859-1" ?> <?xml-stylesheet type="text/xsl"
href="/XSLMPSettings.xsl"?> <vlc> <server name="set1" ip="192.168.1.10"
webif-port="8080" stream-port="9090" user="admin" pass="admin" /> <!-- I
edited this line, you can use max 4 server and config sets --> <server
name="set2" ip="192.168.178.93" webif-port="8080" stream-port="9090"
user="admin" pass="admin" /> <server name="set3" ip="192.168.178.94"
webif-port="8080" stream-port="9090" user="admin" pass="admin" />
<server name="set4" ip="192.168.178.25" webif-port="8080"
stream-port="9090" user="admin" pass="admin" /> <config name="set1"
startdir="c:movies" cddrive="g:" /> <!-- I edited here too --> <config
name="set2" startdir="/home/mordillo/video" cddrive="/media/cdrom0" />
<config name="set3" startdir="d:/" cddrive="g:" /> <config name="set4"
startdir="c:/" cddrive="g:" /> <codec mpeg1="mpgv" mpeg2="mp2v"
audio="mpga" /> <setup name="SVCD" pic="mp4.png" ext="NONE"
Videorate="1000" Videotranscode="0" Videocodec="mpeg2"
Videosize="352x576" Audiorate="192" Audiotranscode="0" fps="25"
soutadd="soverlay,senc" /> <setup name="VCD" pic="mp4.png" ext="NONE"
Videorate="1000" Videotranscode="0" Videocodec="mpeg1"
Videosize="352x576" Audiorate="192" Audiotranscode="0" fps="25"
soutadd="soverlay,senc" /> <setup name="DVD" pic="default.png"
ext="NONE" Videorate="1000" Videotranscode="0" Videocodec="mp2v"
Videosize="704x576" Audiorate="192" Audiotranscode="1" fps="25"
soutadd="soverlay,senc" /> <setup name="File" pic="mpg.png" ext="MPG"
Videorate="1000" Videotranscode="1" Videocodec="mp2v"
Videosize="704x576" Audiorate="192" Audiotranscode="1" fps="25"
soutadd="soverlay,senc" /> <setup name="File" pic="mpg.png" ext="MPEG"
Videorate="1000" Videotranscode="1" Videocodec="mp2v"
Videosize="704x576" Audiorate="192" Audiotranscode="1" fps="25"
soutadd="soverlay,senc" /> <setup name="File" pic="mpg.png" ext="M2P"
Videorate="1000" Videotranscode="0" Videocodec="mpgv"
Videosize="704x576" Audiorate="192" Audiotranscode="0" fps="25"
soutadd="soverlay,senc" /> <setup name="File" pic="mpg.png" ext="MPV"
Videorate="1000" Videotranscode="0" Videocodec="mpgv"
Videosize="704x576" Audiorate="192" Audiotranscode="0" fps="25"
soutadd="soverlay,senc" /> <setup name="File" pic="mpg.png" ext="DAT"
Videorate="1000" Videotranscode="0" Videocodec="mpgv"
Videosize="704x576" Audiorate="192" Audiotranscode="0" fps="25"
soutadd="soverlay,senc" /> <setup name="File" pic="divx.png" ext="AVI"
Videorate="2048" Videotranscode="1" Videocodec="mp2v"
Videosize="704x576" Audiorate="192" Audiotranscode="1" fps="25"
soutadd="soverlay,senc" /> <setup name="File" pic="divx.png" ext="MOV"
Videorate="2048" Videotranscode="1" Videocodec="mp2v"
Videosize="704x576" Audiorate="192" Audiotranscode="1" fps="25"
soutadd="soverlay,senc" /> <setup name="File" pic="wmv.png" ext="WMV"
Videorate="2048" Videotranscode="1" Videocodec="mpgv"
Videosize="704x576" Audiorate="192" Audiotranscode="1" fps="25"
soutadd="soverlay,senc" /> <setup name="File" pic="h264.png" ext="H264"
Videorate="2048" Videotranscode="1" Videocodec="mpgv"
Videosize="704x576" Audiorate="192" Audiotranscode="1" fps="25"
soutadd="soverlay,senc" /> <setup name="File" pic="mp4.png" ext="MP4"
Videorate="2048" Videotranscode="1" Videocodec="mpgv"
Videosize="704x576" Audiorate="192" Audiotranscode="1" fps="25"
soutadd="soverlay,senc" /> <setup name="File" pic="divx.png" ext="DIVX"
Videorate="2048" Videotranscode="1" Videocodec="mp2v"
Videosize="704x576" Audiorate="192" Audiotranscode="1" fps="25"
soutadd="soverlay,senc" /> <setup name="File" pic="default.png"
ext="ASF" Videorate="1000" Videotranscode="1" Videocodec="mp2v"
Videosize="704x576" Audiorate="192" Audiotranscode="1" fps="25"
soutadd="soverlay,senc" /> <setup name="File" pic="default.png" ext="TS"
Videorate="1000" Videotranscode="0" Videocodec="mp2v"
Videosize="704x576" Audiorate="192" Audiotranscode="0" fps="25"
soutadd="soverlay,senc" /> <setup name="File" pic="dvd.png" ext="VOB"
Videorate="1000" Videotranscode="0" Videocodec="mp2v"
Videosize="704x576" Audiorate="192" Audiotranscode="0" fps="25"
soutadd="soverlay,senc" /> <setup name="File" pic="dvd.png" ext="ISO"
Videorate="1000" Videotranscode="0" Videocodec="mp2v"
Videosize="704x576" Audiorate="192" Audiotranscode="0" fps="25"
soutadd="soverlay,senc" /> <setup name="File" pic="dvd.png" ext="BIN"
Videorate="1000" Videotranscode="0" Videocodec="mp2v"
Videosize="704x576" Audiorate="192" Audiotranscode="0" fps="25"
soutadd="soverlay,senc" /> <setup name="File" pic="mp3.png" ext="MP3"
Videorate="2048" Videotranscode="1" Videocodec="mp2v"
Videosize="704x576" Audiorate="192" Audiotranscode="1" fps="25"
soutadd="" /> <setup name="File" pic="mp3.png" ext="WMA"
Videorate="2048" Videotranscode="1" Videocodec="mp2v"
Videosize="704x576" Audiorate="192" Audiotranscode="1" fps="25"
soutadd="" /> <setup name="File" pic="mp3.png" ext="WAV"
Videorate="2048" Videotranscode="1" Videocodec="mp2v"
Videosize="704x576" Audiorate="192" Audiotranscode="1" fps="25"
soutadd="" /> <setup name="File" pic="mp3.png" ext="OGG"
Videorate="2048" Videotranscode="1" Videocodec="mp2v"
Videosize="704x576" Audiorate="192" Audiotranscode="1" fps="25"
soutadd="" /> <!--Feel free to add filextensions as you like. Every
listet extension will be proceed now. Example below--> <!--setup
name="File" ext="RATDVD" Videorate="2048" Videotranscode="1"
Videocodec="mp2v" Videosize="720x576" Audiorate="192" Audiotranscode="1"
fps="25" soutadd="soverlay,senc" /--> </vlc> </syntaxhighlight>

Now that the xml file has been made and transferred to the dreambox it
is time to set up the backend VLC to feed the frontend.

== Use == === VLC for Windows === Start VLC on the PC. Then: \* Select
File → Open Network Stream (<kbd>Ctrl+N</kbd>) \* Click Advanced Options
\* check Stream/Save and click Settings \* check HTTP \* check Video
codec and select mp2v from the dropdown list \* check Audio codec and
select mpga from the dropdown list \* click Ok \* click Ok

Now, activate the WebInterface (WEBIF) by selecting Settings → Add
Interface → Web Interface from the VLC menu.

=== VLC for Ubuntu === For Ubuntu Linux users first install vlc by
running this command: {{$}} sudo apt-get install vlc This will in
general install a \****load of stuff, codecs and other things needed. As
I learnt, it is also required to install something called the
avahi-daemon. This is done by running this command: {{$}} sudo apt-get
install avahi-daemon If you are having trouble finding these packages,
you might want to run: {{$}} sudo apt-get update Now that all this has
been installed, you need to launch VLC using the following command-line:
{{$}} vlc -d -I http
--sout="#transcode{vcodec=mp2v,vb=1024,scale=1,acodec=mpga,ab=192,channels=2}:duplicate{dst=std{access=http,mux=ts,dst=/}}"
--http-port=9090 This specifies that the web interface is to be used,
together with some transcoding stuff <span title="wink">;-)</span>

At the time of writing this, I am still trying to tune the vlc backend a
bit. It is currently using 50%+ cpu when streaming…

Now it is time to start the VLC frontend on the dreambox and set it up
to use the correct xml file. \* Start VLC frontend plugin by starting
blue panel (blue button on the remote) and selecting Plugins \* VLC
Frontend will show up as a plugin \* select it and press Ok

VLC frontend is now started \* select settings (blue button) \* In the
dropdown list, select the xml file you created earlier,
'''''movieplayer_My_Server.xml''''' \* Then select Switch \* You will
now be told to restart VLC Frontend; do this by using the exit button
until you are back at the plugins page \* Now start VLC Frontend again
\* Use the red button (File) \* You will now be able to see the movie
files that is in the folder specified as startdir in the xml file \*
Select the file you'd like to watch and press Ok \* Then wait for the
buffering to complete, sit back and enjoy the movie…
