<span style="color:red;font-size:20pt;">Discussion finished.</span><br
/>

<span style="color:red;font-size:20pt;">Discuss on the mailing-list now
about what is already implemented</span> :=)

== Read this first ==

The current preferences use a tree that matches the vlc internal
mechanisms. The new preferences don't have to use this tree. We can use
whatever we want. My first thought is a 1-level sorting, with the main
topics displayed with images on the left pane and preferences pages on
the right pane.

We can select preferences items one by one, we don't need the full pages
that are currently used

VLC definitively needs a "simple" preferences window. Here is a list of
some of the settings which would be needed:

== Now, proceed ==

(?) = to be decided

\* Audio \*\* Enable Audio \*\* Default audio volume \*\* Use S/PDIF
when available \*\* Force detection of Dolby surround **\*
Filters**\ \*\* Equalizer \*\*\ **\* Equalizer preset**\ \*\* Headphone
effect \*\ **\* Volume normalizer**\ \*\* Parmetric equalizer **\*
Output modules (?) -- Disagree. Only needs to be modified in case of
problems -- [[User:Zorglub]] --> It's still one of the options which
many people have to change, having it handy will be useful --
[[User:DJ]]. If we show it up, we should only include really useful
modules, like DirectX/Waveout only for aout under windows. Don't show
file and dummy for instance [[User:Zorglub]] . I agree with last remark
[[User:J-b|J-b]]**\ \* DirectX Audio output -- It'd be best to not have
any "module specific" option in these simple prefs. We could have an
"Output device" option ... which could be shared by each of the audio
output modules. -- [[User:Dionoea]]. Very hard to do. Much simpler is to
ask for all of them to show. Only those compiled in will show up. Very
easy. [[User:Zorglub]] \*\ **\* Output device**\ \* Visualizations

\* Video \*\* Enable video output \*\* Full screen video output \*\*
Skip Frames (?) -- Agree [[User:J-bJ-b]] **\* Video filters**\ \* Output
module -- Disagree. Only needs to be modified in case of problems --
[[User:Zorglub]] --> It's still one of the options which many people
have to change, having it handy will be usefull -- [[User:Dionoea]] I
agree with dionoea [[User:J-bJ-b]]

\* Input / Codecs \*\* Audio language \*\* Subtitle language \*\* DVD
device -- IMO, the devices should be detected and listed in the Open
dialog box. And if really needed, the options would still be in the full
preferences. They could also be remembered from one session to the other
-- [[User:ipkiss]] \*\* VCD device \*\* Audio CD device \*\* UDP port --
err ... what does that mean ? -- [[User:Dionoea]] Means nothing here
[[User:J-bJ-b]] 00:34, 19 February 2007 (CET)

\* Stream output (DEPRECATED) \*\* Keep stream output open -- That
shouldn't be in the prefs but in the stream configuration wizards and
dialogs -- [[User:Dionoea]] Is there basic cases where we don't want to
keep it open. I would be to changed the default to true in libvlc --
[[User:Xtophe|Xtophe]]. Has been changed.

\* Advanced -- We don't want to see a Advanced in Simple Prefs
[[User:J-bJ-b]] \*\* Enqueue items to playlist when in one instance mode

\* Playlist -- Do these options really need to be in the prefs ?
couldn't we just leave them in the playlist dialog/main controller and
remember the state when quiting ? -- [[User:Dionoea]]. These options are
indeed useless here. Just add change_autosave() on them [[User:Zorglub]]
Is it already done ? [[User:J-bfeepk]] \*\* Play files randomly forever
\*\* Repeat all \*\* Repeat current item \*\* Play and stop

\* Interface \*\* Language \*\* Show advanced options (DEPRECATED) --
This is "Complex preferences" specific so it shouldn't be in the "simple
prefs" -- [[User:Dionoea]]

\*\* ffmpeg-hq ? -- Is this out of place? I can't find it in this
context -- [[User:DJ]]. It's currently not in video, but codecs, but we
are free to put whatever we want wherever. [[User:Zorglub]]. Isn't that
going to get kinda confusing? [[User:DJ]]. Nope :) [[User:Zorglub]]

\* Subtitles \*\* default encoding \*\* size \*\* color \*\* font

-  HTTP proxy

\* HotKeys !!!
   [[Category:Dev Discussions]]
