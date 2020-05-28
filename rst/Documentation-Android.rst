<big>------ Work in progress ------</big>

Here is the documentation of the Android port of VLC media player.

== Preliminary Notes == VLC for Android is a little different from VLC
on desktops. In some ways, you can do more; in other ways, you can do
less. VLC for Android only does media playback. Active streaming or file
/ stream to file conversations are not supported for usability and
performance reasons. This walk-through does only include screenshots of
a phone interface for size reasons. However, all features are also
available on tablets with a similar appearance.

<br> == Feature Overview ==

{\| border="1" cellpadding="2" class="wikitable" style="border: 1px
solid dark green; text-align: center; width: 100%; margin: 1em auto 1em
auto" ! scope="col" width="150px" \| Feature ! scope="col" width="100px"
\| Version 1.0 ! scope="col" width="100px" \| Version 1.6 ! scope="col"
width="100px" \| Version 2.0 ! scope="col" width="100px" \| Version 2.5
! scope="col" width="100px" \| Version 3.0 ! scope="col" width="100px"
\| Version 3.1 Opening Network Streams \|\| {{No}} \|\| {{Yes}} \|\|
{{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} UPnP discovery and
streaming \|\| {{No}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\|
{{Yes}} \|\| {{Yes}} Plex server discovery and streaming \|\| {{No}}
\|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}}
Password-protected Plex shares \|\| {{No}} \|\| {{No}} \|\| {{No}} \|\|
{{No}} \|\| {{No}} \|\| {{No}} Downloads from UPnP multimedia servers
\|\| {{No}} \|\| {{No}} \|\| {{No}} \|\| {{No}} \|\| {{No}} \|\| {{No}}
FTP discovery, streaming \|\| {{No}} \|\| {{Yes}} \|\| {{Yes}} \|\|
{{Yes}} \|\| {{Yes}} \|\| {{Yes}} Store FTP server bookmarks \|\| {{No}}
\|\| {{No}} \|\| {{No}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} Audio
Playback via Connector Cables \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}}
\|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} Video Playback via Connector
Cables \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}}
\|\| {{Yes}} Subtitles playback \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}}
\|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} Subtitles Font Customization \|\|
{{No}} \|\| {{No}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}}
Closed Caption playback \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\|
{{Yes}} \|\| {{Yes}} \|\| {{Yes}} Teletext subtitles playback \|\|
{{No}} \|\| {{No}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}}
Multi-track audio handling \|\| {{No}} \|\| {{Yes}} \|\| {{Yes}} \|\|
{{Yes}} \|\| {{Yes}} \|\| {{Yes}} Video Filtering incl. Screen
Brightness \|\| {{No}} \|\| {{No}} \|\| {{No}} \|\| {{No}} \|\| {{No}}
\|\| {{No}} Video Cropping and Aspect Ratio variation \|\| {{Yes}} \|\|
{{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}}
Deinterlacing \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\|
{{Yes}} \|\| {{Yes}} Playback Speed control \|\| {{Yes}} \|\| {{Yes}}
\|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} Audio/Subtitles
delay control \|\| {{No}} \|\| {{No}} \|\| {{Yes}} \|\| {{Yes}} \|\|
{{Yes}} \|\| {{Yes}} Repeated playback \|\| {{Yes}} \|\| {{Yes}} \|\|
{{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} Gestures based playback
control \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}}
\|\| {{Yes}} Playback of Audio-only media (mp3, m4a, flac, …) \|\|
{{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}}
Audio Playback in Background \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\|
{{Yes}} \|\| {{Yes}} \|\| {{Yes}} Video Playback in Background \|\|
{{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}}
Playback timer \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\|
{{Yes}} \|\| {{Yes}} Chapter & title selection \|\| {{No}} \|\| {{No}}
\|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} 10-band equalizer
\|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\|
{{Yes}} Playback UI Lock \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\|
{{Yes}} \|\| {{Yes}} \|\| {{Yes}} Smart Media Library sorting for audio
albums and TV shows \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}}
\|\| {{Yes}} \|\| {{Yes}} Media Library Search \|\| {{No}} \|\| {{Yes}}
\|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} Passcode Lock \|\|
{{No}} \|\| {{No}} \|\| {{No}} \|\| {{No}} \|\| {{No}} \|\| {{No}} Voice
search support \|\| {{No}} \|\| {{No}} \|\| {{No}} \|\| {{Yes}} \|\|
{{Yes}} \|\| {{Yes}} Voice actions support \|\| {{No}} \|\| {{No}} \|\|
{{No}} \|\| {{No}} \|\| {{No}} \|\| {{No}} Organize media in folders
\|\| {{No}} \|\| {{No}} \|\| {{No}} \|\| {{No}} \|\| {{No}} \|\| {{No}}
Use folders as playlists \|\| {{No}} \|\| {{No}} \|\| {{Yes}} \|\|
{{Yes}} \|\| {{Yes}} \|\| {{Yes}} Loop playlists \|\| {{Yes}} \|\|
{{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} Playback
control through headphones or lock screen \|\| {{Yes}} \|\| {{Yes}} \|\|
{{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} Mediasession support
(Wear, TV, etc…) \|\| {{No}} \|\| {{No}} \|\| {{Partial}} \|\| {{Yes}}
\|\| {{Yes}} \|\| {{Yes}} Playback is paused when headphones are
unplugged \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\|
{{Yes}} \|\| {{Yes}} WiFi upload and HTTP downloads in background \|\|
{{No}} \|\| {{No}} \|\| {{No}} \|\| {{No}} \|\| {{No}} \|\| {{No}}
Support for password protected HTTP streams \|\| {{No}} \|\| {{No}} \|\|
{{No}} \|\| {{No}} \|\| {{No}} \|\| {{No}} Sharing files with further
apps \|\| {{No}} \|\| {{No}} \|\| {{No}} \|\| {{No}} \|\| {{No}} \|\|
{{No}} Custom vlc:// protocol \|\| {{No}} \|\| {{No}} \|\| {{Yes}} \|\|
{{Yes}} \|\| {{Yes}} \|\| {{Yes}} Support for x-callback-url \|\| {{No}}
\|\| {{No}} \|\| {{No}} \|\| {{No}} \|\| {{No}} \|\| {{Yes}} Action mode
\|\| {{No}} \|\| {{No}} \|\| {{No}} \|\| {{Yes}} \|\| {{Yes}} \|\|
{{Yes}} Android TV \|\| {{No}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}}
\|\| {{Yes}} \|\| {{Yes}} Picture-in-Picture \|\| {{No}} \|\| {{No}}
\|\| {{Partial}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} ChromeOS support
\|\| {{No}} \|\| {{ARC}} \|\| {{ARC}} \|\| {{Yes}} \|\| {{Yes}} \|\|
{{Yes}} Android Auto \|\| {{No}} \|\| {{No}} \|\| {{No}} \|\| {{Yes}}
\|\| {{No}} \|\| {{Yes}} Sorting \|\| {{No}} \|\| {{No}} \|\|
{{Partial}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} 360° videos \|\|
{{No}} \|\| {{No}} \|\| {{No}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}}
DayNight mode \|\| {{No}} \|\| {{No}} \|\| {{No}} \|\| {{Yes}} \|\|
{{Yes}} \|\| {{Yes}} Chromecast \|\| {{No}} \|\| {{No}} \|\| {{No}} \|\|
{{No}} \|\| {{Yes}} \|\| {{Yes}} Equalizer custom presets \|\| {{No}}
\|\| {{No}} \|\| {{No}} \|\| {{No}} \|\| {{Yes}} \|\| {{Yes}} Audio
boost \|\| {{No}} \|\| {{No}} \|\| {{No}} \|\| {{No}} \|\| {{Yes}} \|\|
{{Yes}} Android 2.1 support \|\| {{Yes}} \|\| {{Yes}} \|\| {{No}} \|\|
{{No}} \|\| {{No}} \|\| {{No}} Android 2.2 support \|\| {{Yes}} \|\|
{{Yes}} \|\| {{Yes}} \|\| {{No}} \|\| {{No}} \|\| {{No}} Android 2.3
support \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}}
\|\| {{No}} Android 6 (Runtime permissions) \|\| {{No}} \|\| {{No}} \|\|
{{Yes}} \|\| {{Yes}} \|\| {{Yes}} \|\| {{Yes}} Android 8 support \|\|
{{No}} \|\| {{No}} \|\| {{No}} \|\| {{Partial}} \|\| {{Partial}} \|\|
{{Yes}} \|}

