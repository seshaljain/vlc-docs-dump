.. raw:: mediawiki

   {{Lowercase}}

.. raw:: mediawiki

   {{Back to|Category:x264}}

This is an archive of the x264 Development Newsletters.

Volume 1
--------

*9/18/2010*

From now on, with each weekly-ish push of new patches, I'll try to post a newsletter as well to give an update of what's going on and the changes.

Fixes:
''''''

Different versions of 64-bit MinGW gcc were inconsistent with regards to whether or not to add a \_ prefix to called functions. This broke compilation because the assembly code wouldn't link in correctly.

Intra refresh got a lot of fixes thanks to bug reports by Chris Brien <chris.brien@tandberg.com>. Because x264 uses column refresh instead of row refresh, it has to be more careful with regards to which pixels it can predict from. This should fix some cases where intra refresh didn't refresh the whole frame correctly. Furthermore, it turns out that the recovery_frame_cnt syntax element, signaling the length of the intra refresh, is limited by the max frame number. Accordingly, x264 will raise the max frame number to ensure that recovery_frame_cnt is in spec.

Improvements:
'''''''''''''

I've gone through the file headers and updated them to be more accurate and consistent in terms of dates and authorship. It now also mentions the commercial license, on request from a licensee.

The new --disable-gpl configure option is now added for companies using the commercial license. x264 --version will print both the license information of itself and of the linked libavformat (for decoding). It'll also warn you if the combination you've put together isn't distributable, such as a nonfree ffmpeg + GPL x264, or a GPL ffmpeg + non-GPL x264.

x264 now passes the "full chroma input" flag to swscale. This should fix this quality issue when using point scaling: http://doom10.org/index.php?topic=585.0 .

New features:
'''''''''''''

Kieran Kunhya <kieran@kunhya.com> has finally committed his arbitrary SEI patch, which lets calling apps give x264 any SEI they want to include in the stream. This is useful for closed-captioning, frame packing, and all kinds of other SEIs that x264 doesn't explicitly support but which the calling application can create itself if necessary. The advantage of giving these to x264 instead of just inserting them separately is that it allows the resulting stream to remain HRD-compliant, since x264 knows they exist.

Upcoming:
'''''''''

High bit-depth input and filtering! x264 supports 10-bit encoding, but currently only takes 8-bit input. This change will finally create a stable API for high bit-depth input and allow users to filter in higher precision. It will also add dithering support to x264CLI for downconversion of high-bit-depth material.

HQDN3D (denoiser) and YADIF (deinterlacer) will be making their way into the x264CLI filter framework.

Chroma ME in B-frames will be coming soon, giving an extra bit of compression to those using slower presets.

Adaptive MBAFF development is coming along, with B-frames being finished up currently.

After high bit-depth input is complete, a large amount of assembly code will be committed as well, improving high bit-depth encoding performance greatly.

Ubuntu Maverick will include an updated x264, r1653.

`Volume 2 <http://mailman.videolan.org/pipermail/x264-devel/2010-September/007808.html>`__
------------------------------------------------------------------------------------------

*9/27/2010*

This is the second x264 development newsletter. If you missed the first one, this is a regular email containing updates on fixes and improvements in the most recent x264 push, along with updates on what's coming next.

.. _fixes-1:

Fixes:
''''''

libx264 should now give correct DTS and print the correct bitrate if the input PTS do not start at zero. This doesn't affect x264CLI, but does affect calling apps that don't start their PTS at zero.

libx264 ratecontrol should now work correctly in CFR mode with timebase != 1/fps. As documented, x264 was supposed to ignore the timebase if CFR mode is set (for purposes of ratecontrol), but that's not what actually happened; things just broke. This should now be fixed. This is necessary for correct behavior with tune=zerolatency in gstreamer.

A missing emms has been added to dump-yuv, fixing some Heisenbug brokenness when dump-yuv was used.

.. _improvements-1:

Improvements:
'''''''''''''

Slice-max-size has been made more aggressive. Previously we just made some blind assumptions about the distribution of escape bytes and other such inaccuracies -- now it should work absolutely. It accounts for a few extra bytes that are highly predictable (CABAC's extra byte, CAVLC's skip runs). The primary problem, however, was caused by the terrible design of H.264's CABAC, which outputs a string of zeroes if CABAC is perfectly adapted, thus forcing tons of escape bytes for any perfectly uniform image. Slice-max-size should be fixed in this case.

Chroma mode decision and subpel, mentioned in the last newsletter, is finally in. It's enabled at subme >= 9 and provides a ~0.4-1% compression improvement.

.. _new-features-1:

New features:
'''''''''''''

High-bit-depth support has been finished in libx264 and x264cli. The assembly code is still yet to be committed, so it's a bit slow, but libx264 now supports high-bit-depth input. Additionally, the filter framework now supports 16-bit, which will be useful for future filters to avoid rounding error and banding. It'll automatically perform dither to go down from 16-bit to 8, 9, or 10-bit, thus making this useful for 8-bit encoding as well.

High 10 Intra profile is supported now, which makes x264 now capable of encoding AVC Intra 50. See the commit message for a sample commandline.

.. _upcoming-1:

Upcoming:
'''''''''

