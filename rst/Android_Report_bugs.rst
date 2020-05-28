{{See alsoreport Android bugs}}

[[File:VLC Android Crash.pngright|VLC for Android has crashed]]

=Are you sure it's a ''true'' bug?= Well, you know the old adage:
''"Have you tried turning it off and on again?"''

Don't be mistaken - we believe you but sometimes, it is truly not our
fault... So before becoming grumpy, try these steps: \* Restart your
Android device, then relaunch VLC. \* Still getting the bug? Try to
uninstall and re-install VLC.

The bug is definitely still there? Now you can keep reading this page...

=What you have to do= If you want to help us solve an issue you
experience on VLC for Android, we need to know a few things: \* your
exact device name (go to '''Settings > About Phone > Model Number''') \*
your Android version (go to '''Settings > About Phone > Android
Version''') \* your VLC version (go to '''VLC > Options > About''') \* a
log file (see below) \* whether the issue occurs only on one media
(video or music) or all of them \* location to a sample, a screenshot,
etc...

If you were asked to do this by a developer from
[https://forum.videolan.org/ the VideoLAN forum], then please respond
with this information in the same thread.

If not, send us this information at
'''[`mailto:videolan.android@gmail.com <mailto:videolan.android@gmail.com>`__
videolan.android@gmail.com]'''.

However, if you are competent enough, feel free to create a report on
the [https://trac.videolan.org/vlc/ VLC bug tracker]. Please note that
any tickets which do not follow the standards for bug reporting ''will
be closed'' systematically.

=How to find the log file?= ==If VLC for Android crashes== Normally,
when VLC for Android crashes it will leave behind a
'''`vlc_logcat <>`__'''''<date and some numbers>'''''.log''' file in
your '''SD card's root'''.

You can then retrieve this to your computer using the file transfer
mechanism offered by your device (e.g. Mass storage, etc). Or, you can
use [http://www.openintents.org/en/filemanager OI File Manager] (open
source file browser) to view and manipulate the file (e.g. move it to a
folder where it's uploadable to PC).

Then, send us this ''`vlc_logcat <>`__\ <...>.log'' file.

If you do not find any log in the form of
''`vlc_logcat <>`__\ <...>.log'', then you probably have a native crash.
See below for details on native crashes.
[[File:VLC_Android_Logcat_File.png%7Cthumb%7Ccenter%7C200px%7CLog files
in your SD card's root]]

==Playback issues where VLC does not crash== If VLC does not crash, you
have to manually create a log file.

# Ensure VLC is completely closed by force-stopping it in Android
settings. # Start VLC. # Go to '''Settings → Advanced''' '''→ Debug
logs''' (at the very bottom), and tap '''Start logging'''. # Go back and
play the media file in question and/or try to reproduce the issue. #
Once you are done playing the file, go back to the '''Debug logs'''
screen. You can find the log in this screen. To retrieve it, copy it to
the Android clipboard and paste it on a mail for example. # Or dump this
log by pressing '''Dump Logcat Log''' and send the generated file by
mail. # You can also paste it on any [http://pastebin.com/ pastebin]
site or however you wish and send us the link. # Press '''Stop
logging''' to end the debugging session and return to normal usage.

And that's it.

==User interface issues== Go to '''Preferences''' → '''Advanced
debugging''' → '''dump logcat''' and upload the provided file.

==Advanced users or developers== However, in some cases (such as on
certain Huawei phones who use a non-standard implementation of Logcat)
you will need access to a computer and enable adb debugging. To do this,
first ADB debugging must be enabled - '''Settings → Developer options →
USB debugging''', or on older phones, '''Settings → Applications →
Development → USB debugging'''. In both cases, ensure that the option is
checked.

An easier approach might be to install
[https://github.com/jackpal/Android-Terminal-Emulator/wiki Terminal
(a.k.a. Term.apk)] if you haven't already. Open Terminal and clear the
logcat buffer with <code>logcat -c</code>. Then, re-open VLC and try to
make it crash. Once it crashes, then re-open Terminal and type in
letter-for-letter, case sensitive: <code>cd /sdcard && logcat -d >
log.txt</code> into the terminal, and hit Enter. Pull the file "log.txt"
under the SD card to your PC and pastebin.

The normal developers' approach is to
[http://developer.android.com/sdk/installing/index.html install the
Android SDK] and run <code>adb logcat -d > log.txt</code>, then pastebin
the log.txt.

==Native crashes (advanced stuff)== Sometimes, you might asked by one of
the developers for a '''backtrace''', or '''native trace'''. If so, then
please see [[AndroidCompile#Native debugging]].

[[Category:Android]] [[Category:Security]]