== Installation == There are many ways to install VLC on Android. This
may be because you have a non-ARMv7 or x86 processor or do not wish to
use the Play Store for whatever reason.

=== From the Play Store (recommended) === The normal way, for ARMv7 (and
above) and x86 processors only. Don't know your processor? Don't worry,
if you can download it, you have a compatible ARMv7 or an x86 processor.

: https://play.google.com/store/apps/details?id=org.videolan.vlc <br>

=== From the F-Droid Repository === The F-Droid repository
(https://f-droid.org) is a completely FOSS (Free and Open Source
Software) equivalent to the Google Play Store. The F-Droid Repository
and all apps within it are provided completely free of charge and
licensed under open source licenses. The F-Droid repository can be
downloaded directly from their website. The "Unknown Sources" setting
must be turned on for Android devices (typically located in Settings ->
Security) in order to install repositories other than the Google Play
Store. <br><br>

=== From VideoLAN === If you can't download from the Play Store or just
want to install the VLC .apk by yourself, follow these steps:

# Go to Android Settings → Security → Device Administration → Enable
'Unknown Sources' # Go to our download server, preferably from your
device: http://get.videolan.org/vlc-android/\ {{Android:latest
version}}/ # Choose your processor architecture (ARMv7 or Intel x86) and
grab the .apk file. # Click on the .apk you just downloaded and install
it.

Don't really know your processor architecture? Try both... it's not very
clever, but it's harmless.

None of the two work? It is possible that you have an older processor
with the ARMv6 architecture. The solution for now is to install a
Nightly Build release. See below.