High bit depth assembly code is coming soon, which should give a nice (3x+) improvement to high bit depth encoding speed.

HQDN3D (denoiser) and YADIF (deinterlacer) will be making their way into the x264CLI filter framework. This was previously being blocked by the high-bit-depth modifications to the filter framework.

Adaptive MBAFF development is coming along, with B-frames being finished up currently.

`Volume 3 <http://mailman.videolan.org/pipermail/x264-devel/2010-October/007858.html>`__
----------------------------------------------------------------------------------------

*10/10/2010*

This is the third x264 development newsletter. If you missed the first two, this is a regular email containing updates on fixes and improvements in the most recent x264 push, along with updates on what's coming next.

.. _fixes-2:

Fixes:
''''''

The sigint handler in x264cli is now volatile, like it should have been. This likely didn't actually affect anything on any real system, but it's more correct.

-DNDEBUG broke the filtering system. This is now fixed.

The bugfix from last week regarding intra refresh predicting from topright blocks didn't work with 8x8dct. This is now fixed.

2-pass ratecontrol now works with CBR HRD. Previously, it ignored filler bits, and thus broke horribly. In general, you don't need 2-pass for CBR (and it probably doesn't help), but it should work better now.

A missing mod4-stack check was added; this should fix ICC builds on Phenom CPUs.

.. _improvements-2:

Improvements:
'''''''''''''

The build tree has been cleaned a bit. A bunch of old stuff, like the non-working regression test and doxy, have been removed.

Some of the information in doc/ has been updated to be less absurdly out of date, or at least inform the reader that it is absurdly out of date.

DTS compression has been moved out of the libx264 API and into the muxers, because it's a giant hack and it was making things ugly and messy (and starting to interfere with ratecontrol).

Various asm functions have been improved, particularly the qpel MC functions. Should help performance a bit on Core 2 and similar CPUs.

.. _upcoming-2:

