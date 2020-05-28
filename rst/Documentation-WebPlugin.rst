.. raw:: mediawiki

   {{Outdated}}

This Documentation speaks about the Web plugins and how to write pages for it.

Introduction: Building Web pages with Video
-------------------------------------------

The webplugins are native browser plugins, similar to Flash or Silverlight plugins and allow playback inside the browser of all the videos that can read.

Additionally to viewing video on all pages, you can build custom pages that will use the advanced features of the plugin, using JavaScript functions to control playback or extract information from the plugin.

There are 2 main plugins: one is ActiveX for IE, the other is NPAPI for the other browsers. They feature the same amount of features.

In older versions, those plugins were very crashy. **We URGE YOU** to use VLC **2.0.0** or newer versions.

Browsers support
~~~~~~~~~~~~~~~~

It has been tested with:

================= =================================
Mozilla Firefox   .. figure:: Firefox-logo.png
                     :alt: Firefox-logo.png
                     :width: 40px
                     :height: 40px
                 
                     Firefox-logo.png
Internet Explorer .. figure:: Internet_Explorer.png
                     :alt: Internet_Explorer.png
                     :width: 40px
                     :height: 40px
                 
                     Internet_Explorer.png
Safari            .. figure:: Apple_Safari.png
                     :alt: Apple_Safari.png
                     :width: 40px
                     :height: 40px
                 
                     Apple_Safari.png
Chrome           
Konqueror        
Opera            
================= =================================

It has been tested on GNU/Linux, Windows and MacOS.

Embed tag attributes
--------------------

To embed the plugin into a webpage, use the following template:

.. code:: html5
   :number-lines:

   <embed type="application/x-vlc-plugin" width="640" height="480" />

If you are using vlc version < 2.2.0 with Internet Explorer, use instead the following template:

.. code:: html5
   :number-lines:

   <object classid="clsid:9BE31822-FDAD-461B-AD51-BE1D1C159921" width="640" height="480"></object>

For the declaration of tag attributes, use the tag . Here an example:

.. code:: html5
   :number-lines:

   <object classid="clsid:9BE31822-FDAD-461B-AD51-BE1D1C159921" width="640" height="480">
       <param name="autostart" value="true" />
       <param name="allowfullscreen" value="false" />
   </object>

For compatibility with the mozilla plugin, you can combine both tags:

.. code:: html5
   :number-lines:

   <object classid="clsid:9BE31822-FDAD-461B-AD51-BE1D1C159921" id="vlc" width="640" height="480">
       <embed type="application/x-vlc-plugin" name="vlc" width="640" height="480" />
   </object>

Required elements
~~~~~~~~~~~~~~~~~

These are **required** attributes for the tag:

-  **width**: Specifies the width of the plugin.
-  **height**: Specifies the height of the plugin.
-  **target** (or one of these alias: **mrl**, **filename**, **src**): Specifies the source location (URL) of the video to load.

Optional elements
~~~~~~~~~~~~~~~~~

These are additional attributes for the tag:

-  **autoplay**, **autostart**: Specifies whether the plugin starts playing on load. Default: *true*
-  **allowfullscreen** (or **fullscreenEnabled**, **fullscreen**): (since VLC version 2.0.0) Specifies whether the user can switch into fullscreen mode. Default: *true*
-  **windowless**: (since VLC version 2.0.6, only for Mozilla) Draw the video on a window-less (non-accelerated) surface and allow styling (CSS overlay, 3D transformations, and much more). Default: *false*
-  **mute**: Specifies whether the audio volume is initially muted. Default: *false*
-  **volume**: (since VLC version 2.2.2) Specifies the initial audio volume as a percentage. Default: *100*
-  **loop**, **autoloop**: Specifies whether the video loops on end. Default: *false*
-  **controls** (or **toolbar**): Specifies whether the controls are shown by default. Default: *true*
-  **bgcolor**: Specifies the background color of the video player. Default: *#000000*
-  **text**: (only for Mozilla on MacOS) Specifies a text displayed as long as no video is shown. Default: empty
-  **branding**: (in vlc version < 2.2.2 only for Mozilla on MacOS) Specifies whether VLC branding should be displayed in the web plugin's drawing context. Default: *true*

Normal DOM elements
~~~~~~~~~~~~~~~~~~~

-  **id**: DOM id
-  **name**: DOM name

Javascript API description
--------------------------

The vlc plugin exports several objects that can be accessed for setting and getting information. When used improperly the API's will throw an exception that includes a string that explains what happened. For example when you set vlc.audio.track out of range.

