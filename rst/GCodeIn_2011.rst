Google Code In
==============

This page is about gathering **ideas** for the VideoLAN project for acceptance in the `Google Code In 2011-2012 <http://code.google.com/opensource/gci/2011-12/index.html>`__ program.

VideoLAN has been part of `Google Summer of Code <http://code.google.com/soc/>`__ in `2007 <SoC_2007>`__, `2008 <SoC_2008>`__, `2009 <SoC_2009>`__ and `2010 <SoC_2010>`__.

`x264 <x264_GCodeIn_Ideas>`__ is also participating in Videolan's Code-In.

Ideas for VideoLAN
==================

Warning
-------

This is a temporary page for listing ideas for Google Code-in tasks.

The final tasks will be moved to melange, when needed.

The list is being migrated to a google doc for ease of importing/processing.

`Simplified Form <https://docs.google.com/spreadsheet/viewform?hl=en_GB&formkey=dHZHenE4WFhXZlBrck5GZmtrQ0wyR2c6MQ#gid=0>`__\ \|\ `List so far <https://docs.google.com/spreadsheet/ccc?key=0ArFsnoouksujdHZHenE4WFhXZlBrck5GZmtrQ0wyR2c&hl=en_GB#gid=0>`__

Please help filling it the data using the form.

libav
-----

Code Cleanup
~~~~~~~~~~~~

| **Category**: Code
| **Description**: libav has a coding style and all the new contributions must abide to it, sadly ancient files do not abide to it
| **Outcome**: provide a patchset with properly formatted code, points will be awarded per file. Additional points if a larger file is split in the process. **Difficulty**:
| **Tools**:
| **Time**:
| **Mentor**:

Video Tutorial: avconv
~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Documentation
| **Description**: avconv had been recently introduced and new and old users of ffmpeg might enjoy having some walkthrough to a number of common tasks.
| **Outcome**: Prepare a video with a short tutorial for one of the following tasks:
| \*Transcode to h264/aac/mov
| \*Transcode to vp8/vorbis/webm
| \*Transcode to h264/speex/flv
| \*Live streaming from a video source (webcam/screen capture) to a remote server (rtmp, rtsp)
| **Difficulty**:
| **Tools**:
| **Time**:
| **Mentor**:

Help document filter usage
~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Documentation
| **Description**: A list of filters is nice, but actual examples would help a lot
| **Outcome**: You'll provide 5 different examples involving filters
| **Difficulty**:
| **Tools**:
| **Time**:
| **Mentor**:

Live-streaming from libav
~~~~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Documentation
| **Description**: Lots of sites let you broadcast yourself, but sometimes getting there can be a challenge- help improve this
| **Outcome**: Produce a guide showing how to do live-streaming to a video site of your choice
| **Difficulty**:
| **Tools**:
| **Time**:
| **Mentor**:

Create a new preset
~~~~~~~~~~~~~~~~~~~

| **Category**: Documentation
| **Description**: libav has a fine set of presets, but they're limited in scope- other codecs could certainly benefit from some nice presets
| **Outcome**: Create a new preset that gets accepted into libav
| **Difficulty**:
| **Tools**:
| **Time**:
| **Mentor**:

Practical examples on capturing from devices
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Documentation
| **Description**: There's many devices that avconv can capture from, but not all are well documented- some only have a mention or two and no examples
| **Outcome**: At least five new examples on capturing from devices will be created
| **Difficulty**:
| **Tools**:
| **Time**:
| **Mentor**:

Document metadata tags and their usage
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Documentation
| **Description**: There are huge number of metadata tags spread across many standards, and libav supports many of them. Documentation on them is sparse, and is mostly contained in the source code
| **Outcome**: At least one metadata format will be documented fully with examples
| **Difficulty**:
| **Tools**:
| **Time**:
| **Mentor**:

Fuzzing MPEG2 files
~~~~~~~~~~~~~~~~~~~

| **Category**: Quality Assurance
| **Description**:
| **Outcome**: Fuzz at least 10 MPEG2 files and file bug reports for crashes w/samples
| **Difficulty**:
| **Tools**:
| **Time**:
| **Mentor**:

Fuzzing H264 files
~~~~~~~~~~~~~~~~~~

