.. raw:: mediawiki

   {{See also|MediaControlIDL}}

.. raw:: mediawiki

   {{Historical|The MediaControl API was removed from VLC in 2010.}}

Description
-----------

The MediaControl API is a generic Media player API. The idea is to define a generic video-player API, that could be reused with other players. It is implemented in VLC by using the new `LibVLC <LibVLC>`__ API, and both APIs can cooperate (i.e. you can instanciate a MediaControl object from an existing libvlc instance, and vice-versa).

Its core part (playback control) has been taken from the `OMG Audio/Video Stream specification <http://www.omg.org/cgi-bin/doc?formal/00-01-03.pdf>`__, and extended with additional functionalities. An `IDL specification MediaControl.idl <http://liris.cnrs.fr/advene/download/MediaControl.idl>`__ has been the base of this work.

FIXME : The API is defined in `"include/vlc/mediacontrol.h" <https://trac.videolan.org/vlc/browser/trunk/include/vlc/mediacontrol.h>`__ and implemented in `"src/control" <https://trac.videolan.org/vlc/browser/trunk/src/control>`__.

The Doxygen documentation can be found at `1 <https://www.videolan.org/developers/vlc/doc/doxygen/html/mediacontrol_8h.html>`__.

Current status
--------------

The API currently includes functions for the following things:

-  Playback

   -  Basic features (play/pause/stop)
   -  Seeking
   -  Setting/getting the played media
   -  Getting stream information

-  Audio/Video

   -  Snapshot control (on the fly only)
   -  OSD display (of text and SVG graphics through the svg rendering module)
   -  Volume setting
   -  Setting the visual ID of an embedding window

Current uses
------------

The MediaControl API is used by the following modules :

-  the `PythonBinding <PythonBinding>`__
-  the `JavaBinding <JavaBinding>`__

Foreseen evolutions
-------------------

The following evolutions should be integrated in the API, but discussion is necessary to ensure that they are sufficiently flexible to match various needs :

-  sound_[sg]et_volume: normalize volume in [0..100]
-  implement get_api_version() or get_capabilities() (which would return the list of capabilities supported by the player: ("core", "svg", "snapshot", etc)
-  Complete the implementation. For instance, the frame-by-frame unit (mediacontrol_SampleCount) is not implemented, and the stop/pause do not take the Position parameter into account (they are applied immediately).
-  Fix VLC initialization on Win32 so that it uses the registry key to find the default plugins directory by default. Currently, it uses the vlc.exe path, which it cannot find when using VLC embedded. A workaround is to chdir to the vlc.exe directory before instanciating the MediaControl() object.

Current API
-----------

Here is an IDL description of the current version of MediaControlAPI (from git rev. 445d63e0e38053, on 20080423). In case of doubt, refer to the `mediacontrol.h file <http://trac.videolan.org/vlc/browser/trunk/include/vlc/mediacontrol.h>`__.

.. code:: c

   /*
     Module inspired by the MediaControl IDL
    */
   module VLC {

     const float VERSION = 0.2;

     enum PositionOrigin {
       AbsolutePosition, RelativePosition, ModuloPosition
     };
     
     enum PositionKey {
       ByteCount, SampleCount, MediaTime
     };
     
     struct Position {
       PositionOrigin origin;
       PositionKey key;
       long long value;
     };
     
     exception PositionKeyNotSupported { string message; };
     exception PositionOriginNotSupported { string message; };
     exception InvalidPosition         { string message; };
     exception InternalException       { string message; };

     typedef sequence<octet> ByteSeq;
     
     struct RGBPicture {
       short width;
       short height;
       long type;
       ByteSeq data;
       long long date;
     };
     
     typedef sequence<RGBPicture> RGBPictureSeq;
     
     /* Cf stream_control.h */
     enum PlayerStatus { PlayingStatus, PauseStatus, ForwardStatus, BackwardStatus, InitStatus, EndStatus, UndefinedStatus };
     
     struct StreamInformation {
       PlayerStatus streamstatus;
       string url;        /* The URL of the current media stream */
       long mux_rate;     /* the rate we read the stream in bytes/s */    
       long long position;     /* actual location in the area (in arbitrary units) */
       long long size;         /* total size of the area (in arbitrary units) */
     };
     
      // MediaControl interface is similar to
      // ControlledStream interface in MSS.
      // It can be inherited by flow endpoints or
      // FlowConnection interfaces.
     interface MediaControl
     {
       Position get_media_position(in PositionOrigin an_origin,
                   in PositionKey a_key)
         raises (InternalException, PositionKeyNotSupported);
       
       void set_media_position(in Position a_position)
         raises (InternalException, PositionKeyNotSupported, InvalidPosition);
        
       void start(in Position a_position)
         raises (InternalException, InvalidPosition, PlaylistException);
       void pause(in Position a_position)
         raises (InternalException, InvalidPosition);
       void resume(in Position a_position)
         raises (InternalException, InvalidPosition);
       void stop(in Position a_position)
         raises (InternalException, InvalidPosition);

       oneway void exit (); // Exits the player (not in the original spec)

       // Set/get the current media file/URL
       void set_mrl (in string a_file)
         raises (PlaylistException);
       string get_mrl ()
         raises (PlaylistException);

       // Returns a snapshot of the currently displayed picture
       RGBPicture snapshot (in Position a_position)
         raises (InternalException);

       RGBPictureSeq all_snapshots ()
         raises (InternalException);

       // Displays the message string, between "begin" and "end" positions
       void display_text (in string message, in Position begin, in Position end)
         raises (InternalException);

       StreamInformation get_stream_information ()
         raises (InternalException);
       
       unsigned short sound_get_volume()
         raises (InternalException);

       void sound_set_volume(in unsigned short volume)
         raises (InternalException);

     };
   };

`Category:Bindings <Category:Bindings>`__