VLC objects
~~~~~~~~~~~

The vlc plugin knows the following objects:

-  **audio**: Access audio properties.
-  **input**: Access input properties.

   -  **input.title**: Access title properties (available in vlc version ≥ 2.2.2, supported only ≥ 3.0.0)
   -  **input.chapter**: Access chapter properties (available in vlc version ≥ 2.2.2, supported only ≥ 3.0.0)

-  **playlist**: Access playlist properties.

   -  **playlist.items**: Access playlist items properties.

-  **subtitle**: Access subtitle properties.
-  **video**: Access video properties.

   -  **video.deinterlace**: Access deinterlace properties.
   -  **video.marquee**: Access marquee video filter properties.
   -  **video.logo**: Access logo video filter properties.

-  **mediaDescription**: Access media info properties (available in vlc version ≥ 2.0.2).

The following are deprecated:

-  **log**: Access log properties (only available in vlc version ≤ 1.0.0-rc1).
-  **messages**: Access to log message properties (only available in vlc version ≤ 1.0.0-rc1).
-  **iterator**: Access to log iterator properties (only available in vlc version ≤ 1.0.0-rc1).
-  **message**: Access to log message properties (only available in vlc version ≤ 1.0.0-rc1).

Example
^^^^^^^

The following JavaScript code shows howto get a reference to the vlc plugin. This reference can then be used to access the objects of the vlc plugin.

.. code:: html5
   :number-lines:

   <!DOCTYPE html>
   <html>
   <title>VLC Mozilla plugin test page</title>
   <body>
   <embed type="application/x-vlc-plugin"
          width="640"
          height="480"
          id="vlc" />
   <script type="text/javascript">

.. code:: javascript
   :number-lines: 10

   <!--
   var vlc = document.getElementById("vlc");
   vlc.audio.toggleMute();
   //-->

.. code:: html5
   :number-lines: 14

   </script>
   </body>
   </html>

Root object
~~~~~~~~~~~

readonly properties

-  **vlc.VersionInfo**: returns version information string

read/write properties

-  *none*

methods

-  **vlc.versionInfo()**: (only for Mozilla) returns version information string (same as VersionInfo)
-  **vlc.getVersionInfo()**: (supported in vlc version ≥ 2.2.2) returns version information string (same as VersionInfo and versionInfo())

-  **vlc.addEventListener(eventname, callback, bubble)**: (only for Mozilla) add a listener for mentioned event name, callback expects a function and bubble influences the order of eventhandling by JS (usually it is set to false).
-  **vlc.removeEventListener(eventname, callback, bubble)**: (only for Mozilla) remove listener for mentioned event name, callback expects a function and bubble influences the order of eventhandling by JS (usually it is set to false).

-  **vlc.attachEvent(eventname, callback)**: (only for ActiveX) add listener for mentioned event name, callback expects a function
-  **vlc.detachEvent(eventname, callback)**: (only for ActiveX) remove listener for mentioned event name, callback expects a function

events

-  **MediaPlayerNothingSpecial**: vlc is in idle state doing nothing but waiting for a command to be issued
-  **MediaPlayerOpening**: vlc is opening an media resource locator (`MRL <MRL>`__)
-  **MediaPlayerBuffering(int cache)**: vlc is buffering
-  **MediaPlayerPlaying**: vlc is playing a media
-  **MediaPlayerPaused**: vlc is in paused state
-  **MediaPlayerStopped**: vlc is in stopped state
-  **MediaPlayerStopAsyncDone**: (supported in vlc version ≥ 3.0.0) playback has stopped asynchronously
-  **MediaPlayerForward**: vlc is fastforwarding through the media (this never gets invoked)
-  **MediaPlayerBackward**: vlc is going backwards through the media (this never gets invoked)
-  **MediaPlayerEncounteredError**: vlc has encountered an error and is unable to continue
-  **MediaPlayerEndReached**: vlc has reached the end of current playlist
-  **MediaPlayerTimeChanged(int time)**: time has changed
-  **MediaPlayerPositionChanged(float position)**: media position has changed
-  **MediaPlayerSeekableChanged(bool seekable)**: media seekable flag has changed (true means media is seekable, false means it is not)
-  **MediaPlayerPausableChanged(bool pausable)**: media pausable flag has changed (true means media is pauseable, false means it is not)
-  **MediaPlayerMediaChanged**: (supported in vlc version ≥ 2.2.0) media has changed
-  **MediaPlayerTitleChanged(int title)**: (in vlc version < 2.2.0 only for Mozilla) title has changed (DVD/Blu-ray)
-  **MediaPlayerChapterChanged(int chapter)**: (supported in vlc version ≥ 3.0.0) chapter has changed (DVD/Blu-ray)
-  **MediaPlayerLengthChanged(int length)**: (in vlc version < 2.2.0 only for Mozilla) length has changed
-  **MediaPlayerVout(int count)**: (supported in vlc version ≥ 2.2.7) the number of video output has changed
-  **MediaPlayerMuted**: (supported in vlc version ≥ 2.2.7) audio volume was muted
-  **MediaPlayerUnmuted**: (supported in vlc version ≥ 2.2.7) audio volume was unmuted
-  **MediaPlayerAudioVolume(float volume)**: (supported in vlc version ≥ 2.2.7) audio volume has changed