| **Category**: Quality Assurance
| **Description**:
| **Outcome**: Fuzz at least 10 H264 files and file bugreports for crashes w/samples
| **Difficulty**:
| **Tools**:
| **Time**:
| **Mentor**:

Fuzzing MPEG4 (Divx/Xvid) files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Quality Assurance
| **Description**:
| **Outcome**: Fuzz at least 10 MPEG4 files and file bug reports on crashes w/samples
| **Difficulty**:
| **Tools**:
| **Time**:
| **Mentor**:

Fuzzing MJPEG files
~~~~~~~~~~~~~~~~~~~

| **Category**: Quality Assurance
| **Description**:
| **Outcome**: Fuzz at least 10 MJPEG files and file bugreports on crashers w/samples
| **Difficulty**:
| **Tools**:
| **Time**:
| **Mentor**:

Fuzzing other codecs
~~~~~~~~~~~~~~~~~~~~

| **Category**: Quality Assurance
| **Description**: Other codecs that aren't as mainstream definitely could use some fuzztesting to shake out problems and possible security threats
| **Outcome**: Fuzz at least 10 files for your chosen codec and file bugreports on crashers w/samples
| **Difficulty**:
| **Tools**:
| **Time**:
| **Mentor**:

Fuzzing existing crashers
~~~~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Quality Assurance
| **Description**: A wide range of projects use libav, and some of them maintain bugtrackers or forums which contain records of crashing files
| It would be nice to know if those files still crash libav, and if fuzzing them creates a new crash
| **Outcome**: Test 10 open reports of crashing files from a libav-using project to see if it still crashes on the latest libav, and then fuzz test those files, filing bugreports on any crashes found
| **Difficulty**:
| **Tools**:
| **Time**:
| **Mentor**:

Common problems with no documented solution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Research
| **Description**: Anyone who has spent some time on mailing lists or IRC channels starts to see the same questions pop up time and again
| The most frequent of these usually get put in an FAQ, or some other easily-accessible place **Outcome**: Document an issue that seems to pop up regularly without getting answered and find an answer for it
| **Difficulty**:
| **Tools**:
| **Time**:
| **Mentor**:

Find a new video codec
~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Research
| **Description**: There are hundreds of video codecs in existence, and many of them are known and documented
| For as many as are known, there's undoubtedly still more out there waiting to be found and written about
| **Outcome**: Find a video file that does not play in current libav, and provide information on it, containing at the least:
| \*Video codec name
| \*How to identify this type (usually a fourcc, a certain file header or a unusual/unique file extension)
| \*Samples with descriptions of what they depict and codec features used in them if known
| \*Links to the original decoder and encoder
| **Difficulty**:
| **Tools**:
| **Time**:
| **Mentor**:

Find a new audio codec
~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Research
| **Description**: There are a large number of audio codecs out there, and just like video codecs, many of them are known and documented
| Undoubtedly though, there are still more out there that are not yet known or documented
| **Outcome**: Find a currently unknown audio codec and provide information about it so it can be eventually supported
| This information should include the following:
| \*Audio codec name
| \*How to identify this type (twoCC, a file header or a distinctive file extension usually)
| \*Samples, ideally made from lossless source and details on any features used if known
| **Difficulty**:
| **Tools**:
| **Time**:
| **Mentor**:

VideoLAN Communication
----------------------

Wiki Orphans and Double tracking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Documentation
| **Description**: The wiki has way too many `orphaned pages <Special:LonelyPages>`__ and `double redirected pages <Special:DoubleRedirects>`__, they should be linked by other pages or marked for deletion, and redirects should be fixed
| **Outcome**: A better wiki with less orphaned pages or redirects
| **Difficulty**: easy
| **Tools**: a wiki account
| **Time**: 4hours
| **Mentor**: `xtophe <User:Xtophe>`__

Wiki short pages tracking
~~~~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Documentation
| **Description**: The wiki has too many `short pages <Special:ShortPages>`__, they should be improved, marked for deletion or merged with other pages
| **Outcome**: A better wiki with less short pages
| **Difficulty**: easy
| **Tools**: a wiki account
| **Time**: 4hours
| **Mentor**: `xtophe <User:Xtophe>`__

