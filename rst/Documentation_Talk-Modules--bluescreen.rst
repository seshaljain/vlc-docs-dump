This example (or the files) are broken for 1.0.2 windows. Note the error in the log below: "Unsupported input chroma 'I420'. Bluescreen can only use "YUVA".

::

   main debug: looking for text renderer module: 2 candidates
   main debug: `rushfondvert.avi' successfully opened
   main debug: Buffering 0%
   main debug: switching to sync mode
   main debug: Buffering 8%
   main debug: adding a new sout input (sout_input:0x3933c68)
   stream_out_duplicate debug: duplicated a new stream codec=s16l (es=1 group=0)
   main debug: Buffering 4%
   main error: cannot create packetizer output (s16l)
   packetizer_mpeg4video warning: waiting for VOL
   main debug: Buffering 13%
   (...)
   main debug: Buffering 25%
   main debug: adding a new sout input (sout_input:0x3933ee0)
   stream_out_duplicate debug: duplicated a new stream codec=mp4v (es=0 group=0)
   main debug: looking for decoder module: 36 candidates
   main debug: Buffering 33%
   (...)
   main debug: Buffering 66%
   mpeg_audio debug: MPGA channels:2 samplerate:44100 bitrate:224
   main debug: Buffering 71%
   (...)
   main debug: Buffering 97%
   main debug: Stream buffering done (306 ms in 21 ms)
   main debug: thread started
   main debug: looking for video filter2 module: 20 candidates
   main debug: Buffering 91%
   main debug: Buffering 100%
   main debug: Stream buffering done (325 ms in 21 ms)
   swscale debug: 32x32 chroma: YUVA -&gt; 16x16 chroma: YUVA with scaling using Bicubic (good quality)
   stream_out_mosaic_bridge debug: psz_chain: bluescreen
   main debug: using video filter2 module "bluescreen"
   main debug: Filter 'bluescreen' (0x39e34c4) appended to chain
   stream_out_duplicate debug: - added for output 0
   main debug: Decoder buffering done in 91 ms
   bluescreen error: Unsupported input chroma "I420". Bluescreen can only use "YUVA".