.. _example-1:

Example
^^^^^^^

The following code snippet provides easy functions to register and unregister event callbacks on all supported platforms.

.. code:: html5
   :number-lines:

   <script type="text/javascript">

.. code:: javascript
   :number-lines: 2

   <!--
   function registerVLCEvent(event, handler) {
       var vlc = getVLC("vlc");
       if (vlc) {
           if (vlc.attachEvent) {
               // Microsoft
               vlc.attachEvent (event, handler);
           } else if (vlc.addEventListener) {
               // Mozilla: DOM level 2
               vlc.addEventListener (event, handler, false);
           }
       }
   }
   // stop listening to event
   function unregisterVLCEvent(event, handler) {
       var vlc = getVLC("vlc");
       if (vlc) {
           if (vlc.detachEvent) {
               // Microsoft
               vlc.detachEvent (event, handler);
           } else if (vlc.removeEventListener) {
               // Mozilla: DOM level 2
               vlc.removeEventListener (event, handler, false);
           }
       }
   }
   // event callbacks
   function handle_MediaPlayerNothingSpecial(){
       console.log("Idle");
   }
   function handle_MediaPlayerOpening(){
       console.log("Opening");
   }
   function handle_MediaPlayerBuffering(val){
       console.log("Buffering: " + val + "%");
   }
   function handle_MediaPlayerPlaying(){
       console.log("Playing");
   }
   function handle_MediaPlayerPaused(){
       console.log("Paused");
   }
   function handle_MediaPlayerStopped(){
       console.log("Stopped");
   }
   function handle_MediaPlayerStopAsyncDone(){
       console.log("Stopped asynchronously");
   }
   function handle_MediaPlayerForward(){
       console.log("Forward");
   }
   function handle_MediaPlayerBackward(){
       console.log("Backward");
   }
   function handle_MediaPlayerEndReached(){
       console.log("EndReached");
   }
   function handle_MediaPlayerEncounteredError(){
       console.log("EncounteredError");
   }
   function handle_MediaPlayerTimeChanged(time){
       console.log("Time changed: " + time + " ms");
   }
   function handle_MediaPlayerPositionChanged(val){
       console.log("Position changed: " + val);
   }
   function handle_MediaPlayerSeekableChanged(val){
       console.log("Seekable changed: " + val);
   }
   function handle_MediaPlayerPausableChanged(val){
       console.log("Pausable changed: " + val);
   }
   function handle_MediaPlayerMediaChanged(){
       console.log("Media changed");
   }
   function handle_MediaPlayerTitleChanged(val){
       console.log("Title changed: " + val);
   }
   function handle_MediaPlayerChapterChanged(val){
       console.log("Chapter changed: " + val);
   }
   function handle_MediaPlayerLengthChanged(val){
       console.log("Length changed: " + val + " ms");
   }
   function handle_MediaPlayerVout(val){
       console.log("Number of video output changed: " + val);
   }
   function handle_MediaPlayerMuted(){
       console.log("Audio volume muted");
   }
   function handle_MediaPlayerUnmuted(){
       console.log("Audio volume unmuted");
   }
   function handle_MediaPlayerAudioVolume(volume){
       console.log("Audio volume changed: " + Math.round(volume * 100) + "%");
   }
   // Register a bunch of callbacks.
   registerVLCEvent("MediaPlayerNothingSpecial", handle_MediaPlayerNothingSpecial);
   registerVLCEvent("MediaPlayerOpening", handle_MediaPlayerOpening);
   registerVLCEvent("MediaPlayerBuffering", handle_MediaPlayerBuffering);
   registerVLCEvent("MediaPlayerPlaying", handle_MediaPlayerPlaying);
   registerVLCEvent("MediaPlayerPaused", handle_MediaPlayerPaused);
   registerVLCEvent("MediaPlayerStopped", handle_MediaPlayerStopped);
   registerVLCEvent("MediaPlayerStopAsyncDone", handle_MediaPlayerStopAsyncDone);
   registerVLCEvent("MediaPlayerForward", handle_MediaPlayerForward);
   registerVLCEvent("MediaPlayerBackward", handle_MediaPlayerBackward);
   registerVLCEvent("MediaPlayerEndReached", handle_MediaPlayerEndReached);
   registerVLCEvent("MediaPlayerEncounteredError", handle_MediaPlayerEncounteredError);
   registerVLCEvent("MediaPlayerTimeChanged", handle_MediaPlayerTimeChanged);
   registerVLCEvent("MediaPlayerPositionChanged", handle_MediaPlayerPositionChanged);
   registerVLCEvent("MediaPlayerSeekableChanged", handle_MediaPlayerSeekableChanged);
   registerVLCEvent("MediaPlayerPausableChanged", handle_MediaPlayerPausableChanged);
   registerVLCEvent("MediaPlayerMediaChanged", handle_MediaPlayerMediaChanged);
   registerVLCEvent("MediaPlayerTitleChanged", handle_MediaPlayerTitleChanged);
   registerVLCEvent("MediaPlayerChapterChanged", handle_MediaPlayerChapterChanged);
   registerVLCEvent("MediaPlayerLengthChanged", handle_MediaPlayerLengthChanged);
   registerVLCEvent("MediaPlayerVout", handle_MediaPlayerVout);
   registerVLCEvent("MediaPlayerMuted", handle_MediaPlayerMuted);
   registerVLCEvent("MediaPlayerUnmuted", handle_MediaPlayerUnmuted);
   registerVLCEvent("MediaPlayerAudioVolume", handle_MediaPlayerAudioVolume);
   //-->

