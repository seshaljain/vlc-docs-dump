.. raw:: mediawiki

   {{Howto|batch transcode or encode}}

.. raw:: mediawiki

   {{Example code|l=GPL}}

Idea
----

The idea is to use VLC to do some batch work to encode or `transcode <transcode>`__ multiple files one after each other, without having to care about it.

You may want to transcode all your videotheque to another format to play them on an `iPod <iPod>`__, a `Zune <Play_on_Zune>`__, a PS3 or an `Xbox <Play_on_Xbox>`__.

Codecs / Muxers
---------------

You have to choose the correct `codecs <codec>`__ for the device you want to transcode for.

We choose here `H.264 <H.264>`__ with `AAC <AAC>`__ in a `MPEG-2/TS <MPEG-TS>`__ muxer as an example.

GUI
---

Batch convert is supported via the in VLC 3.0.0

Otherwise, use command-line batch transcoding below.

Command Lines
-------------

Windows
~~~~~~~

For example, to transcode a batch of m4a files (potentially in multiple subdirectories of a single common root directory) to mp3 files (512kb/s encoding with 44100 sampling frequency) you could use the following code in a Windows XP command prompt:

.. code:: dos

   for %%a in (*.VOB) do "C:\Program Files\VideoLAN\VLC\vlc" -I dummy -vvv %%a --sout=#transcode{vcodec=h264,vb=1024,acodec=mp4a,ab=192,channels=2,deinterlace}:standard{access=file,mux=ts,dst=%%a.mpg} vlc://quit

   @ECHO OFF
   REM ########################################################################
   REM # A Windows XP cmd.com script to batch convert m4a files to mp3.       #
   REM #                                                                      #
   REM # Copyright (C) 2008 Andrew Boden                                      #
   REM # (boden@graduate.uwa.edu.au)                                          #
   REM #                                                                      #
   REM # This program is free software: you can redistribute it and/or modify #
   REM # it under the terms of the GNU General Public License as published by #
   REM # the Free Software Foundation, either version 3 of the License, or    #
   REM # (at your option) any later version.                                  # 
   REM #                                                                      #
   REM # This program is distributed in the hope that it will be useful,      #
   REM # but WITHOUT ANY WARRANTY; without even the implied warranty of       #
   REM # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        #
   REM # GNU General Public License for more details.                         #
   REM #                                                                      #
   REM # You should have received a copy of the GNU General Public License    #
   REM # along with this program.  If not, see <http://www.gnu.org/licenses/>.#
   REM #                                                                      #
   REM # Version 1.0 (June 27th 2008)                                         #
   REM # Uses VideoLAN VLC 0.8.6h (www.videolan.org)                          #
   REM # Gracefully handles commas and apostrophes in file names.             #
   REM # Not aware of any other characters needing graceful handling.         #
   REM # 512kbps encoding with 44100 sampling.                                #
   REM ########################################################################

   FOR /R %%G IN (*.m4a) DO (CALL :SUB_VLC "%%G")
   FOR /R %%G IN (*.m4a.mp*) DO (CALL :SUB_RENAME "%%G")
   GOTO :eof

   :SUB_VLC
    SET _firstbit=%1
    SET _qt="
    CALL SET _newnm=%%_firstbit:%_qt%=%%
    SET _commanm=%_newnm:,=_COMMA_%
    REM echo %_commanm%
    CALL "C:\Program Files\VideoLAN\VLC\vlc" -I dummy -vvv %1 --sout=#transcode{acodec="mpga",ab="512","channels=2",samplerate="44100"}:standard{access="file",mux="mpeg1",dst="%_commanm%.mp3"} vlc://quit
   GOTO :eof

   :SUB_RENAME
    SET _origfnm=%1
    SET _endbit=%_origfnm:*.m4a=%
    CALL SET _newfilenm=%%_origfnm:.m4a%_endbit%=.mp3%%
    SET _newfilenm=%_newfilenm:_COMMA_=,%
    COPY %1 %_newfilenm%
    DEL %1
   GOTO :eof

   :eof

The same as above, for vlc >= 0.9:

.. code:: dos

   @ECHO OFF
   FOR /R %%G IN (*.m4a) DO (CALL :SUB_VLC "%%G")
   FOR /R %%G IN (*.m4a.mp*) DO (CALL :SUB_RENAME "%%G")
   GOTO :eof

   :SUB_VLC
    SET _firstbit=%1
    SET _qt="
    CALL SET _newnm=%%_firstbit:%_qt%=%%
    SET _commanm=%_newnm:,=_COMMA_%
    REM echo %_commanm%
    CALL "C:\Program Files\VideoLAN\VLC\vlc" -I dummy -vvv %1 --sout=#transcode{acodec="mpga",ab="512","channels=2"}:standard{access="file",mux="raw",dst="%_commanm%.mp3"} vlc://quit
   GOTO :eof

   :SUB_RENAME
    SET _origfnm=%1
    SET _endbit=%_origfnm:*.m4a=%
    CALL SET _newfilenm=%%_origfnm:.m4a%_endbit%=.mp3%%
    SET _newfilenm=%_newfilenm:_COMMA_=,%
    COPY %1 %_newfilenm%
    DEL %1
   GOTO :eof

   :eof

Windows 7 SendTo
~~~~~~~~~~~~~~~~

| This batch file allows to use the Windows SendTo context menu in Explorer.
| Copy the content in a file named MOV_to_MPG_Converter.bat and copy it to your SendTo directory (CMD SHELL:sendto)

