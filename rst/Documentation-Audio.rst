{{RightMenu|Documentation TOC}} VLC can play several audio formats:
''.asf, .avi, .divx, .dv, .mxf, .ogg, .gm, .ps, .ts, .vob,'' and
''.wmv''. It can convert audio tracks and use several visualizations.

'''Note:''' The commands in the '''Audio''' menu are only enabled when
an audio file is being played.

== Playing an audio track ==

To play a track:

#Select ''Open File'' in the ''Media'' menu. #Select an audio file and
click on the [[Image:VLC - play button.png]] ''Play'' button. The
selected track is played.

== Enabling and disabling audio tracks ==

*To disable a track, select the ''Disable'' option in the ''Audio
Track'' from the ''Audio'' menu. The selected track will then stop.*\ To
enable the track again, select the designated ''Track'' option in the
''Audio Track'' from the ''Audio'' menu. The selected track will then
play.

== Recording Audio ==

To record audio you need the record button ([[Image:VLC - record
button.png]]) to be visible. The record button is hidden by default. You
can display using one of these methods: *Select Advanced Controls in the
View menu. The Advanced toolbar is displayed on top of the standard
toolbar. The Advanced toolbar contains the Record button.*\ Select
Customize interface in the Tools menu and add the record button to the
Line 2 of buttons (which is the line shown by default).

Once the Record button is visible, click it to start recording.

The recording from a shoutcast stream is stored somewhere in your files
under a name like <tt>vlc-record-Date-Time-Channel-Track.mp3</tt> (e.g.:
<tt>"vlc-record-2011-09-22-10h19m48s-Radio CAFF-Silencio - Arrabal
Salvaje.mp3"</tt>, when recording from [http://radiocaff.com.ar/ Radio
CAFF] (or more precisely from the underlying
[http://panel7.serverhostingcenter.com/tunein.php/radiocaff/playlist.pls
WinAmp stream]). Under my german Windows XP it was stored under "Eigene
Dateien/Eigene Music" so I guess that you find it in an english Windows
under "My Documents/My Music/", I don't know where it will be stored
under Linux or any other OS (updates are welcome).

You can automagically cut the stream into tracks by relaying the stream
through [http://streamripper.sourceforge.net Streamripper], i.e. by
directing StreamRipper to the ShoutCast stream and directing VLC to the
relaying port of StreamRipper <nowiki>(default
http://localhost:8000)</nowiki>.

== Audio Device ==

This option helps you to listen to audio files in two modes: stereo and
mono.

#To listen to an audio track in either the Stereo or Mono mode, select
''Open File or Open Disc'' from the ''Media'' menu. The Open dialog box
is displayed. #Select an audio file and click on the [[Image:VLC - play
button.png]] ''Play'' button. The selected track is played. #Select
''Mono'' in ''Audio Device'' from the ''Audio'' menu if you want to
listen to the audio track in the Mono mode. Mono refers to monaural
sound that uses a single channel for sound reproduction.

#Select ''Stereo'' in ''Audio Device'' from the ''Audio'' menu if you
want to listen to the audio track in the Stereo mode. Stereo refers to
sound that uses two channels for sound reproduction or stereophonic
sound.

[[File:Basic_audio_stereomono.png]]

== Audio Channels ==

In audio, a channel refers to a stream of audio that is to be played by
one speaker. For example, stereo audio, consists of two channels. This
option is useful for codecs that don’t have support for more than 2
channels.

Select a channel type in ''Audio Channels'' from the ''Audio'' menu. VLC
media player provides four audio channels and they are:

#''Stereo'' – Refers to the reproduction of the sound in two or more
independent audio channels using more than one speaker. If you use this
option, you would feel as though the sound is played from all the
directions. You can observe this in a regular home theatre with 5.1 or
6.1 speakers. #''Left'' – You can observe this in a regular audio player
with 2.1 speakers. If you select the '''Left''' option, the music is
played only in the left speaker. The speaker on your right is
automatically switched OFF. #''Right'' - If you select the '''Right'''
option, the music is played only in the speaker on your right side. The
speaker on your left is automatically switched OFF. #''Reverse Stereo''
– There are several applications that are used to reverse the stereo
whereas VLC has an in-built feature to reverse the stereo. This option
is useful if you want the audio to play in tandem with the video. You
can use the '''Reverse Stereo''' option if you want to deliberately
change the audio output.

Imagine that you are watching a video. In the video, a person walks on
the left side but the sound is produced on the right speaker. You can
correct this by selecting the ''Reverse Stereo'' option in VLC. Select
the ''Reverse Stereo'' option and play the same scene in the video and
observe the difference.

You can observe this with 2.1, 5.1, 6.1 and 8.1 speakers.

== Visualize Audio ==

Visualizations display splashes of colour and geometric shapes and
generate animated imagery based on a piece of music.

The different visual effects available are ''Spectrometer, Scope,
Spectrum, VU Meter and Goom''. This menu item can also be used to
disable a visualization.

#Select an option under the ''Visualizations'' option from the ''Audio''
menu to view the effects. The selected visualization is then played. #To
disable visualizations, select ''Disable'' under ''Visualizations'' from
the ''Audio'' menu. The visualization is then disabled.

Spectrum visualization on VLC: [[File:Spectrum
visualization.pngcenter|400px]]

== Maximum VLC Volume == To change the maximum volume in % that VLC
should use, go to '''Tools''' → '''Preferences''' (select '''All''' at
bottom left corner) → '''Interface''' → '''Main interfaces''' → '''Qt'''
→ '''Maximum volume displayed'''.

Save it and restart VLC.

[[File:Set_Maximum_Volume.png%7Cthumb%7Ccenter%7C500px]]

{{Documentation}}
