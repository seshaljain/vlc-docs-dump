{{Lowercase}} {{Open}} libdvdnav and libdvdread are ([[VideoLAN]])
[[libraries]] for [[DVD]] navigation based off the earlier code of the
[[Ogle]] project: \* libdvdnav is for complex navigation (DVDs with
menus and other features) \* libdvdread is for simpler navigation (DVDs
without menus)

As described by the developer documentation
''[https://www.videolan.org/developers/libdvdnav.html libdvdnav &
libdvdread]'' on videolan.org: <blockquote>libdvdnav is a library for
developers of multimedia applications. It allows easy use of
sophisticated DVD navigation features such as DVD menus, multiangle
playback and even interactive DVD games. All this functionality is
provided through a simple {{API}} which provides the DVD playback as a
single logical stream of blocks, intermitted by special dvdnav events to
report certain conditions. The main usage of libdvdnav is a loop
regularly calling a function to get the next block, surrounded by
additional calls to tell the library of user interaction. The whole DVD
virtual machine and internal playback states are completely
encapsulated.</blockquote>

== Links == === libdvdnav === \*
[https://code.videolan.org/videolan/libdvdnav libdvdnav] at
code.videolan.org \*\*
[https://code.videolan.org/videolan/libdvdnav/blob/master/README
libdvdnav README] - an extended introduction \*
[[Documentation:Modules/dvdnav]] === libdvdread === \*
[https://code.videolan.org/videolan/libdvdread libdvdread] at
code.videolan.org \* [[Documentation:Modules/dvdread]]

[[Category:Libraries]] [[Category:VideoLAN projects]]
