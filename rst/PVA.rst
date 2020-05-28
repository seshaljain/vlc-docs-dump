.. raw:: mediawiki

   {{mux|id=pva|encoder=n}}

PVA is the extension denoting `Packetized <Packetize>`__ Elementary Streams (PES) containing both video and audio. PES files are muxed `elementary streams <elementary_stream>`__. By their nature elementary streams are only audio or video files. However, by recording `timestamps <timestamp>`__ PVA files can contain both with a low overhead for `muxing <muxing>`__ real-time `MPEG-2 video <MPEG-2_video>`__ with `AC3 <AC3>`__ Dolby Digital audio. Such files are often recorded with Digital Video Broadcast `DVB <DVB>`__ capturing software.

Source code
-----------

.. raw:: mediawiki

   {{file|modules/demux/pva.c|input demuxer}}
