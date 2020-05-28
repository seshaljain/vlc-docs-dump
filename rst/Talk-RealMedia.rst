== Can anyone explain further, please?! ==

"Currently, VLC can only play the audio on some .rm files." - Can anyone
elaborate on exactly which .rm files VLC will play? Can it handle .ram
files? Thanks! : Hello, : VLC supports .rm/.ram in 2 ways. If you use
Windows and have RealPlayer installed, VLC will try to use RealPlayer's
DLLs to play the file. Otherwise, it will use [[ffmpeg]] to decode these
files (which is included in vlc unless you compiled it yourself). From
source code comments and ffmpeg's website, vlc appears to support
"RealVideo 1.0 / 1.3 / 2.0", and "RealAudio 1.0". : As far as I can
tell, the way the system works is that a website publishes a .ram file,
which is actually a text file containing an internet address. RealPlayer
then opens this address, which is to the actual file, which is usually
accessed over an RTSP connection. If VLC can't play the file, it's
usually because it doesn't understand the latest RTSP commands. : &nbsp;
:If you can't open the .ram file, try editing it in notepad and
copy-and-pasting the link into VLC's open box. If you want to know
exactly what versions are supported, you should get a better answer at
the [[forum]], which more people keep an eye on. :
--[[User:H2g2bob|H2g2bob]] 19:03, 7 February 2006 (CET)
