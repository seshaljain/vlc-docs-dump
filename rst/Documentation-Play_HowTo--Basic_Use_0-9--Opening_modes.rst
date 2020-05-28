Opening a File
--------------

The **Media** menu can be used to open a file. VLC offers a range of options to open media files. See the table below to see the available options. When you open a file, the file is played according to the default play options.

.. raw:: html

   <table width="60%" border="1px">

.. raw:: html

   <tr>

.. raw:: html

   <td width="10%" bgcolor="#F5F5F5">

Option

.. raw:: html

   </td>

.. raw:: html

   <td width="10%" bgcolor="#F5F5F5">

Shortcut Key

.. raw:: html

   </td>

.. raw:: html

   <td width="40%" bgcolor="#F5F5F5">

Description

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td width="10%">

Open File

.. raw:: html

   </td>

.. raw:: html

   <td width="10%">

Ctrl+O

.. raw:: html

   </td>

.. raw:: html

   <td width="40%">

Use this option to play a single media file from a specified location on the hard disk.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td width="10%">

Advanced Open File

.. raw:: html

   </td>

.. raw:: html

   <td width="10%">

 

.. raw:: html

   </td>

.. raw:: html

   <td width="40%">

In addition to opening a file from a hard disk, you can open files from a disc, from any computer on the network or directly from a capturing device.

You can also open a subtitles file associated with the selected media file.

You can also set a few playing options. Refer to `Advanced File Open <#Advanced_File_Open>`__.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td width="10%">

Open Folder

.. raw:: html

   </td>

.. raw:: html

   <td width="10%">

Ctrl+F

.. raw:: html

   </td>

.. raw:: html

   <td width="40%">

Use this option to play all the files in a certain folder.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td width="10%">

Open Disc

.. raw:: html

   </td>

.. raw:: html

   <td width="10%">

Ctrl+D

.. raw:: html

   </td>

.. raw:: html

   <td width="40%">

Use this option to play files from a disc. Based on the type of disc you select, you can have a few more playing options. Refer to `Opening a file from a disc <#Opening_a_Disc>`__.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td width="10%">

Open Network

.. raw:: html

   </td>

.. raw:: html

   <td width="10%">

Ctrl+N

.. raw:: html

   </td>

.. raw:: html

   <td width="40%">

Use this option to open a file present on any system on the network to which you are currently connected.

You can also set a few playing options. Refer to `Opening a file on the network <#Opening_a_Network>`__

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td width="10%">

Open Capture Device

.. raw:: html

   </td>

.. raw:: html

   <td width="10%">

Ctrl+C

.. raw:: html

   </td>

.. raw:: html

   <td width="40%">

Use this option to open a file directly from a capturing device which is currently connected to your system.

You can also set a few playing options. Refer to `Opening a file from the capturing device <#Opening_a_Capture_Device>`__.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td width="10%">

Convert / Save

.. raw:: html

   </td>

.. raw:: html

   <td width="10%">

Ctrl+R

.. raw:: html

   </td>

.. raw:: html

   <td width="40%">

Use this option to convert a media file from one format to another.

Refer to `Converting a media file into another format <#Converting_and_Saving_a_Media_File_Format>`__.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td width="10%">

Streaming

.. raw:: html

   </td>

.. raw:: html

   <td width="10%">

Ctrl+S

.. raw:: html

   </td>

.. raw:: html

   <td width="40%">

Use this option to stream a recorded media file.

Refer to `Streaming a media file <#Streaming_Media_Files>`__.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </table>

.. figure:: VLC_-_media_menu.png
   :alt: VLC_-_media_menu.png

   VLC_-_media_menu.png

You can open audio or video files. A file can be opened in two ways.

#. From the **Media** menu select the **Open File** option or the **Advanced Open File** option.
#. Select the **File** tab in the Open dialog box.
#. Enter file name in the **File names** box or browse and select a file.
#. Select a format from the **Filter** list. The supported formats are .a52, .aac, .ac3, .dts, .p3, .ogg, .oma, .spx, .wav, .wma and .wm.
#. Check the **Use a subtitle file** option to select a subtitles file to be viewed with the media file.
   From the **Alignment** list, select an option to align selected subtitle. The available options are Left, Right and Center.
   From the **Size** list, select a font size for the selected subtitle. The available options are Small, Smaller, Normal, Large and Larger.
#. Click **Open**. VLC starts playing the selected file with the default options.

Advanced File Open
------------------

| To open a file

#. Select the **Advanced Open File** option from the **Media** menu.
#. The Open file dialog box is displayed. There are four tabs such as **File**, **Disc**, **Network** and **Capture Device**.

