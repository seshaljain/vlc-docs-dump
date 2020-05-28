== VLC cannot play MKV files at all. ==

The software just freezes up and fails to play anything.

This is a fault with an older version of VLC Media Player.

Please upgrade to the latest version. It is an issue with the video
encoding. Just re-download the software, and re-install and all should
be fine.

<br><br>

== VLC hangs when opening MKV file ==

This problem might occur when using VLC to view an [[mkv]] file in a
directory that has a large number of .mkv files. (e.g. in an Azureus
download directory).

VLC will attempt to preload all the .mkv files in the directory and
therefore will hang, especially if some .mkv files are not fully
downloaded yet (thus seem to be broken).

The solution is to set the mkv option:
<code>--mkv-preload-local-dir</code> to ''false'':

'''Preferences → Input / Codecs → Demuxers → Matroska → Preload
Directory''' (uncheck the checkbox).

<br><br><br><br>

{{VSG}}
