.. raw:: mediawiki

   {{SoCProject|year=2010|student=[[User:salsaman|salsaman]]|mentor=Christophe Mutricy}}

**Week 1:**

**26th May 2010**

I started by porting and adapting the existing code from the LiVES ogg/theora decoder.

I made some updates to `ogg.c <http://lives.sourceforge.net/other_projects/vlc/ogg.c>`__ and added the new files `oggseek.c <http://lives.sourceforge.net/other_projects/vlc/oggseek.c>`__ and `oggseek.h <http://lives.sourceforge.net/other_projects/vlc/oggseek.h>`__. Some definitions from ogg.c were moved into the new file `ogg.h <http://lives.sourceforge.net/other_projects/vlc/ogg.h>`__ since they are now common to both ogg.c and oggseek.c. I also updated `Modules.am <http://lives.sourceforge.net/other_projects/vlc/Modules.am>`__ with the new files.

As a first test, I was able to correctly determine the total number of frames in various ogg/theora files:

| ``- seek to the last ogg page for a given stream (i.e. the theora stream)``
| ``- get the granulepos``
| ``- convert the granulepos to a frame number``
| ``- set the total number of frames``

As a result the demuxer can now return the file length in microseconds. This can be seen in the interface at the bottom. Previously this figure was an estimate, but now it is accurate.

As a second test, I was able to seek roughly to any given frame or time in a clip. Right now it is not frame accurate, so there are still some minor artifacts after seeking. I plan to fix this properly in the next couple of days.

One thing which was slightly unexpected - vlc may (?) start playback before all of the stream header data is read. This means that when getting the frame count, for very small files we may read back into the header data. I need to investigate if this is a problem or not - so far it has not caused any issues.

**27th May 2010**

Today I hit the first problem. In order to seek to an inter frame, we need to rewind to the previous intra frame and the pre-roll to the target. However, when vlc does a pre-roll it does so *at the normal frame rate*. This can be uncomfortable for the user because it could require a pre-roll of quite a few frames, so you can see the time slider moving at the bottom but there is no video or audio playing until the pre-roll catches up. What I would like to know, is there a way to tell the player "give me the next packet as quick as possible" ? Then it would zip through the pre-roll quickly and the user would not notice anything. I have emailed my mentor to ask this (since the player code is done outside of the demuxer).

Implementing pre-roll for theora meant a minor change to the `theora.c <http://lives.sourceforge.net/other_projects/vlc/theora.c>`__ codec file. This change should not impact any of the other demuxers.

**28th May 2010**

I will be changing ISP's today, so there may be some unavoidable disruption to my schedule.

Resolved the problem with slow pre-roll (thanks Fenrir !).

For future reference, use es_out_Control(), and send ES_OUT_SET_NEXT_DISPLAY_TIME to set the pre-roll target time.

ogg/theora is pretty much done now. I still need a clip with subtitles to test. There seems to be a strange problem with seeking in Kate files, it's not possible to seek to the middle of titles. Will take a look at this next week, but I think it is not an important issue.

**TODO:**

**This week:**

- seek to the exact frame required (i.e skip frames until we hit the target frame) - **done** (but see above)

- work out how to tell if we are dealing with a remote stream (which has no seek capabilities) - **done**

- check audio and subtitle sync after a seek - **done**

- test with more ogg/theora clips (including very small clips, see above) - postponed due to ISP change, OS upgrade and other issues - **done**

- clean up the code - **done** (but left some debug output in to help with the dirac seeking)

- see if we can pull/use more meta data from the stream (e.g. comments, codec version, aspect ratio, frame and picture size, x and y offsets) - **done** (no changes needed/possible)

**Week 2:**

``- look briefly into Kate issue, see if it is trivial to fix``

``- check with very small file and with captions``

``- look at meta data``

I plan to backport the updated code back in to LiVES, since I made a few corrections and improvements to the code. Split the LiVES code into demuxer/decoder - this will be necessary for the next part.