Update wiki guides
~~~~~~~~~~~~~~~~~~

| **Category**: Documentation
| **Description**: Not all of the guides on the wiki have been updated for newer versions of VLC
| Update one for the latest released version of VLC
| **Outcome**: A working guide for the latest release of VLC
| **Difficulty**:
| **Tools**:
| **Time**:
| **Mentor**:

Create a guide on capturing video from capture cards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Documentation
| **Description**: A guide to capturing video from video capture cards
| One for hardware-encoder cards, and one for non-hardware encoder cards would be great
| **Outcome**: A guide with screenshots for one type of video capture card
| **Difficulty**:
| **Tools**:
| **Time**:
| **Mentor**:

VideoLAN flyer/poster
~~~~~~~~~~~~~~~~~~~~~

| **Category**: Outreach
| **Description**: The VideoLAN project needs a flyer for promotional matters
| **Outcome**: A cool A5-sized flyer presenting VideoLAN
| **Difficulty**: medium
| **Tools**: Image-Editing software
| **Time**: 3days
| **Mentor**: `Jean-Paul Saman <User:Jpsaman>`__

VideoLAN Forum improvements
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Research and Outreach
| **Description**: The VideoLAN `forums <http://forum.videolan.org>`__ have many shortcomings, especially regarding spam and "Solved topics"
| We need research on solutions and advise us how we can improve the forums
| **Outcome**: small report on ideas, advice and solution
| **Difficulty**: medium
| **Tools**: Browser and Text editor
| **Time**: 3days
| **Mentor**: VLC_help

VideoLAN PHP webpage for file uploading for bugreports
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Code
| **Description**: The VideoLAN project needs a small WebPage in PHP to be able to upload the files for the bugreports
| As some of those files are big, some progression bar should be done in Javascript too
| **Outcome**: a working deployed PHP script
| **Difficulty**: hard
| **Tools**: PHP development environment
| **Time**: 5days
| **Mentor**: etix

VLC
---

Create VLC videos for training
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Training
| **Description**: Creation of youtube Videos of screencasts of VLC usage
| This task can be divided in chunks of 5 videos
| **Outcome**: VLC Youtube channels
| **Difficulty**: easy
| **Tools**: VLC, screencast recorders
| **Time**: 2 days
| **Mentor**: `linkfanel <User:linkfanel>`__

VLC documentation illustration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Documentation
| **Description**: Creation of VLC screenshots and small diagrams to improve the VLC documentation on the wiki
| **Outcome**: VLC illustrations on the documentation
| **Difficulty**: easy
| **Tools**: VLC, Image Editing software
| **Time**: 5 days
| **Mentor**: `Rémi Duraffort <User:ivoire>`__

VLC users survey creation
~~~~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Outreach
| **Description**: Creation of a survey for VLC users, about their usage of VLC, that we will put on the website
| **Outcome**: Survey ready to be sent to the VLC users
| **Difficulty**: medium
| **Tools**: text editor and web browser
| **Time**: 5 days
| **Mentor**: `jb <User:J-b>`__

VLC fullscreen controller redesign
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Category**: User Interface
| **Description**: Find ideas to improve and redesign the fullscreen controller of the VLC version on Windows/Linux
| **Outcome**: Sketchs and ideas for the fullscreen controller
| **Difficulty**: medium
| **Tools**: web browser and image editor
| **Time**: 5 days
| **Mentor**: `jb <User:J-b>`__

Help out your language's translation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Translation
| **Description**: Help translate more of VLC into your language
| **Outcome**: Add at least 5% more translations
| **Difficulty**:
| **Tools**:
| **Time**:
| **Mentor**:

VLC volume controller redesign
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Category**: User Interface
| **Description**: Find ideas to improve and redesign the volume controller of the VLC version on Windows/Linux
| **Outcome**: Sketchs and ideas for the volume controller
| **Difficulty**: hard
| **Tools**: web browser and image editor
| **Time**: 3 weeks
| **Mentor**: `jb <User:J-b>`__

VLC Lyrics extension
~~~~~~~~~~~~~~~~~~~~

