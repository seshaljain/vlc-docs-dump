:''This page is outdated. Please see [[Documentation:Streaming HowTo
New#Streaming using the GUI]] for updated streaming tutorials.''

{{RightMenu|documentation streaming howto toc}}

==Intro==

The easier way to start streaming with VLC is by using one of the
graphical user interfaces. These are the wxWindows and skinnable
interfaces for Windows and GNU/Linux and the Mac OS X native interface.

==Streaming using the Wizard==

The ''Streaming/Transcoding Wizard'' leads you step by step through the
process of streaming your media on a network or saving it to your hard
drive. This ''Wizard'' offers easy to use menus but provides a
restricted set of options.

Note: The wizard is only available on the wxWindows interface.

===Launching the wizard===

To launch the ''Streaming/Transcoding Wizard'' open the "File" menu, and
select the Wizard menu item.

https://images.videolan.org/images/documentation/streaming-howto/intf-wx-wizard.jpg
Launching the Wizard

===Wizard dialog===

First select the type of task: *''Stream to network'': Choose this
option if you want to stream media on a network.*''Transcode/Save to
file'': Choose this option if you want to change a file's audio codec
and/or video codec, its bitrate, and/or encapsulation method.

https://images.videolan.org/images/documentation/streaming-howto/intf-wx-wizard-first.jpg
The Wizard Dialog

===Input selection===

Select a stream (such as a file, a network stream, a disk, a capture
device ...) by selecting the ''Choose...'' dialog or an existing item in
your playlist, using the ''Existing playlist item'' option.

''Partial Extract'': To read only part of the stream, check the "Enable"
checkbox and choose a start and end date (in seconds). This option
should only be used with streams you can control such as files or discs
but not network streams or capture devices.

https://images.videolan.org/images/documentation/streaming-howto/intf-wx-wizard-input.jpg
Wizard input selection

https://images.videolan.org/images/documentation/streaming-howto/intf-wx-wizard-input-playlist.jpg
Wizard input selection from playlist

===Streaming methods===

If you chose ''Stream to network'' option, you can now specify the
streaming method. Available methods are: *''RTP/UDP Unicast'': Stream to
a single computer. Enter the client's IP address (in the 0.0.0.0 -
223.255.255.255 range).*''RTP/UDP Multicast'': Stream to multiple
computers using multicast. Enter the IP address of the multicast group
(in the 224.0.0.0 to 239.255.255.255 range). \*''HTTP'': Stream by using
the HTTP protocol. If you leave the ''Destination'' text box empty, VLC
will listen on all the network interfaces of the server on port 8080.
Specify an address, port and path on which to listen using the following
syntax [ip][:port][/path]. For instance, ''192.168.0.1:80/stream'' will
make VLC listen on the interface carrying the 192.168.0.1 IP address, on
the 80 TCP port, in the /stream ''virtual file''.

https://images.videolan.org/images/documentation/streaming-howto/intf-wx-wizard-stream.jpg
Wizard streaming method

===Transcoding options===

If you chose the ''Transcode/Save to file'' option, you can now specify
the new audio and video codecs and bitrates you want you input converted
to.

(See <xref linkend="smc" endterm="tsmc" />)

https://images.videolan.org/images/documentation/streaming-howto/intf-wx-wizard-transcode.jpg
Wizard transcode

===Encapsulation method===

Choose the method format. The UDP streaming methods require MPEG TS
encapsulation. The HTTP streaming method can be used with the MPEG PS,
MPEG TS, MPEG 1, OGG, RAW or ASF encapsulation. Saving to a file can be
done using any encapsulation format compatible with the chosen codecs.

(See <xref linkend="smc" endterm="tsmc" />)

https://images.videolan.org/images/documentation/streaming-howto/intf-wx-wizard-mux.jpg
Wizard encapsulation method

===Streaming options===

If you chose to ''Stream to network'' you can now specify several
options.

*''Time To Live (TTL)'' This sets the numbers of routers your stream can
go through, for UDP unicast and unicast access methods. If you do not
know what this means, you should leave the default value. Note: With UDP
multicast, the default TTL is set to 1, meaning that your stream won't
get across any router. You may want to increase it if you want to route
your multicast stream.* ''SAP Announce'' To advertise your stream over
the network when using the UDP streaming method, using the SAP protocol,
enter the name of the stream in the text input and check the checkbox.
This is NOT available for the HTTP streaming method.

https://images.videolan.org/images/documentation/streaming-howto/intf-wx-wizard-streaming-options.jpg
Wizard streaming options

===Save to file destination===

If you chose ''Transcode/Save to file'' you can now specify the file you
want to save the stream to.

https://images.videolan.org/images/documentation/streaming-howto/intf-wx-wizard-save.jpg
Wizard save file - wxWindows interface

You can now select the ''Finish'' button to start streaming/converting
the source.

==Streaming using the GUI==

===Introduction===

A second way to set up a streaming instance using VLC is using ''Stream
Output'' panel in the ''Open...'' dialog of the wxWindows (Windows / GNU
Linux), skinnable (Windows / GNU Linux) and MacOS X interfaces.
Streaming methods and options used 99% of time should be available in
this panel.

To stream the opened media, check the "Stream output" or "Stream/Save"
checkbox in the "Open File/Disc/Network Stream/Capture Device" dialog
and click on the "Settings" button.

https://images.videolan.org/images/documentation/streaming-howto/intf-wx-open-file.jpg
Open file dialog - wxWindows interface

https://images.videolan.org/images/documentation/streaming-howto/intf-osx-open-file.jpg
Open file dialog - Mac OS X interface

Note that "Capture" is not available as an option in Mac OSX because VLC
does not support live streaming of audio or video under Mac OSX.

===The Stream Output dialog===

https://images.videolan.org/images/documentation/streaming-howto/intf-wx-stream-output.jpg
Stream output dialog - wxWindows interface

https://images.videolan.org/images/documentation/streaming-howto/intf-osx-stream-output.jpg
Stream output dialog - wxWindows interface

====Stream Output MRL====

On the wxWindows interface, a text box displays the ''Stream Output
MRL'' (Media Resource Locator). This is updated as you change options in
the Stream output dialog. For more information on how to edit the
''Stream Output MRL'' read <xref linkend="cmdline" endterm="tcmdline"
/>.

====Output methods====

*''Play locally'': display the stream on your screen. This allows you to
display the stream you are actually streaming. Effects of transcoding,
rescaling, etc. can be monitored locally using this function.*''File'':
Save the stream to a file. The ''Dump raw input'' option allows you to
save the input stream as it is read by VLC, without any processing.
*''HTTP'': Use the HTTP streaming method. Specify the IP address and TCP
port number on which to listen.*''MMSH'': This access method allows you
to stream to Microsoft Windows Media Player. Specify the IP address and
TCP port number on which to listen. Note: This will only work with the
''ASF'' encapsulation method. *''UDP'': Stream in unicast by providing
an address in the 0.0.0.0 - 223.255.255.255 range or in multicast by
providing an address in the 224.0.0.0 - 239.255.255.255 range. It is
also possible to stream to IPv6 addresses. Note: This will only work
with the ''TS'' encapsulation method.*''RTP'': Use the Real-Time
Transfer Protocol. Like UDP, it can use both unicast and multicast
addresses.

Note: UDP, HTTP, MMSH, and RTP methods require you to select the
''Stream'' option on the MacOS X interface.

(See <xref linkend="smc" endterm="tsmc" />)

====Encapsulation method====

Select an encapsulation method that fits the codecs and access method of
your stream, among MPEG TS, MPEG PS, MPEG 1, OGG, Raw, ASF, AVI, MP4 and
MOV. (See <xref linkend="smc" endterm="tsmc" />)

====Transcoding options====

Enable video transcoding by checking the "Video Codec" checkbox. Choose
a codec from the list. You can also specify an average bitrate and scale
the input. (See <xref linkend="smc" endterm="tsmc" />)

Enable audio transcoding by checking the "Audio Codec" checkbox. Choose
a codec from the list. You can also specify an average bitrate and the
number of audio channels to encode. (See <xref linkend="smc"
endterm="tsmc" />)

====Miscellaneous options====

Select methods to announce your stream. You can use SAP (Service
Announce Protocol) or SLP (Service Location Protocol). You must also
specify a channel name. The Mac OS X interface also allows you to export
the description (SDP) file of a RTP session using the internal HTTP or
RTSP server of VLC, or as a file. This can be done using the according
checkboxes. The ''SDP URL'' text box allows to give the url or
destination where the SDP file will be available.

{{Documentation}}

[[Category:Outdated pages]]
