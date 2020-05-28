(~) I would like to know if it is ok to modify the page like this?

Changes:

I added a linux section, but I'm not sure if it's good or not. Any
sugestions? And this is my very first edit so is more like a test for me
to get the handle on things.

What I did try to do was give some more information and change some
formatting.

([[User:Nimitz Sad Dog|Nimitz Sad Dog]] 12:15, 10 February 2009 (CET))

==How to create a thumbnail from a video==

For all those people wanting a thumbnail from a video, use the following
command:

(win) <pre>vlc -V image --start-time 0 --stop-time 1 --image-out-format
jpg --image-out-ratio 24 --image-out-prefix snap test.mpg
vlc://quit</pre>

===What it does:===

When {{VLC}} runs it 'plays' the video for one second without actually
showing the video on screen, and then quits, leaving us with a file
named 'snap000000.jpg', containing an image of the first frame of the
video.

===How it works:===

First select the image output with: '''-V image''' or '''--vout
image'''.

Next set the interval (in seconds) you want an image from with:
'''--start-time 0 --stop-time 1''' In my example the first second of the
video. In that case you could omit the parameter --start-time. If you
want an image from the 5th second fill in: '''--start-time 5 --stop-time
6'''

The image format will be .jpg because i provided: '''--image-out-format
jpg'''. You could specify '''--image-out-format png''' to get a
.png-image instead.

'''--image-out-ratio 24''' specifies we want one image out of 24. In my
case the video contains 24 images per second so this is the right value.
If your video has more images per seconds you should increase this value
to prevend you get more images as one. If the number is too high (for
example 500) it still produces only one image, so the actual value is
not so important as long as it is higher then the images per second.

'''--image-out-prefix snap''' specifies the filename must start with
'snap'. You can prefix with a path, for example c:snap and resulting
images will be created there.

You can specify '''--image-out-replace'''. In that case Vlc produces the
file 'snap.jpg'. This will prevent VLC from creating multiple images.

'''test.mpg''' specifies the video to play and finally '''vlc://quit'''
forces vlc to quit when ready.

== Linux ==

=== Fedora===

==== What You Need: ====

-  Video: [http://www.bigbuckbunny.org/index.php/download/ Big Buck
   Bunny] License: [http://creativecommons.org/licenses/by/3.0/ Creative
   Commons Attribution 3.0]
