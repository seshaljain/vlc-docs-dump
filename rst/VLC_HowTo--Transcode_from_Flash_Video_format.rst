.. raw:: mediawiki

   {{see also|VLC HowTo/Transcode from Windows Media format}}

.. raw:: mediawiki

   {{howto|Fix broken .flv files}}

.. raw:: mediawiki

   {{historical}}

You can use `ffmpeg <ffmpeg>`__ to change `.flv <.flv>`__ files to `.avi <.avi>`__ files (or one of many other types of files).

If you have problems playing .flv files, changing them to .avi will probably fix the problem.

Windows
-------

VideoLan **cannot** write .avi, as you can read in the forum this funcionality is not yet fixed.

Install
~~~~~~~

Precompiled windows binaries are avaliable at:

-  http://arrozcru.no-ip.org/ffmpeg_builds/

Pick the file **ffmpeg-SVN-r6708-static-gpl-win32.zip** (about 5MB)

Extract the files from the .zip and copy ffmpeg.exe to your Windows directory (Windows folder), or somewhere else in your search path.

Ubuntu users
^^^^^^^^^^^^

Ubuntu users can type "sudo apt-get install ffmpeg" in terminal to install ffmpeg from repository.

Run
~~~

Ffmpeg.exe is command-line based, so to use it you need to open a `command prompt <wikipedia:cmd.exe>`__. In the start menu pick "Run", and type

``cmd.exe``

into the box and press enter. This opens a cool black box with white text. It'll say something like C:\>.

At the prompt, type

``cd "``\ *``somewhere``*\ ``"``

where "*somewhere*" is the path to the folder where you saved your files, it's probably something like

``cd "c:\windows\profiles\user\Desktop\"``

Then press enter. You can find out the path (location) of a file by right clicking on the file and selecting properties.

Finally type

``ffmpeg -i "``\ *``your_file``*\ ``.flv" "``\ *``your_file``*\ ``.avi"``

and press enter. This takes "*your_file*.flv" as the input file and spits out "*your_file*.avi" as an avi file. Job done (at last!)

Close the command prompt by closing the window as normal, or typing "exit".

Automating Conversion with VBScript
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you prefer to convert a file using the right-click menu, you can try this VBScript: `ConvertAndPlayInVLC_vbs.txt <http://jeffersonscher.com/res/ConvertAndPlayInVLC_vbs.txt>`__. The following assumes that you have downloaded and unpacked the ffmpeg zip archive.

To Install the Script
^^^^^^^^^^^^^^^^^^^^^

#. Download the script to the same folder where you have ffmpeg.exe (any folder, not necessarily in the search path)
#. Using Windows Explorer or My Computer, rename the file from the .txt extension back to .vbs (if you cannot see the extension, use Tools > Folder Options..., View to stop hiding file extensions)
#. Right-click the file and choose Create Shortcut
#. Copy/Paste or Drag the shortcut to your SendTo folder (c:\Documents and Settings\\\ *Username*\\SendTo); you can rename it to something shorter if you like

To Use the Script
^^^^^^^^^^^^^^^^^

Right-click your .flv file, choose the Send To "fly-out" menu, and then your shortcut. The script will run ffmpeg.exe in a command window and then play the newly created avi file in VLC.
