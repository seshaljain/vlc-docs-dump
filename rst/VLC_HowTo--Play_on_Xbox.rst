{{howto|Make your Video Files playable on a XBox}}

To play on XBox and XBox360 the file you copy to it needs to be of the
correct format. This format is summarized below:

== Codec Information ==

=== AVI support === \* File extensions: .avi, .divx \* Containers: AVI
\* Video profiles: MPEG-4 Part 2 (Simple Profile and Advanced Simple
Profile) \* Video bit rate: 5 Mbps with resolutions of 1280 × 720 at 30
fps \* Audio profiles: Dolby® Digital (2 channel and 5.1 channel), MP3
\* Audio max bit rate: No restrictions

=== H.264 support === \* File extensions: .mp4, .m4v, mp4v, .mov, .avi
\* Containers: MPEG-4, QuickTime \* Video profiles: Baseline, main and
high (up to level 4.1) \* Video bit rate: 10 Mbps with resolutions of
1920 × 1080 at 30 fps \* Audio profiles: AAC, 2-channel, Low Complexity
\* Audio max bit rate: No restrictions

=== MPEG-4 Part 2 support === \* File extensions: .mp4, .m4v, .mp4v,
.mov, .avi \* Containers: MPEG-4, QuickTime \* Video profiles: MPEG-4
Part 2 (Simple Profile and Advanced Simple Profile) \* Video bit rate: 5
Mbps with resolutions of 1280 × 720 at 30 fps \* Audio profiles: AAC,
2-channel, Low Complexity \* Audio max bit rate: No restrictions

=== WMV (VC-1) support === \* File extensions: .wmv \* Containers: ASF
\* Video profiles: WMV7 (WMV1), WMV8 (WMV2), WMV9 (WMV3), VC-1 (WVC1 or
WMVA) in simple, main and advanced up to level 3 \* Video bit rate: 15
Mbps with resolutions of 1920 × 1080 at 30 fps \* Audio profiles:
WMA7/8, WMA9 Pro (stereo and 5.1), WMA Lossless \* Audio max bit rate:
No restrictions

=== Maximum supported video file size === The maximum file size for an
MPEG-4 Part 2 or H.264 file is 4 GB. However, Windows Media Player 11
and the Zune software support streaming WMV files larger than 4 GB.

Source:
[http://support.xbox.com/en-US/xbox-360/settings-and-initial-setup/watch-dvds-movies]

== Batch file ==

The batch file can look like that on [[Windows]] <pre>c:vlcvlc -vvv %1
:sout=#transcode{vcodec=WMV2,vb=1500,scale=1,acodec=wma,ab=96,channels=2}:duplicate{dst=std{access=file,mux=asf,dst=%1.wmv}}</pre>
or <pre>"C:Program FilesVideoLANVLCvlc.exe" -vvv %1 --sout-ffmpeg-qscale
1
:sout=#transcode{vcodec=WMV2,scale=1,acodec=wma,ab=96,channels=2}:duplicate{dst=std{access=file,mux=asf,dst=%1.wmv}}</pre>

== VLC360 ==

If you have your computer connected at the same time, you can use VLC360
to play directly your Computer files on your Xbox 360.

[http://jortega74.free.fr/serendipity/ VLC360 forum]
[http://forums.xbox-scene.com/lofiversion/index.php/t499940.html
Screenshots]