-  [http://www.videolan.org/vlc/ VLC Media Player] License:
   [http://www.gnu.org/licenses/gpl-2.0.html GPL 2.0]

==== Getting Started ====

Using this command in the folder that you download the movie(or you can
pass the path to the file in the command line).

<pre>vlc -V image --start-time 13 --stop-time 14 --image-out-format png
--image-out-width 128 --image-out-height 128 --image-out-ratio 24
--image-out-prefix thumbnail --image-out-replace
big_buck_bunny_1080p_stereo.ogg vlc://quit</pre>

You should get something like this:<br/>

http://upload.wikimedia.org/wikipedia/commons/8/86/Vlc_thumbnail_big_buck_bunny.png

Since I downloaded the '''big_buck_bunny_1080p_stereo.ogg''' that is the
name of the file that I put in the command line. But you can do it with
any video file you want to.<br/> If the name of the file have spaces
just put it in single or double quotes.<br/> Ex: 'big buck bunny 1080p
stereo.ogg' or "big buck bunny 1080p stereo.ogg" or '/home/[username
here]/Desktop/big buck bunny 1080p stereo.ogg'

==== What Its Happening? ====

VLC will start playing the movie without the image because the images
are not going to the display but to the output file '''"thumbnail"'''
with the extension '''PNG''' that VLC created by now in the folder you
launched the command in, and it should close after a second into the
video(if the video starts from the begning probably VLC didn't recognize
the file header see options references for more details), don't be
worried if you hear the soundtrack. After that if you look at the folder
you will see a new file called "thumbnail.png".

If you want to understand what is going on read the options reference.

==== Options Reference ====

{\| class="wikitable" \| '''Option''' \| \| '''Value''' \| '''Default'''
\| '''Description''' \| '''Reference''' '''Short''' \| '''Long''' \| \|
\| \| '''-V''' \| '''--vout''' \|
image<br/>aa<br/>caca<br/>x11<br/>xvideo<br/>glx<br/>opengl<br/>snapshot<br/>dummy
\| Automatically select<br/>the best method available. \| Select the
output. This means where to send the video stream to.<br/> Using
'''''image''''' as destination means VLC will create a file somewhere.
\| '''[http://wiki.videolan.org/Video_Output Video Output]''' \|
'''--start-time''' \| integer \| \| Start time.<br/>The stream will
start at this position (in seconds).<br/>ps: Beware that if VLC don't
recognize the header of the file this doesn't work well.<br/> \|
'''[http://wiki.videolan.org/VLC_command-line_help VLC Command Line
Help]''' \| '''--stop-time''' \| integer \| \| Stop time<br/>The stream
will stop at this position (in seconds).<br/>ps: Beware that if VLC
don't recognize the header of the file this doesn't work well. \|
'''[http://wiki.videolan.org/VLC_command-line_help VLC Command Line
Help]''' \| '''--image-out-format''' \| png, jpeg \| png \| Choose the
image file format for the output destination. \|
'''[http://wiki.videolan.org/Documentation:Modules/image Image video
output]''' \| '''--image-out-width''' \| integer \| -1 \| You can force
an image width.<br/>The default '''-1''' will adapt to the video
characteristics.<br/>ps: If you don't set this parameter VLC will save
the image with its original size. \|
'''[http://wiki.videolan.org/Documentation:Modules/image Image video
output]''' \| '''--image-out-height''' \| integer \| -1 \| You can force
the image height.<br/>The default '''-1''' will adapt to the video
characteristics.<br/>ps: If you don't set this parameter VLC will save
the image with its original size. \|
'''[http://wiki.videolan.org/Documentation:Modules/image Image video
output]''' \| '''--image-out-ratio''' \| integer \| 3 \| Ratio of images
to record. 3 means that one image out of three is recorded.<br/>The
ratio is calculate based on the framerate of the video so if your video
have a framerate of 24 frames per second and you set the
--image-out-ratio to 3 you should get 8 image files.<br/>'''ps:'''
Beware that if VLC don't recognize the header of the file this doesn't
work.<br/>You have to use '''--image-out-replace''' instead. \|
'''[http://wiki.videolan.org/Documentation:Modules/image Image video
output]''' \| '''--image-out-prefix''' \| string \| img \| Prefix of the
output images filenames.<br/>Output filenames will have the
[prefix][NUMBER].[Image Format] form (ex: img101.png).<br/>Starting with
VLC 0.9.0 you can also use
[http://wiki.videolan.org/Documentation:Play_HowTo/Format_String format
time and meta variables]. \|
'''[http://wiki.videolan.org/Documentation:Modules/image Image video
output]''' \| '''--image-out-replace''' \| \| disabled \| Always write
to the same file. This means that the last image captured will be the
one you will see saved. \|
'''[http://wiki.videolan.org/Documentation:Modules/image Image video
output]''' \| '''vlc://quit''' \| \| \| Special item to quit
VLC.<br/>Works with the command '''cvlc''' too. \|
'''[http://wiki.videolan.org/VLC_command-line_help VLC Command Line
Help]''' \|}

== Credits: == <br/> [http://www.bigbuckbunny.org/ Big Buck Bunny] was
produced by [http://www.blender.org/ Blender Foundation]

== Doesn't make sense ==

Sorry but this article doesn't make sense and is not helpful. # Where am
I supposed to copy and paste the syntax? # How do I select the image
output? Is it under Preferences? I only see video output. The article
presumes that all users are already familiar with with the
inner-workings of VideoLAN. Please help by writing a step-by-step
how-to. --[[User:Eggfu|Eggfu]] 02:12, 19 April 2010 (UTC)

== Merge ==

I just fixed a cut-and-paste move.

My best guess is that the user [[Special:Contributions/Rozistalk]])
wrote this page over at the (now-deleted) [[What can vlc do,]] page, and
[[User:j-btalk]]) copied it over here without attribution. Rather than
deleting the original page, I used [//en.wikipedia.org/wiki/WP:CUTPASTE
this method] of merging page histories, for copyright purposes&nbsp;–
which are supposedly very nitpicky about these sorts of things.

I think this is fixed. {{User:DoesItReallyMatter/real_sig}} 22:29, 31
October 2016 (CET)