Upcoming:
'''''''''

High bit depth assembly code is coming soon, which should give a nice (3x+) improvement to high bit depth encoding speed.

HQDN3D (denoiser) and YADIF (deinterlacer) will be making their way into the x264CLI filter framework. This was previously being blocked by the high-bit-depth modifications to the filter framework.

Adaptive MBAFF development is coming along, with B-frames being finished up currently.

x262 is under development: a best-in-class MPEG-2 encoder built using the x264 framework.

`Volume 4 <http://mailman.videolan.org/pipermail/x264-devel/2010-November/007920.html>`__
-----------------------------------------------------------------------------------------

*11/10/2010*

This is the fourth x264 development newsletter. If you missed the first three, this is a regular email containing updates on fixes and improvements in the most recent x264 push, along with updates on what's coming next. Previous versions can be found in the mailing list archives.

.. _fixes-3:

Fixes:
''''''

The Altivec SATD gave wrong results with very small strides (e.g. 8). This made output on PPC slightly different from x86, due to different results in lookahead and chroma ME. This is now fixed.

FPS reporting on Windows 64-bit was very imprecise (the timers were only accurate to 1 second). This was due to \_ftime using the wrong struct due to the Windows ABI's complete retardation. This has been fixed by using ftime instead.

ssd_nv12 has been improved to eliminate overflow at high bit depths (this would, in theory, give wrong PSNR).

SATD/SA8D/Hadamard_ac have been improved to eliminate overflow at high bit depths (this would cause wrong analysis results).

Three ratecontrol bugs have been fixed:

#. B-frame size prediction has been fixed (it used quantizer instead of linearized qscale). This should improve VBV.
#. Overflow compensation, originally designed for 1-pass ABR, has been disabled with CRF on, as it doesn't do anything useful with pure CRF and causes very bizarre results with CRF+VBV in areas of extremely high complexity.
#. A bug in the way that clip_qscale caps the amount by which a frame can be higher quality than a previous frame (as a result of attempting to use up extra bits that would otherwise be wasted) has been fixed. This caused CBR to take extremely long times (e.g. seconds) to recover from extreme changes in complexity at low bitrates.

A possible linking problem with lavf has been fixed.

Some MV/ref prefetching code was in the wrong place. Fixing this may result in a tiny performance improvement.

.. _improvements-3:

Improvements:
'''''''''''''

doc/threads.txt has been updated with modern benchmarks. This information may be useful to anyone looking to compare the impact of various threading strategies on quality and performance, as well as get an idea of how well x264 scales over multiple cores at various encoding speeds.

| The presets are now addressable numerically (0=ultrafast...9=placebo).
| The exact mappings may change in the future if new presets are added or old presets removed, but they will always be in linear order of fast to slow.

The ffmpeg -vpre error message (if a user doesn't use a -vpre) has been made more descriptive, to better instruct users about how the ffmpeg -vpre system works.

weightp -1 offset dupes are now disabled in high bit depth mode, as they're a hack to get around crappy rounding in 8-bit encoding, and thus don't help in high bit depth.

PSNR and SSIM measurements are now VFR-aware! This means they will take into account the duration of frames. This may result in PSNR and SSIM results appearing dramatically different from other tools when used on variable framerate video. Don't fret; x264 is correct, they are not. Of course, results will stay the same for constant framerate video. This is the first step to VFR-aware MB-tree.

| Quantizer handling has been improved.
| Library change: i_qpplus1 now defaults to X264_QP_AUTO. This doesn't actually change anything, as X264_QP_AUTO is 0, but this may change in the future. As a reminder, all x264_picture_t structs must be initialized using x264_picture_init or x264_picture_alloc!
| CRF values now make sense in high bit depth: --crf 23 means roughly the same quality in 8-bit or 10-bit, instead of being 4 times higher quality in 10-bit than in 8-bit.
| This means that --qp 0 should be used for lossless, not --crf 0. The latter will not result in lossless compression when in high bit depth mode.
| Bit depth has been added to statsfiles, to prevent users from inadvertently using a statsfile with the wrong bit depth.

Scenecut's flash detection has been improved to work more sanely in the case of flashes at the end of the videos.

.. _upcoming-3:

Upcoming:
'''''''''

High bit depth assembly code is nearly ready. Speed boost has been measured as about 4.3x and is still improving.

VBV Emergency Mode is finally completed, with just fine-tuning and bugfixing left. This makes x264 able to deal gracefully with extreme input combined with VBV restrictions (e.g. noise, Doremi Labs test boxes). This is critical for some broadcast applications. Unlike most competing encoders, this VBV Emergency Mode does not drop frames or force all blocks to skip or some similarly extreme step: it adds a "denoising" step to reduce the complexity of the video, which scales upwards until it simply removes all content at the most extreme level.

A pad filter is nearly ready for the x264CLI filter framework.

HQDN3D (denoiser) and YADIF (deinterlacer) will be making their way into the x264CLI filter framework.

Adaptive MBAFF development is coming along, with B-frames being finished up currently.

x262 is under development: a best-in-class MPEG-2 encoder built using the x264 framework. Basic structure is done, with intra coding mostly finished.

Work is planned to integrate x264 with the Sandy Bridge's encoding ASIC for improved encoding performance. Current status is: waiting on Intel.

`Volume 5 <http://mailman.videolan.org/pipermail/x264-devel/2010-November/007950.html>`__
-----------------------------------------------------------------------------------------

