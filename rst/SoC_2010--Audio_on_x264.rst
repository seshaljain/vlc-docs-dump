.. raw:: mediawiki

   {{SoCProject|year=2010|student=[[User:Kovensky|Diogo Franco]]|mentor=[[User:Dark_Shikari|Jason Garret-Glaser]]}}

Abstract
--------

Implement an audio filtering system that allows transcoding of audio with resampling, sample format conversion and channel remixing.

This is meant to be used for using with the soon-to-be-merged video filtering system for doing transcoding using only x264. Is also a prerequisite for the planned --device option that will automatically downscale the video if needed, set the appropriate H.264 level options and transcode to the appropriate audio codec.

Milestones
----------

This list is preliminary.

====== ======== ===========================================================================
Status Deadline Description
====== ======== ===========================================================================
-      May 30   Basic audio transcoding working
-      June 6   Integrate the audio framework into x264
-      June 6   Modify a muxer in x264 to support audio (most likely flv)
-      -        Implement the essential filters
-      -        Make the system automatically insert filters if needed for the target codec
\              
====== ======== ===========================================================================

Repository
----------

-  http://github.com/Kovensky/x264-audio/tree/audio_new
