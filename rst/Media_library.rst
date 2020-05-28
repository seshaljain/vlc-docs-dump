This is a brand-new page as of 2009/03/21, an attempt to provide
instructions on how to use the media player's Media Library feature.

As of VLC media player version 0.9.8a, the Media Library feature offers
only the most basic abilities.

This author is working from a MacBook Pro using OS 10.4.11, so if you
are using Windows (XP or Vista) or Linux, the exact locations of your
menus and controls, as well as their appearance, can be expected to vary
somewhat.

Everything presented here so far has been garnered from the user forums,
and/or exploring the preferences and controls of my own copy of the
program.

== To Begin ==

To use the media player's "Media Library" feature, first verify that the
function has been enabled in Preferences, then adjust the controller so
that the window where the function is displayed automatically opens.

From the "VLC" menu select "Preferences...". It will not matter which
tab you select. The desired option is an Advanced option: in the
Preferences window, in the lower left hand corner find radio buttons
labeled "Basic" and "All". Click the "All" button.

The preferences window will change to show a narrow left-hand pane and a
wide right-hand pane. The left pane lists categories of preferences that
may be adjusted. Most items have triangles(Mac) or "+"(Qt) next to them,
which may be clicked to show subcategories. For the moment we don't need
to click any of them. Just know that expanded subcategories give quick
access to particular options. Occasionally a subcategory may be the only
way to gain access to the options desired.

If the left-hand pane is too narrow to view the list, click on the
divider between the panes and drag it to adjust the width.

In the left-hand pane find and click the word "Playlist" to view the
Playlist controls.

In the right-hand pane, next to "Use media library", ensure the box is
checked. If it was necessary to change this option, be sure to click
"Save", at the bottom right of the preferences pane.

On this control pane, note "Play files randomly forever" - uncheck this
if desired. (Users have reported files playing in random order even when
they
[http://forum.videolan.org/viewtopic.php?f=13&t=55953&hilit=media+library
don't want them to]. For 0.98 it is uncertain whether this control is
working. If you have not enabled it, but are getting random play,
consider reporting it as a bug.)

To close this window, click either the "Cancel" or "Save" button.

Once "Use media library" is enabled, open the Playlist window to see the
Media Library in action. There are several ways to accomplish this, but
one certain way is: from the media player's menu bar, \* Mac: click
"Window" menu and select "Controller...". The last time the VLC media
player was used, if the playlist window was already opened, then it will
automatically reopen. If not, then click the "Window" menu again and
select "Playlist...". \* Qt: click "View" menu and select "Playlist".

Due to redundant controls, there are other ways get this done. On the
basic controller, in the lower right-hand corner, is a pair of buttons.
The left button when toggled will open and close the 10 band audio
equalizer. (If you want to use it, be sure that there is a checkmark in
the "Enable" box in the Equalizer's window.) The right-hand button when
toggled will open and close the "Playlist" window. You can also open and
close the "Playlist" window by grabbing and dragging the very edge of
the lower right corner of controller window. At a certain shape and
size, the "Playlist" window will snap opened or closed as appropriate.

== What's Next? ==

Other users report in the forum that the Media Library file will appear
in the VLC media player folder along with the application and will be
named "ml.xspf". Thus the Media Library file is in fact a sophisticated
playlist in xspf format. To learn more about it, go to the [[XSPF]]
article in this wiki.

''Note: the Media Library file can be hard to find on Mac OS X. As of
VLC version 1.1.3 (and possibly before) it is located in
~/Library/Application Support/org.videolan.vlc/ .''

Once you know how the xspf format works, you need to use a text editor
suitable for things like writing XML code to put your playlist together.

I use TextWrangler 2.3.0 (262) ub.app, a free OS X Mac program, for
example. http://barebones.com/products/textwrangler/

Once created, from the VLC media player use "Open File..." and/or "Save
Playlist..." to bring it to the media player's attention.

On Mac OS 10.4.11, these items are found on the "File" menu.

On Linux and Windows try looking for "Playlist -> Save playlist to
file..."

== Adding media to the Media Library ==

To add files/folders to your Media Library:

1. Select "Media Library" in the left pane of the main window.
2. Right-click the Media Library area, and click Add Folder (or Add
   File)
3. Select the file/folder you wish to add, then click OK.

== See also == \* [[:Category:Playlist]] \* [[M3U]] short for "MP3
Uniform Resource Locator", refers to a computer file format that stores
multimedia playlists \* http://www.xspf.org/quickstart/ \*
[[Documentation:Hacker's Guide/Playlist|VLC Playlist and Media Library]]
\* [[What is cool in 0.9]] includes relevant details under the topic
"Playlist" \* [[Next changes]] includes relevant details under the topic
"Playlist" \* [[VLC Source code]] useful especially in the absence of
user friendly documentation

[[Category:Documentation]]