*11/19/2010*

This is the fifth x264 development newsletter. If you missed the first four, this is a regular email containing updates on fixes and improvements in the most recent x264 push, along with updates on what's coming next. Previous versions can be found in the mailing list archives.

Note that we pushed a bugfix release this time around, so this newsletter includes fixes from those commits as well, i.e. it covers everything since the last newsletter.

.. _fixes-4:

Fixes:
''''''

HRD now works correctly when used with intra refresh. Thanks to a certain x264 commercial licensee for the bug report.

QPfile parsing now works as it was supposed to have worked last time: users should be able to omit QP values.

Allocate the correct amount of memory for weightp buffers with weightp + high bit depth (it allocated too much, not too little).

Fix flash detection to work correctly near the end of the keyframe interval.

Fix a crash in dump yuv with some resolutions.

Various fixes have been made to ratecontrol in high-bit-depth mode.

Constrained intra pred is working properly again in all cases.

.. _improvements-4:

Improvements:
'''''''''''''

x264's SEI header now indicates whether the build used was GPL or proprietary.

x264 is now compatible with FFMS2's most recent API break.

configure now logs test programs that failed, not just the error output.

Merge Oskar's (irock's) 10-bit asm branch: ~4.4x overall speed boost in high bit depth mode.

Chroma weighted prediction: dramatically improved chroma compression and quality in fades.

Custom cropping rectangle support: users can now specify --crop-rect to add values to the H.264 cropping header. This is supposedly useful for 3D television applications (to allow legacy decoders to access only one view of the image).

.. _upcoming-4:

Upcoming:
'''''''''

VBV Emergency Mode is finally completed, with just fine-tuning and bugfixing left. This makes x264 able to deal gracefully with extreme input combined with VBV restrictions (e.g. noise, Doremi Labs test boxes). This is important for some broadcast applications.

The pad filter and yadif are nearly ready for the x264CLI filter framework. Both now support high bit depth.

Adaptive MBAFF development is coming along, with B-frames being finished up currently.

x262 is under development: a best-in-class MPEG-2 encoder built using the x264 framework. Basic structure is done, with intra coding finished and inter coding begun.

Work is planned to integrate x264 with the Sandy Bridge's encoding ASIC for improved encoding performance. Current status is: waiting on Intel (these guys move at the speed of a three-toed sloth swimming down a river of bricks).

Other news:
'''''''''''

Since we started a couple of months ago, over 40 companies have contacted us regarding x264 licensing!

At least one major Blu-ray authoring house is switching to x264 for their commercial Blu-rays.

At least one commercial encoding application based on x264 is currently in the works. An announcement will come Soon™.

`Volume 6 <http://mailman.videolan.org/pipermail/x264-devel/2010-November/008003.html>`__
-----------------------------------------------------------------------------------------

*11/25/2010*

This is the sixth x264 development newsletter. If you missed the first five, this is a regular email containing updates on fixes and improvements in the most recent x264 push, along with updates on what's coming next. Previous versions can be found in the mailing list archives.

Note that we pushed a bugfix release this time around, so this newsletter includes fixes from those commits as well, i.e. it covers everything since the last newsletter.

.. _fixes-5:

Fixes:
''''''

Fix some crashes in high bit depth on some compilers due to insufficient array alignment.

Fix a bug in chroma weightp which could cause corruption in rare cases.

Fix some weird issues in the resize filter's rounding code.

Fix the build on SPARC Solaris 10 machines.

Fix high bit depth mode on SPARC.

Fix an odd issue in VFR input + forced timebase.

.. _improvements-5:

Improvements:
'''''''''''''

QPmin default is now 0.

x264 --version now prints a lot more useful information.

x264_encoder_reconfig now copies field order flags.

There's a new API function to return the maximum number of delayed frames with the current parameters (requested by Gstreamer).

| Google Code-In is in full swing, with two sets of patches committed:
| SSE versions of some high-bit-depth (i)DCT functions
| x264 now has a totally sweet Python regression test tool.
| --weightp 1 is now a better speed tradeoff. It also doesn't do any reference duplication, so it's suitable when encoding for broken decoders that don't handle reference duplication correctly (while still getting the benefits of fade detection).