Still doesn't work? Really? Well, then you must have an exotic
processor... Contact us, on the
[http://forum.videolan.org/viewforum.php?f=35 Android forum] or directly
at
[`mailto:videolan.mobile@gmail.com <mailto:videolan.mobile@gmail.com>`__
videolan.mobile@gmail.com]. <br><br>

=== Be a Beta tester or try a Beta release === You want want to know the
future of VLC for Android? You want to help us and/or test if your issue
is already fixed for the next release ?

==== Be a Beta tester ====

Just follow this link
[https://play.google.com/apps/testing/org.videolan.vlc Be a Beta tester]

Soon, Beta release will automatically install on our device.

==== Try a Beta release ==== You don't want to be a Beta Tester but just
try a Beta ? Follow these steps :

# Go to Android Settings → Security → Device Administration → Enable
'Unknown Sources' # Go to our server, preferably from your device, :
http://get.videolan.org/testing/android/\ {{Android:latest beta
version}}/ # Choose your processor architecture (ARMv7, ARMv8, x86...)
<br /> Don't really know your processor architecture? Try both... it's
not very clever, but it's harmless # Download the chosen .apk on your
device # Click on the .apk you just download and install it.

<br><br>

=== Install a Nightly Build === You fear nothing and want our very last
works on VLC ? Or you have an ARMv6 Processor and want VLC? Follow these
steps:

# Go to Android Settings → Security → Device Administration → Enable
'Unknown Sources' # Go to our server, preferably from your device:
http://nightlies.videolan.org/ # Choose your processor architecture
(ARMv7, ARMv8, x86...) # Grab the latest .apk # Click on the .apk you
just download and install it.

You may experience some weird issues but generally, it works fine. If
not, please try an older nightly release, and contact us.

<br>

==Interface== At first start, VLC scans all your device to find all your
media files. This is the main interface after the scan :

{ style="vertical-align:top;width: 25%;"\| {\| \| Show Menu
[[File:caption_2.png%7C40x40px]] \|\| Video view
[[File:caption_3.png%7C40x40px]] \|\| Audio view
[[File:caption_4.png%7C40x40px]] \|\| Directory view
[[File:caption_5.png%7C40x40px]] \|\| History view
style="vertical-align:top;width: 25%;"\| {\| \|
[[File:caption_6.png%7C40x40px]] \|\| Video browser view
[[File:caption_7.png%7C40x40px]] \|\| Search a specific media
[[File:caption_8.png%7C40x40px]] \|\| Open network MRL
[[File:caption_9.png%7C40x40px]] \|\| Load last playlist
style="vertical-align:top;" More actions :<br> \* Sort by name or
length<br> \* Refresh your media library<br> \* Equalizer<br> \*
Preferences<br> \* About VLC<br> }

<br><br>

==Playing Video== ===Video browser view=== This view displays all your
videos present in your device, or in the directories you have specified
(see Preferences). To play one, just click on it, like the video
[[File:caption_1.png%7C30x30px]].

Note the difference with the video [[File:caption_2.png%7C30x30px]]
which is a group of videos : VLC automatically groups your videos with
the 4 same starting letters.

{ 550x550px]] {\| \| A Video [[File:caption_2.png%7C40x40px]] \|\| A
group of videos. }

<br><br>

=== Video playback interface ===

{ style="vertical-align:top;width: 25%;"\| {\| \| Video title
[[File:caption_2.png%7C40x40px]] \|\| Battery and time
[[File:caption_3.png%7C40x40px]] \|\| Play / Pause
[[File:caption_4.png%7C40x40px]] \|\| Aspect ratio
[[File:caption_5.png%7C40x40px]] \|\| Audio tracks
[[File:caption_6.png%7C40x40px]] \|\| Subtitles tracks
style="vertical-align:top;width: 25%;"\| {\| \|
[[File:caption_7.png%7C40x40px]] \|\| Video menu (for DVD iso)
[[File:caption_8.png%7C40x40px]] \|\| Lock screen
[[File:caption_9.png%7C40x40px]] \|\| Elapsed time
[[File:caption_10.png%7C40x40px]] \|\| Seek bar
[[File:caption_11.png%7C40x40px]] \|\| Total time / Remaining time
style="vertical-align:top;"\| [[File:caption_12.png%7C40x40px]] \|\|
Advanced Options \* Playback Speed \* Sleep timer \* Jump to specific
time \* Add subtitle }

Some precisions: \* You can change audio and/or subtitle track if there
are any. If not, these icons won't be displayed. \* The Video Menu icon
is only displayed for iso video (a DVD iso for example)

<br><br>

=== Video playback gesture ===

{ style="vertical-align:top;width: 25%;"\| {\| \| Adjust Brightness
[[File:caption_2.png%7C40x40px]] \|\| Adjust Volume
[[File:caption_3.png%7C40x40px]] \|\| Quick search }

<br><br>

== Playing Audio == TODO

-  You can change the time display to remaining time (e.g. -1:30 for
   1:30 minutes remaining) in the audio player by tapping on the current
   time label in the left.

== Settings ==

== See Also ==

[[AndroidFAQ]] <br /> [[Android Checklist]] <br /> [[Android Player
Intents]] <br /> [[Android Report bugs]] <br />

[[Category:Android|*]]
