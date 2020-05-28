My vlc player doesnt have audio only video ...any suggestions how to
solve the issue? --

You should give us some more information such as <br> \* which plateform
do you use (Windows, Linux, MacOS) \* which VLC are you using (from SVN
or a pre-compiled release..)

If you use Linux and you compile your own VLC from the sources, maybe
you forgot to install the package ''libasound2-dev'' or something like
that. If you install it, retry "make clean", "./configure ....." and
"make". I suggest you to store what ''./configure'' says. It can help
you to find missing libraries.. to do that, you can append "|tee
/tmp/configure.out.txt" to you ''./configure'' command.

You will find a list of package that can help you to find which one is
missing on your system in the [[Contrib_Status]] page. You can have a
more dynamic help on the IRC chat (server irc.videolan.org, channel
[irc://irc.videolan.org#videolan #videolan]).

--[[User:Thannoy|Thannoy]] 20:43, 27 February 2008 (CET)