.. _upcoming-5:

Upcoming:
'''''''''

VBV Emergency Mode is finally completed, with just fine-tuning and bugfixing left. This makes x264 able to deal gracefully with extreme input combined with VBV restrictions (e.g. noise, Doremi Labs test boxes). This is important for some broadcast applications.

Adaptive MBAFF development is coming along, with B-frames being finished up currently.

x262 is under development: a best-in-class MPEG-2 encoder built using the x264 framework. Basic structure is done, with intra coding finished and inter coding begun.

Work is planned to integrate x264 with the Sandy Bridge's encoding ASIC for improved encoding performance. Current status is: waiting on Intel (these guys move at the speed of a three-toed sloth swimming down a river of bricks).

.. _other-news-1:

Other news:
'''''''''''

[STRIKEOUT:A commercial encoding application based on x264 is currently in the works. An announcement will come this week.]

This week? Perhaps I should have said "today"!

Pegasys Inc. switches to x264 for their flagship product, TMPGEnc.

English: http://tmpgenc.pegasys-inc.com/en/press/10_1125.html

日本語: http://tmpgenc.pegasys-inc.com/ja/press/10_1126.html

`Volume 7 <http://mailman.videolan.org/pipermail/x264-devel/2010-December/008041.html>`__
-----------------------------------------------------------------------------------------

*12/07/2010*

This is the seventh x264 development newsletter. If you missed the first six, this is a regular email containing updates on fixes and improvements in the most recent x264 push, along with updates on what's coming next. Previous versions can be found in the mailing list archives.

.. _fixes-6:

Fixes:
''''''

Fix SPARC and Solaris building (really this time!)

Three timecode input fixes: for nonzero starting pts, for a corner case in auto timebase generation, and fixing a spurious error in case of a frame read error.

Actually fix fittobox resizing code.

Fix incorrect handling of some pixfmts with non-mod2 resolutions in the resize filter.

Fix a file handle leak in libx264 with certain file reading errors in statsfile handling.

Fix intra refresh's quality masking: the ipratio wasn't correctly applied in threaded mode.

Fix an overflow in fdct asm in 10-bit builds.

.. _improvements-6:

Improvements:
'''''''''''''

Automatically restrict QPs to avoid quantization (under|over)flow, so you don't have to. Will error out if this, combined with insane user constraints, makes encoding impossible. This makes fprofiling work out of the box again.

