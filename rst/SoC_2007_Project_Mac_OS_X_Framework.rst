{{SoCProjectstudent=[[User:Pdherbemontmentor=[[User:Fkuehne|Felix Paul
Kühne]]}}

'''If you wish to use the framework refer to the [[Mac OS X Framework]]
wiki page'''

=== Introduction ===

I ([[User:PdherbemontFelix Kühne]].

=== Project Objectives ===

More information in [http://pdherbemont.free.fr/gsoc/vlc_framework.html
my original Proposal].

=== Status Summary ===

The simple test app that links to VLC.framework is able to play a given
video just fine.

I have been re-working libvlc, so that the OS X framework can be a nice
umbrella over it. A vlc application could be rewritten without the need
of any other VLC interface than LibVLC.

I have implemented a master-detail-view interface a-la iTunes using
Cocoa Bindings, and the framework. It may be a good candidate to replace
current VLC.app but it still need a lot of work. Main advantages are
code base is very light. It is easily modifiable. It makes uses of
Bindings (with its pros and cons).

So far I didn't complete some of my objectives for the Google Summer of
Code: \* Some functionality of the framework such as media transcoding,
(config) preferences tuning, and vout filter are not implemented. \* The
web plugin does not take

=== Timeline ===

{\| class="wikitable" ! Task Description !! Due Date !! Accomplished
'''My proposition has been accepted''' \|\| N/A \|\| {{yes}} 12/04/2007
'''Work on setting up a git server to publish my work.''' See [[Git]]
(thanks to [[User:Dionoea\| 15/04/2007 \|\| {{yes}} 13/04/2007
'''Implement the stub framework and the sample code that links to it.'''
See the commit on
[http://git.videolan.org/cgi-bin/gitweb.cgi?p=vlc-soc.git;a=commit;h=164ffd0787906e6b6ef1be731a450d0296fde9e9
commit 1],
[http://git.videolan.org/cgi-bin/gitweb.cgi?p=vlc-soc.git;a=commit;h=72e8aa87d1f2b5249e00d596ae015b049da6108d
commit 2]. \|\| 15/04/2007 \|\| {{yes}} 13/04/2007 '''First draft of the
headers, plus partial implementation.''' Events, playlist, vout basic
usage demo in the sample code. \* We do have some draft which cover
vout/playlist and shows how events will be relayed. \* The sample code
is less advanced than expected but that's fine, given the wanted
simplicity. \* We do have, as a side effected, implemented
VLCPlaylistDataSource which is an NSOutlineView data source, and is an
efficient way to display the playlist from guest app. \|\| 29/04/2007
\|\| {{yes}} 29/04/2007 '''Event structure in place in MediaControl.'''
\|\| no due date \|\| {{yes}} 29/04/2007 '''Auto evalutation, keeping in
mind [http://pdherbemont.free.fr/gsoc/vlc_framework.html my original
Proposal]:''' Would current VLC be able to work with the object defined?
Is there any simplification possible? What changes to libvlc are
needed?. \|\| 29/04/2007 \|\| {{yes}} '''Make delegate callback (events)
get called on main thread.''' \|\| 6/05/2007 \|\| {{yes}} 03/05/2007
'''Implement my
[http://138.195.130.71/via/ml/vlc-devel/2007-06/msg00254.html RFC on
libvlc (v2)].''' The RFC v2 is partly implemented. And the work is now
on a RFC on libvlc playlist. \|\| ? \|\| {{yes}} 10/07/2007 '''Implement
Meta data in VLCMedia.''' \|\| ? \|\| {{yes}} 10/07/2007 '''Implement my
new RFC on libvlc playlist.''' media_list, media_list_player,
media_library, media_discoverer are implemented. \|\| ? \|\| {{yes}}
'''First draft of Media Library object.''' \|\| ? \|\| {{yes}} '''First
draft of Dynamic playlist object.''' for now. We can use the bindings
facility plus NSPredicate to imlement that. \|\| ? \|\| {{no}} - dumped
'''First draft of transcoding objects.''' \|\| ? \|\| {{no}} - not
completed for SoC '''First draft of picture effect objects.''' \|\| ?
\|\| {{no}} - not completed for SoC '''First draft of preferences
objects.''' \|\| ? \|\| {{no}} - not completed for SoC '''Have VLC/Mac
OS X use the Framework.''' \|\| ? \|\| {{no}} - VLC.app is implemented,
this is a rewrite from scratch, but we still need to get some of the old
code back. '''Make VLC work without interface.''' (and remove VLC Cocoa
hack from core) \|\| ? \|\| {{yes}} - already works without
intervention. '''End of the Google summer of code''' \|\| N/A \|\|
20/08/2007 '''Merge the code in trunk, and preserve old VLC.app.''' \|\|
? \|\| {{no}} \|}

=== Todo reminder === \* Rename VLCMovieView to VLCMediaView \* Use a 1
sec time frame for the DidChangePosition \* Make mediacontrol uses
libvlc

=== Code repository === All the code I did for the GSoC is publicly
stored on VideoLan's svn trunk (libvlc related changes) and VideoLan's
[http://git.videolan.org/cgi-bin/gitweb.cgi?p=vlc-soc.git;a=shortlog;h=pdherbemont_branch
Git Repository for GSoC] on the '''pdherbemont_branch''' branch. To
check it out: $ git clone git://git.videolan.org/vlc-soc.git $ cd
vlc-soc Now get my branch in a new local osx_framework branch: $ git
checkout -b osx_framework remotes/origin/pdherbemont_branch And to keep
sync-ed, tell git to use remote pdherbemont_branch for osx_framework. $
git config branch.osx_framework.merge refs/heads/pdherbemont_branch And
tell git the remote repository is named origin. $ git config
branch.osx_framework.remote origin Now a simple: $ git pull Should be
enough to get synced.

=== Building the framework and the test app === \* Build VLC as usual.
see [[OSXCompile\| How to build VLC on Mac OS X]]. \* Build the
framework $ cd extra/MacOSX/Framework $ make \* Now open
extra/MacOSX/Framework/Examples/test/test.xcodeproject with Xcode \* hit
command-R

Voilà!
