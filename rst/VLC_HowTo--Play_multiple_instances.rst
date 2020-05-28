.. raw:: mediawiki

   {{Howto|play multiple instances of VLC media player}}

In version 0.8.5 it was easy to have multiple instances of VLC playing each with its unique stream of data.

Graphical
---------

Windows
~~~~~~~

In versions 2.1.x and 3.x.x playing multiple VLC instances and different streams in each is as easy as *clicking* **Tools → Preferences...** (or just *press* **Ctrl+P**): `framed|after unticking the two checkboxes it should look like this,then click on save <File:Play2instances.jpeg>`__

-  in the **Interface** tab *scroll down* to **playlist and instances**
-  *untick checkbox* **Allow only one instance**
-  *untick checkbox* **use only one instance when started from file manager**
-  *Press* **Save**.

      This allows users to use more than one VLC player at a time. Once you've done the above you should be able to play as many VLC instances and video or audio files as you like.

macOS
~~~~~

On the Mac, running multiple instances of VLC is not supported out of the box.

As a workaround, you can create a Droplet/App that does the following:

-  launch the VLC droplet/app to get a separate instance of VLC,
-  drop one or more files onto VLC droplet/app, or
-  associate your .mov, .avi, and other files directly with the VLC droplet/app, allowing you to simply click on the files to launch the files in a new standalone VLC session.

Paste the code below into a new AppleScript Editor script and save it as an application.

.. code:: applescript

   on run
       do shell script "open -n /Applications/VLC.app"
       tell application "VLC" to activate
   end run

   on open theFiles
       repeat with theFile in theFiles
           do shell script "open -na /Applications/VLC.app " & quote & (POSIX path of theFile) & quote
       end repeat
       tell application "VLC" to activate
   end open

File Association with the Droplet/App can be done as follows:

#. *Open* **Finder** and find the video file of interest
#. *Right click* on the file (assumes you have right click enabled)
#. Choose **Get Info**
#. Under **Open with:**, click **dropdown** and select the VLC droplet/app
#. *Click* **Change All** button
#. If prompted "are you sure", *select* "Yes".

Command-line
------------

Use the option ``--no-one-instance``.

On \*nix systems you can create background jobs:

\ `` vlc --no-one-instance file1.ogg & vlc --no-one-instance file2.ogg``

On Windows systems you might use `START <https://ss64.com/nt/start.html>`__:

\ `` START "VLC media player - Instance 1" ``\ \ `` "--no-one-instance file1.ogg" && START "VLC media player - Instance 2" ``\ \ `` "--no-one-instance file2.ogg"``

`Category:How To <Category:How_To>`__
