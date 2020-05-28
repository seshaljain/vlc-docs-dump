Description
-----------

Windows service (called ntservice) is feature in VLC, which allows to run VLC as Windows service.

Usage help
----------

copied from `here <http://forum.videolan.org/viewtopic.php?f=14&t=54028#p177582>`__

This config can be usefull to broadcast remote stations, recording internet radio propuse, etc.

I am sending you the final configuration for future reference:

1. To install the services, go to de command prompt Start->Run->cmd

2. Then go to the VLC install directory. (for example *cd c:\software\vlc*)

3. Install the Autoplay Stream Service, with an http Administrative remote console on ports 1080 and 1081.

3.1. Autoplay for radio station #1 (Clasical), output device directX audio #1: **vlc -I ntservice --ntservice-install --ntservice-name=VLC-CLASICAL --ntservice-extraintf=http --ntservice-options="--http-host=0.0.0.0:1080 --volume=250 --directx-audio-device=1 --directx-audio-float32 --force-dolby-surround=2**\ http://dir.xiph.org/listen/1391606/listen.m3u\ **"**

3.2. Autoplay for radio station #2 (Jazz), output device directX audio #2: '''vlc -I ntservice --ntservice-install --ntservice-name=VLC-JAZZ --ntservice-extraintf=http --ntservice-options="--http-host=0.0.0.0:1081 --volume=250 --directx-audio-device=2 --directx-audio-float32 --force-dolby-surround=2 http://dir.xiph.org/listen/1003756/listen.m3u" '''

4. Optional, add Service Description.

Troubleshooting
---------------

VLC Windows Service Hangs
~~~~~~~~~~~~~~~~~~~~~~~~~

From this `post <http://forum.videolan.org/viewtopic.php?f=14&t=50434#p211639>`__ in the forums.

VLC as windows service (starting with 0.9.x and also with 1.x) sometimes hangs because it is actually trying to display the following dialog boxes:

#. "Privacy and Network Policy" dialog box (occurs the first time you run VLC, or if launched with the --reset-config option).
#. "Crash reporting" dialog (occurs the next time VLC is launched after a crash)

Using the following two options as part of the service installation command solves the issue:

-  --no-qt-privacy-ask
-  --no-qt-error-dialogs

for example: **c:\Program Files\VideoLAN\VLC\vlc.exe -I ntservice --ntservice-install --ntservice-name=VLC-Service --ntservice-extraintf=rc --ntservice-options="--no-qt-privacy-ask --no-qt-error-dialogs ..." vlc://quit**

`Category:Windows <Category:Windows>`__
