== HTML integration issue == i ve tried this code

its not working can any body help me ?

<embed id="vlc" type="application/x-vlc-plugin"
pluginspage="http://www.videolan.org" width="500px" height="500px"
src="VIdeo/sampurna.avi"/>

<script type="text/javascript" language="Javascript"> <!-- var vlc =
document.getElementById("vlc"); vlc.audio.toggleMute(); //!--> </script>

   Hello, You should ask support questions to the forum instead. This
   wiki is used for reference documentations. Regards.

== Subtitles issue ==

Hello,

i've tried to use subtitle api, but i've got an error message :

When i use : ''document.getElementById('vlc').subtitle.count'' i've got
this error triggered : ''Uncaught TypeError: Cannot read property
'count' of undefined''

i use it just after i play the
video(''document.getElementById('vlc').playlist.play()''), and this
video actually have 2 subtitle tracks.

am i supposed to do something before using subtitles ?

Regards.