**31 May**

I had a look at the metadata, it seems that comments and so on are already read and included by the theora decoder. So no changes are needed here. It would be nice to show the codec version, but this seems not to be possible.

Regarding the Kate issue, for some reason now I discovered that Kate subtitles are not being read on my machine - vlc is complaining that it has no decoder for them ! I will look into this. I am testing with the Elephants Dream with subtitles clip - audio and video seek are working perfectly, so I would imagine that subtitles will be fine also.

The "kate issue" mentioned from last week actually seems to have nothing to do with Kate, in fact it seems to be peculiar to that one clip - vlc also has some strange timing issues with it.

**1 Jun**

OK, managed to test Kate (seems like I was missing the Kate libraries), and all seems OK. Got a bit sidetracked today by some urgent issues in LiVES, and an upgrade from ubuntu Karmic to Lucid.

**2 Jun**

All issues have been resolved now, apart from 1 item which came up during my testing. For clips with small number of frames, with few changes between frames (e.g. 10 blank frames), we are unable to find the keyframe. I believe this is due to the minumum size of the search domain (8500 bytes). The solution may be to keep reducing the search size until we find the keyframe. I will test this as part of the backporting into LiVES. Apart from this everything is working nicely for ogg/theora. I will have a first patch ready this week.

**3 Jun**

Preparing LiVES codebase for backport of code from vlc.

Sent first set of patches to vlc-devel.

Today was a holiday in Brazil, so I worked only half a day.

**4 Jun**

Some minor problems with the first patch were fixed, and it was checked and resubmitted.

I have now backported most of the updated code back into LiVES - except for some things to do with metadata.

**Week 3:**

Still todo:

- grab extra metadata in LiVES. - **postponed till later.**

- see if LiVES could use the decoder codecs from vlc - **still investigating**

- look into the 1 remaining oggseek issue - **still TODO, although I think I have an idea for solving it**

Investigate how seeking works with dirac video streams (it is slightly different to theora in that there is a lower bound, but no upper bound). Test implementation of this in LiVES first.

**7 Jun**

Worked on some formatting issues to do with the patch I submitted last week.

**8 Jun**

Working on some more formatting issues to do with the patch.

**9 Jun**

I hope the patch is OK now, I think I covered all of the issues mentioned in feedback.

Here is a brief explanation of how the seeking works:

*We create an index on the fly, this index is basically:* *offset in file -> maximum frame number*

*When asked to seek to a particular frame, we first check the index to see if we have approximate boundaries for the seek, otherwise we will seek in the whole file, from data_start until the end.*

*The area to be searched is divided into two halves. We first check the upper half, and get the highest and lowest granulepos. (The granulepos is basically keyframe \* keyframe_offset + frame offset). If our target frame lies in this region we subdivide it into two halves, otherwise we check the lower half from earlier. We stop when we have found the keyframe for our target frame, or the search region is < minimum_page_size.*

*What we are aiming to find on this first pass, is the highest keyframe (sync point) which is <= target frame.*

*Once we have found this, we need to rewind a bit further, because the ogg container only discloses where a frame ends, not where it begins. So we do a second pass and find the highest granulepos < target granulepos from the last step. We begin decoding from here, ignoring any frames which are output on this first page. We then start counting down until we reach the target frame.*

*As we discover keyframes (sync points) these are added to the index. Also, if we discover a higher frame number which is based on the same keyframe we update our index. Additionally, during normal playback the index is updated with keyframes as we play them.*

*If the codec/demuxer is installed and working properly you can see this in operation - the first seek takes a noticable fraction of a second, subsequent seeks become increasingly faster as the keyframe -> highest frame index is built up.*

*I believe this is the most efficient way of seeking in ogg (at least for theora - and probably for dirac; although dirac seems a little different in that there is a lower bound but no upper bound for dirac, and according to the dirac spec the granulepos shows the first frame decoded on a page rather than the last frame).*

