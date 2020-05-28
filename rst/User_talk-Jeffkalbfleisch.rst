Codecs 2vuy / Video Scrubbing 1 frame at a time
-----------------------------------------------

I love VLC as a media player it plays a huge variety of video formats.

I have a couple issues I cannot figure out though.

I use Fedora Core 6 and VLC 0.8.6c-4.lvn6

1. I have quicktime files created via a dds frame cycler that use the 2vuy codec.

| ``       I downloaded this file called 2vuy.bin which is a codec for use with ffmpeg.``
| ``       I think I need to add this file to the codecs for vlc but have no idea how or where or even if it would work. ``
| ``       But I would like too play quicktimes that use 2vuy codec so I can look at quicktimes of this format. ``
| ``       The current documentation seems to cover the codecs vlc handles and does not mention what to do ``
| ``       for codecs that are not listed.``

   VLC doesn't use external codecs. How does VLC plays this file from scratch? `jb <User:J-b>`__

it doesnt

[jeffk@mrk morenamespace]$ vlc 066A-0402.mov VLC media player 0.8.6c Janus [00000337] main decoder error: no suitable decoder module for fourcc \`2vuy'. VLC probably does not support this sound or video format. [00000314] main playlist: nothing to play [00000314] main playlist: stopping playback

2. Video Scrubbing seems to have a minimum frame choice of 1 second. (or 24 frames)

| ``       I need to set it up for animation to do lip sync for video sync to audio.``
| ``       This would require frame by frame scrubbing like quicktime for windows can do.``

``       If I love vlc and want to continue using it am I boned and have to switch to another player for my purpose?``

   I don't understand what is missing in VLC? `jb <User:J-b>`__

When you move forward and backwards the minimum value for very short length is 1 (Shift -Left, Shift -Right). This jumps 1 second instead of 1 frame. To be able to use VLC for timing animation voices to mouths it woud have to be able to go 1 frame at a time. Its important to be able to match sound types to mouth positions to make it look like animated characters are speaking.

IE 1/24 seconds for very short jump length if the mov is cycling 24 frames per second.

Right now we have to use Quicktime for syncing audio to video mouth charts in animation files.
