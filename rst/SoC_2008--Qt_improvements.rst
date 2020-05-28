{{SoCProjectstudent=[[User:Lukas.durfinamentor=[[User:J-b|Jean-Baptiste
Kempf]]}}

== GSoC - QT improvements ==

Goals of my project:
   Fullscreen controller (FSC) for Linux and Windows make VLC interface
   for Phonon to provide it as backend <s>playlist enhancements</s> =>
   phonon improvements

== Repositories ==

web browsing: http://git.videolan.org/?p=vlc-lukas.git;a=summary

getting code: git clone git://git.videolan.org/vlc-lukas.git

Phonon: http://code.google.com/p/phonon-vlc-mplayer/

feel free to clone, compile, test and make feedback

== Finished (or partially finished) parts ==

Fullscreen controller

Phonon related: \* enable setting brightness, contrast... \* dvd
handling, setting chapters, audio, video tracks, channels, subtitles \*
video, audio filters \* audio devices

== Work timetable == 26th May - start of coding

9th June - FSC should be mostly done, start Phonon part of project

9th - 12th June - one or two free days caused by bachelor exams

9th - 12th Jule - trip, with notebook, without internet connection

3th August - VLC Phonon backend should be greatly working

4th August - <s>start coding around playlist</s>

This part was dropped and phonon development continues, because phonon
is in development and always provides new functions

5th September - end of the SoC project

== Status of work == 26th May prototype of fullscreen controller is
working on linux, but on windows there is issue with hidding of FS
controller I requested Tanguy Krotoff for svn account in VLC(-mplayer)
Phonon backend repository

28th May
   I have account in VLC(-mplayer) Phonon backend repository FSC works
   in unintergrated and integrated video

29th May
   hidding on windows is working, it is done by trick, but searching for
   resolving problem with hide() continue

2nd June
   remove equalizer button from FSC it seems nobody knows why hide()
   doesnt work for windows, so it is solved by setting opacity and
   resending key press events to libvlc

3rd June
   press events resending enabled for linux, works fine, now it is
   usable. I was trying several tests wtih transparency it seems to be
   serious problem on windows, it is blinking a lot. On linux you need
   composite manager to make it working, I dont have it and my attempts
   to make it working failed on first step with installing proprietary
   ATI driver, which doesnt want to work with actaul X.Org My work is a
   bit slowed-down, because I have to prepare for my exams on 10th June.

4th June
   add debuging mode for testing transparency on windows add teletext
   buttons slow hidding enabled on non windows platforms, but working
   only with composite manager and also turn on when transparency debug
   is enabled

5th June
   learning for exams, created first prototype of patch for master
   branch

6th June
   redesign, some tests and learning

9th June
   travelling to unniversity, learning

10th June
   exams passed, I am bachelor now I am going to install qt4.4 some way
   for fedora, it seems it wouldnt be easy and then try Phonon btw fs
   controller was merged with master branch and it is available in night
   builds

11th June
   some testing and fixing fs controller start studying and
   experimenting with phonon

12th June
   travelling home from university continueing study of phonon and
   related things

16th June
   start working on adding functions to libvlc interface for setting
   brightness, contrast, gamma, hue and saturation

17th June
   point mentioned above wouldnt be so easy as I thought

19th June
   these functions are done, and works correctly with phonon backend
   design of whole filter architecture in libvlc was done and going to
   be implemented

20th June
   implementing of filter architecture, start investigation about next
   point for phonon backend: DVD handling, as Tanguy said, it could be
   more complexed than filters :(

23th June
   fixing qt4 problems

24th June
   start work around DVD handling in libvlc

25th June
   fixing fullscreen controller

26th June
   studying architecture of playlist and Qt model/view

30th June
   added functions for controlling video tracks, audio device

1st July
   functions getting description about video, audio tracks and subtitles
   (libvlc) fixing fs controller => change style of initialization, now
   it doesnt use ugly hack. It is done by seeting variable on
   p_input_thread to signal new vout

3rd July
   new branch in phonon repo for phonon-vlc, add support for functions
   provided by adjust video filter

4th July
   first dvd related functions in phonon-vlc (subtitles, audio channel)

7th July
   continue searching solution for fs controller, add some new DVD
   features to phonon-vlc

9th July
   going on holiday

12th July
   comeback

15th July
   DVD handling in phonon-vlc is mostly done, I add naming of titles and
   chapters, fix changing chapters when title is change, fix refreshing
   audio channels and sutitles when titles changed

16th July
   add persistence of applied video filters, so when it is set and new
   vout is created, the previous applied filters are restored to new
   vout - needed for phonon. Now I feel and can tell, that phonon-vlc is
   much more better working.

17th July
   testing and fixing my new code on win32 platform studying next phonon
   parts and going deeper in code and its contextes

18th July
   start adding support for audio and video filters I hope it will work
   as I want, that user would be able to use same audio and video
   filters with phonon-vlc as he cas use with VLC

22th July
   first audio filter (equalizer options) is working now I have to
   research other audio and video filter and design some clever
   architecture in phonon for them

23th July
   I am travelling to university to get documents

24th July
   preparetion for moving to git repo, clearing from mplayer code
   editing for qt phonon version

28, 29th July
   some fixing and testing FS controller, various small phonon tests
   finding differences between qt and KDE phonon

30th July
   fixed advanced buttons and related stuff in FS controller adding
   setting aspect ratio in phonon-vlc

31th July
   I am going to try integrate phonon-vlc with trunk phonon in KDE repo,
   then it will be possible to move it to KDE repo o/

4th August
   free day, I gave my blood

5th August
   some fixes around effects in phonon start work to provide various
   audio devices and effect parameters by phonon

7th August
   phonon can set audio device for playing, I have to finish better
   handling of alsa devices

8th August
   audio devices handling is done