.. code:: html5
   :number-lines: 119

   </script>

Audio object
~~~~~~~~~~~~

readonly properties

-  **vlc.audio.count**: (supported in vlc version ≥ 1.1.0) returns the number of audio track available.

read/write properties

-  **vlc.audio.mute**: boolean value to mute and unmute the audio.
-  **vlc.audio.volume**: a value between [0-200] which indicates a percentage of the volume.
-  **vlc.audio.track**: (supported in vlc version > 0.8.6) a value between [1-65535] which indicates the audio track to play or that is playing. a value of 0 means the audio is/will be disabled.
-  **vlc.audio.channel**: (supported in vlc version > 0.8.6) integer value between [1-5] that indicates which audio channel mode is used, values can be: "1=stereo", "2=reverse stereo", "3=left", "4=right", "5=dolby". Use vlc.audio.channel to check if setting of the audio channel mode has succeeded.

methods

-  **vlc.audio.toggleMute()**: boolean toggle that mutes and unmutes the audio based upon the previous state.
-  **vlc.audio.description(int i)**: (supported in vlc version ≥ 1.1.0) give the i-th audio track name. 0 corresponds to disable and 1 to the first audio track.

.. _example-2:

Example
^^^^^^^

.. code:: html5
   :number-lines:

   Audio Channel:
   <select onChange='doAudioChannel(this.value)'>
       <option value=1>Stereo</option>
       <option value=2>Reverse stereo</option>
       <option value=3>Left</option>
       <option value=4>Right</option>
       <option value=5>Dolby</option>
   </select>
   <script type="text/javascript">

.. code:: javascript
   :number-lines: 10

   <!--
   function doAudioChannel(value)
   {
       var vlc = getVLC("vlc");
       vlc.audio.channel = parseInt(value);
       alert(vlc.audio.channel);
   }
   //-->

.. code:: html5
   :number-lines: 18

   </script>

Input object
~~~~~~~~~~~~

readonly properties

-  **vlc.input.length**: length of the input file in number of milliseconds. 0 is returned for 'live' streams or clips whose length cannot be determined by VLC. It returns -1 if no input is playing.
-  **vlc.input.fps**: frames per second returned as a float (typically 60.0, 50.0, 23.976, etc...)
-  **vlc.input.hasVout**: a boolean that returns true when the video is being displayed, it returns false when video is not displayed

read/write properties