Refer to the following sections for more details:

| `Opening a media file with advanced options <##Advanced_File_Open>`__
| `Opening a folder <#Opening_a_Folder>`__
| `Opening a media disc <#Opening_a_Disc>`__
| `Opening a media network <#Opening_a_Network>`__
| `Opening a capture device <#Opening_a_Capture_Device>`__

Additional Playing Options
--------------------------

When you select the **File** tab after selecting the **Advanced Open File** menu, apart from selecting a file you have the following choices:

**Caching:** When you specify caching value for a media file, the stream is still rendered by VLC media player at the specified data rate, but the client system buffers a much larger portion of the content before rendering it. This allows the client to handle variable network conditions without a perceptible impact on the playback quality of either on-demand or broadcast content. Specify a caching value so that the file is played smoother. The default value is 300 milliseconds.

**Customizing:** File names from different locations can be added directly into the **Customize** box without having to browse the folders.

**Synchronous play:** Play another file in synch with the selected file.

**Start time:** Not play the file from the beginning. If start time is specified as 120 seconds, the file is played after skipping the content of the first two minutes. (Specify time in seconds; not minutes)

Opening a Folder
----------------

You can select a folder to play all media files one after the other in that folder.

#. Select the **Open Folder** option. The Browse for Folders dialog box is displayed.
#. Browse and select the folder.
#. Click on **OK**.

All the files present in the selected folder are played in the alphabetical order, one after another, without expecting any action from you.

Opening a Disc
--------------

You can open media files from a disc. In VLC, you can play Audio CDs, SVCD/VCDs, and DVDs. You can open a file from a disc in two ways.

#. Select the **Open Disc** option from the **Media** menu.
   Or
   Select the **Advanced Open File** option from the **Media** menu.

The Open dialog box is displayed.

.. raw:: html

   <li>

Select the **Disc** tab.

.. raw:: html

   </li>

.. raw:: html

   <li>

Check the type of disc connected to the system. The options are **Audio CD**, **DVD**, and **SVCD/VCD**.

.. raw:: html

   </li>

.. raw:: html

   <li>

| In the **Disc Device** box, by default, the path for the disc is displayed. You may select a different path using the **Browse** button.
| Click on the Eject |VLC_-_eject.png| button. The disk drive opens automatically and you can check if the drive is empty or if the correct disc is in the drive.

.. raw:: html

   </li>

.. raw:: html

   <li>

Based on the selected disc type, specify the following options:

.. raw:: html

   </li>

-  DVD

-  Some original DVDs may have complex, proprietary menu options and VLC may not handle all the options well. If you check the **No DVD menus** option, VLC reads the raw video files directly into the film regardless of the options present while creating the original DVD. Check this option if you want to listen to or view the basic version without availing the menus present in the DVD.
-  When a DVD is played, the entire disc need not be played. To specify the part to be played, specify the **Title** and **Chapter number** in the **Starting Position** box.
-  Under the Audio and Subtitles group, select the **Subtitles track** and **Audio track**.

.. raw:: html

   <li>

Audio CD

.. raw:: html

   </li>

In the **Track** box of the **Starting Position** group, select the track number at which the play should start.

.. raw:: html

   <li>

SVCD/VCD

.. raw:: html

   </li>

In the **Starting Position** group, specify the **Entry** number at which the play should start. Under the **Audio and Subtitles** group, select the **Subtitles track** and **Audio track**.

.. raw:: html

   </ul>

.. raw:: html

   <li>

Check **Show more options** to see more play options. Refer to `Additional playing options <#Additional_Playing_Options>`__.

.. raw:: html

   </li>

.. raw:: html

   </ol>

Playing more than one media file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VLC has an option to play two media files synchronously.

#. From the **Media** menu, select the **Advanced Open File** option.

The Open dialog box is displayed.

.. raw:: html

   <li>

Select a media file.

.. raw:: html

   </li>

.. raw:: html

   <li>

Check the **Show more options** option. The screen expands to show more options.

.. raw:: html

   </li>

.. raw:: html

   <li>

Check the **Play another media synchronously** option. The **Extra media** box and a **Browse** button are displayed.

.. raw:: html

   </li>

.. raw:: html

   <li>

In the **Extra media** box, enter the name of another media file with complete path or use the **Browse** button to select the media file.

.. raw:: html

   </li>

.. raw:: html

   <li>

You can change the **Caching** value for the media file being played.

.. raw:: html

   </li>

.. raw:: html

   <li>

Select the time at which the media file should start from the **Start Time** list.

.. raw:: html

   </li>

.. raw:: html

   <li>

