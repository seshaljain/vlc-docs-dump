== Error in the documentation regarding subtitle track value == The
documentation claims that in the input/codecs tab in preferences,
setting the "subtitle track" value to "0" will disable subtitles by
default. In actuality (as of VLC 2.1.5) a value of "-1" will disable
subtitles.

Furthermore, it appears that the subtitle track number is not a
boolean/toggle setting, but a ''relative index'' for the "Subtitle>Sub
Track" selection menu; with "-1" corresponding to "Disable", "0" for the
first subtitle-track, "1" for the second track, and so on...

I suppose it might be more intuitive if the values did start at "0", as
then a "1" would correspond to subtitle track 1... but it appears that
this setting instead adheres to the convention of "-1" to disable an
option or feature.

At present, the doc is simply incorrect ;-)

--[[User:Aprilia1ktalk]]) 18:50, 1 February 2015 (CET), <small>edited
for conciseness by {{User:DoesItReallyMatter/real_sig}} 09:45, 24
February 2015 (CET)</small> :{{Fixed}}
{{User:DoesItReallyMatter/real_sig}} 10:00, 24 February 2015 (CET)
