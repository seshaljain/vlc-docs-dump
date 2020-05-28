.. raw:: mediawiki

   {{Example code}}

.. raw:: mediawiki

   {{howto|Switch off your computer automatically, when VLC has finished playing a file}}

General idea
------------

It is not a feature included in but small scripts can do it for you upon quitting VLC.

Quitting VLC
------------

.. raw:: mediawiki

   {{VLC}}

can exit once all items have finished playing, this can done by enabling **Play and exit** in the Playlist section under `Preferences <Preferences>`__

.. figure:: Play_and_exit.gif
   :alt: Play_and_exit.gif

   Play_and_exit.gif

Alternatively, you can quit after playback is finished, by adding the following to the end of the playlist:

::

   vlc://quit

Shutdown
--------

Windows
~~~~~~~

Bat File
^^^^^^^^

1.) Create a new file with extension .BAT [use notepad] and paste in the contents from below. For use multi select file, juste made and forget your list... :) enjoy :

.. code:: winbatch

   START /WAIT C:\"Program Files"\VideoLAN\VLC\vlc.exe %* vlc://quit
   shutdown -s -t 60

2.) Use VLC to create/save playlist with desired content.

3.) Drag saved playlist icon on top of .bat file

The batch file will launch VLC and load the playlist. It will wait for the playlist to finish playing VLC will quit Batch will continue processing and system will be shutdown in 60 sec.'s.

VBScript
^^^^^^^^

Make a .vbs file, copy in the code below and save. Drag and drop files onto the script file or double click the script to start it up. Supports avi, mp4, mov, wmv and 3gp files.

Note: Change line 6 to TRUE to force quit all other applications.

.. figure:: VLC_Auto_Shutdown.PNG
   :alt: VLC_Auto_Shutdown.PNG

   VLC_Auto_Shutdown.PNG

