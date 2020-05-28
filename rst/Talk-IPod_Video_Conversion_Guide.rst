== Choice between H.264 and MPG4v unclear ==

The choice between H.264 and MPG4v should be made clearer. The
difference should be explained and used consistently. Different sections
switch between them, probably just historical, but it's confusing to the
first time reader. Most people just want to know "what's best", which
isn't obvious, so we should say that, use one consistently and describe
how to use the other one.

== Other ==

I am having troubles with the conversion. I have an ipod nano 4th gen
but when i finished the rip, i draged it into my ipod but when i turned
my ipod on, it wasnt there. Can some one help me?

: The wiki is not the right place for such question. Please open a topic
on the [http://forum.videolan.org forum]. --[[User:Thannoy|Thannoy]]
08:05, 25 June 2009 (UTC)

== script ==

In Windows-Script I had to replace '''url'''=%outfile% with
'''dst'''=%outfile% and maybe vlc:quit with vlc://quit I was using VLC
1.0.2

== GUI instructions don't work on Mac OS X (VLC 1.1.x) ==

"Stream output MRL Target:" is not available in the GUI on Mac OS X.
Additionally, the command-line variant does not work because, at least
for the binary at "VLC.app/Contents/MacOS/vlc", it attempts to stick the
current working directory on the front of the :sout parameter, then
falls over when that's not a real filename.
