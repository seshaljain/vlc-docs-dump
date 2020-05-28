Five people from Ecole Centrale Paris ([[http://www.ecp.fr ECP]]) have a
second year project related to VLC Media Player. Three of them work on
VLC development : ivoire, phytos and JPeg.

= Project ECP =

== Main goal ==

The main objective of our project is to create a Media Collection, or
Media Library, based on an SQL database. This would allow people to use
VLC Media Player as a real Media Center.

The database will be used to store information about every medias, and
create a collection with them. The database will be a little complex
because VLC Media Player is able to read Videos, Musics, Streams from
the Internet, ... and all of these medias have to be collected.

== Git repository ==

Thanks to pdherbemont, we have our own git branch in the VLC repository.
See [[http://git2.videolan.org/?p=vlc-ecp-project.git;a=summary]] for
more details.

= Pending patches =

Some of these patches may have already been included in the main SVN or
Git repo.

== Subtitles downloader ==

''By JPeg''

I have written a module to automagically download subtitles from
[[http://www.opensubtitles.org OpenSubtitles.Org]] and insert them in
the Video playback. It is based on a lua script to fetch a list of
subtitles from a webpage. This way allows us to implement other
subtitles databases than only OpenSubtitles.Org.

An user interface has been implemented only for Qt4.

== Zip files extractor ==

''By JPeg''

As OpenSubtitles.Org does not provide directly .srt, .sub, etc...
subtitles files but a .zip archive, I had to decompress the files. I
just reused code from skins2 and create a simple module with it. This
module, called extractzip provides functions to extract files from
archives. (On 25 February 2008, it supports only ZIP compression model).

It would be great to create a demux on this model, so that you don't
need to extract files on the hard drive to read them.

[[Category:Coding]]