-  **vlc.input.position**: normalized position in multimedia stream item given as a float value between [0.0 - 1.0]
-  **vlc.input.time**: the absolute position in time given in milliseconds, this property can be used to seek through the stream

.. code:: javascript

    <!-- absolute seek in stream -->
    vlc.input.time = <absolute seek>
    <!-- relative seek in stream -->
    vlc.input.time = vlc.input.time + <relative seek>

-  **vlc.input.state**: current state of the input chain given as enumeration:

= =========
0 IDLE
1 OPENING
2 BUFFERING
3 PLAYING
4 PAUSED
5 STOPPING
6 ENDED
7 ERROR
= =========

Note: Test for ENDED=6 to catch end of playback. Checking for STOPPING=5 is NOT ENOUGH.

-  **vlc.input.rate**: input speed given as float (1.0 for normal speed, 0.5 for half speed, 2.0 for twice as fast, etc.).

======== ============
rate > 1 fast forward
rate = 1 normal speed
rate < 1 slow motion
======== ============

methods

-  *none*

Title object
^^^^^^^^^^^^

readonly properties

-  **vlc.input.title.count**: (supported in vlc version ≥ 2.2.2) returns the number of title available.

read/write properties

-  **vlc.input.title.track**: (supported in vlc version ≥ 2.2.2) get and set the title track. The property takes an integer as input value [0..65535]. It returns -1 if no titles are available.

methods

-  **vlc.input.title.description(int i)**: (supported in vlc version ≥ 2.2.2) give the i-th title name.

Chapter object
^^^^^^^^^^^^^^

readonly properties

-  **vlc.input.chapter.count**: (supported in vlc version ≥ 2.2.2) returns the number of chapter available in the current title.

read/write properties

-  **vlc.input.chapter.track**: (supported in vlc version ≥ 2.2.2) get and set the chapter track. The property takes an integer as input value [0..65535]. It returns -1 if no chapters are available.

methods

-  **vlc.input.chapter.description(int i)**: (supported in vlc version ≥ 2.2.2) give the i-th chapter name.
-  **vlc.input.chapter.countForTitle(int i)**: (supported in vlc version ≥ 2.2.2) returns the number of chapter available for a specific title.
-  **vlc.input.chapter.prev()**: (supported in vlc version ≥ 2.2.2) play the previous chapter.
-  **vlc.input.chapter.next()**: (supported in vlc version ≥ 2.2.2) play the next chapter.

Playlist object
~~~~~~~~~~~~~~~

readonly properties

-  **vlc.playlist.itemCount**: number that returns the amount of items currently in the playlist (**deprecated**, do not use, see `Playlist items <#Playlist_items_object>`__)
-  **vlc.playlist.isPlaying**: a boolean that returns true if the current playlist item is playing and false when it is not playing
-  **vlc.playlist.currentItem**: (supported in vlc version ≥ 2.2.0) number that returns the index of the current item in the playlist. It returns -1 if the playlist is empty or no item is active.
-  **vlc.playlist.items**: return the playlist items collection, see `Playlist items <#Playlist_items_object>`__

read/write properties

-  *none*

methods

-  **vlc.playlist.add(mrl)**: add a playlist item as `MRL <MRL>`__. The MRL must be given as a string. Returns the index of the just added item in the playlist as a number.
-  **vlc.playlist.add(mrl,name,options)**: add a playlist item as MRL, with metaname 'name' and options 'options'. options are text arguments which can be provided either as a single string containing space separated values, akin to VLC command line, or as an array of string values. Returns the index of the just added item in the playlist as a number.

.. code:: javascript
   :number-lines:

   var options = new Array(":aspect-ratio=4:3", "--rtsp-tcp");
   // Or: var options = ":aspect-ratio=4:3 --rtsp-tcp";
   var id = vlc.playlist.add("rtsp://servername/item/to/play", "fancy name", options);
   vlc.playlist.playItem(id);

-  **vlc.playlist.play()**: start playing the current playlist item
-  **vlc.playlist.playItem(number)**: start playing the item whose identifier is number
-  **vlc.playlist.pause()**: pause the current playlist item
-  **vlc.playlist.togglePause()**: toggle the pause state for the current playlist item
-  **vlc.playlist.stop()**: stop playing the current playlist item
-  **vlc.playlist.stop_async()**: (supported in vlc version ≥ 3.0.0) stop playing the current playlist item asynchronously and fire the event MediaPlayerStopAsyncDone, if done
-  **vlc.playlist.next()**: iterate to the next playlist item
-  **vlc.playlist.prev()**: iterate to the previous playlist item
-  **vlc.playlist.clear()**: empty the current playlist, all items will be deleted from the playlist (**deprecated**, do not use, see `Playlist items <#Playlist_items_object>`__)
-  **vlc.playlist.removeItem(number)**: remove the item from playlist whose identifier is number (**deprecated**, do not use, see `Playlist items <#Playlist_items_object>`__)
-  **vlc.playlist.parse(options, timeout)**: (supported in vlc version ≥ 3.0.0) Parse the first media in the playlist. This fetches (local or network) art, meta data and/or tracks information. Returns the parsed status.

