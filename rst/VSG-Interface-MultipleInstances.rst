Play multiple instances of VLC
------------------------------

In version .8.5 it was easy to have multiple instances of VLC playing each with its unique stream of data.

In version .8.6x playing multiple VLC instances and different streams in each is as easy as clicking **Settings** -> **Preferences** (note this does not exist on the Mac version):

| The go to **Advanced** (tick Advanced options to see all the options available)
| The untick **Allow only one running instance.**
| This allows users to use more than one VLC player at a time. Press '''Save '''and restart VLC. Once you've done the above you should be able to play as many VLC instances and video or audio files as you like.

In version 0.9.6 (on Windows, this may not apply to other OS's):

| You must also go to **Tools** -> **Preferences** -> (set "**Show settings**" to "**All**") -> **Advanced**, and uncheck "**One instance when started from file**".

Mac OS X
~~~~~~~~

On the Mac, running multiple instances of VLC is not supported out of the box.

| As a workaround, you can create a Droplet that behaves as expected. Paste the code below into a new AppleScript Editor script and save it as an application. Launch the app to get a separate instance of VLC, or drop one or more files onto it.

::

   on run
       do shell script "open -n /Applications/VLC.app"
   end run
   on open theFiles
       repeat with theFile in theFiles
           do shell script "open -na /Applications/VLC.app " &amp; quote &amp; (POSIX path of theFile) &amp; quote
       end repeat
   end open

| 
| 