Use the Avisynth 2.6 API to detect Avisynth initialization failure and print the associated error (only available in Avisynth 2.6 alphas; doesn't affect older versions).

Install an x264_config.h containing information about how x264 was configured. This will allow ffmpeg to link with commercially licensed copies of libx264 without --enable-gpl.

Massive amounts of high bit depth assembly code from Google Code-In (about two dozen functions).

.. _upcoming-6:

Upcoming:
'''''''''

--device and automatic --level restriction support is in the works, as part of Google Code-In.

A per-option help system is in the works, as part of Google Code-In.

VBV Emergency Mode is finally completed, with just fine-tuning and bugfixing left. This makes x264 able to deal gracefully with extreme input combined with VBV restrictions (e.g. noise, Doremi Labs test boxes). This is important for some broadcast applications.

Adaptive MBAFF development is coming along, with B-frames being finished up currently.

x262 is under development: a best-in-class MPEG-2 encoder built using the x264 framework. Basic structure is done, with intra coding finished and inter coding begun.

Work is planned to integrate x264 with the Sandy Bridge's encoding ASIC for improved encoding performance. Current status is: waiting on Intel (these guys move at the speed of a three-toed sloth swimming down a river of bricks).

`Volume 8 <http://mailman.videolan.org/pipermail/x264-devel/2010-December/008070.html>`__
-----------------------------------------------------------------------------------------

*12/15/2010*

This is the eighth x264 development newsletter. If you missed the first seven, this is a regular email containing updates on fixes and improvements in the most recent x264 push, along with updates on what's coming next. Previous versions can be found in the mailing list archives.

.. _fixes-7:

Fixes:
''''''

Weightp analysis now calculates offsets correctly in high bit depth mode.

High bit depth intra pred x86 asm functions are now fixed (and thus re-enabled).

That nasty gnu ld alignment bug on windows (ld refuses to align .bss to 16 bytes even when asked nicely) has been squashed with -fno-zero-initialized-in-bss.

.. _improvements-7:

Improvements:
'''''''''''''

.gitignore is now even more useful than before.

Another bit of memory saved in high bit depth weightp.

The regression test script now tests interlaced compression.

8x8dct is now allowed with cavlc+lossless and subme>=6, for a slight compression improvement.

Frame-packing SEI support is now in, for official 3D support in x264.

A metric crapload of new high bit depth asm functions are now in (thanks, Google Code-In!)

x264 now supports Windows threads in addition to pthreads. Thanks to Pegasys Inc. for the original patch.

.. _upcoming-7:

Upcoming:
'''''''''

--device and automatic --level restriction support is in the works, as part of Google Code-In.

A per-option help system is in the works, as part of Google Code-In.

VBV Emergency Mode is finally completed, with just fine-tuning and bugfixing left. This makes x264 able to deal gracefully with extreme input combined with VBV restrictions (e.g. noise, Doremi Labs test boxes). This is important for some broadcast applications.

Adaptive MBAFF development is coming along, with B-frames being finished up currently.

x262 is under development: a best-in-class MPEG-2 encoder built using the x264 framework. Basic structure is done, with intra coding finished and inter coding begun.

Work is planned to integrate x264 with the Sandy Bridge's encoding ASIC for improved encoding performance. Current status is: waiting on Intel (these guys move at the speed of a paraplegic three-toed sloth swimming down a frozen river of bricks).

`Volume 9 <http://mailman.videolan.org/pipermail/x264-devel/2011-January/008132.html>`__
----------------------------------------------------------------------------------------

*01/10/11*

This is the ninth x264 development newsletter. If you missed the first eight, this is a regular email containing updates on fixes and improvements in the most recent x264 push, along with updates on what's coming next. Previous versions can be found in the mailing list archives.

.. _fixes-8:

Fixes:
''''''

The win32 alignment crash issue is actually fixed now. Apparently gcc doesn't work right unless you initialize zero arrays explicitly.

High bit depth now compiles with --disable-asm properly again.

| SATD predictors with high bit depth work properly with --no-mbtree on.
| \*Bug resulted in bizarre/wrong bitrates in CRF mode with --no-mbtree.

The lavf demuxer no longer memory leaks like crazy on inputs with multiple video streams.

Some overflows in VFR ratecontrol with extreme timebases have been fixed. These affected some actual videos.

SSIM now works properly in 10-bit.

A bug with negative costs that caused assertions on some videos in high bit depth mode has been fixed.

YV12 now works correctly in the resize filter (there was an issue with swapped chroma planes).

The endianness test and as test in configure now work properly in cross-compile mode.

Weightp no longer prints random extra linebreaks to the statsfile.

A few minor improvements have been made to the parameter SEI.

.. _improvements-8:

Improvements:
'''''''''''''

Some incorrect GCC uninitialized variable warnings have been shut up.

Metric craptons of high bit depth assembly have been added, for significant performance improvements. Thanks to Google Code-In (now over) and our students for their enormous amount of work, particularly Daniel Kang.

Also a few improvements in 8-bit assembly functions as well.

Check an extra offset in weightp analysis, for improved compression on fades with --weightp 1 (and slightly, but much less, improved with weightp 2).

Improve reference ordering in 3D frame-interleaved mode.

VFR-aware ratecontrol: MB-tree and non-MB-tree ratecontrol will now be aware of how long frames last. This results in greatly improved quality in VFR video, particularly dedup'd anime and similar content. It is now even MORE important that calling applications give x264 correct timestamps! Note this also affects the definition of CRF; higher framerate videos will get lower quality at the same CRF, which should improve how well CRF measures quality (as compared to the human brain itself).

.. _upcoming-8:

Upcoming:
'''''''''

--device and automatic --level restriction support is in the works, as part of Google Code-In. The patch is done, but needs review.

| A per-option help system is in the works, as part of Google Code-In.
| The patch is done, but needs editing of the help entries.

VBV Emergency Mode is finally completed, with just fine-tuning and bugfixing left. This makes x264 able to deal gracefully with extreme input combined with VBV restrictions (e.g. noise, Doremi Labs test boxes). This is important for some broadcast applications. This was delayed due to Google Code-In.

Adaptive MBAFF development is coming along, with B-frames being finished up currently.

x262 is under development: a best-in-class MPEG-2 encoder built using the x264 framework. Basic structure is done, with intra coding finished and inter coding begun.

Work is planned to integrate x264 with the Sandy Bridge's encoding ASIC for improved encoding performance. Current status is: waiting on Intel (these guys move at the speed of a paraplegic three-toed sloth swimming down a frozen river of bricks while chained to an osmium anchor).

`Volume 10 <http://mailman.videolan.org/pipermail/x264-devel/2011-January/008192.html>`__
-----------------------------------------------------------------------------------------

*01/26/2010*

This is the tenth x264 development newsletter. If you missed the first nine, this is a regular email containing updates on fixes and improvements in the most recent x264 push, along with updates on what's coming next. Previous versions can be found in the mailing list archives.

.. _fixes-9:

Fixes:
''''''

Some asm fixes to high bit depth: fix cases where SSE2-only instructions were used in MMX functions (caused SIGILL on old CPUs).

Fix the cacheline check in cache32 avg2 code (minor speed improvement on some old CPUs).

Fix CPU detection on Windows systems with >= 64 CPUs. x264 still doesn't use more than one processor group (it really doesn't need to), but at least it'll work now.

Fix reconfiguration of b_tff: make changing field order during encoding work properly. Required for ffmpeg to signal TFF/BFF, since ffmpeg's TFF/BFF is signaled per-frame instead of per-stream.

Fix cases where x264_encoder_encode failures (due to malloc failure) could cause x264_encoder_close to crash.

Write the 3D frame packing SEI values more correctly (thanks to Nero for the bug report).

.. _improvements-9:

Improvements:
'''''''''''''

Bump all the dates to 2011.

Add some missing values to the non-extended SAR table.

Improve the regression test script to not break with really complex commandlines on OSs with limited filename length, as well as correctly return to the original branch the user is on after testing.

Add an --input-fmt option to serve the same purpose of -f in ffmpeg; useful for cases where ffmpeg can't successfully probe the format of the input file.

Double the base framerate of frame-sequential 3D files; a "60fps" frame-sequential 3D file is really only 30fps.

Add AVX support to x264's assembly abstraction layer as well as one example function: still needs the actual AVX code to be written, but x264 can now take advantage of 3-operand instructions.

VBV Emergency Mode is finally completed. This makes x264 able to deal gracefully with extreme input combined with VBV restrictions (e.g. noise, Doremi Labs test boxes). This is important for some broadcast applications.

.. _upcoming-9:

Upcoming:
'''''''''

--device and automatic --level restriction support is in the works, as part of Google Code-In. The patch is done, but needs review.

| A per-option help system is in the works, as part of Google Code-In.
| The patch is done, but needs editing of the help entries.

Adaptive MBAFF development is actually coming along for once this time.

x262 is under development: a best-in-class MPEG-2 encoder built using the x264 framework. Basic structure is done, with intra coding finished and inter coding begun.

Work is planned to integrate x264 with the Sandy Bridge's encoding ASIC for improved encoding performance. Current status is: waiting on Intel (these guys move at the speed of a paraplegic three-toed sloth swimming down a river of frozen helium while chained to an osmium anchor stuck inside a black hole).

`Volume 11 <http://mailman.videolan.org/pipermail/x264-devel/2011-February/008251.html>`__
------------------------------------------------------------------------------------------

*02/06/2011*

This is the eleventh x264 development newsletter. If you missed the first nine, this is a regular email containing updates on fixes and improvements in the most recent x264 push, along with updates on what's coming next. Previous versions can be found in the mailing list archives.

.. _fixes-10:

Fixes:
''''''

Fix various regressions introduced in VBV emergency.

Fix AVX detection on OSs that don't support AVX.

Fix a crash on Phenom that could occur with the lookahead disabled and a calling application that tweaks the SSE control flags.

Fix a divide-by-zero crash in the MKV/FLV muxers that could occur if encoder initialization failed.

Fix a race condition that resulted in slightly wrong frame durations calculated for VFR input.

Fix an overflow in i16x16 NEON planar prediction, backported from ffmpeg.

In x86inc.asm, error on duplicate functions instead of silently renaming one of them.

.. _improvements-10:

Improvements:
'''''''''''''

Enable FastShuffle on crippled Nehalem/Penryn CPUs without SSE4.

Output pic_struct information in the libx264 API.

Allow weightp_fake in interlaced mode: it seems to work fine as-is.

In Windows, restore the old console title after encoding. MSDN says this is supposed to happen automatically, but MSDN is wrong.

Make x264cli update its progress every 0.25 seconds instead of every certain number of frames. This should be more visually consistent and fix some problems with extremely fast-updating status bars (e.g. from FFMS indexing of large files) in some situations.

.. _upcoming-10:

Upcoming:
'''''''''

--device and automatic --level restriction support is in the works, as part of Google Code-In. The patch is done, but needs review.

A per-option help system is in the works, as part of Google Code-In. The patch is done, but needs editing of the help entries.

Adaptive MBAFF development is actually coming along for once this time. Inter frames are mostly done.

x262 is under development: a best-in-class MPEG-2 encoder built using the x264 framework. Basic structure is done, with intra coding finished and inter coding begun.

Work is planned to integrate x264 with the Sandy Bridge's encoding ASIC for improved encoding performance. Current status is: waiting on Intel (these guys move at the speed of a one-legged paraplegic three-toed sloth swimming down a river of frozen helium while chained to an osmium anchor stuck inside a black hole).

`Volume 12 <http://mailman.videolan.org/pipermail/x264-devel/2011-February/008293.html>`__
------------------------------------------------------------------------------------------

*02/18/2011*

This is the twelfth x264 development newsletter. If you missed the first eleven, this is a regular email containing updates on fixes and improvements in the most recent x264 push, along with updates on what's coming next. Previous versions can be found in the mailing list archives.

.. _fixes-11:

Fixes:
''''''

Fix some Intel compiler warnings.

Fix a crash in the mp4 muxer in x264cli if x264_encoder_open failed.

Fix a case in which a malloc(0) was done; on some OSs, like Solaris, this returned a null pointer instead of a pointer to a 0-byte memory block, thus causing libx264 to think that its malloc failed. Both these behaviors are POSIX-compatible.

Fix a minor bug in RD caused by a stray semicolon. It probably didn't affect much.

Fix a memory leak on encoder close if not all frames were flushed during encoding.

.. _improvements-11:

Improvements:
'''''''''''''

Save memory: don't init MV cost data that isn't needed.

Use bs_write1 for all 1-bit header bits, not just some.

Even more accurate handling of slice-max-size escape bytes: track the actual bytes rather than trying to estimate them. Slightly slower, but should cover even the most insane corner cases (we found a corner case in which x264 could literally end up outputting one escape byte for every single macroblock!).

In frame-packing 3D, don't place scenecuts on the right view, ever. Some players dislike this. Note: x264 won't stop you from using an odd keyint, which will mess this up.

The first edition of Daniel Kang's massive AVX patch is in -- hopefully this will give a few % of performance on the new Sandy Bridge chips.

.. _upcoming-11:

Upcoming:
'''''''''

--device and automatic --level restriction support is in the works, as part of Google Code-In. The patch is done, but needs review.

A per-option help system is in the works, as part of Google Code-In. The patch is done, but needs editing of the help entries.

Adaptive MBAFF development is actually coming along for once this time. Inter frames are basically done.

x262 is under development: a best-in-class MPEG-2 encoder built using the x264 framework. P-frames are done and working.

Work is planned to integrate x264 with the Sandy Bridge's encoding ASIC for improved encoding performance. Current status is: waiting on Intel (these guys move at the speed of an obese one-legged paraplegic three-toed sloth swimming down a river of frozen helium while chained to an osmium anchor stuck inside a black hole).

`Category:x264 <Category:x264>`__