*There is currently one known issue, which is if the entire file is < min_page_size, we never find any keyframes. I am working on a fix for this, I believe the solution in this case is simply to divide the min_page_size by 2 until we get a keyframe produced.*

Also, one issue which I suggested on the vlc-devel mailing list:

*I would like to propose a new flag for the stream:*

**STREAM_CAN_EXACTSEEK**

*- the proposed meaning of this flag is that within the stream one can seek exactly to any given frame without artifacts in the frame. This flag must be settable by the demuxer plugin, and is not fixed - for example you could have a container with two video streams one after the other, the first could set this flag and the second (using a different codec) could be not seekable.*

*Rationale:* *I understand that you are creating libvlc with the intention of this being used for video editing applications. I know from my own experience with LiVES that such applications require demuxers which can deliver the exact frame requested, so generally one would need to look at STREAM_CAN_EXACTSEEK \| STREAM_CAN_FASTSEEK to see if the stream is immediately usable or requires further processing (caching, indexing, etc).*

Just for fun today I started creating an avformat demuxer for LiVES based on the vlc avformat demuxer.

**10 Jun**

I played around a bit more with the avformat demuxer in LiVES to see if any of the code would be useful for the ogg demuxer, but I found it is totally unsuitable for serious video editing. Quite often it gives the wrong frame rate (1000 fps) and it is pretty much useless for seeking. The seek function doesn't even attempt to find a keyframe, and the display_picture_number is always 0. The only things it seems to get right every time are the frame size and pixel format, and the audio format.

**11 Jun**

Returning to the main part of the work, I started implementing a dirac decoder in the LiVES ogg demuxer. I think I understand pretty much how decoding works in libschroedinger now. The seek method which I am using will need some updating for sure. For theora, each pair of keyframe + frame translates to a unique granulepos, but for dirac there is no unique mapping of frame -> granulepos. I will need to adjust the seek functions to avoid any such frame -> granulepos mappings.

I noticed one error in the current vlc ogg demuxer relating to dirac. The demuxer assumes that there is a gap of 2 between granulepos of one frame and the next. However, this is only true for non-interlaced frames, for interlaced frames the gap is 1. So I intend to correct this in the vlc code.

**13 Jun**

Spent waaaay too long this weekend trying to debug the schroedinger code which I added to LiVES. Finally got it working and decoding frames (yay !), although random seeking is not yet functioning.

**Week 4:**

Continue work from week 3, and begin porting dirac code from LiVES to vlc.

Still TODO:

- complete the dirac decoding work in the LiVES ogg demuxer - **decoding is working, seeking is in progress.**

- port any updates into the vlc ogg demuxer

- fix remaining oggseek theora issue

**15 Jun**

After some experimentation with dirac sequence start and finding sync points I now have most of the dirac seek algorithm down in code in LiVES. I added a new field to the demux_index_entry (pagepos_end), and this will be used to scan regions within the ogg cointainer to search for sync points.

Note that the ogg granulepos for dirac streams does not work as it is supposed to. It appears also that nobody answers questions on the schroedinger developers mailing list.

**16 Jun**

Work is progressing steadily on seeking in dirac. I am now able to find first and last sync frames for any given region, and update the internal index. Some improvments to seeking generally were mentioned on the vlc-devel mailing list (targetting the bi-section search). I will look at building this in after the dirac seeking is done.

**17 Jun**

Continuing with my dirac investigations in LiVES. After a frustrating day of debugging dirac searching (amongst other things I was accidentally cutting the end off some packets), I now have seeking working to frame accuracy (although not yet fully optimised). I am also able to play back the test video (720x576) at around 30 fps on a moderately loaded AMD64 2.2GHz.

**18 Jun**

I have discovered one insurmountable problem with seeking in Dirac.

The problem is that any particular frame can reference one or two earlier frames, and each of these frames in turn can also reference earlier frames, and so on.

