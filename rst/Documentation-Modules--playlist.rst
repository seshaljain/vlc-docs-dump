.. raw:: mediawiki

   {{Module|name=playlist|type=Access demux|description=[[Playlist]]}}

The option ``--parent-item`` has been obsolete since VLC 1.1.0.

Options
-------

.. raw:: mediawiki

   {{Option
   |name=playlist-skip-ads
   |value=boolean
   |default=enabled
   |description=Use playlist options usually used to prevent ads skipping to detect ads and prevent adding them to the playlist
   }}

Sub-modules
-----------

============== ================================================ ========= ============================ =============
Submodule name Description                                      Shortcuts Opens file extensions        First version
============== ================================================ ========= ============================ =============
m3u            `M3U <M3U>`__ playlist import                    m3u, m3u8 .m3u, .m3u8, `.vlc <.vlc>`__ 0.5.0, 1.0.4
ram            `RAM <Real>`__ playlist import                   N/A       .ram, .rm                    2.0.2
pls            `PLS <PLS>`__ playlist import                    N/A       .pls                         0.5.2
b4s            `B4S <B4S>`__ playlist import                    shout-b4s .b4s                         0.6.1
dvb            `DVB <DVB>`__ playlist import                    dvb       .conf                        ?
podcast        `Podcast <Podcast>`__ parser                     podcast   N/A                          0.8.5
xspf           `XSPF <XSPF>`__ playlist import                  N/A       .xspf                        0.8.5
asx            `ASX <ASX>`__ playlist import                    N/A       .asx, .wax, .wvx             0.5.0
sgimb          `Kasenna MediaBase <Kasenna_MediaBase>`__ parser sgimb     N/A                          ?
qtl            `QuickTime <QuickTime>`__ Media Link importer    qtl       .qtl                         ?
ifo            `Dummy <Dummy>`__ IFO demux                      N/A       .IFO                         ?
bdmv           `Dummy <Dummy>`__ BDMV demux                     N/A       .BDMV                        ?
itml           `iTunes <iTunes>`__ Music Library importer       itml      .xml                         ?
wpl            `WPL <WPL>`__ playlist import                    wpl       .wpl, .zpl                   1.1.0
============== ================================================ ========= ============================ =============

Source code
-----------

-  

   .. raw:: mediawiki

      {{VLCSourceFile|modules/demux/playlist/playlist.c}}

   (file)

-  

   .. raw:: mediawiki

      {{VLCSourceFolder|modules/demux/playlist}}

   (folder)

.. raw:: mediawiki

   {{Documentation}}

`Category:Playlist <Category:Playlist>`__
