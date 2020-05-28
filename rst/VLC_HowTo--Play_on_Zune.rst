{{howto|Make your Video Files playable on a Zune}}

To play on this device, the file you copy to it needs to be of the
correct format. This format is summarized below: {\| \| Video Codec \|
'''wmv2''' ([[WMV]]), '''wmv3''' ([[WMV]]) Audio Codec \| '''wma'''
([[wma]]) [[Container]] \| '''avi''' ([[AVI]]), '''asf''' ([[ASF]]) Size
\| 320x240, 320x180 \|}

To make the video the correct size, you can edit the [[preferences]], or
run vlc from a [[command prompt]].

== CLI Example == Don't forget to point %outdir% to your target
directory. This will handle drag-and-drop batch conversion.

   @REM Set this next line to where you want your output files: @SET
   outdir=c:video@REM No further changes should be needed below for VLC
   0.9.8a @SET infile=%1 @SET infile=%infile:"=% @FOR /F "delims=" %%i
   in ("%infile%") do SET filename=%%~ni @SET
   outfile=%outdir%%filename%.wmv "C:Program FilesVideoLANVLCvlc.exe"
   -vvv
   --sout="#transcode{vcodec=WMV2,vb=750,width=320,canvas-height=240,acodec=wma,ab=128,channels=2}:duplicate{dst=std{access=file,mux=asf,dst=%outfile%}}"
   "%infile%" --play-and-exit

''The last line may be wrapped in your browser, however from "C:Program"
to "-and-exit" is all on one line.''

This is a script to batch process all files of a certain type in the
folder in is placed in to be compatible with the Zune.

<code><pre>for %%a in (*.mpg) do "C:Program FilesVideoLANVLCvlc.exe" -I
dummy -vvv "C:<output_folder>%%a" :sout="#transcode{width=320,
canvas-height=240, vcodec=WMV2, vb=1024, acodec=wma2, ab=128,
samplerate=44100,
channels=2}:standard{access=file,mux=asf,dst=C:<output_folder>%%a.wmv}"
vlc:quit</pre></code>

''This will look for all .MPG files in a folder. You can change this to
search for any type of file.''

''You need to change <output_folder> and/or the drive in both locations
to where the output files will go.''

== DVD Example ==

This script will transcode a dvd into a wmv compatible for the zune
software.

<code><pre>"C:Program FilesVideoLANVLCvlc.exe" -I dummy -vvv --color
dvdsimple:d::sout="#transcode{width=320, canvas-height=240, vcodec=WMV2,
vb=1024, acodec=wma2, ab=128, samplerate=44100,
channels=2}:standard{access=file,mux=asf,dst=C:<output_folder>output.wmv}"
vlc:quit</pre></code>

''You need to change <output_folder> and/or the dvd drive location.''

==Special Note==

As of VLC (0.8.6d) <01/01/2008>, the VLC client cannot transcode
correctly to WMV3, the video codec that the Zune player natively
requires. This is due to the fact that the new WMV3 codec does not open
have an open source counterpart like WMV1/WMV2 does. VLC instead uses
the Windows API to transcode and play WMV3 encoded videos. Transcoded
videos to WMV3 will be lacking in quality and although sync flawlessly
via the Zune software, they will restart the zune device after a few
seconds of playback.

Therefore it is recommended/required to transcode into the WMV2 codec,
and let the Zune software convert the video(s) into the required WMV3
codec for the Zune device.
