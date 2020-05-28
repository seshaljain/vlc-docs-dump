== DVD Movies don't work or crash == If you open '''DVD''' with DVD
selection, try with '''No DVD menus''' option (aka '''dvdsimple''').

Some new DVD movies use copy protection mechanisms that VLC doesn't
support.It might help if you rip that movie to hard drive using tools
like '''DVDFab Decrypter''' or '''AnyDVD''' and use VLC to playback
these files from hard drive.

You may also be able to play these copy protected DVDs by opening the
movie initialization file directly. Use the '''Open File''' function in
VLC and navigate to the '''VIDEO_TS''' directory on the DVD, then open
the '''VIDEO_TS.IFO''' file. Some of the newest copy protection schemes
have been found to use tricks that confuse many of the current DVD
software programs so they cannot locate this file properly to initiate
playback on their own. This method has been found to work with some of
the newest DVDs that won't open properly in VLC 1.1.11 using the
standard approaches.

<br>

{{VSG}}
