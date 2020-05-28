Discussion about API
--------------------

`OlivierAubert <User:OlivierAubert>`__ (`talk <User_talk:OlivierAubert>`__) And isn't that too VLC-specific ? The rest of the API (minus suggested VLM, which is clearly identified) is fairly generic. We could move vlc specific features in an 'extra' module.

`Zorglub <User:Zorglub>`__ (`talk <User_talk:Zorglub>`__) The generic part is actually very worrying to me. I think we anyway should *definitely* have "VLC" in the symbol names, to avoid any clashes. "mediacontrol" is far too generic to me.

`Littlejohn <User:Littlejohn>`__ (`talk <User_talk:Littlejohn>`__) At the moment the opportunity an external developer has to use this interface is very little. There are coding issues making the interface usable only within the VLC tree. See `this <http://bugzilla.videolan.org/cgi-bin/bugzilla/show_bug.cgi?id=2189>`__ bug I filed.

`OlivierAubert <User:OlivierAubert>`__ (`talk <User_talk:OlivierAubert>`__) I would like to precise the context that lead me to implement this API: I am developping an application that needs to control some video player. I do not want it to be bound to a single player, so I first defined a control API, reusing some OMC specification, and then wrote the code to implement that interface on some players. I did that (at python level, using rc communication) for mplayer, xine and (at C level) for VLC. So this API has been defined based on user/programmer needs, rather than on VLC functionalities exposed by some interface. I do not want to have to rewrite my application when I finally find the time to write the same control interface for the avidemux engine for instance (in order to get frame-by-frame positioning.

In an ideal world, there would be a well-established standard API, that would be supported by all major linux (and more) players : VLC, xine, player... The mediacontrol aims to be a start at this.

`Zorglub <User:Zorglub>`__ (`talk <User_talk:Zorglub>`__) Here is what I propose :

-  We keep providing the normal LibVLC API in vlc/vlc.h
-  in vlc/vlc.h we also provide a "VLC_Control" API which gives access to much more data and uses a semi-object concept (with exceptions, playlist object, stream object, ...) It can include some VLC-specific things (VLM, Filters, ...)
-  We provide the "VLC implementation of mediacontrol" in vlc/control.h which is a wrapper around a common set of functions from VLC_Control. The symbols are prefixed with vlc\_ to avoid symbol clashes, but nothing should be VLC specific here
-  The python binding provides access to vlc.MediaControl (no clash problem here as pyton (and java too) provide the notion of namespace)

`Littlejohn <User:Littlejohn>`__ (`talk <User_talk:Littlejohn>`__) Here is a proposed plan to accomplish the points zorglub listed:

-  rewrite playlist management to solve current issues with playlist (see the playlist section)
-  factorize the functions of all interesting (stream, etc) objects in vlc and write the VLC_Control API
-  implement mediacontrol interface using the VLC_Control API
-  complete support of mediacontrol in bindings

Since I'm not still very accostumed with VLC internals I cannot say how to proceed with every object.

`Zorglub <User:Zorglub>`__ (`talk <User_talk:Zorglub>`__) Ok, but you are focusing on playlist, which is only a minor point of this API rework :)

`OlivierAubert <User:OlivierAubert>`__ (`talk <User_talk:OlivierAubert>`__) Another proposed way to proceed (avoiding too many levels of wrapping) :

-  define the (generic) mediacontrol API in a player- and language-independent way (using the current MediaControl.idl file as a start)
-  implement this API in VLC, using a VLC-specific prefix (vlc_mediacontrol_) for methods
-  extend this API with VLC-specific functions (VLM, filters...), with another prefix (vlc_mediacontrol_ext_)

This way, the number of wrappers would be minimized, and we can accomodate both generic and vlc-specific APIs. I do not know if you agree on the usefulness of first defining an API based on what is needed, then seeing how this API can be implemented in the player.

`Littlejohn <User:Littlejohn>`__ (`talk <User_talk:Littlejohn>`__) I see having more layers as an opportunity to implement a stable mediacontrol interface. The current VLC API problem is APIs being changed constantly, and this prevents the possibility to expose such APIs (defined as private). Layering would indeed allow to expose a set of stable functions programmers can use, and focus changes on the inner levels. Anyway I do agree in defining the interface before bothering about actual implementation in the player.

API Design
----------

`OlivierAubert <User:OlivierAubert>`__ (`talk <User_talk:OlivierAubert>`__) For me, the mediacontrol API is a generic API, independent from the player. If the player does not support some feature (like position parameter to pause and resume), then the API should try its best to have a coherent behaviour.

`Littlejohn <User:Littlejohn>`__ (`talk <User_talk:Littlejohn>`__) Well, I think even if the interface is generic it has to call functions contained in the player. For example the position parameter for pause and resume should be implemented in the player and then called by the mediacontrol interface. In this way we have to opportunity to enrich the player and ease maintainance of the interface (otherwise features in the interface could overlap with those in the player or changes in the player could break the interface).

Stream Information
------------------

-  mediacontrol_get_status_information *Return synthetized information (position, url, status), so that applications can quickly get it (*\ `Advene <http://liris.cnrs.fr/advene/>`__\ *for instance calls this method every 100ms)*
-  **mediacontrol_get_video_information** ''Return misc. information about the video (aspect ratio, dimensions, bitrate, codec, author, etc).

Playlist
--------

`OlivierAubert <User:OlivierAubert>`__ (`talk <User_talk:OlivierAubert>`__) Could be transformed into a Playlist object (returned by MediaControl.playlist), that would feature the corresponding methods: add, clear, next, prev, play, sort...

`Littlejohn <User:Littlejohn>`__ (`talk <User_talk:Littlejohn>`__) This is ok for me. Maybe we could apply this abstraction to other parts of the interface, ie having a Stream object and so on.

`Littlejohn <User:Littlejohn>`__ (`talk <User_talk:Littlejohn>`__) The current playlist implementation makes it impossible to correctly honor the position argument in mediacontrol_<start|stop|pause|etc>. The problem is that moving through the playlist implies playing the item we moved to. It should be possible to move in the playlist without automatically playing the item. Doing so we have the possibility to add the "start-time" option before starting to play. We could think about two ways of doing so: either let playlist_Next() accept a position parameter or make playlist_Next not to start playing. So playing should be possible only from playlist_Play and playlist_Play should accept the position parameter.

Video
-----