Playlist items object
^^^^^^^^^^^^^^^^^^^^^

readonly properties

-  **vlc.playlist.items.count**: number of items currently in the playlist

read/write properties

-  *none*

methods

-  **vlc.playlist.items.clear()**: empty the current playlist, all items will be deleted from the playlist. (note: if a movie is playing, it will not stop)
-  **vlc.playlist.items.remove(number)**: remove the item whose identifier is number from playlist. (note: this number is the current position in the playlist. It's not the number given by vlc.playlist.add(), if any items of the playlist were removed in the meantime.)

Subtitle object
~~~~~~~~~~~~~~~

readonly properties

-  **vlc.subtitle.count**: (supported in vlc version ≥ 1.1.0) returns the number of subtitle available.

read/write properties

-  **vlc.subtitle.track**: (supported in vlc version ≥ 1.1.0) get and set the subtitle track to show on the video screen. The property takes an integer as input value [1..65535]. If subtitle track is set to 0, the subtitles will be disabled.

methods

-  **vlc.subtitle.description(int i)**: (supported in vlc version ≥ 1.1.0) give the i-th subtitle name. 0 correspond to disable and 1 to the first subtitle.

Video object
~~~~~~~~~~~~

readonly properties

-  **vlc.video.width**: returns the horizontal size of the video
-  **vlc.video.height**: returns the vertical size of the video
-  **vlc.video.count**: (supported in vlc version ≥ 2.2.7) returns the number of video track available.

read/write properties

-  **vlc.video.fullscreen**: when set to true the video will be displayed in fullscreen mode, when set to false the video will be shown inside the video output size. The property takes a boolean as input.
-  **vlc.video.aspectRatio**: get and set the aspect ratio to use in the video screen. The property takes a string as input value. Typical values are: "1:1", "4:3", "16:9", "16:10", "221:100" and "5:4"
-  **vlc.video.scale**: (supported in vlc version ≥ 3.0.0) get and set the video scaling factor as float. That is the ratio of the number of pixels on screen to the number of pixels in the original decoded video in each dimension. Zero is a special value; it will adjust the video to the output window.
-  **vlc.video.subtitle**: (supported in vlc version > 0.8.6a) get and set the subtitle track to show on the video screen. The property takes an integer as input value [1..65535]. If subtitle track is set to 0, the subtitles will be disabled.
-  **vlc.video.crop**: get and set the geometry of the zone to crop. This is set as x + + . A possible value is: "120x120+10+10"
-  **vlc.video.teletext**: (supported in vlc version ≥ 0.9.0) get and set teletext page to show on the video stream. This will only work if a teletext elementary stream is available in the video stream. The property takes an integer as input value [0..1000] for indicating the teletext page to view, setting the value to 0 means hide teletext.
-  **vlc.video.track**: (supported in vlc version ≥ 2.2.7) a value between [1-65535] which indicates the video track to play or that is playing. a value of 0 means the video is/will be disabled.

methods

-  **vlc.video.takeSnapshot()**: (supported in vlc version ≥ 0.9.0, only for ActiveX) generates a snapshot and saves it on the desktop
-  **vlc.video.toggleFullscreen()**: toggle the fullscreen mode based on the previous setting
-  **vlc.video.toggleTeletext()**: (supported in vlc version ≥ 0.9.0) toggle the teletext page to overlay transparent or not, based on the previous setting
-  **vlc.video.description(int i)**: (supported in vlc version ≥ 2.2.7) give the i-th video track name. 0 corresponds to disable and 1 to the first video track.

Deinterlace Object
^^^^^^^^^^^^^^^^^^

readonly properties

-  *none*

read/write properties

-  *none*

methods

-  **vlc.video.deinterlace.enable("my_mode")**: (supported in vlc version ≥ 1.1.0) enable deinterlacing with my_mode. You can enable it with "blend", "bob", "discard", "linear", "mean", "x", "yadif" or "yadif2x" mode. Enabling too soon deinterlacing may cause some problems. You have to wait that all variable are available before enabling it.
-  **vlc.video.deinterlace.disable()**: (supported in vlc version ≥ 1.1.0) disable deinterlacing.

Marquee Object
^^^^^^^^^^^^^^

readonly properties

-  *none*

read/write properties

-  **vlc.video.marquee.text**: (supported in vlc version ≥ 1.1.0) display my text on the screen.
-  **vlc.video.marquee.color**: (supported in vlc version ≥ 1.1.0) change the text color. val is the new color to use (WHITE=0x000000, BLACK=0xFFFFFF, RED=0xFF0000, GREEN=0x00FF00, BLUE=0x0000FF...).
-  **vlc.video.marquee.opacity**: (supported in vlc version ≥ 1.1.0) change the text opacity, val is defined from 0 (completely transparent) to 255 (completely opaque).
-  **vlc.video.marquee.position**: (supported in vlc version ≥ 1.1.0) change the text position ("center", "left", "right", "top", "top-left", "top-right", "bottom", "bottom-left", "bottom-right").
-  **vlc.video.marquee.refresh**: (supported in vlc version ≥ 1.1.0) change the marquee refresh period.
-  **vlc.video.marquee.size**: (supported in vlc version ≥ 1.1.0) val define the new size for the text displayed on the screen. If the text is bigger than the screen then the text is not displayed.
-  **vlc.video.marquee.timeout**: (supported in vlc version ≥ 1.1.0) change the timeout value. val is defined in ms, but 0 value correspond to unlimited.
-  **vlc.video.marquee.x**: (supported in vlc version ≥ 1.1.0) change text abscissa.
-  **vlc.video.marquee.y**: (supported in vlc version ≥ 1.1.0) change text ordinate.

methods

-  **vlc.video.marquee.enable()**: (supported in vlc version ≥ 1.1.0) enable marquee filter.
-  **vlc.video.marquee.disable()**: (supported in vlc version ≥ 1.1.0) disable marquee filter.

Some problems may happen (option like color or text will not be applied) because of the VLC asynchronous functioning. To avoid it, after enabling marquee, you have to wait a little time before changing an option. But it should be fixed by the new vout implementation.

NOTE: see `this forum post <https://forum.videolan.org/viewtopic.php?f=16&t=89427#p295058>`__

Logo Object
^^^^^^^^^^^

readonly properties

-  *none*

read/write properties

-  **vlc.video.logo.opacity**: (supported in vlc version ≥ 1.1.0) change the picture opacity, val is defined from 0 (completely transparent) to 255 (completely opaque).
-  **vlc.video.logo.position**: (supported in vlc version ≥ 1.1.0) change the text position ("center", "left", "right", "top", "top-left", "top-right", "bottom", "bottom-left", "bottom-right").
-  **vlc.video.logo.delay**: (supported in vlc version ≥ 1.1.0) display each picture for a duration of 1000 ms (default) before displaying the next picture.
-  **vlc.video.logo.repeat**: (supported in vlc version ≥ 1.1.0) number of loops for picture animation (-1=continuous, 0=disabled, n=n-times). The default is -1 (continuous).
-  **vlc.video.logo.x**: (supported in vlc version ≥ 1.1.0) change the x-offset for displaying the picture counting from top-left on the screen.
-  **vlc.video.logo.y**: (supported in vlc version ≥ 1.1.0) change the y-offset for displaying the picture counting from top-left on the screen.

methods

-  **vlc.video.logo.enable()**: (supported in vlc version ≥ 1.1.0) enable logo video filter.
-  **vlc.video.logo.disable()**: (supported in vlc version ≥ 1.1.0) disable logo video filter.
-  **vlc.video.logo.file("file.png")**: (supported in vlc version ≥ 1.1.0) display my file.png as logo on the screen.

Some problems may happen because of the VLC asynchronous functioning. To avoid it, after enabling logo video filter, you have to wait a little time before changing an option. But it should be fixed by the new vout implementation.

MediaDescription Object
~~~~~~~~~~~~~~~~~~~~~~~

readonly properties

-  **vlc.mediaDescription.title**: (supported in vlc version ≥ 2.0.2) returns title meta information field.
-  **vlc.mediaDescription.artist**: (supported in vlc version ≥ 2.0.2) returns artist meta information field.
-  **vlc.mediaDescription.genre**: (supported in vlc version ≥ 2.0.2) returns genre meta information field.
-  **vlc.mediaDescription.copyright**: (supported in vlc version ≥ 2.0.2) returns copyright meta information field.
-  **vlc.mediaDescription.album**: (supported in vlc version ≥ 2.0.2) returns album meta information field.
-  **vlc.mediaDescription.trackNumber**: (supported in vlc version ≥ 2.0.2) returns trackNumber meta information field.
-  **vlc.mediaDescription.description**: (supported in vlc version ≥ 2.0.2) returns description meta information field.
-  **vlc.mediaDescription.rating**: (supported in vlc version ≥ 2.0.2) returns rating meta information field.
-  **vlc.mediaDescription.date**: (supported in vlc version ≥ 2.0.2) returns date meta information field.
-  **vlc.mediaDescription.setting**: (supported in vlc version ≥ 2.0.2) returns setting meta information field.
-  **vlc.mediaDescription.URL**: (supported in vlc version ≥ 2.0.2) returns URL meta information field.
-  **vlc.mediaDescription.language**: (supported in vlc version ≥ 2.0.2) returns language meta information field.
-  **vlc.mediaDescription.nowPlaying**: (supported in vlc version ≥ 2.0.2) returns nowPlaying meta information field.
-  **vlc.mediaDescription.publisher**: (supported in vlc version ≥ 2.0.2) returns publisher meta information field.
-  **vlc.mediaDescription.encodedBy**: (supported in vlc version ≥ 2.0.2) returns encodedBy meta information field.
-  **vlc.mediaDescription.artworkURL**: (supported in vlc version ≥ 2.0.2) returns artworkURL meta information field.
-  **vlc.mediaDescription.trackID**: (supported in vlc version ≥ 2.0.2) returns trackID meta information field.

read/write properties

-  *none*

methods

-  *none*

DEPRECATED APIs
~~~~~~~~~~~~~~~

DEPRECATED: Log object
^^^^^^^^^^^^^^^^^^^^^^

   **CAUTION**: For security concern, VLC 1.0.0-rc1 is the latest (near-to-stable) version in which this object and its children are supported.

This object allows accessing VLC main message logging queue. Typically this queue capacity is very small (no more than 256 entries) and can easily overflow, therefore messages should be read and cleared as often as possible.

readonly properties

-  **vlc.log.messages**: returns the message collection, see `Messages object <#DEPRECATED:_Messages_object>`__

read/write properties

-  **vlc.log.verbosity**: write number [-1,0,1,2,3] for changing the verbosity level of the log messages; messages whose verbosity is higher than set will be not be logged in the queue. The numbers have the following meaning: -1 disable, 0 info, 1 error, 2 warning, 3 debug.

methods

-  *none*

DEPRECATED: Messages object
^^^^^^^^^^^^^^^^^^^^^^^^^^^

   **CAUTION**: For security concern, VLC 1.0.0-rc1 is the latest (near-to-stable) version in which this object and its children are supported.

readonly properties

-  **messages.count**: returns number of messages in the log

read/write properties

-  *none*

methods

-  **messages.clear()**: clear the current log buffer. It should be called as frequently as possible to not overflow the message queue. Call this method after the log messages of interest are read.
-  **messages.iterator()**: creates and returns an iterator object, used to iterate over the messages in the log. **Don't clear the log buffer while holding an iterator object.**

DEPRECATED: Messages Iterator object
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   **CAUTION**: For security concern, VLC 1.0.0-rc1 is the latest (near-to-stable) version in which this object and its children are supported.

readonly properties

-  **iterator.hasNext**: returns a boolean that indicates whether *vlc.log.messages.next()* will return the next message.

read/write properties

-  *none*

methods

-  **iterator.next()**: returns the next message object in the log, see `Message object <#DEPRECATED:_Message_subobject>`__

DEPRECATED: Message subobject
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   **CAUTION**: For security concern, VLC 1.0.0-rc1 is the latest (near-to-stable) version in which this object and its children are supported.

-  **message.severity**: number that indicates the severity of the log message (0 = info, 1 = error, 2 = warning, 3 = debug)
-  **message.name**: name of VLC module that printed the log message (e.g: main, http, directx, etc...)
-  **message.type**: type of VLC module that printed the log message (eg: input, access, vout, sout, etc...)
-  **message.message**: the message text

.. raw:: mediawiki

   {{Documentation}}

`Category:Development‏‎ <Category:Development‏‎>`__ `Category:VLC plugins <Category:VLC_plugins>`__