You can see the selection you made in the **Customize** box.

.. raw:: html

   </li>

.. raw:: html

   <li>

Click on the **Play** button.

.. raw:: html

   </li>

.. raw:: html

   </ol>

You can use the **Show more options** to watch a video while listening to an audio file or listen to two audio files played synchronously (one audio track can have the instrumental part and the other can have the corresponding voice).

Opening a Network
-----------------

You can open a network and stream media from the selected network to the specified hosts. When you open a network you specify the network to be used for streaming media content.

#. From the **Media** menu select **Open Network** or **Advanced Open File** option and then select the **Network** tab.

The Open dialog box is displayed.

.. raw:: html

   <li>

Select a protocol from the **Protocol** list.

.. raw:: html

   </li>

The supported protocols are HTTP, HTTPS, FTP, MMS, RTSP, RTP, UDP and RTMP. MMS, RTP, RTMP, RTSP and UDP protocols are suitable for streaming media. The RTP, RTMP and RTSP protocols are for real transmission.

.. raw:: html

   <li>

Select a protocol suitable to your content.

.. raw:: html

   </li>

.. raw:: html

   <li>

In the **Address** box, enter the address of the system from which the media is going to be streamed.

.. raw:: html

   </li>

.. raw:: html

   <li>

In the **Port** box, enter the port number from which streaming is done.

.. raw:: html

   </li>

The default number is 1234.

.. raw:: html

   <li>

When UDP is selected, the **Allow Timeshifting** option is enabled.

.. raw:: html

   </li>

Timeshifting refers to the recording of programmes in a storage medium which is to be viewed or listened to at a time more convenient. Typically, this refers to TV programming but can also refer to radio shows through podcasts.

When the network stream is played, the stream can be paused even if it is a live stream

.. raw:: html

   <li>

Enter a URL in the **Address** box.

.. raw:: html

   </li>

Note: The **Port** list is enabled only when RTP or UDP is selected.

.. raw:: html

   <li>

Click on the |submenu.JPG| before the **Play** button and select **Stream** from the popup menu.

.. raw:: html

   </li>

.. raw:: html

   <li>

| In the Stream Output dialog box, specify the media file to be streamed and the address to which the streaming should be done.
| In the Stream Output dialog, you can specify further options. Refer to `Specifying the Streaming Options <#Specifying_Streaming_Options>`__.

.. raw:: html

   </li>

.. raw:: html

   <li>

Click on the **Stream** button.

.. raw:: html

   </li>

Note: When the streaming is being done, the slider moves to show the progress.

Specifying Streaming Options
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

VLC provides several options for streaming media files. You can stream media files in two ways.

#. Select **Streaming** from the **Media** menu.

| 
| Or
| Select **Advanced Open File** from the **Media** menu. The Open dialog box is displayed.

.. raw:: html

   </li>

.. raw:: html

   <li>

Click on the |submenu.JPG| icon next to the **Play** button and select **Stream** from the popup menu.

.. raw:: html

   </li>

The Stream Output dialog box is displayed.

.. raw:: html

   </ol>

Specify Outputs

#. Check the **Play locally** option to play the file while it is being streamed.
#. Check the **File** option to specify a path to save the converted file or click on the **Browse** button. The Save File dialog box is displayed. Select a container format from the **Save As Type** list.

A container is a file that can contain audio and video. You can also browse a folder to save the converted file. The audio and video is encoded using codecs and then stored in a container. A file’s extension can be used to identify the container format. VLC provides the following container formats:

.. raw:: html

   <table width="80%" border="1">

.. raw:: html

   <tr>

.. raw:: html

   <td width="5%" bgcolor="#F5F5F5">

Format

.. raw:: html

   </td>

.. raw:: html

   <td width="75%" bgcolor="#F5F5F5">

Description

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td width="5%">

.ps

.. raw:: html

   </td>

.. raw:: html

   <td width="75%">

Refers to MPEG program stream. Stores M-PEG 2 video muxed with other streams.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td width="5%">

.ts

.. raw:: html

   </td>

.. raw:: html

   <td width="75%">

Refers to MPEG transport stream. Used for streaming video through a network or by a satellite.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td width="5%">

.mpg

.. raw:: html

   </td>

.. raw:: html

   <td width="75%">

Refers to a family of standards used for coding audio and visual information.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td width="5%">

.ogg

.. raw:: html

   </td>

.. raw:: html

   <td width="75%">

Refers to professional grade media product. Ogg Vorbis encodes audio and Ogg Theora encodes video.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td width="5%">

.asf

.. raw:: html

   </td>

.. raw:: html

   <td width="75%">

