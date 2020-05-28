Antoine Cellerier

Contact me: dionoea on irc.freenode.net #videolan (`#videolan IRC logs since March 2004 <http://dionoea.chewa.net/irc/videolan>`__)

My vlc compilation scripts are available online: http://people.videolan.org/~dionoea/config/ .

`My contributions to this wiki <Special:Contributions/Dionoea>`__

My VLC to do list
-----------------

For 0.9.0:

-  finish the video filter2 transition (core + interface).
-  clean up the motion detection plugin code + add VLM callbacks when motion is detected.
-  help with the Qt interface.
-  fix the marq/logo callbacks in the RC interface. **Done**

Other stuff I'm thinking about:

-  my secret project (can't tell you what that is yet ... sorry).
-  erase video filter2 to remove logos from a live stream. **Done**
-  change hotkeys handling in VLC (from 1 action -> 1 key to 1 key -> 1 action). Would make it possible to have multiple hotkeys for 1 action.
-  add DVD menu controls to the HTTP interface (using hotkey simulations from the HTTP interface code ... or maybe something cleaner).
-  improve the HTTP interface's Flash plugin page. Add a page using the VLC plugin (both IE and Mozilla).
-  subtitles support in the ffmpeg muxer.

Code I have lying around which might need to be commited one day:

-  cache access filter (not finished). Basic idea was to read as much data as possible from the hard drive (or a DVD drive) and put it in RAM to lower battery usage (and noise) in VLC. Maybe we'd need to implement that directly in the VLC core ... and maybe it's even already available using some obscure command line option. I'll have to ask fenrir about that.
-  VLC screen saver on win32.
-  Start of native windows (XP(?)) remote control handling code on win32.

My VideoLAN to do list
----------------------

-  add country detection to our mirrors script (using mod_geoip from `maxmind <http://www.maxmind.com>`__ ? Test page available `here <http://dionoea.chewa.net/geoip.php>`__). **Done**
-  install punBB with `User:J-b <User:J-b>`__ to offload Ganesh. **Not needed since phpBB 3 works far better**
-  move the last 2 pages from the `documentation <http://www.videolan.org/doc/>`__ to the `wiki <Documentation:Documentation>`__ and start updating it. **Done**
