**.pls** files are a type of `playlist <playlist>`__. This playlist is a text document with the following format:

.. code:: ini

    [playlist]
    NumberOfEntries=4
    File1=/fs/My Music/Eloy/02 Journey into 1358.mp3
    File2=http://some.website.com/music.mp3
    File3=//NETWORKCOMPUTER/Videoclips/A12345.mp4
    Title3=A Short Videoclip
    File4=''any url to file''

The VLC media player requires the parameter in dark red. The parameter "Title(n)" is optional, but if presented with it, VLC will display the title in its Titlebar, and in case of video material the title will be briefly displayed on the screen at the beginning. The tile may not be displayed if a non-Latin character set is used, e.g., containing diacritical marks like ñ, é, ö, etc. If such characters are required the file `should be saved in UTF-8 format <Character_encoding>`__ (quality text editors generally offer this option)

Troubleshooting
~~~~~~~~~~~~~~~

If an existing playlist does not work, check that it has the "NumberOfEntries" parameter at the beginning (some `media players <media_player>`__ do not require it). Also make sure that the file is saved as an ANSI-text file and that the last line is finished off with a line break.

`Category:Playlist <Category:Playlist>`__