Stores Windows Media Audio and Windows Media Video. ASF is designed to be used over audio and video information and is specially designed to run over networks.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td width="5%">

.mp4

.. raw:: html

   </td>

.. raw:: html

   <td width="75%">

M-PEG 4 audio and video. Provides compression for web, voice and broadcast television applications.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td width="5%">

.mov

.. raw:: html

   </td>

.. raw:: html

   <td width="75%">

Refers to the QuickTime media format. Used to store audio and video.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </table>

.. raw:: html

   <li>

Select a file or enter the file name in the **File** name box.

.. raw:: html

   </li>

.. raw:: html

   <li>

Click on **Save** to save the media file in the selected container format.

.. raw:: html

   </li>

.. raw:: html

   <li>

Check the **Dump Raw Output** box to save the input stream as it is read by VLC, without any processing. If this option is selected, all other options are disabled.

.. raw:: html

   </li>

.. raw:: html

   <li>

Select HTTP to stream media files using the HTTP streaming method. Specify the **Address** and **Port**.

.. raw:: html

   </li>

.. raw:: html

   <li>

| Select the **MMSH** access method to stream media files to the Microsoft Windows Media Player. The **Address** and **Port** options are enabled. Specify the **Address** and **Port**.
| MMS is a proprietary digital media streaming protocol developed by Microsoft. MMSH is MMS over HTTP.

.. raw:: html

   </li>

.. raw:: html

   <li>

| Select **RTP** to stream the media using the RTP method. The Prefer UDP over RTP, Address, Port, Audio Port and Video Port options are enabled.
| RTP refers to the Real-Time Transfer Protocol. Like UDP, RTP can use both unicast and multicast addresses. RTP or UDP is extensively used for streaming live audio and video.

.. raw:: html

   </li>

.. raw:: html

   <li>

Specify the **Address**, **Port**, **Audio Port** and **Video Port**.

.. raw:: html

   </li>

.. raw:: html

   <li>

Select the **Prefer UDP over RTP** option.

.. raw:: html

   </li>

VLC automatically tries to stream the media using the UDP protocol. If the streaming fails, VLC uses the IP address specified for the RTP protocol. This option can be used when no intervention is required from the consumer. The **Audio Port** and **Video Port** options get disabled if the Prefer UDP over RTP option is selected.

.. raw:: html

   <li>

| Select **IceCast** to distribute live audio and video over the Internet in real time.

-  Enter the **Address** and **Port** details.
-  Enter the login name and password in the **Login:pass:** box.
-  Enter the name of the **Mount Point** where the current listener should be redirected to.

An IceCast mount point refers to a connector between an IceCast source stream and IceCast listeners.

.. raw:: html

   </li>

.. raw:: html

   <li>

| Select a profile from the **Profile** list. The available profiles are Custom, Ogg/Vorbis, MPEG-2, MP3, MPEG-4 audio AAC, MPEG-4/DivX, H264, IPod (MP4, aac), Xbox, Windows (wmv/asf), and PSP.

.. raw:: html

   </li>

.. raw:: html

   <li>

Choose the encoder format from the **Profiles** or customise it.

.. raw:: html

   </li>

.. raw:: html

   <li>

Customise the other options by selecting the Encapsulation, Video codec, Audio codec and Subtitles tabs.

.. raw:: html

   </li>

Note: The options under Encapsulation, Video codec, Audio codec and Subtitles tabs are enabled only if you select the **Custom** option.

Encapsulation

Refers to the format in which a stream is encapsulated. The available formats are MPEG-TS, MPEG-PS, MPEG 1, Ogg/Ogm, ASF/WMV, MP4, MOV, WAV, RAW, FLV and MKV. From the **Encapsulation** tab, select an encapsulation method that fits the codecs and access method of your stream.

Video Codec

The **Video** option is selected by default. The options related to codec, and bitrate are enabled only if the Video option is checked.

-  Select the required codec from the **Codec** list. The available video codecs are MPEG-1, MPEG-2, MPEG-4, DIVX 1, DIVX 2, DIVX 3, H-263, H-264, WMV1, WMV2, MPEG, and Theora.
-  Specify an average bitrate in the **Bitrate** (kb/s) box.
-  Select a scale from the Scale list. The values are 1, 0.25, 0.5, 0.75, 1.25, 1.5, 1.75, and 2.

Audio Codec

The **Audio** option is selected by default. The options related to codec, bitrate and channels are enabled only if the Audio option is checked.

