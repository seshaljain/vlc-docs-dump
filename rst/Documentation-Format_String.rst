.. raw:: mediawiki

   {{RightMenu|Documentation TOC}}

Time
----

Starting with `VLC media player <VLC_media_player>`__ 0.9.0, the following options specify a character formatted time string, rather than just a plain character string:

-  --marq-marquee
-  --snapshot-path
-  --snapshot-prefix
-  --sout-file-format
-  --sout-livehttp-index

Time variables are those defined by the **strftime** C function. The following expansions are most common:

-  %Y : year
-  %m : month
-  %d : day
-  %H : hour
-  %M : minute
-  %S : second

For an extensive list have a look at `1 <http://pubs.opengroup.org/onlinepubs/9699919799/functions/strftime.html>`__ (or the strftime manual page on Unix systems).

Input meta
----------

VLC-specific meta-data expansions are available for the following options:

-  --input-title-format
-  --snapshot-path (in version 2.2.0 and later)
-  --snapshot-prefix (in version 2.2.0 and later)

The following expansion are performed:

-  $a : artist
-  $b : album
-  $c : copyright
-  $d : description
-  $e : encoded by
-  $f : total decoded frame count (since VLC started)
-  $g : genre
-  $l : language
-  $n : track number
-  $o : track total
-  $p : now playing
-  $r : rating
-  $s : subtitles language
-  $t : title
-  $u : url
-  $A : date
-  $B : audio bitrate (in kb/s)
-  $C : chapter (as in DVD chapter number)
-  $D : duration
-  $F : full name with path
-  $I : title (as in DVD title number)
-  $L : time left
-  $N : name (media name as seen in the VLC playlist)
-  $O : audio language
-  $P : position (in %)
-  $R : rate
-  $S : audio sample rate (in kHz)
-  $T : time code of the video
-  $U : publisher
-  $V : volume
-  $Z : now playing (artist - title)
-  $\_ : new line
-  $ : (for example: $$ transforms to $)

You can insert a space between the $ sign and the character to tell it to not display anything if the meta data isn't available. For example: ``$ T`` instead will display "" while ``$T`` would display "--:--:--", if no time is available. If a time is available, it would display something like "01_22_13" (for a snapshot from one hour, 22 minutes and 13 seconds in a video).

Source code
~~~~~~~~~~~

If you want to know how this works, check out (search for ``vlc_strfinput``)

The variable b_empty_if_na refers to the leading space feature:

.. raw:: mediawiki

   {{Documentation}}
