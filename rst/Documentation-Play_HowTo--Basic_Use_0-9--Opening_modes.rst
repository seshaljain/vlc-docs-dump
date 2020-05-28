==Opening a File== <p>The '''Media''' menu can be used to open a file.
VLC offers a range of options to open media files. See the table below
to see the available options. When you open a file, the file is played
according to the default play options.</p>

<table width="60%" border="1px"> <tr> <td width="10%"
bgcolor="#F5F5F5"><b>Option</b></td> <td width="10%"
bgcolor="#F5F5F5"><b>Shortcut Key</b></td> <td width="40%"
bgcolor="#F5F5F5"><b>Description</b></td> </tr>

<tr> <td width="10%">Open File</td> <td width="10%">Ctrl+O</td> <td
width="40%">Use this option to play a single media file from a specified
location on the hard disk.</td> </tr>

<tr> <td width="10%">Advanced Open File</td> <td width="10%">&nbsp;</td>
<td width="40%"><p>In addition to opening a file from a hard disk, you
can open files from a disc, from any computer on the network or directly
from a capturing device.</p> <p>You can also open a subtitles file
associated with the selected media file. </p> <p>You can also set a few
playing options. Refer to [[#Advanced_File_Open|Advanced File
Open]].</p></td> </tr>

<tr> <td width="10%">Open Folder</td> <td width="10%">Ctrl+F</td> <td
width="40%"><p>Use this option to play all the files in a certain
folder.</p></td> </tr>

