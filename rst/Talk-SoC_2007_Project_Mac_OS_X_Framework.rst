What is the best place to put the framework sources?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I am thinking of extra/MacOSX. Any better idea? -- `pdherbemont <User:Pdherbemont>`__. --- Nope, that's the correct place for stuff like this. Putting there a subfolder for the framework is just fine. `feepk <User:Fkuehne>`__ 14:26, 14 April 2007 (CEST)

Should I dump VLCPlaylistDataSource in favor of Cocoa bindings?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The problem is that bindings are not complete enough on Tiger, and don't support as-is drag and dropping. Is it fixed in leopard? --`pdherbemont <User:Pdherbemont>`__ 14:36, 6 May 2007 (CEST) --- I can't talk about this yet, although it may change once a feature complete beta version becomes available at WWDC. Anyway, I wouldn't want the Framework-based VLC.app to be for Leopard only, so we would still need a VLCPlaylistDataSource which is capable to run on Tiger. I hope that I understood your question correctly.\ `feepk <User:Fkuehne>`__ 15:32, 10 May 2007 (CEST)

Should I dump VLC playlist support in VLCMovieView?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It seems that implementing a -setMedia: for a single VLCMovieView would be really more sound. But then we redo VLC playlist handling in the VLCPlaylist obect. It is obviously not really hard to do, as it could be something like ten lines of code.

-  draw back

   -  we might introduce new bugs

-  advantage

   -  ability to use special CoreAnimation transition between video, which is cool.
   -  we don't have to implement more in mediacontrol (this is probably not an advantage --`Pdherbemont <User:Pdherbemont>`__ 23:08, 9 May 2007 (CEST))

--`pdherbemont <User:Pdherbemont>`__ 14:36, 6 May 2007 (CEST)

I agree with you. Having a -setMedia: would surely make sense especially for 3rd party usage of the framework. BTW. I will review your headers, etc. tomorrow, as I have an entire day off :-) `feepk <User:Fkuehne>`__ 15:32, 10 May 2007 (CEST)

Should I merge Timeline/todo reminder?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Not vital, but I should really rethink the way I am presenting things.
