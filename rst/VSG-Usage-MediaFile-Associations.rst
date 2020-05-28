Messed-up file associations
---------------------------

Associating media files should be done through the VLC settings interface. Choose "Tools \| Preferences " and then click on the "Set up Associations..." button. Select any file extension that you wish to open with VLC, then click "Apply". This should change all media files icons to the VLC cone, and double-clicking any of them should open VLC and immediately start playing the media.

| 
| If this seems to have no effect on the UI, and/or double-clicking the file icon does not start VLC, check that you have correctly set Windows preferences through "Start \| Default Programs" (on Vista; see the relevant item on Windows XP or newer Windows OS; possibly this is not applicable to Windows 2000). In that UI click on "Set default programs", select the "VLC media player" item and check the description (it will usually say "All default settings for this program are active"). Then choose your own course of actions by either clicking on "Set this program as default" or "Choose default settings for this program".

| 
| Other ways to achieve the same effects are as follows (not really recommended).

-  **Use Windows Explorer's context menu**

| In Windows Explorer, right-click a file you wish to open.
| Click "Open With" in the context menu that pops up.
| Click "VLC media player" to use VLC just this once, or click "Default program..."
| Click the name of the program (VLC) which you want to be used to open the file.
| If VLC is not displayed, click Browse to locate it on your hard drive.

**Alternatively:**

| In Windows Explorer, right-click the file you want to open with VLC.
| Click Properties in the context menu that pops up.
| On the General tab, click Change.
| Click the name of the program (VLC) which you want to be used to open the file.

| Either of these options affects all files that have the same filename extension (the letters after the filename's period) as the file you selected. For example, if you change the program that opens goober.avi, then all .avi files will be opened with VLC.

-  **Rerun the installer**

Reinstall VLC and choose the "associate files" option when it comes up. Please note that on Vista and newer OSes this will not cure the "Windows Media Player won't go away" symptom, and you should go the "Set default program" route instead, as described above.

| 

-  **Edit the registry**

**Warning:** this instruction set is outdated and should not be used. Direct registry editing should be avoided anyway unless you're desperate and you really really know what you're doing.

**Warning:** use this technique only if you really know what you are doing! And be sure to back-up your registry first.

#. Open a text editor, like Notepad (but not WordPad).
#. Copy this text below.
#. Modify the strings C:\\Program Files\\VideoLAN\\VLC\\vlc.exe to match your VLC installation.
#. Save as vlc.reg.
#. Execute vlc.reg (adding this data to your registry).
#. Enjoy VLC :)

| 
| Text to copy:

::

   Windows Registry Editor Version 5.00

   [HKEY_CLASSES_ROOT\.ASF]
   @="VlcFile"

   [HKEY_CLASSES_ROOT\.ASX]
   @="VlcFile"

   [HKEY_CLASSES_ROOT\.AVI]
   @="VlcFile"

   [HKEY_CLASSES_ROOT\.DIVX]
   @="VlcFile"

   [HKEY_CLASSES_ROOT\.MPEG]
   @="VlcFile"

   [HKEY_CLASSES_ROOT\.MPG]
   @="VlcFile"

   [HKEY_CLASSES_ROOT\.VOB]
   @="VlcFile"

   [HKEY_CLASSES_ROOT\.WMV]
   @="VlcFile"

   [HKEY_CLASSES_ROOT\VlcFile]
   @="VLC File"

   [HKEY_CLASSES_ROOT\VlcFile\DefaultIcon]
   @="C:\\Program Files\\VideoLAN\\VLC\\vlc.exe,0"

   [HKEY_CLASSES_ROOT\VlcFile\shell\Open]
   [HKEY_CLASSES_ROOT\VlcFile\shell\Open\command]
   @="C:\\Program Files\\VideoLAN\\VLC\\vlc.exe \"%L\""

| **Note:** This associates asf, asx, avi, divx, mpeg, mpg, vob and wmv files. If you get the idea, you can associate any file you want.
| 