.. code:: dos


   @ECHO OFF
   rem ***********************************************************************
   rem * MOV to MPG batch converter. (2014-09-29 Sinx)                       *
   rem *                                                                     *
   rem * For installation just copy batch file to SendTo directory.          *
   rem * On Win8 execute "SHELL:sendto" to go to Sendto folder.              *
   rem *                                                                     *
   rem * I got quite good compression rations with these parameters:         *
   rem * vcodec=h264      codec used                                         *
   rem * vb=10000         video bandwidth                                    *
   rem * deinterlace=1    rebuild full pictures from keyframes and diffs.    *
   rem * acodec=mp3       audio codec                                        *
   rem * ab=128           128kbps mp3 quality                                *
   rem * channels=2       stereo                                             *
   rem *                                                                     *
   rem * for parameters see                                                  *
   rem * http://www.videolan.org/doc/vlc-user-guide/de/ch04.html             *
   rem ***********************************************************************
   echo **********************************************************************
   echo MOV to MPG VLC batch converter called: %0 %1 %2 %3 %4 %5 %6 %7 %8
   echo **********************************************************************
   echo.
   echo For installation, just copy batch file to SendTo folder..
   echo.

   SET _new_extention=mpg

   :start
   if "%~1"=="" (call goto :the_end)
   CALL :SUB_CONVERT %1
   SHIFT
   goto :start


   :SUB_CONVERT
   SET _orig_path=%~1
   rem SET _orig_extention=%_orig_filename:*.=%
   echo %_orig_path%
   SET _orig_extention=%_orig_path:*.=%
   CALL SET _new_path=%%_orig_path%:.%_orig_extention%=.%_new_extention%%%
   set _new_path="%_new_path%"
   echo.
   echo Converting %1 ======TO===== %_new_path% ...
   echo.

   if exist "%ProgramFiles%\VideoLAN\VLC\vlc.exe" (
   SET _vlc_path="%ProgramFiles%\VideoLAN\VLC\vlc"
   ) else (
   SET _vlc_path="%ProgramFiles(x86)%\VideoLAN\VLC\vlc"
   )

   CALL %_vlc_path% -I dummy -vvv %1 --sout=#transcode{vcodec=h264,vb=10000,deinterlace=1,acodec=mp3,ab=128,channels=2,samplerate=44100}:standard{access=file,mux=ts,dst=%_new_path%} vlc://quit
   GOTO :eof

   :the_end
   echo **********************************************************************
   echo * FINISHED                                                           *
   echo **********************************************************************
   pause

Powershell
~~~~~~~~~~

.. code:: powershell

       
   $outputExtension = ".mp3"
   $bitrate = 160
   $channels = 2

   foreach($inputFile in get-childitem -recurse -Filter *.wav)
   { 
     $outputFileName = [System.IO.Path]::GetFileNameWithoutExtension($inputFile.FullName) + $outputExtension;
     $outputFileName = [System.IO.Path]::Combine($inputFile.DirectoryName, $outputFileName);
     
     $programFiles = ${env:ProgramFiles(x86)};
     if($programFiles -eq $null) { $programFiles = $env:ProgramFiles; }
     
     $processName = $programFiles + "\VideoLAN\VLC\vlc.exe"
     $processArgs = "-I dummy -vvv `"$($inputFile.FullName)`" --sout=#transcode{acodec=`"mp3`",ab=`"$bitrate`",`"channels=$channels`"}:standard{access=`"file`",mux=`"wav`",dst=`"$outputFileName`"} vlc://quit"
     
     start-process $processName $processArgs -wait
   }

Unix / Linux
~~~~~~~~~~~~

Transcodes all files in current directory (except hidden files), saving with suffix ``.transcoded``.

.. code:: bash

   #!/bin/sh                                                                                                                                                     
   ######################## Transcode the files using ... ########################
   vcodec="mp4v"
   acodec="mp4a"
   vb="1024"
   ab="128"
   mux="mp4"
   ###############################################################################

   # Store path to VLC in $vlc
   if command -pv vlc >/dev/null 2>&1; then
       # Linux should find "vlc" when searching PATH
       vlc="vlc"
   else
       # macOS seems to need an alias
       vlc="/Applications/Utilities/VLC.app/Contents/MacOS/VLC"
   fi
   # Sanity check
   if ! command -pv "$vlc" >/dev/null 2>&1; then
       printf '%s\n' "Cannot find path to VLC. Abort." >&2
       exit 1
   fi

   for filename in *; do
       printf '%s\n' "=> Transcoding '$filename'... "
       "$vlc" -I dummy -q "$filename" \
          --sout '#transcode{vcodec="$vcodec",vb="$vb",acodec="$acodec",ab="$ab"}:standard{mux="$mux",dst="$filename.transcoded",access=file}' \
          vlc://quit
       ls -lh "$filename" "$filename.transcoded"
       printf '\n'
   done

The wildcard ``*.transcoded`` will select all of the transcoded files for group operations.

To move files:

.. code:: bash

   mv *.transcoded <directory>

To remove all filename extensions (including ``.transcoded``):

.. code:: bash

   for filename in *.transcoded; do mv "$filename" "${filename%%.*}"; done

To remove all filename extensions and replace with another (e.g. ``.mp3``):

.. code:: bash

   for filename in *.transcoded; do mv "$filename" "${filename%%.*}.mp3"; done