-  Select an audio codec from the **Codec** list. The available audio codecs are Vorbis, MPEG Audio, MP3, MPEG4 Audio (AAC), A52/AC-3, Flac, Speex, WAV and WMA.
-  Specify an average bit rate in the **Bitrate** (kb/s) box.
-  Select a channel from the **Channels** list. In audio, a channel refers to a stream of audio that is to be played by one speaker. For example, stereo audio, consists of two channels.

Subtitles

Specify subtitles to be streamed along with your media file. To specify subtitles

-  Check the **Subtitles** checkbox and select a subtitle from the **Subtitle** list.

This is the subtitle format that is to be included with the media that is streamed.

.. raw:: html

   <li>

Check the **Overlay subtitles on the video** option to render subtitles directly on the video, while transcoding it.

.. raw:: html

   </li>

.. raw:: html

   </ul>

Miscellaneous

Time-To-Live (TTL)- This sets the numbers of routers your stream can go through, for UDP unicast and unicast access methods. With UDP multicast, the default TTL is set to 1, meaning that your stream won't get across any router. You may want to increase it if you want to route your multicast stream.

SAP Announce - SAP is a way to publicly announce streams that are being sent using multicast UDP or RTP. Enter the name of the stream in the text box. This is available only for the RTP streaming method.

   Group Name – This allows you to specify a group for the session, which will be announced. Enter a name. This option is enabled only if the **SAP Announce** box is checked.

Stream all elementary streams – Select this option to you to stream all soundtracks and subtitles. This option separates the different elementary streams from a stream, and saves each of them in a different file or sends it to a separate destination.

Keep stream output open - Select this option to save incoming streams. This option is also used to make VLC act as a streaming server.

The options selected are displayed as a concatenated string in the **Generated Stream Output String** box.

.. raw:: html

   <li>

Click on the Stream button. The selected file is streamed to the selected locations.

.. raw:: html

   </li>

**Note:** The **Streaming** option present under the **Media** menu is the same as the **Stream** option in the |submenu.JPG| list.

Common Options
~~~~~~~~~~~~~~

VLC provides some common options which are easily accessible. Select **Advanced Open File** from the **Media** menu.

The Open file dialog box is displayed. There are four tabs such as **File**, **Disc**, **Network** and **Capture Device**. The options mentioned in the table are part of a dropdown list which is displayed when the |submenu.JPG| button is clicked.

.. raw:: html

   <table width="60%" border="1">

.. raw:: html

   <tr>

.. raw:: html

   <td width="10%" bgcolor="#F5F5F5">

Option

.. raw:: html

   </td>

.. raw:: html

   <td width="10%" bgcolor="#F5F5F5">

Shortcut Key

.. raw:: html

   </td>

.. raw:: html

   <td width="40%" bgcolor="#F5F5F5">

Description

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td width="10%">

Enqueue

.. raw:: html

   </td>

.. raw:: html

   <td width="10%">

Alt + E

.. raw:: html

   </td>

.. raw:: html

   <td width="40%">

Adds media files to the playlist but doesn't play it until you click **Play**.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td width="10%">

Play

.. raw:: html

   </td>

.. raw:: html

   <td width="10%">

Alt + P

.. raw:: html

   </td>

.. raw:: html

   <td width="40%">

Adds media files to the playlist and plays the media.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td width="10%">

Stream

.. raw:: html

   </td>

.. raw:: html

   <td width="10%">

Alt + S

.. raw:: html

   </td>

.. raw:: html

   <td width="40%">

Adds media files to the playlist and streams it on the network.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td width="10%">

Convert

.. raw:: html

   </td>

.. raw:: html

   <td width="10%">

Alt + C

.. raw:: html

   </td>

.. raw:: html

   <td width="40%">

| Adds media files to the playlist.
| Converts a media file into the selected format.

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </table>

**Note:** Leave **Play locally** unchecked because it decreases the conversion time. If you simultaneously play a file and convert it, it takes much more time.

Opening a Capture Device
------------------------

A capture device captures an image from a video file or sound from an audio file. Capture devices include webcams, external DVD players, TV cards and acquisition cards. VLC supports capture devices if the devices have the DirectShow compatible drivers.

To capture media

#. Select **Open Capture Device** from the **Media** menu. The Open dialog box is displayed with the **Capture Device** tab selected.

VLC media player supports three modes of capture DirectShow, DVB DirectShow and Desktop.

**DirectShow:** DirectShow, a Windows media streaming architecture, supports capture from digital and analog devices. DirectShow automatically detects and uses video and audio acceleration hardware when available, but also supports systems without acceleration hardware.

To capture content using the DirectShow plug-in, select **DirectShow** from the **Capture Mode** list. The options in the rest of the dialog box change based on the option selected in the Capture Mode list.

