It would be better to change function probe() to contain:

   if string.find( vlc.path, "video.google.com/videoplay", 1, 1 )

instead of

   if string.match( vlc.path, "video.google.com/videoplay" )

to avoid using regular expressions and use plain search/find instead.
Also, if we decide to still use string.match() then the dot (".") must
be encoded like ("%.") otherwise a lot of other false positives would
match, too. For example "www.example.com/video-google_com/videoplay"
would also match.