.. code:: vb
   :number-lines:

   'By eyehawk78, posted on http://forum.videolan.org/viewtopic.php?f=16&t=70391

   Dim oShell, FSO, FileData, vlc_path, video_dir, user, programs
   Dim files, seconds

   force_shutdown = FALSE 'Set to true to force quit all other applications set to false otherwise

   Function SelectFile()
      Set file = CreateObject("UserAccounts.CommonDialog")
      file.Filter = "Video Files (avi, mp4, mov, wmv, 3gp)|*.avi;*.mp4;*.mov;*.wmv;*.3gp;"
      file.FilterIndex = 1
      file.InitialDir = video_dir
      InitFSO = file.ShowOpen
      
      If InitFSO = True Then   
         SelectFile = file.FileName
      Else
         WScript.Quit
      End If
   End Function

   Sub InputError(ErrorString)
      Wscript.Echo ErrorString
      Wscript.Quit
   End Sub

   files = ""

   Set FSO = CreateObject("Scripting.FileSystemObject")
   Set oShell = CreateObject("WScript.Shell")

   If Wscript.Arguments.Count > 0 Then
      For Each FileData In Wscript.Arguments   
         Set FileInfo = FSO.GetFile(FileData)
         If InStr(FileInfo.Type, ".avi") or InStr(FileInfo.Type, ".mp4") or InStr(FileInfo.Type, ".mov") or InStr(FileInfo.Type, ".wmv") or InStr(FileInfo.Type, ".3gp") Then
            files = files & " " & CHR(34) & FileData & CHR(34)
         Else
            InputError("File " & CHR(34) & FileInfo.Name & CHR(34) & " has an unrecognised file type - Must be of type .avi, .mp4, .mov, .wmv or .3gp")
         End If
      Next
   Else
      user = oShell.ExpandEnvironmentStrings("%USERPROFILE%")
      video_dir = oShell.ExpandEnvironmentStrings("%VLC_SHUTDOWN_VIDEOS_DIRECTORY%")

      'If this if first run, we must save where the default video directory is

      If video_dir = "%VLC_SHUTDOWN_VIDEOS_DIRECTORY%" Then
         video_dir = InputBox("Please input the directory where your Videos are kept." & vbcrlf & vbNewLine & "E.g. C:\Documents and Settings\User Name\My Documents\My Videos", "First Run", user)
         If video_dir <> "" Then
            strComputer = "."
            Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\cimv2")

            Set objVariable = objWMIService.Get("Win32_Environment").SpawnInstance_

            objVariable.Name = "VLC_SHUTDOWN_VIDEOS_DIRECTORY"
            objVariable.UserName = "<System>"
            objVariable.VariableValue = video_dir
            objVariable.Put_   
         Else
            WScript.Quit
         End If
      End If   
      
      answer = 6

      'Loop while user wishes to add more files to playlist

      Do While answer = 6
         files = files & " " & CHR(34) & SelectFile() & CHR(34)
         answer = MsgBox("Would you like to add another file to the playlist?", 3, "Continue?")
      Loop

      If answer = 2 Then
         WScript.Quit
      End If
      
   End If

   'If this if first run, we must save where the default VLC directory is

   programs = oShell.ExpandEnvironmentStrings("%PROGRAMFILES%")
   vlc_path = oShell.ExpandEnvironmentStrings("%VLC_SHUTDOWN_VLC_LOCATION%")

   If vlc_path = "%VLC_SHUTDOWN_VLC_LOCATION%" Then
      vlc_path = InputBox("Please input the directory where VLC program file is kept." & vbcrlf & vbNewLine & "E.g. C:\Program Files\VideoLAN\VLC", "First Run", programs)
      
      If vlc_path <> "" Then
         strComputer = "."
         Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\cimv2")

         Set objVariable = objWMIService.Get("Win32_Environment").SpawnInstance_

         objVariable.Name = "VLC_SHUTDOWN_VLC_LOCATION"
         objVariable.UserName = "<System>"
         objVariable.VariableValue = vlc_path
         objVariable.Put_
      Else
         WScript.Quit
      End If
   End If

   vlc_path = CHR(34) & vlc_path & "\vlc.exe" & CHR(34) 'VLC directory location

   seconds = InputBox("Please enter the number of seconds the system should delay before commencing shutdown", "Enter Number of Seconds", "5")
   If seconds <> "" Then
      If IsNumeric(seconds) And seconds > 0 Then

         oShell.Run vlc_path & " " & files & " vlc://quit", 1, TRUE
         'Execute shutdown command
         If force_shutdown Then
            oShell.Run "shutdown -s -f -t " & Round(seconds) & " -c " & CHR(34) & "Automatic Shutdown: Playlist Complete" & CHR(34)
         Else
            oShell.Run "shutdown -s -t " & Round(seconds) & " -c " & CHR(34) & "Automatic Shutdown: Playlist Complete" & CHR(34)
         End If
      Else
         InputError("Input not a number or negative")
      End If
   End If
   Wscript.Quit

Linux
~~~~~

Make a .sh
^^^^^^^^^^

Create and execute a bash script with the following:

.. code:: bash

   #! /bin/sh

   vlc && shutdown -h now

With **&&**, figuratively speaking if it returns something other than "success" it doesn't perform the next command in the line.

Ubuntu 11.04 onwards / ConsoleKit based systems
'''''''''''''''''''''''''''''''''''''''''''''''

You are able to shutdown without requiring sudo / root privileges by using dbus-send\ `1 <http://askubuntu.com/questions/49553/how-to-give-shutdown-privileges-to-a-user>`__

.. code:: bash

   #! /bin/sh

   vlc && dbus-send --system --print-reply --dest=org.freedesktop.ConsoleKit /org/freedesktop/ConsoleKit/Manager org.freedesktop.ConsoleKit.Manager.Stop

Older Ubuntu versions / HAL based systems
'''''''''''''''''''''''''''''''''''''''''

.. code:: bash

   #! /bin/sh

   vlc && dbus-send --system --print-reply --dest=org.freedesktop.Hal /org/freedesktop/Hal/devices/computer org.freedesktop.Hal.Device.SystemPowerManagement.Shutdown