<tr> <td width="10%">Open Disc</td> <td width="10%">Ctrl+D</td> <td
width="40%"><p>Use this option to play files from a disc. Based on the
type of disc you select, you can have a few more playing options. Refer
to [[#Opening_a_Disc|Opening a file from a disc]].</p></td> </tr>

<tr> <td width="10%">Open Network</td> <td width="10%">Ctrl+N</td> <td
width="40%"><p>Use this option to open a file present on any system on
the network to which you are currently connected.</p> <p>You can also
set a few playing options. Refer to [[#Opening_a_Network|Opening a file
on the network]]</p></td> </tr>

<tr> <td width="10%">Open Capture Device</td> <td
width="10%">Ctrl+C</td> <td width="40%"><p>Use this option to open a
file directly from a capturing device which is currently connected to
your system.</p> <p>You can also set a few playing options. Refer to
[[#Opening_a_Capture_Device|Opening a file from the capturing
device]].</p></td> </tr>

<tr> <td width="10%">Convert / Save</td> <td width="10%">Ctrl+R</td> <td
width="40%"><p>Use this option to convert a media file from one format
to another. </p> <p>Refer to
[[#Converting_and_Saving_a_Media_File_Format|Converting a media file
into another format]].</p></td> </tr>

<tr> <td width="10%">Streaming</td> <td width="10%">Ctrl+S</td> <td
width="40%"><p>Use this option to stream a recorded media file. </p>
<p>Refer to [[#Streaming_Media_Files|Streaming a media file]].</p></td>
</tr>

</table> [[`Image:VLC <>`__-_media_menu.png]]

You can open audio or video files. A file can be opened in two ways.
<ol> <li>From the '''Media''' menu select the '''Open File''' option or
the '''Advanced Open File''' option. </li> <li>Select the '''File''' tab
in the Open dialog box. </li> <li>Enter file name in the '''File
names''' box or browse and select a file.</li> <li>Select a format from
the '''Filter''' list. The supported formats are <i>.a52, .aac, .ac3,
.dts, .p3, .ogg, .oma, .spx, .wav, .wma</i> and <i>.wm</i>.</li>
<li>Check the '''Use a subtitle file''' option to select a subtitles
file to be viewed with the media file. <br> From the '''Alignment'''
list, select an option to align selected subtitle. The available options
are <i>Left, Right</i> and <i>Center</i>. <br> From the '''Size''' list,
select a font size for the selected subtitle. The available options are
<i>Small, Smaller, Normal, Large</i> and <i>Larger</i>. </li> <li>Click
'''Open'''. VLC starts playing the selected file with the default
options.</li> </ol>

==Advanced File Open== <p>To open a file<br> <ol> <li>Select the
'''Advanced Open File''' option from the '''Media''' menu. </li> <li>The
Open file dialog box is displayed. There are four tabs such as
'''File''', '''Disc''', '''Network''' and '''Capture Device'''.</li>
</ol>

Refer to the following sections for more details:

[[##Advanced_File_OpenOpening a folder]]<br> [[#Opening_a_DiscOpening a
media network]]<br> [[#Opening_a_Capture_Device|Opening a capture
device]]

==Additional Playing Options== When you select the '''File''' tab after
selecting the '''Advanced Open File''' menu, apart from selecting a file
you have the following choices:

'''Caching:''' When you specify caching value for a media file, the
stream is still rendered by VLC media player at the specified data rate,
but the client system buffers a much larger portion of the content
before rendering it. This allows the client to handle variable network
conditions without a perceptible impact on the playback quality of
either on-demand or broadcast content. Specify a caching value so that
the file is played smoother. The default value is 300 milliseconds.

'''Customizing:''' File names from different locations can be added
directly into the '''Customize''' box without having to browse the
folders.

'''Synchronous play:''' Play another file in synch with the selected
file.

'''Start time:''' Not play the file from the beginning. If start time is
specified as 120 seconds, the file is played after skipping the content
of the first two minutes. (Specify time in seconds; not minutes)

==Opening a Folder== You can select a folder to play all media files one
after the other in that folder. <ol> <li>Select the '''Open Folder'''
option. The Browse for Folders dialog box is displayed.</li> <li>Browse
and select the folder.</li> <li>Click on '''OK'''.</li> </ol> All the
files present in the selected folder are played in the alphabetical
order, one after another, without expecting any action from you.

==Opening a Disc== You can open media files from a disc. In VLC, you can
play Audio CDs, SVCD/VCDs, and DVDs. You can open a file from a disc in
two ways. <ol> <li>Select the '''Open Disc''' option from the
'''Media''' menu.<br> <i>Or </i><br> Select the '''Advanced Open File'''
option from the '''Media''' menu. </li> The Open dialog box is
displayed. <li>Select the '''Disc''' tab.</li> <li>Check the type of
disc connected to the system. The options are '''Audio CD''', '''DVD''',
and '''SVCD/VCD'''.</li> <li>In the '''Disc Device''' box, by default,
the path for the disc is displayed. You may select a different path
using the '''Browse''' button.<br> Click on the Eject
[[`Image:VLC <>`__-_eject.png]] button. The disk drive opens
automatically and you can check if the drive is empty or if the correct
disc is in the drive.</li> <li>Based on the selected disc type, specify
the following options:</li> <ul><li>DVD</li> <ul> <li>Some original DVDs
may have complex, proprietary menu options and VLC may not handle all
the options well. If you check the '''No DVD menus''' option, VLC reads
the raw video files directly into the film regardless of the options
present while creating the original DVD. Check this option if you want
to listen to or view the basic version without availing the menus
present in the DVD.</li> <li>When a DVD is played, the entire disc need
not be played. To specify the part to be played, specify the '''Title'''
and '''Chapter number''' in the '''Starting Position''' box. </li>
<li>Under the Audio and Subtitles group, select the '''Subtitles
track''' and '''Audio track'''.</li> </ul> <li>Audio CD</li> In the
'''Track''' box of the '''Starting Position''' group, select the track
number at which the play should start. <li>SVCD/VCD</li> In the
'''Starting Position''' group, specify the '''Entry''' number at which
the play should start. Under the '''Audio and Subtitles''' group, select
the '''Subtitles track''' and '''Audio track'''. </ul> <li>Check '''Show
more options''' to see more play options. Refer to
[[#Additional_Playing_Options|Additional playing options]].</li> </ol>
===Playing more than one media file=== VLC has an option to play two
media files synchronously. <ol> <li>From the '''Media''' menu, select
the '''Advanced Open File''' option. </li> The Open dialog box is
displayed. <li>Select a media file.</li> <li>Check the '''Show more
options''' option. The screen expands to show more options.</li>
<li>Check the '''Play another media synchronously''' option. The
'''Extra media''' box and a '''Browse''' button are displayed.</li>
<li>In the '''Extra media''' box, enter the name of another media file
with complete path or use the '''Browse''' button to select the media
file. </li> <li>You can change the '''Caching''' value for the media
file being played.</li> <li>Select the time at which the media file
should start from the '''Start Time''' list.</li> <li>You can see the
selection you made in the '''Customize''' box.</li> <li>Click on the
'''Play''' button. </li> </ol> You can use the '''Show more options'''
to watch a video while listening to an audio file or listen to two audio
files played synchronously (one audio track can have the instrumental
part and the other can have the corresponding voice).

==Opening a Network== You can open a network and stream media from the
selected network to the specified hosts. When you open a network you
specify the network to be used for streaming media content.

<ol> <li>From the '''Media''' menu select '''Open Network''' or
'''Advanced Open File''' option and then select the '''Network''' tab.
</li> The Open dialog box is displayed. <li>Select a protocol from the
'''Protocol''' list. </li> The supported protocols are HTTP, HTTPS, FTP,
MMS, RTSP, RTP, UDP and RTMP. MMS, RTP, RTMP, RTSP and UDP protocols are
suitable for streaming media. The RTP, RTMP and RTSP protocols are for
real transmission. <li>Select a protocol suitable to your content. </li>
<li>In the '''Address''' box, enter the address of the system from which
the media is going to be streamed. </li> <li>In the '''Port''' box,
enter the port number from which streaming is done. </li> The default
number is 1234. <li>When UDP is selected, the '''Allow Timeshifting'''
option is enabled.</li>

Timeshifting refers to the recording of programmes in a storage medium
which is to be viewed or listened to at a time more convenient.
Typically, this refers to TV programming but can also refer to radio
shows through podcasts.

When the network stream is played, the stream can be paused even if it
is a live stream

<li>Enter a URL in the '''Address''' box. </li>

<b>Note:</b> The '''Port''' list is enabled only when RTP or UDP is
selected.

<li>Click on the [[Image:submenu.JPG]] before the '''Play''' button and
select '''Stream''' from the popup menu.</li>

<li>In the Stream Output dialog box, specify the media file to be
streamed and the address to which the streaming should be done. <br> In
the Stream Output dialog, you can specify further options. Refer to
[[#Specifying_Streaming_Options|Specifying the Streaming Options]].</li>

<li>Click on the '''Stream''' button.</li>

<b>Note:</b> When the streaming is being done, the slider moves to show
the progress. ===Specifying Streaming Options=== VLC provides several
options for streaming media files. You can stream media files in two
ways. <ol> <li>Select '''Streaming''' from the '''Media''' menu.
</li><br> <i>Or</i><br> Select '''Advanced Open File''' from the
'''Media''' menu. The Open dialog box is displayed. </li> <li>Click on
the [[Image:submenu.JPG]] icon next to the '''Play''' button and select
'''Stream''' from the popup menu. </li> The Stream Output dialog box is
displayed. </ol> <b>Specify Outputs</b>

<ol> <li>Check the '''Play locally''' option to play the file while it
is being streamed.</li> <li>Check the '''File''' option to specify a
path to save the converted file or click on the '''Browse''' button. The
Save File dialog box is displayed. Select a container format from the
'''Save As Type''' list.</li>

A container is a file that can contain audio and video. You can also
browse a folder to save the converted file. The audio and video is
encoded using codecs and then stored in a container. A file’s extension
can be used to identify the container format. VLC provides the following
container formats:

<table width="80%" border="1"> <tr> <td width="5%"
bgcolor="#F5F5F5"><b>Format</b></td> <td width="75%"
bgcolor="#F5F5F5"><b>Description</b></td> </tr>

<tr> <td width="5%">.ps</td> <td width="75%">Refers to MPEG program
stream. Stores M-PEG 2 video muxed with other streams.</td> </tr>

<tr> <td width="5%">.ts</td> <td width="75%">Refers to MPEG transport
stream. Used for streaming video through a network or by a
satellite.</td> </tr>

<tr> <td width="5%">.mpg</td> <td width="75%">Refers to a family of
standards used for coding audio and visual information.</td> </tr>

<tr> <td width="5%">.ogg</td> <td width="75%">Refers to professional
grade media product. Ogg Vorbis encodes audio and Ogg Theora encodes
video.</td> </tr>

<tr> <td width="5%">.asf</td> <td width="75%">Stores Windows Media Audio
and Windows Media Video. ASF is designed to be used over audio and video
information and is specially designed to run over networks.</td> </tr>

<tr> <td width="5%">.mp4</td> <td width="75%">M-PEG 4 audio and video.
Provides compression for web, voice and broadcast television
applications.</td> </tr>

<tr> <td width="5%">.mov</td> <td width="75%">Refers to the QuickTime
media format. Used to store audio and video.</td> </tr> </table>

<li>Select a file or enter the file name in the '''File''' name box.
</li> <li>Click on '''Save''' to save the media file in the selected
container format.</li> <li>Check the '''Dump Raw Output''' box to save
the input stream as it is read by VLC, without any processing. If this
option is selected, all other options are disabled. </li> <li>Select
HTTP to stream media files using the HTTP streaming method. Specify the
'''Address''' and '''Port'''.</li> <li>Select the '''MMSH''' access
method to stream media files to the Microsoft Windows Media Player. The
'''Address''' and '''Port''' options are enabled. Specify the
'''Address''' and '''Port'''.<br> MMS is a proprietary digital media
streaming protocol developed by Microsoft. MMSH is MMS over HTTP.</li>

<li>Select '''RTP''' to stream the media using the RTP method. The
Prefer UDP over RTP, Address, Port, Audio Port and Video Port options
are enabled.<br> RTP refers to the Real-Time Transfer Protocol. Like
UDP, RTP can use both unicast and multicast addresses. RTP or UDP is
extensively used for streaming live audio and video.</li> <li>Specify
the '''Address''', '''Port''', '''Audio Port''' and '''Video Port'''.
</li> <li>Select the '''Prefer UDP over RTP''' option. </li> VLC
automatically tries to stream the media using the UDP protocol. If the
streaming fails, VLC uses the IP address specified for the RTP protocol.
This option can be used when no intervention is required from the
consumer. The '''Audio Port''' and '''Video Port''' options get disabled
if the Prefer UDP over RTP option is selected.

<li>Select '''IceCast''' to distribute live audio and video over the
Internet in real time. <br> <ul> <li>Enter the '''Address''' and
'''Port''' details. </li> <li>Enter the login name and password in the
'''Login:pass:''' box.</li> <li>Enter the name of the '''Mount Point'''
where the current listener should be redirected to.</li> </ul> An
IceCast mount point refers to a connector between an IceCast source
stream and IceCast listeners.</li> <li>Select a profile from the
'''Profile''' list. The available profiles are <i>Custom, Ogg/Vorbis,
MPEG-2, MP3, MPEG-4 audio AAC, MPEG-4/DivX, H264, IPod (MP4, aac), Xbox,
Windows (wmv/asf),</i> and <i>PSP</i>.<br></li> <li>Choose the encoder
format from the '''Profiles''' or customise it. </li> <li>Customise the
other options by selecting the Encapsulation, Video codec, Audio codec
and Subtitles tabs. </li> <b>Note:</b> The options under Encapsulation,
Video codec, Audio codec and Subtitles tabs are enabled only if you
select the '''Custom''' option.

<b>Encapsulation </b>

Refers to the format in which a stream is encapsulated. The available
formats are <i>MPEG-TS, MPEG-PS, MPEG 1, Ogg/Ogm, ASF/WMV, MP4, MOV,
WAV, RAW, FLV</i> and <i>MKV</i>. From the '''Encapsulation''' tab,
select an encapsulation method that fits the codecs and access method of
your stream.

<b>Video Codec</b>

The '''Video''' option is selected by default. The options related to
codec, and bitrate are enabled only if the Video option is checked. <ul>
<li>Select the required codec from the '''Codec''' list. The available
video codecs are <i>MPEG-1, MPEG-2, MPEG-4, DIVX 1, DIVX 2, DIVX 3,
H-263, H-264, WMV1, WMV2, MPEG,</i> and <i>Theora</i>. </li> <li>Specify
an average bitrate in the '''Bitrate''' (kb/s) box.</li> <li>Select a
scale from the Scale list. The values are <i>1, 0.25, 0.5, 0.75, 1.25,
1.5, 1.75,</i> and<i> 2</i>. </li> </ul>

<b>Audio Codec</b>

The '''Audio''' option is selected by default. The options related to
codec, bitrate and channels are enabled only if the Audio option is
checked. <ul> <li>Select an audio codec from the '''Codec''' list. The
available audio codecs are <i>Vorbis, MPEG Audio, MP3, MPEG4 Audio
(AAC), A52/AC-3, Flac, Speex, WAV</i> and <i>WMA</i>. </li> <li>Specify
an average bit rate in the '''Bitrate''' (kb/s) box.</li> <li>Select a
channel from the '''Channels''' list. In audio, a channel refers to a
stream of audio that is to be played by one speaker. For example, stereo
audio, consists of two channels. </li> </ul>

<b>Subtitles</b>

Specify subtitles to be streamed along with your media file. To specify
subtitles <ul> <li>Check the '''Subtitles''' checkbox and select a
subtitle from the '''Subtitle''' list.</li> This is the subtitle format
that is to be included with the media that is streamed. <li>Check the
'''Overlay subtitles on the video''' option to render subtitles directly
on the video, while transcoding it.</li> </ul>

<b>Miscellaneous</b>

<b>Time-To-Live (TTL)</b>- This sets the numbers of routers your stream
can go through, for UDP unicast and unicast access methods. With UDP
multicast, the default TTL is set to 1, meaning that your stream won't
get across any router. You may want to increase it if you want to route
your multicast stream.

<b>SAP Announce</b> - SAP is a way to publicly announce streams that are
being sent using multicast UDP or RTP. Enter the name of the stream in
the text box. This is available only for the RTP streaming method.

<blockquote> <b>Group Name</b> – This allows you to specify a group for
the session, which will be announced. Enter a name. This option is
enabled only if the '''SAP Announce''' box is checked.</blockquote>

<b>Stream all elementary streams</b> – Select this option to you to
stream all soundtracks and subtitles. This option separates the
different elementary streams from a stream, and saves each of them in a
different file or sends it to a separate destination.

<b>Keep stream output open</b> - Select this option to save incoming
streams. This option is also used to make VLC act as a streaming server.

The options selected are displayed as a concatenated string in the
'''Generated Stream Output String''' box. <li>Click on the Stream
button. The selected file is streamed to the selected locations.</li>
'''Note:''' The '''Streaming''' option present under the '''Media'''
menu is the same as the '''Stream''' option in the [[Image:submenu.JPG]]
list.

===Common Options=== VLC provides some common options which are easily
accessible. Select '''Advanced Open File''' from the '''Media''' menu.

The Open file dialog box is displayed. There are four tabs such as
'''File''', '''Disc''', '''Network''' and '''Capture Device'''. The
options mentioned in the table are part of a dropdown list which is
displayed when the [[Image:submenu.JPG]] button is clicked.

<table width="60%" border="1"> <tr> <td width="10%"
bgcolor="#F5F5F5"><b>Option</b></td> <td width="10%"
bgcolor="#F5F5F5"><b>Shortcut Key</b></td> <td width="40%"
bgcolor="#F5F5F5"><b>Description</b></td> </tr>

<tr> <td width="10%">Enqueue</td> <td width="10%">Alt + E</td> <td
width="40%">Adds media files to the playlist but doesn't play it until
you click '''Play'''.</td> </tr>

<tr> <td width="10%">Play</td> <td width="10%">Alt + P</td> <td
width="40%">Adds media files to the playlist and plays the media.</td>
</tr>

<tr> <td width="10%">Stream</td> <td width="10%">Alt + S</td> <td
width="40%">Adds media files to the playlist and streams it on the
network.</td> </tr>

<tr> <td width="10%">Convert</td> <td width="10%">Alt + C</td> <td
width="40%">Adds media files to the playlist.<br> Converts a media file
into the selected format. </td> </tr> </table>

'''Note:''' Leave '''Play locally''' unchecked because it decreases the
conversion time. If you simultaneously play a file and convert it, it
takes much more time.

==Opening a Capture Device== A capture device captures an image from a
video file or sound from an audio file. Capture devices include webcams,
external DVD players, TV cards and acquisition cards. VLC supports
capture devices if the devices have the DirectShow compatible drivers.

To capture media

<ol> <li>Select '''Open Capture Device''' from the '''Media''' menu. The
Open dialog box is displayed with the '''Capture Device''' tab selected.
</li> VLC media player supports three modes of capture <i>DirectShow,
DVB DirectShow</i> and <i>Desktop</i>.

'''DirectShow:''' DirectShow, a Windows media streaming architecture,
supports capture from digital and analog devices. DirectShow
automatically detects and uses video and audio acceleration hardware
when available, but also supports systems without acceleration hardware.

To capture content using the DirectShow plug-in, select '''DirectShow'''
from the '''Capture Mode''' list. The options in the rest of the dialog
box change based on the option selected in the Capture Mode list.

If you want to capture video, select a device from the list next to the
'''Configure''' button under the '''Card Selection''' group. VLC
provides default values. To adjust more options, select the required
options from the device settings. <br>

<ol> <li>Click on the '''Configure''' button for Video. The Properties
dialog box is displayed with two tabs, '''Device Settings''' and
'''Advanced'''. </li> <li>If the device name does not appear in the
list, click on the '''Refresh''' button. The device name appears in a
list next to the '''Configure''' button.</li>

'''Device Settings'''<br> [[Image:Device settings.JPG]]

If the '''Auto''' box is checked for any parameter, the software
automatically fixes the value for the parameter based on the video file.
By default, the Auto option is enabled only for the White Balance
parameter. <ul> <li>'''Brightness:''' Move the slider till you get the
desired brightness for the video capture. The default value is 5000.
</li>

<li>'''Contrast:''' Refers to the difference in visual properties that
makes an object distinguishable from other objects and the background.
Move the slider till you get the desired contrast. The default value is
5000. </li>

<li>'''Saturation:''' Refers to the difference of a color against its
own brightness. Move the slider to get the desired effect. The default
value is 5000. </li>

<li>'''Sharpness:''' Refers to the clarity of a video. Move the slider
till you get the desired sharpness for the video capture. The default
value is 6000. </li>

<li>'''White Balance:''' Refers to colour balance. This option helps to
make white actually white and makes skin tones look more natural.
Uncheck the '''Auto''' option and Move the slider to get the desired
effect.</li>

<li>'''Backlight Comp:''' Refers to the ability of a camera to
compensate in cases where a subject with a large amount of background
light would otherwise be obscured by excessive light. The default value
is 0. Move the slider to get the desired effect.</li> </ul>

'''Advanced Settings'''

[[Image:advanced settings.JPG]]

'''Automatic Gain Control''' – Is a circuit found on some electronic
devices that automatically controls the gain of a signal. In AGC, weaker
signals receive more gain and stronger signals receive less gain or none
at all. <ul> <li>'''Exposure''' - Refers to the amount of light allowed
to fall on a selected media file while capturing images. There are
occasions when you may have to manually adjust the exposure on your
camera. Exposure is measured in seconds. <br>

For example, you have to take a shot of a person from a certain angle,
and there is bright light behind the person. In such case, aim your
camera on the person and adjust the exposure value by moving the slider.
The specified value remains unchanged even after closing the VLC
application.</li>

<li>'''Gain''' - This option allows increasing or decreasing the
brightness of the video being captured. <br> When '''Automatic Gain
Control''' is selected, the values you specified are taken as the
default values for Exposure and Gain. <br>

Uncheck '''Automatic Gain Control''' to change the values of
'''Exposure''' and '''Gain''' by moving the sliders.</li> </ul>

'''Image Mirror''' <ul> <li>'''Mirror Horizontal''' – If you select this
option, the video clip is flipped horizontally. You can see a mirror
view of the captured picture.</li> <li>'''Mirror Vertical''' - If you
select this option, the video clip is flipped upside down. </li> </ul>

'''Anti-Flicker''' – Refers to a process of filtering digital images to
reduce image flicker. The available options are <i>Off, 50 Hz
(European)</i> and <i>60 Hz (North America)</i>.

'''Image Enhancement''' – You can enhance the video being captured in
terms of light and color using the following options: <ul> <li>'''Low
Light Boost''' – If you check this option, the exposure time of the
camera increases in poor light conditions.</li> <li>'''Color Boost''' –
If you check this option, the colors of the video being captured are
boosted.</li> </ul>

If you want to capture audio, select a device from the list next to the
'''Configure''' button under the '''Card Selection''' group.

Click on the '''Configure''' button for Audio. The Properties dialog box
is displayed. Specify the AudioInputMixer properties.

[[Image:Audioinputprop.JPG]]

In the Master Input Mix group, check the '''Enable''' box. Control the
tone of the audio using the Treble and Bass sliders. <ul>
<li>'''Loudness''' – Refers to volume of the audio. Adjust the volume by
moving the slider.</li> <li>'''Mono''' – Refers to an amplifier
connection. Adjust the volume by moving the slider.</li> </ul> In the
Pin Line Input Mix group, check the '''Enable''' box. Select a line from
the '''Pin Line''' list. The values in the Pin Line list are populated
based on the selected audio input device.

<li>Click on the '''Advanced options''' button to specify the following
properties:</li> <ul> <li>'''Caching value in ms''' – Refers to the
caching value for DirectShow streams. Enter or select a value.</li>
<li>'''Video device name''' – Refers to the name of the video device
that is used by DirectShow plugin. If you do not specify a device, the
default device is used.</li> <li>'''Audio device name''' – Refers to the
name of the audio device that is used by DirectShow plugin. If you do
not specify a device, the default device is used.</li> <li>'''Video
size''' – Refers to the size of the video that is displayed by the
DirectShow plugin. The size of video is measured in pixels. If you do
not specify the size, the default size is used.</li> <li>'''Video input
chroma format''' - Chroma refers to the way colors are encoded. Enter a
specific chroma format. The default value is 1420. </li> <li>'''Video
input frame rate''' – Enter a specific frame rate. The default value is
0. </li> <li>'''Device properties''' – Check this option to view the
properties dialog of the selected device before starting the
stream.</li> <li>'''Tuner properties''' – Using this option you can set
channels. A tuner converts signals into picture and sounds. Select this
option to view the tuner properties (channel selection) dialog box.
</li> <ul> <li>'''Tuner TV channel''' – Refers to a tuner for setting TV
channels. The default is 0. The default channel is used to capture the
media.</li> <li>'''Tuner country code''' – This option helps to
establish the current channel-to-frequency mapping. The default is 0.
</li> <li>'''Tuner input type''' – Select the tuner input type.
Available values are cable and antenna. </li> <li>'''Video input pin'''
– Select a video input source. Available values are Composite, S-video,
and Tuner. These settings are hardware-specific. -1 means that settings
will not be changed.</li> <li>'''Audio input pin''' – This option is
used to capture audio using a specific audio input pin. These settings
are hardware-specific. Select a number from the Audio input pin list.
</li> <li>'''AM Tuner mode''' – This option is used to select a AM
(amplitude modulation). The following are the tuner modes:</li> <table
border="1"> <tr> <td bgcolor="#F5F5F5"><b>Value</b></td> <td
bgcolor="#F5F5F5"><b>Mode</b></td> </tr> <tr> <td>0</td>
<td>Default</td> </tr> <tr> <td>1</td> <td>TV</td> </tr> <tr> <td>2</td>
<td>AM Radio</td> </tr> <tr> <td>3</td> <td>FM Radio</td> </tr> <tr>
<td>4</td> <td>DSS</td> </tr> </table> Select a number from the '''AM
Tuner mode''' list. <li>Number of audio channels – Select an audio input
format with the given number of audio channels. If the channels are
unavailable, select 0.</li> <li>Audio sample rate – This option is used
to set the sample rate. If the rates are unavailable, select 0.</li>
<li>Audio bits per sample – Select audio input format with the given
bits or sample. If the audio bits are unavailable, select 0.</li> </ul>
</ul>

<li>Select the '''Convert''' option to select the encoding formats and
click on the '''Save''' button. Refer to
[[#Converting_and_Saving_a_Media_File_Format|Converting and Saving a
media file format]].</li> <li>Click on the '''Play''' button. The
capturing of the media starts.</li> </ol>

'''DVB DirectShow''' - Refers to a suite of internationally accepted
open standards for digital television. VLC media player supports three
types of DVBs and they are:

<ul> <li>'''DVB-S''' - Is an abbreviation for Digital Video Broadcasting
- Satellite. It is the Digital Video Broadcasting forward error coding
and modulation standard for satellite television. This is used via
satellites. </li>

<li>'''DVB-C''' – Is an abbreviation for Digital Video Broadcasting –
Cable. It is the DVB European consortium standard for the broadcast
transmission of digital television over cable. This system transmits
MPEG-2 or MPEG-4 audio and video streams using a QAM modulation.</li>

<li>'''DVB-T''' - Is an abbreviation for Digital Video Broadcasting –
Terrestrial. It is the DVB European-based consortium standard for the
broadcast transmission of digital terrestrial television. This system
transmits compressed audio, video and other data in the MPEG format
using the COFDM modulation.</li> </ul>

'''Note:''' Ensure that you have the DVB card installed on your PC.

'''DVB-S''' – You can stream a live TV from a PC using the DVB-S option.
To stream <ol> <li>Select '''Open Capture Device''' from the '''Media'''
menu. The Open dialog box is displayed.</li> <li>Select the '''Open
Capture Device''' tab. </li> <li>Select '''DVB DirectShow''' from the
'''Capture Mode''' list. </li> <li>Select '''DVB-S''' from '''DVB
Type''' under the '''Card Selection''' group. In the '''Options'''
group, specify the following </li> <li>Select '''Transponder/multiplex
frequency''' to set the transponder frequency. A transponder is a device
that receives, amplifies and retransmits a signal on a different
frequency.</li> <li>Select '''Transponder symbol rate''' to set the
transponder symbol rate. </li> <li>Click on the '''Advanced options'''
button to specify the following parameters:</li> <ul> <li>'''Caching
value in ms''' – Refers to caching value for the DirectShow stream.
Enter a value in milliseconds.</li> <li>'''Transponder / multiplex
frequency''' - A transponder is a device that receives, amplifies and
retransmits a signal on a different frequency. Select a frequency.</li>
<li>'''Inversion Mode''' - <i>Description to be added</i></li>
<li>'''Satellite polarization''' – Polarization is a method of giving
transmission signals a specific direction. The signals transmitted by a
satellite can be polarized in four ways and they are: <i>Horizontal,
Vertical, Circular Left</i> and <i>Circular Right</i>. Select an
option.</li> <li>'''Network identifier''' – Refers to a unique ID used
to identify a network. Select a number from the '''Network identifier'''
list.</li> <li>'''Satellite Azhimuth''' – Azhimuth is an angular
measurement made in the horizontal plane. Enter a value.</li>
<li>Satellite Elevation– This option defines the angle between the Earth
and the position of a satellite. Enter a value.</li> <li>'''Satellite
Longitude''' – Refers to the satellite longitude in 10ths of degree.
Enter a value.</li> <li>'''Antenna lnb_lof1''' – Refers to low band
local Osc Freq in kHz. Enter a value in kHz.</li> <li>'''Antenna
lnb_lof2''' - Refers to high band local Osc Freq in kHz. Enter a value
in kHz.</li> <li>'''Antenna lnb_slof''' – Refers to low noise block
switch freq in kHz. Enter a value in kHz.</li> <li>'''Transponder FEC'''
– Refers to the forward error correction mode. Enter a value in
kHz.</li> <li>'''Transponder symbol rate in kHz''' <i>Description to be
added</i></li> <li>'''Modulation Type''' – Refers to the QAM
constellation points. The available values are <i>16, 32, 64, 126,</i>
and <i>256</i>.</li> <li>'''Terrestrial high priority stream code rate
(FEC)''' – Refers to the high priority FEC Rate. The available values
are Undefined, <i>1/2, 2/3, 3/4, 5/6</i> and <i>7/8</i>.</li>
<li>'''Terrestrial low priority stream code rate (FEC)''' – Refers to
the low priority FEC Rate. The available values are <i>Undefined, 1/2,
2/3, 3/4, 5/6,</i> and <i>7/8</i>.</li> <li>'''Terrestrial bandwidth'''
- <i>Description to be added</i></li> <li>'''Terrestrial guard
interval''' – Refers to a parameter that is used in encoding and
modulation. Select an interval from the list. </li> <li>'''Terrestrial
transmission mode''' - <i>Description to be added</i></li>
<li>'''Terrestrial hierarchy mode''' - <i>Description to be
added</i></li> </ul> </ol>

'''DVB-C''' - You can stream digital TV using digital signal cables. The
following is a procedure to stream content using the DVB-C standard.
<ol> <li>Select '''Open Capture Device''' from the '''Media''' menu. The
Open dialog box is displayed.</li> <li>Select the '''Open Capture
Device''' tab. </li> <li>Select '''DVB DirectShow''' from the '''Capture
Mode''' list. </li> <li>Select '''DVB-C''' from '''DVB Type''' under the
'''Card Selection''' group. </li> <li>Select '''Transponder/multiplex
frequency''' to set the transponder frequency. </li> <li>Select
'''Transponder symbol rate''' to set the transponder symbol rate.</li>
<li>Select an extra media if you want some background music using
'''Show more options'''. Refer to
[[#Playing_more_than_one_media_filePlaying more than one media
file.</li> <li>Select '''Convert''' to select the encoding formats and
click on the '''Save''' button. Refer to Converting and Saving a Media
File Format.</li> <li>Click on the '''Play''' button to play the
media.</li> <li>Click on the '''Cancel''' button to exit the screen.
</li> </ol>

'''DVB-T''' - Follow the procedure below to stream DVB-T channels: <ol>
<li>Select '''Open Capture Device''' from the '''Media''' menu. The Open
dialog box is displayed.</li> <li>Select the '''Open Capture Device'''
tab. </li> <li>Select '''DVB DirectShow''' from the '''Capture Mode'''
list. </li> <li>Select '''DVB-T''' from '''DVB Type''' under the '''Card
Selection''' group. </li> <li>Select '''Transponder/Multiplex
frequency''' to set the transponder frequency. </li> <li>Select
'''Bandwidth''' to set the terrestrial bandwidth. </li> <li>Select an
extra media if you want some background music using '''Show more
options'''. Refer to Playing more than one media file.</li> <li>Click on
the '''Play''' button to play the media.</li> <li>Click on the
'''Cancel''' button to exit the screen.</li> </ol>

'''Note:''' The Advanced Options for the DVB-C and DVB-T are the same as
the Advanced Options for the DVB-S.

'''Desktop''' - You can capture all your mouse movements and application
actions and save the video in the selected format. This option is used
to record the on-screen activity on your Windows desktop. For example,
you can create videos to demonstrate the features or usage of a
software.

<ol> <li>To capture the desktop, select '''Open Capture Device''' from
the '''Media''' menu. The Open dialog box is displayed.</li> <li>Select
the '''Open Capture Device''' tab. </li> <li>Select '''Desktop''' from
the '''Capture Mode''' list. </li> <li>Enter a frame rate in the
'''Desired frame rate''' for the capture box.</li> <li>Select
'''Convert''' to select the encoding formats and click on the '''Save'''
button. Refer to Converting and Saving a media file format.</li>
<li>Select an extra media if you want some background music using
'''Show more options'''. Refer to Playing more than one media file.</li>
<li>Click on the '''Play''' button to play the media.</li> <li>Click on
the '''Cancel''' button to exit the screen.</li> </ol>