In fact in the dirac documentation it recommends seeking from the first frame and decoding only reference frames until the target frame is reached. However doing it this way can cause a delay of several seconds (or even longer for large files) to reach higher frame numbers.

This can be almost worked around by selecting a point far enough back and then decoding from that point forwards, however there will always be some information lost this way.

As I see it there are 2 options:

- implement a reasonably fast seek, but accept that there may be a loss of quality in the images

- implement a very slow seek but with perfect quality

For now I will continue with the first option.

**Week 5**

Continue with dirac seeking and other issues...

**23 Jun**

Ogg/dirac seeking is now working in LiVES. The code just needs cleaning up a little and I can start porting it to vlc. I have managed to remove anything dependant on bitrate or filesize, so this should also fix seeking in very small files mentioned above.

**24 Jun**

Today was a public holiday in Brazil.

**25 Jun**

Still working on some minor code corrections. Frame count for very small ogg (and maybe dirac) files is still broken; the last granulepos is not being found.

**Update**: I can now get the last granulepos (and hence number of frames) for even the smallest of files. Unfortunately this caused some breakage elsewhere, so I will have to do a bit of debugging.

**Week 6**

**TODO**: finish debugging regression, port code into vlc.

**29 Jun**

Today I began backporting the new search code frome LiVES back into vlc.

**1 Jul**

OK, I am almost done with porting the dirac seeking code into vlc. However there is one big problem - when the decoder decodes a frame it needs to pass the frame number back to the demuxer. However there seems to be no mechanism for doing this. My first idea was to set a dummy block as the block->p_next and have the decoder set the i_pts field for this, however this does not work as vlc tries to parse block->p_next as an actual block and frees it.

*For now I cannot continue any further with this part of the project (dirac seeking).*

**2 Jul**

I have submitted a patch with everything I have done so far. The patch suffers from the p_next problem noted yesterday and will crash in block_fifoEmpty. This seems to be an error in vlc, as I have set the free function, block->pf_free to a function which does nothing.

This behaviour can be avoided by uncommenting #define DISABLE_DIRAC_SEEK in ogg.h, which will revert to the old style of handling dirac.

**Weeks 7 & 8**

**14 Jul** I have been spending the last few days reviewing my work so far (thanks to some feedback from mentors). At their suggestion I have been working on splitting all my contributions into 4 patches:

- non-seek related logic and code refactoring - seek logic changes - theora seek capability - dirac seek capability

These patches can then be applied in sequence. I have completed a first pass of this, now I need to tweak the patches a little.

Summary

**9th August** Most of the rest of the time has been spent transforming my updates into a sequence of patches (9 in all), and testing the results.

There are still a couple of outstanding issues to be resolved:

a) The function to get the length (time) of a clip has been implemented in ogg.c. If there is a theora or dirac video stream present then the precise video duration will be returned. If neither of these streams are present then VLC_EGENERIC is returned.

It seems that enabling this function and returning VLC_EGENERIC causes a regression whereby the estimated duration is no longer set.

There are two parts to fixing this: 1) vlc itself needs to check for VLC_EGENERIC returned from DEMUX_GET_LENGTH and do whatever calculation it was doing previously when this function was not implemented.

2) due to an oversight on my part I had not considered audio only ogg/vorbis files. For these files there is a method to get an accurate length. I have agreed with the vlc team to implement this after the end of the GSOC project (probably as an update in september).

b) seeking in dirac still requires communcation of timestamps between demuxer and codec. It may not be optimal to implement this since it creates a strong coupling between the demuxer and decoder plugin. However if such a shared data scheme is implemented then ogg/dirac seeking can be properly performed. I have given an example implementation of this using block->next, but there may be better solutions to be devised.

``c) VLC_CAN_EXACTSEEK flag for stream would be nice (see above).``

.. raw:: mediawiki

   {{GSoC}}