| If you want to capture video, select a device from the list next to the **Configure** button under the **Card Selection** group. VLC provides default values. To adjust more options, select the required options from the device settings.

#. Click on the **Configure** button for Video. The Properties dialog box is displayed with two tabs, **Device Settings** and **Advanced**.
#. If the device name does not appear in the list, click on the **Refresh** button. The device name appears in a list next to the **Configure** button.

| **Device Settings**
| |Device_settings.JPG|

If the **Auto** box is checked for any parameter, the software automatically fixes the value for the parameter based on the video file. By default, the Auto option is enabled only for the White Balance parameter.

-  **Brightness:** Move the slider till you get the desired brightness for the video capture. The default value is 5000.
-  **Contrast:** Refers to the difference in visual properties that makes an object distinguishable from other objects and the background. Move the slider till you get the desired contrast. The default value is 5000.
-  **Saturation:** Refers to the difference of a color against its own brightness. Move the slider to get the desired effect. The default value is 5000.
-  **Sharpness:** Refers to the clarity of a video. Move the slider till you get the desired sharpness for the video capture. The default value is 6000.
-  **White Balance:** Refers to colour balance. This option helps to make white actually white and makes skin tones look more natural. Uncheck the **Auto** option and Move the slider to get the desired effect.
-  **Backlight Comp:** Refers to the ability of a camera to compensate in cases where a subject with a large amount of background light would otherwise be obscured by excessive light. The default value is 0. Move the slider to get the desired effect.

**Advanced Settings**

.. figure:: advanced_settings.JPG
   :alt: advanced_settings.JPG

   advanced_settings.JPG

**Automatic Gain Control** – Is a circuit found on some electronic devices that automatically controls the gain of a signal. In AGC, weaker signals receive more gain and stronger signals receive less gain or none at all.

-  **Exposure** - Refers to the amount of light allowed to fall on a selected media file while capturing images. There are occasions when you may have to manually adjust the exposure on your camera. Exposure is measured in seconds.
   For example, you have to take a shot of a person from a certain angle, and there is bright light behind the person. In such case, aim your camera on the person and adjust the exposure value by moving the slider. The specified value remains unchanged even after closing the VLC application.
-  **Gain** - This option allows increasing or decreasing the brightness of the video being captured.
   When **Automatic Gain Control** is selected, the values you specified are taken as the default values for Exposure and Gain.
   Uncheck **Automatic Gain Control** to change the values of **Exposure** and **Gain** by moving the sliders.

**Image Mirror**

-  **Mirror Horizontal** – If you select this option, the video clip is flipped horizontally. You can see a mirror view of the captured picture.
-  **Mirror Vertical** - If you select this option, the video clip is flipped upside down.

**Anti-Flicker** – Refers to a process of filtering digital images to reduce image flicker. The available options are Off, 50 Hz (European) and 60 Hz (North America).

**Image Enhancement** – You can enhance the video being captured in terms of light and color using the following options:

-  **Low Light Boost** – If you check this option, the exposure time of the camera increases in poor light conditions.
-  **Color Boost** – If you check this option, the colors of the video being captured are boosted.

If you want to capture audio, select a device from the list next to the **Configure** button under the **Card Selection** group.

Click on the **Configure** button for Audio. The Properties dialog box is displayed. Specify the AudioInputMixer properties.

.. figure:: Audioinputprop.JPG
   :alt: Audioinputprop.JPG

   Audioinputprop.JPG

In the Master Input Mix group, check the **Enable** box. Control the tone of the audio using the Treble and Bass sliders.

-  **Loudness** – Refers to volume of the audio. Adjust the volume by moving the slider.
-  **Mono** – Refers to an amplifier connection. Adjust the volume by moving the slider.

In the Pin Line Input Mix group, check the **Enable** box. Select a line from the **Pin Line** list. The values in the Pin Line list are populated based on the selected audio input device.

.. raw:: html

   <li>

Click on the **Advanced options** button to specify the following properties:

.. raw:: html

   </li>

-  **Caching value in ms** – Refers to the caching value for DirectShow streams. Enter or select a value.
-  **Video device name** – Refers to the name of the video device that is used by DirectShow plugin. If you do not specify a device, the default device is used.
-  **Audio device name** – Refers to the name of the audio device that is used by DirectShow plugin. If you do not specify a device, the default device is used.
-  **Video size** – Refers to the size of the video that is displayed by the DirectShow plugin. The size of video is measured in pixels. If you do not specify the size, the default size is used.
-  **Video input chroma format** - Chroma refers to the way colors are encoded. Enter a specific chroma format. The default value is 1420.
-  **Video input frame rate** – Enter a specific frame rate. The default value is 0.
-  **Device properties** – Check this option to view the properties dialog of the selected device before starting the stream.
-  **Tuner properties** – Using this option you can set channels. A tuner converts signals into picture and sounds. Select this option to view the tuner properties (channel selection) dialog box.