| **Category**: Code
| **Description**: Creation of one extension in lua that can be able to fetch and display Lyrics from one website API
| **Outcome**: Working Lua Lyrics extension script
| **Difficulty**: hard
| **Tools**: text editor and VLC
| **Time**: 10 days
| **Mentor**: `jpeg <User:Jpeg>`__

VLC Songkick extension
~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Code
| **Description**: Creating one extension in lua that can be able to fetch and display Lyrics from Songkick API
| **Outcome**: Working Lua Songkick extension script
| **Difficulty**: hard
| **Tools**: text editor and VLC
| **Time**: 10 days
| **Mentor**: `jpeg <User:Jpeg>`__

VLC webplugin testpages
~~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Code
| **Description**: This task is about updating the Html/CSS/JS scripting test pages for the `Webplugins <Documentation:WebPlugin>`__.
| **Outcome**: Usable pages for testing the VLC webplugins
| **Difficulty**: hard
| **Tools**: text editor and a browser
| **Time**: 10 days
| **Mentor**: `Jean-Paul Saman <User:Jpsaman>`__

VLC warnings cleanup
~~~~~~~~~~~~~~~~~~~~

| **Category**: Code
| **Description**: This has for objective to delete a lot of warnings in C and C++ code when doing VLC compilation for Linux and Windows.
| **Outcome**: Less warnings in C and C++ code
| **Difficulty**: hard
| **Tools**: text editor and compilation toolchain
| **Time**: 10 days
| **Mentor**: `Rémi Duraffort <User:ivoire>`__

libVLC Qt example media player
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Code
| **Description**: Creating a small example of how to create a media player based on libVLC and Qt on Windows/Linux.
| **Outcome**: a cool media player to demonstrate the libVLC API in Qt
| **Difficulty**: hard
| **Tools**: complete compilation toolchain
| **Time**: 15 days
| **Mentor**: pdherbemont

libVLC Gtk example media player
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Code
| **Description**: Creating a small example of how to create a media player based on libVLC and Gtk on Windows/Linux.
| **Outcome**: a cool media player to demonstrate the libVLC API in Gtk
| **Difficulty**: hard
| **Tools**: complete compilation toolchain
| **Time**: 15 days
| **Mentor**: pdherbemont

libVLC Elementary example media player
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Code
| **Description**: Creating a small example of how to create a media player based on libVLC and Elementary on Linux.
| **Outcome**: a cool media player to demonstrate the libVLC API in Elementary
| **Difficulty**: hard
| **Tools**: complete compilation toolchain
| **Time**: 15 days
| **Mentor**: pdherbemont lu_zero

libVLC wxWidgets example media player
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Code
| **Description**: Creating a small example of how to create a media player based on libVLC and wxWidgets on Windows/Linux.
| **Outcome**: a cool media player to demonstrate the libVLC API in wxWidgets
| **Difficulty**: hard
| **Tools**: complete compilation toolchain
| **Time**: 15 days
| **Mentor**: pdherbemont

VLMC
----

Create VLMC videos for training
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| **Category**: Training
| **Description**: Creation of youtube Videos of screencasts of VLMC usage
| This task can be divided in chunks of 3 videos
| **Outcome**: VLMC Youtube channels
| **Difficulty**: easy
| **Tools**: VLMC, screencasting tools
| **Time**: 3 days
| **Mentor**: `etix <User:etix>`__

VLMC UI testing
~~~~~~~~~~~~~~~

| **Category**: Quality Assurance
| **Description**: Testing VLMC Interface and testing all dialogs and options to find bugs
| **Outcome**: Bugreports
| **Difficulty**: easy
| **Tools**: VLMC
| **Time**: 3 days
| **Mentor**: Hugo

VLMC files testing
~~~~~~~~~~~~~~~~~~

| **Category**: Quality Assurance
| **Description**: Testing VLMC for Windows or Linux with many file formats
| **Outcome**: Bug reports on the forum that don't work
| **Difficulty**: medium
| **Tools**: VLMC, mediainfo, Windows/Linux
| **Time**: 7 days
| **Mentor**: Hugo

Contact
-------

For ANY question, contact `jb <User:J-b>`__ or `xtophe <User:xtophe>`__

IRC channel: #videolan or irc://irc.freenode.net

.. raw:: mediawiki

   {{GSoC}}

`\* <Category:SoC_2011_Project>`__
