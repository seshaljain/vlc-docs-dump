Hi all, I was wondering if it was possible to use a 'dynamic' background image, for example an image on which one could read the hour ?

When you define the mosaic, is the background image reloaded sometimes or just loaded once when starting ?

Several solutions are available : 1/ You can use several images with the switcher module (but i don't think those can be changed once the switcher module is launched) 2/ You can use another video stream as the background (instead of a fixed image). This image can be generated with VLC and you can use the marq, logo or time video filters that can be updated real time.

--------------

I've set up the mosaic example and I run the example with:

./vlc -- color -- extraintf telnet -- vlm-conf ../custom_vlc/mosaic.vlc.conf

Some times the mosaic stay inside of the "window" wxWindow, and other times the mosaic stay outside of the "window" wxWindow. Somebody knows as to assert that the mosaic always stays inside of the "window" wxWindows?

--------------

Would it be possible to compile a win32 binary with the older ffmpeg source so that mosaic can function under Windows?

I would really like to get this working and tried compiling under Mandriva LE 2005 but ran into too many troubles.

--------------

How I can change in execution time the mosaic-order, and others mosaic's attributes?

Something more in depth please
------------------------------

This page would really benefit from a more thorough description of the elements. An example is helpful, but there's not really a lot of description of what's going on under the hood.

   So you want to know how mosaic really works from a developper's point of view? Or just some enhanced description of everything involved in setting up a mosaic in VLC? `Dionoea <User:Dionoea>`__ 09:59, 14 December 2006 (CET)

      Well, the problem is that it isn't clear how these components are connected. For example, what is mosaic-bridge, what is bridge-in, and what is bridge-out, and how do these things fit together? It seems like bg is having its output piped to bridge-in; however, where and how is mosaic-bridge connected to the main bridge? The example helps, but since no explanation is given for how the individual pieces together, it's tough to generalize and extend/change the example to fit my needs. I've been mostly trying to figure out how things work by changing things and seeing where the mosaic breaks.--\ `Ianarcher <User:Ianarcher>`__ 17:56, 14 December 2006 (CET)

      Ok. I'll improve this howto (and put it in the VLC Documentation). `Dionoea <User:Dionoea>`__ 18:07, 14 December 2006 (CET)

      One thing I'm confused about, for example, is that running a mosaic with the transform filter causes weird artifacts in windows. For example, a vertical flip causes the streams to be both flipped and have their original displayed simultaneously! It is unclear where the display and the bridge fit together!

VLM example didn't quite work as expected
-----------------------------------------

While a very good jumping-off point, at least for me the VLM example created extra streams of each input which opened an additional window for every mosaic stream on the client viewer. It also tended to crash the client whether the mosaic stream was opened via SAP or with a direct UDP URL.

So I changed the following:

`` setup channel1 output #duplicate{dst=mosaic-bridge{id=1,height=144,width=180},select=video,dst=bridge-out{id=1},select=audio}                                                         ``

to:

`` setup channel1 output #duplicate{dst=mosaic-bridge{id=1,height=144,width=180}} ``

to make everything work as expected.

However, that said, none of my input streams contain audio, so I have no idea if this change created a problem I don't know about. Also, I'm not confident enough in this change to edit the Wiki page itself, so I will leave this to others to confirm.

As an aside, it might be mentioned somewhere along the line that mosaic processing takes considerable horsepower. My normal VLC test machine might be a wheezy old (1.2GHz) PC, and it has worked fine for everything... up to this. A four-tile mosaic brought it to its knees. Success took 60% on both CPUs of a 2 GHz dual-core Intel, which is pretty intense.

   If you don't have any audio, a plain

``setup channel1 output #mosaic-bridge{id=1,height=144,width=180}``

   should be enough. (Since you don't have to split the input stream in order to blend the video and append the audio elementary stream)
   About your load problem, that's to be expected. You have to decode the 4 input videos, scale them, blend them on the background (decode the background too) and then encode the whole thing. So that takes a bit more processing power than the usual 1 video setups. If you're using the developpement version of VLC, you can add a chroma option the mosaic-bridge module. Setting it to I420 will improve your blending performance considerably.
   As a reference, the 20 video mosaic example runs on a two year old bi-xeon server (at full load). Using the chroma=I420 thing lowers the CPU usage by 10% if I remember correctly.
   I hope this helps,
   `Dionoea <User:Dionoea>`__ 14:30, 10 December 2007 (CET)

CPU usage
---------

I've run into the CPU load problem even on 1 input video, with vlc 1.0.1.

I'm using a 640x480 image and a 640x480 video, streamed locally from a file. The VLC doing the mixing (of the still image and video) is eating 60-80% of my CPU (Intel(R) Core(TM)2 Duo CPU T7250 @ 2.00GHz) which seems pretty excessive.

Is there any way to decrease the CPU usage? The chroma thing didn't work for me.

What I **need** is a "no signal" image when the video stream is interrupted. Perhaphs there is another way to do it, more CPU-friendly?

--`Karol <User:Karol>`__ 12:45, 22 September 2009 (UTC)

General Update
--------------

So far I haven't been able to get anything on the `Mosaic <Mosaic>`__ page working for VLC 1.0.5 in Windows. I think I read somewhere that another method beside mosaic should be used to play multiple videos in VLC. Does anyone know what that method is? I think we need a general update of the mosaic wiki page. I volunteer to write it, but I have yet to get any mosaic stuff working with 1.0.5. What has changed that breaks the tutorials on this page? --`diafygi <User:Diafygi>`__ 19:39, 7 May 2010 (UTC)

Specific Reply
~~~~~~~~~~~~~~

After more failed attempts than I'm willing to admit to, I've finally gotten the mosaic working somewhat, though I'd be completely lost without the wizard. I've been having a problem with the stream terminating after the shortest video in the mosaic has finished playing. However, I do remember reading somewhere that as a Windows user, I'm not supposed to use the 'fake' command for my BG, but some other thing.

As far as another method, well, yeah, there's a super easy one that I had been using (and will probably continue to use), and it's dead simple. I use Windows7 x64 but I think most of these features have been around for a while, and there's probably a similar method on any OS. So ANYWAYS

1. Right click your desktop, click personalize, and make a tiny theme. I mean TINY. So like you go into window color --> advanced appearance settings, and anything that you can make smaller, make it smaller. With Aero still turned on I've managed to get my window borders so thin that I can barely click them to resize a window. Using non-Aero themes makes your title bars microscopic.

2. Ignoring the fact that you can barely see, let alone click the minimize/maximize/close buttons (who uses those anyway), Fire up a few instances of VLC and load some playlists. Then when you've got a nice, round number of videos playing (think FOUR for a 4:3 monitor, and SIX for a 16:9), right click your taskbar and select "show windows side by side". Make sure you don't have any other non-minimized windows running as they will gank spots from your "mosaic".

3. If you know your way around Windows Appearance settings, you should be looking at a grid of videos with a reasonably low amount of padding. If you're running a playlist with multiple video resolutions, make sure to set the video to scale itself to the player, and not the other way around.

Here's an example. http://i53.tinypic.com/2pytb0j.png On my left monitor I'm using the ThinWindows method. On my right monitor I've got the mosaic out of the wizard in the HTML interface. The gigantic left-side start menu is just there to keep everything 4:3 for the purpose of comparison. I figured that'd be easier than comparing a 4-vid wall to a 6-vid wall.

I find that the advantage here is that I have control over each video, which is good because I only stream things to myself. I've also been experimenting with the "--align #" tag at the end of a VLC shortcut in combination with Direct3D desktop mode, but honestly I'm getting better results from the "thin windows" method. The more advanced users of VLC may find this method severely lacking, though perhaps mildly entertaining.

P.S. If you're really a stickler for padding, you can pull the bottom of an upper window over the title bar of a lower window. But if you feel the urge to do that, you probably didn't make your title bars small enough.

P.P.S. - At risk of stating the obvious, don't forget to start up your player(s) in minimal view.