-  **Tuner TV channel** – Refers to a tuner for setting TV channels. The default is 0. The default channel is used to capture the media.
-  **Tuner country code** – This option helps to establish the current channel-to-frequency mapping. The default is 0.
-  **Tuner input type** – Select the tuner input type. Available values are cable and antenna.
-  **Video input pin** – Select a video input source. Available values are Composite, S-video, and Tuner. These settings are hardware-specific. -1 means that settings will not be changed.
-  **Audio input pin** – This option is used to capture audio using a specific audio input pin. These settings are hardware-specific. Select a number from the Audio input pin list.
-  **AM Tuner mode** – This option is used to select a AM (amplitude modulation). The following are the tuner modes:

.. raw:: html

   <table border="1">

.. raw:: html

   <tr>

.. raw:: html

   <td bgcolor="#F5F5F5">

Value

.. raw:: html

   </td>

.. raw:: html

   <td bgcolor="#F5F5F5">

Mode

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

0

.. raw:: html

   </td>

.. raw:: html

   <td>

Default

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

1

.. raw:: html

   </td>

.. raw:: html

   <td>

TV

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

2

.. raw:: html

   </td>

.. raw:: html

   <td>

AM Radio

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

3

.. raw:: html

   </td>

.. raw:: html

   <td>

FM Radio

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   <tr>

.. raw:: html

   <td>

4

.. raw:: html

   </td>

.. raw:: html

   <td>

DSS

.. raw:: html

   </td>

.. raw:: html

   </tr>

.. raw:: html

   </table>

Select a number from the **AM Tuner mode** list.

.. raw:: html

   <li>

Number of audio channels – Select an audio input format with the given number of audio channels. If the channels are unavailable, select 0.

.. raw:: html

   </li>

.. raw:: html

   <li>

Audio sample rate – This option is used to set the sample rate. If the rates are unavailable, select 0.

.. raw:: html

   </li>

.. raw:: html

   <li>

Audio bits per sample – Select audio input format with the given bits or sample. If the audio bits are unavailable, select 0.

.. raw:: html

   </li>

.. raw:: html

   </ul>

.. raw:: html

   </ul>

.. raw:: html

   <li>

Select the **Convert** option to select the encoding formats and click on the **Save** button. Refer to `Converting and Saving a media file format <#Converting_and_Saving_a_Media_File_Format>`__.

.. raw:: html

   </li>

.. raw:: html

   <li>

Click on the **Play** button. The capturing of the media starts.

.. raw:: html

   </li>

.. raw:: html

   </ol>

**DVB DirectShow** - Refers to a suite of internationally accepted open standards for digital television. VLC media player supports three types of DVBs and they are:

-  **DVB-S** - Is an abbreviation for Digital Video Broadcasting - Satellite. It is the Digital Video Broadcasting forward error coding and modulation standard for satellite television. This is used via satellites.
-  **DVB-C** – Is an abbreviation for Digital Video Broadcasting – Cable. It is the DVB European consortium standard for the broadcast transmission of digital television over cable. This system transmits MPEG-2 or MPEG-4 audio and video streams using a QAM modulation.
-  **DVB-T** - Is an abbreviation for Digital Video Broadcasting – Terrestrial. It is the DVB European-based consortium standard for the broadcast transmission of digital terrestrial television. This system transmits compressed audio, video and other data in the MPEG format using the COFDM modulation.

**Note:** Ensure that you have the DVB card installed on your PC.

**DVB-S** – You can stream a live TV from a PC using the DVB-S option. To stream

#. Select **Open Capture Device** from the **Media** menu. The Open dialog box is displayed.
#. Select the **Open Capture Device** tab.
#. Select **DVB DirectShow** from the **Capture Mode** list.
#. Select **DVB-S** from **DVB Type** under the **Card Selection** group. In the **Options** group, specify the following
#. Select **Transponder/multiplex frequency** to set the transponder frequency. A transponder is a device that receives, amplifies and retransmits a signal on a different frequency.
#. Select **Transponder symbol rate** to set the transponder symbol rate.
#. Click on the **Advanced options** button to specify the following parameters:

