{{Image requested}}<!-- All images shown are out of date. The subtitles
menu is no longer a sub-menu of the video menu, and Windows and Linux
both use the same interface (Qt4) --> {{RightMenu|Documentation TOC}}
VLC supports many kinds of subtitles.

==Media with included subtitles==

Many types of media can have embedded subtitles. VLC can read subtitles
for the following media formats: *DVD*\ SVCD *OGM files*\ Matroska (MKV)
files

Subtitles are enabled by default in VLC media player. To disable them,
go to the ''Video'' menu, and to ''Subtitles track''. All available
subtitles tracks will be listed. Select "Disable" to turn off the
subtitles. Depending on the media, a description (language, for example)
might be available for the track.

To disable subtitles by default, select "Preferences", then "Show All".
Select "Input/Codecs". On the "Subtitle Track ID" selection window,
change the value to "-1". (NOTE: Changing the value in the "Subtitle
Track" menu will not disable the subtitle file.) In the case of multiple
subtitle tracks, a value of "0" will enable subtitle track 1, a value of
"1" will enable subtitle track 2, and so on.

VLC under Linux:

[[File:VLCSubs.png]]

VLC under OSX:

https://images.videolan.org/images/documentation/play-howto/intf-osx-select-sub.jpg

VLC under Windows:

[[File:Basic_subtitles_selection.png]]

DVD and SVCD subtitles are merely images, so you won't be able to change
anything for them. OGM and Matroska subtitles are rendered text, so you
will be able to change several options.

Text rendering options can be changed in the ''Preferences'' in the
''Tools'' tab. To adjust the font preference check the ''All'' bullet in
the ''Show Settings'' box, and then click ''Subtitles/OSD''. You can
then set the font and its size under ''Text Renderer''. For the font,
you have to select a font file. In Windows, they can be found in
''C:WindowsFonts''. Under MacOS X, they are in
''/System/Library/Fonts''. Sizes can be set either relatively or as a
number of pixels.

[[File:Basic_subtitles_prefs.png]]

Subtitle text rendering preferences under Windows, VLC 1.1.5

You need to restart your stream for the font modifications to take
effect.

==Subtitles files==

While modern file formats like Matroska or OGM can handle subtitles
directly, older formats like AVI can't. Therefore, a number of subtitles
files formats have been created. You need two files: the video file and
the subtitles file that only contains the text of the subtitles and
timestamps.

VLC can handle these types of subtitles files: *MicroDVD*\ SubRIP
*SubViewer*\ SSA *Sami*\ Vobsub (this one is quite special: it is not
made from text but from images, which means that you can't change the
fonts)

To open a subtitles file, use the Advanced Open dialog box (Menu File,
Open file). Select your file by clicking on the ''Browse'' button. Then,
check the ''Subtitle options'' checkbox and click on the "Settings"
button.

[[File:Subtitles.PNG]]

You can then select the subtitles file by clicking the ''Browse''
button. You can also set a few options like character encoding,
alignment and size.

An alternative is loading subtitles from the ''Subtitles Track'' menu
item under the ''Video'' tab.

Note: For Vobsub subtitles, you need to select the '''.idx''' file, not
the '''.sub''' file. Encoding, alignment and size won't have any effect
for Vobsub subtitles.

Font can be changed as explained in the previous section.

{{Documentation}}

[[Category:Subtitles|*]]
