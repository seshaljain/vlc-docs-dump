== User-side requirements ==

\* working hotkeys in embed, windowed, or fullscreen mode \*\* Partially
related to GUI, but some work will have to be done, see lower \* ability
to position subtitles virtually anywhere (eg outside the picture) \*\*
Ok, planned. See vout_render, cropping/padding \* screen-resolution OSD
\*\* Planned, see subpictures \* ability to switch from embed to
windowed vouts with the mouse \* screenshots \*\* Already existing ...
Want something more ? Answer: yes. The current architecture is meant for
interactive use, but is not really usable from an external application
embedding VLC (cf [[MediaControlAPI]] for an example). Screenshot
functionality should at least provide : **\* the ability to use a
destination other than a file (think embedded)**\ \* a small cache of
pictures to take into account the reaction time **\* precise timestamp
of the snapshot (in movie time)**\ \* Replace image video output cleanly
\* close helper vouts without stopping the stream \*\* More or less
planned \* chained video filters \* on-the-fly AR correction \*
enable/disable video filters on the fly \*\* Should work, currently
buggy (suxxor thread suxxing). Planned \* stream video filters with
stream output (eg start a stream, deinterlace it, invert the colors,
distort the picture, add a logo and a rss feed and stream the result to
your grandmother). \* Screensaver desactivation \* Screensaver output :
maybe having sub-module with screensaver capatibilities and a way to ask
the core to use a screensaver module instead of a regular vout module

[[Category:Dev Discussions]]