-  **Caching value in ms** – Refers to caching value for the DirectShow stream. Enter a value in milliseconds.
-  **Transponder / multiplex frequency** - A transponder is a device that receives, amplifies and retransmits a signal on a different frequency. Select a frequency.
-  **Inversion Mode** - Description to be added
-  **Satellite polarization** – Polarization is a method of giving transmission signals a specific direction. The signals transmitted by a satellite can be polarized in four ways and they are: Horizontal, Vertical, Circular Left and Circular Right. Select an option.
-  **Network identifier** – Refers to a unique ID used to identify a network. Select a number from the **Network identifier** list.
-  **Satellite Azhimuth** – Azhimuth is an angular measurement made in the horizontal plane. Enter a value.
-  Satellite Elevation– This option defines the angle between the Earth and the position of a satellite. Enter a value.
-  **Satellite Longitude** – Refers to the satellite longitude in 10ths of degree. Enter a value.
-  **Antenna lnb_lof1** – Refers to low band local Osc Freq in kHz. Enter a value in kHz.
-  **Antenna lnb_lof2** - Refers to high band local Osc Freq in kHz. Enter a value in kHz.
-  **Antenna lnb_slof** – Refers to low noise block switch freq in kHz. Enter a value in kHz.
-  **Transponder FEC** – Refers to the forward error correction mode. Enter a value in kHz.
-  **Transponder symbol rate in kHz** Description to be added
-  **Modulation Type** – Refers to the QAM constellation points. The available values are 16, 32, 64, 126, and 256.
-  **Terrestrial high priority stream code rate (FEC)** – Refers to the high priority FEC Rate. The available values are Undefined, 1/2, 2/3, 3/4, 5/6 and 7/8.
-  **Terrestrial low priority stream code rate (FEC)** – Refers to the low priority FEC Rate. The available values are Undefined, 1/2, 2/3, 3/4, 5/6, and 7/8.
-  **Terrestrial bandwidth** - Description to be added
-  **Terrestrial guard interval** – Refers to a parameter that is used in encoding and modulation. Select an interval from the list.
-  **Terrestrial transmission mode** - Description to be added
-  **Terrestrial hierarchy mode** - Description to be added

.. raw:: html

   </ol>

**DVB-C** - You can stream digital TV using digital signal cables. The following is a procedure to stream content using the DVB-C standard.

#. Select **Open Capture Device** from the **Media** menu. The Open dialog box is displayed.
#. Select the **Open Capture Device** tab.
#. Select **DVB DirectShow** from the **Capture Mode** list.
#. Select **DVB-C** from **DVB Type** under the **Card Selection** group.
#. Select **Transponder/multiplex frequency** to set the transponder frequency.
#. Select **Transponder symbol rate** to set the transponder symbol rate.
#. Select an extra media if you want some background music using **Show more options**. Refer to [[#Playing_more_than_one_media_filePlaying more than one media file.
#. Select **Convert** to select the encoding formats and click on the **Save** button. Refer to Converting and Saving a Media File Format.
#. Click on the **Play** button to play the media.
#. Click on the **Cancel** button to exit the screen.

**DVB-T** - Follow the procedure below to stream DVB-T channels:

#. Select **Open Capture Device** from the **Media** menu. The Open dialog box is displayed.
#. Select the **Open Capture Device** tab.
#. Select **DVB DirectShow** from the **Capture Mode** list.
#. Select **DVB-T** from **DVB Type** under the **Card Selection** group.
#. Select **Transponder/Multiplex frequency** to set the transponder frequency.
#. Select **Bandwidth** to set the terrestrial bandwidth.
#. Select an extra media if you want some background music using **Show more options**. Refer to Playing more than one media file.
#. Click on the **Play** button to play the media.
#. Click on the **Cancel** button to exit the screen.

**Note:** The Advanced Options for the DVB-C and DVB-T are the same as the Advanced Options for the DVB-S.

**Desktop** - You can capture all your mouse movements and application actions and save the video in the selected format. This option is used to record the on-screen activity on your Windows desktop. For example, you can create videos to demonstrate the features or usage of a software.

#. To capture the desktop, select **Open Capture Device** from the **Media** menu. The Open dialog box is displayed.
#. Select the **Open Capture Device** tab.
#. Select **Desktop** from the **Capture Mode** list.
#. Enter a frame rate in the **Desired frame rate** for the capture box.
#. Select **Convert** to select the encoding formats and click on the **Save** button. Refer to Converting and Saving a media file format.
#. Select an extra media if you want some background music using **Show more options**. Refer to Playing more than one media file.
#. Click on the **Play** button to play the media.
#. Click on the **Cancel** button to exit the screen.

.. |VLC_-_eject.png| image:: VLC_-_eject.png
.. |submenu.JPG| image:: submenu.JPG
.. |Device_settings.JPG| image:: Device_settings.JPG

