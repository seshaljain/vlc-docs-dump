MediaWiki's built-in image-upload functionality
-----------------------------------------------

The documentation pages could look a lot cleaner and friendlier if we used MediaWiki's built-in image upload functionality. People who don't know HTML and CSS could make use the existing image syntax (http://en.wikipedia.org/wiki/Wikipedia:Extended_image_syntax) to add captions, use thumbnails and position the images.

--`Danwinckler <User:Danwinckler>`__ 01:43, 14 March 2007 (CET)

   The reason why we disabled that feature was that it has previously been used to hack the server we're hosting the wiki on (I don't remember if we were using MediaWiki at the time or another framework). I guess that we could enable it again and trust MediaWiki to prevent that from happening again ... but we're not too confident :) I might give it a look next week-end. -- `Dionoea <User:Dionoea>`__ 13:45, 14 March 2007 (CET)

   If I may chime in here, one of the disadvantages to embedded images (instead of having them uploaded to the wiki itself) that is implicit in Danwinckler's comment is that MediaWiki does not allow embedded images to be resized or have captions added to them. So, you're stuck using them at their original resolution. Would it be possible to upload to the wiki the images from www.videolan.org/doc/play-howto/en/images that are currently being embedded? That way, editors could start captioning/positioning/resizing the images in a consistent fashion. --`Jeremy Butler <User:Jeremy_Butler>`__ 21:47, 11 July 2007 (CEST)

Suggestion: Put authors' names in the *discussion* page
-------------------------------------------------------

I just made this suggestion over on `Documentation Talk:Play HowTo <Documentation_Talk:Play_HowTo>`__, but then I realized it'd be better suited over here.

I'd suggest de-emphasizing the authors of this article. For one, this will change as more authors edit this wiki. In a sense they are credited in the article's *history* page, but, of course, the basic principle of a wiki is that the authors are relatively anonymous.

But my suggestion is mostly based on what a reader wants to know. He/she is not so much interested in the authors as in getting information. Hence, I'd suggest the information come first in this, and all other articles, and the authors, if they need to be listed at all, be moved to the *discussion* pages.

Just my 2 cents...

--`Jeremy Butler <User:Jeremy_Butler>`__ 17:26, 9 July 2007 (CEST)

   Answered on `Documentation Talk:Play HowTo <Documentation_Talk:Play_HowTo>`__. -- `Dionoea <User:Dionoea>`__ 17:54, 9 July 2007 (CEST)

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

2. Video Scrubbing seems to have a minimum frame choice of 1 second. (or 24 frames)

| ``       I need to set it up for animation to do lip sync for video sync to audio.``
| ``       This would require frame by frame scrubbing like quicktime for windows can do.``

``       If I love vlc and want to continue using it am I boned and have to switch to another player for my purpose?``
