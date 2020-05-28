=Open a media with VLC Player= To play a media with VLC player, use an
intent with the following settings

== action ==
   Intent.ACTION_VIEW ("android.intent.action.VIEW")

== Package name ==
   "org.videolan.vlc"

== data == The media Uri

== type == one of:

-  video/\*
-  audio/\*
-  \*/rmvb
-  \*/avi
-  \*/mkv
-  application/3gpp\*
-  application/mp4
-  application/mpeg\*
-  application/ogg
-  application/sdp
-  application/vnd.3gp\*
-  application/vnd.apple.mpegurl
-  application/vnd.dvd\*
-  application/vnd.dolby\*
-  application/vnd.rn-realmedia\*
-  application/x-iso9660-image
-  application/x-extension-mp4
-  application/x-flac
-  application/x-matroska
-  application/x-mpegURL
-  application/x-ogg
-  application/x-quicktimeplayer
-  application/x-shockwave-flash
-  application/xspf+xml
-  misc/ultravox

== Extras (optional) ==

{\| class="wikitable" -\| "subtitles_location" \|\| String \|\| Path of
a subtitles file "title" \|\| String \|\| Title you want to display
"from_start" \|\| boolean \|\| Force playback from the beginning
"position" \|\| int/long \|\| Set position to start playback, in
milliseconds "extra_duration" \|\| long \|\| Media duration \|}

== Sample code == For a simple media playback: int vlcRequestCode = 42;
Uri uri = Uri.parse("\ file:///storage/emulated/0/Movies/KUNG FURY
Official Movie.mp4"); Intent vlcIntent = new Intent(Intent.ACTION_VIEW);
vlcIntent.setPackage("org.videolan.vlc");
vlcIntent.setDataAndTypeAndNormalize(uri, "video/*");
vlcIntent.putExtra("title", "Kung Fury");
vlcIntent.putExtra("from_start", false); vlcIntent.putExtra("position",
90000l); vlcIntent.putExtra("subtitles_location",
"/sdcard/Movies/Fifty-Fifty.srt"); startActivityForResult(vlcIntent,
vlcRequestCode);

If you specifically want start VideoPlayerActivity, you can set
   vlcIntent.setComponent(new ComponentName("org.videolan.vlc",
   "org.videolan.vlc.gui.video.VideoPlayerActivity"));

=Get result code from VLC= Since version 1.4.1, Android VLC application
returns an intent when closing.

Here is the description of this intent:

==Intent action==
   "org.videolan.vlc.player.result"

==Result code== {\| class="wikitable" -\| RESULT_OK \|\| -1 \|\| Video
finished or user ended playback RESULT_CANCELED \|\| 0 \|\| No
compatible cpu, incorrect VLC abi variant installed
RESULT_CONNECTION_FAILED \|\| 2 \|\| Connection failed to audio service
RESULT_PLAYBACK_ERROR \|\| 3 \|\| VLC is not able to play this file, it
could be incorrect path/uri, not supported codec or broken file
RESULT_HARDWARE_ACCELERATION_ERROR \|\| 4 \|\| Error with hardware
acceleration, user refused to switch to software decoding
RESULT_VIDEO_TRACK_LOST \|\| 5 \|\| VLC continues playback, but for
audio track only. (Audio file detected or user chose to) \|}

==Data== Media Uri

You can check the source
[http://git.videolan.org/?p=vlc-ports/android.git;a=blob;f=vlc-android/src/org/videolan/vlc/gui/video/VideoPlayerActivity.java;hb=HEAD
here].

==Extras== {\| class="wikitable" -\| "extra_position" \|\| long \|\|
Last position in media when player exited "extra_duration" \|\| long
\|\| Total duration of the media

\|}

==See also== \* [[Android Report bugs]] - Bug reporting guide for
VLC-Android.

[[Category:Building]] [[Category:Android]]
